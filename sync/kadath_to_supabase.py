"""
Kadath -> Supabase sync script.

WHAT THIS DOES
--------------
Pulls data from Kadath (an MCP server) and upserts it into Supabase tables
defined in ../schema/001_init_schema.sql. Meant to run on a schedule
(GitHub Actions cron) or manually.

WHY THIS NEEDS ITS OWN CREDENTIALS
-----------------------------------
Kadath is normally accessed via an MCP connection inside a Claude chat
session (claude.ai), where auth is handled for you. This script does NOT
run inside that session -- it's a standalone process (e.g. a GitHub Actions
runner), so it needs its own way to authenticate to Kadath's MCP endpoint
directly: https://kadath-production.up.railway.app/mcp

You'll need to get a Kadath API key/token from whoever operates that server
and set it as KADATH_API_KEY below. This script cannot discover or reuse
the credential from your claude.ai connection -- that's a separate, chat-
session-scoped auth flow.

REQUIRED ENV VARS
------------------
    KADATH_MCP_URL       (default: https://kadath-production.up.railway.app/mcp)
    KADATH_API_KEY        <- you need to obtain this
    SUPABASE_URL           https://dfuqhspmstqcrurtdutu.supabase.co
    SUPABASE_SERVICE_KEY   <- Supabase project settings -> API -> service_role key

STATUS AS OF 2026-09-01
-------------------------
- L1 (macro, prices, fundamentals) is confirmed LIVE and returning real data.
- L8/L9/L10 (portfolio weights, NAV, attribution) are currently returning
  EMPTY results for all four registered portfolios. This may be a temporary
  outage/reset on Kadath's side. The sync_portfolios() function below is
  written and ready, but will insert nothing useful until that data returns.
  Re-run l8_get_portfolios / l9_get_nav_history from a Claude session to
  check status before relying on this half of the script.

USAGE
-----
    pip install mcp supabase python-dateutil
    python kadath_to_supabase.py --macro-only          # just L1 macro
    python kadath_to_supabase.py                        # macro + portfolios
"""

import argparse
import asyncio
import os
from datetime import date

from supabase import create_client, Client

# --- MCP client for Kadath -------------------------------------------------
# Uses the official `mcp` Python SDK to open a session against Kadath's
# HTTP MCP endpoint and call tools the same way Claude does.
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

KADATH_MCP_URL = os.environ.get("KADATH_MCP_URL", "https://kadath-production.up.railway.app/mcp")
KADATH_API_KEY = os.environ.get("KADATH_API_KEY")  # required -- see module docstring

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_SERVICE_KEY = os.environ["SUPABASE_SERVICE_KEY"]

# Macro series we track. Extend this list as you widen the "check all macro
# data against the market" idea -- keep it small while validating the
# pipeline, then grow it.
MACRO_SERIES = [
    {"series_id": "vix", "description": "CBOE Volatility Index", "unit": "index"},
    {"series_id": "us_10y", "description": "US 10-Year Treasury Yield", "unit": "percent"},
    {"series_id": "se_policy", "description": "Riksbank policy rate", "unit": "percent"},
]

PORTFOLIO_IDS = [
    "mvl8_largecap_v1",
    "mvl8_monthly_v1",
    "mvl8_quarterly_v1",
    "mvl8_semiannual_v1",
]

BACKFILL_FROM = "2025-01-01"


def supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)


async def kadath_session():
    """Open an MCP session against Kadath. Auth header shape depends on
    what Kadath's server expects (bearer token shown here as the common
    case) -- confirm with Kadath's operator and adjust if needed."""
    headers = {"Authorization": f"Bearer {KADATH_API_KEY}"} if KADATH_API_KEY else {}
    async with streamablehttp_client(KADATH_MCP_URL, headers=headers) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            yield session


async def sync_macro(sb: Client, to_date: str = None):
    to_date = to_date or date.today().isoformat()

    # Ensure reference rows exist
    for series in MACRO_SERIES:
        sb.table("macro_series").upsert({**series, "source": "kadath"}).execute()

    async for session in kadath_session():
        for series in MACRO_SERIES:
            result = await session.call_tool(
                "l1_get_macro",
                arguments={
                    "series_id": series["series_id"],
                    "from_date": BACKFILL_FROM,
                    "to_date": to_date,
                },
            )
            observations = result.get("observations", [])
            rows = [
                {
                    "series_id": obs["series_id"],
                    "obs_date": obs["observation_date"],
                    "value": obs["value"],
                    "as_of": result.get("as_of", to_date),
                }
                for obs in observations
            ]
            if rows:
                sb.table("macro_observations").upsert(rows, on_conflict="series_id,obs_date").execute()
            print(f"  {series['series_id']}: upserted {len(rows)} rows")
        break  # one session for the whole loop


async def sync_portfolios(sb: Client):
    async for session in kadath_session():
        portfolios_result = await session.call_tool("l8_get_portfolios", arguments={})
        portfolios = portfolios_result.get("portfolios", [])

        for p in portfolios:
            sb.table("portfolios").upsert({
                "portfolio_id": p["portfolio_id"],
                "description": p.get("description"),
                "rebal_freq": p.get("rebal_freq"),
                "w_max": p.get("w_max"),
                "benchmark": p.get("benchmark_id"),
                "is_synthetic_market": False,
            }).execute()

        for portfolio_id in PORTFOLIO_IDS:
            nav_result = await session.call_tool(
                "l9_get_nav_history", arguments={"portfolio_id": portfolio_id}
            )
            nav_rows = nav_result.get("nav_history", [])
            if nav_rows:
                sb.table("portfolio_nav_history").upsert(
                    [
                        {
                            "portfolio_id": portfolio_id,
                            "rebal_date": r["rebal_date"],
                            "execution_date": r.get("execution_date"),
                            "nav": r.get("nav"),
                            "gross_return_pct": r.get("gross_return_pct"),
                            "commission": r.get("commission"),
                            "position_count": r.get("position_count"),
                            "as_of": nav_result.get("as_of"),
                        }
                        for r in nav_rows
                    ],
                    on_conflict="portfolio_id,rebal_date",
                ).execute()
            print(f"  {portfolio_id}: upserted {len(nav_rows)} NAV rows")

            period_result = await session.call_tool(
                "l10_get_period_returns", arguments={"portfolio_id": portfolio_id}
            )
            period_rows = period_result.get("periods", []) or []
            if period_rows:
                sb.table("portfolio_period_returns").upsert(
                    [
                        {
                            "portfolio_id": portfolio_id,
                            "period_start": r["period_start"],
                            "period_end": r["period_end"],
                            "gross_return_pct": r.get("gross_return_pct"),
                            "benchmark_return_pct": r.get("benchmark_return_pct"),
                            "active_return_pct": r.get("active_return_pct"),
                            "factor_return_pct": r.get("factor_return_pct"),
                            "specific_return_pct": r.get("specific_return_pct"),
                            "as_of": period_result.get("as_of"),
                        }
                        for r in period_rows
                    ],
                    on_conflict="portfolio_id,period_end",
                ).execute()
            print(f"  {portfolio_id}: upserted {len(period_rows)} period-return rows")
        break


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--macro-only", action="store_true")
    args = parser.parse_args()

    if not KADATH_API_KEY:
        raise SystemExit(
            "KADATH_API_KEY is not set. See module docstring -- this script "
            "needs its own Kadath credential, separate from any claude.ai "
            "MCP connection."
        )

    sb = supabase_client()

    print("Syncing macro data...")
    await sync_macro(sb)

    if not args.macro_only:
        print("Syncing portfolio data...")
        await sync_portfolios(sb)


if __name__ == "__main__":
    asyncio.run(main())
