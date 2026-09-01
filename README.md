# Kadath_explore

Testing different MVPs on top of Kadath (quant equity research/portfolio
system) data: macro-vs-market/portfolio comparisons, with an eventual
hover-to-analyze LLM + web search layer.

## Architecture

- **Data source:** Kadath, an MCP server (`https://kadath-production.up.railway.app/mcp`)
- **Database:** Supabase project `kadath-explore` (`dfuqhspmstqcrurtdutu`, eu-north-1)
- **Sync:** `sync/kadath_to_supabase.py` -- standalone script, not run from
  inside a Claude session. See that file's docstring for required
  credentials.
- **Frontend:** undecided (Lovable vs. custom -- schema is frontend-agnostic)

## Status (as of 2026-09-01)

| Layer | Data | Status |
|---|---|---|
| L1 macro (vix, us_10y) | daily observations | **Widened to Mar 2 - Aug 18 2026** (~120 trading days each). se_policy/eur_sek still only cover Aug 2026 -- widen those next if needed. |
| Market level (OMXSPI) | daily index values | **Widened to match** (Mar 2 - Aug 20 2026, 119 obs), sourced from FRED, stored under MARKET portfolio row. **First real multi-month macro-vs-market picture**: a clean VIX spike (21->31) coinciding with a ~9% OMXSPI drawdown in March, mirrored by a recovery in April, then a calmer May-Aug regime with both series broadly improving together. Visually a much more convincing negative VIX/OMXSPI relationship than the original 12-day window suggested. |
| L8 weights / L9 NAV / L10 attribution | all 4 portfolios | Returning empty/null -- Kadath side, not ours. Re-check before relying on portfolio sync. |

`portfolios` table now includes all 4 real portfolios plus a synthetic
`MARKET` row (benchmark OMXSPI) so macro-vs-market and macro-vs-portfolio
comparisons can share the same schema.

## Schema

See `schema/001_init_schema.sql`. Key design choice: `portfolios` includes
room for a synthetic "market" row (not yet added) so macro-vs-market and
macro-vs-portfolio comparisons can share the same downstream tables.

## Open items

- [ ] Get a Kadath API key/token for the standalone sync script (separate
      from the claude.ai MCP connection used to design this schema)
- [ ] Confirm with Kadath operator whether L8/L9/L10 outage is temporary
- [ ] Decide macro resampling strategy (native frequency vs. resampled to
      rebalance periods) before building comparison charts
- [ ] Pick frontend (Lovable vs. custom) once first chart is validated
- [ ] Widen macro backfill beyond Aug 2026 (currently a small proof-of-pipeline
      slice, deliberately kept small -- see conversation history for reasoning)
- [x] Checked for an L1-level market-index shortcut (to unblock "macro vs
      market" while L8/L9/L10 is down) -- doesn't exist. l1_get_prices is
      per-symbol only.
- [x] **Wider finding (2026-09-01):** it's not just L8/L9/L10. Confirmed empty
      right now: l1_get_prices, l1_get_fundamentals, l2_get_features_for_date,
      l4_get_factor_snapshot -- i.e. every stock-level layer, not just
      portfolios. Only l1_get_macro (macro series) is live. A synthetic
      equal-weight "market proxy" from individual stock prices is NOT
      currently buildable either -- this is one broader outage, not several
      independent gaps. Re-check stock-level tools before attempting any
      market-vs-macro work; only macro-internal analysis is possible today.
- [x] **Unblocked via external data (2026-09-01):** pulled real OMXSPI daily
      index values from FRED (web, not Kadath) for the same Aug 3-20 window
      as the macro backfill. Stored under the MARKET portfolio row
      (migration 004). This sidesteps the Kadath stock-level outage entirely
      for market-level analysis -- worth keeping as a standing pattern
      (Kadath macro + web-sourced market/price data) rather than waiting
      for Kadath's stock layers, especially if that outage persists.
- [x] Widened the OMXSPI + VIX + US 10Y dataset to Mar 2 - Aug 18/20 2026
      (~120 trading days), all date-aligned. First finding: a clean VIX
      spike (21->31) coincided with a ~9% OMXSPI drawdown in March, with a
      mirrored recovery in April -- a real, visually convincing pattern
      across a genuine volatility event, not just a calm 12-day snapshot.
- [ ] Widen se_policy/eur_sek to match the Mar-Aug window (currently Aug-only)
- [ ] Consider widening further back (2025, or the full FRED history to 2008)
      once ready to test the relationship across more distinct regimes
- [ ] Run this same OMXSPI-from-FRED pattern for other indices/benchmarks if
      the project expands beyond Sweden
- [x] Add synthetic "MARKET" row to `portfolios` table for macro-vs-benchmark
      comparisons independent of any specific portfolio
- [x] Validate full pipeline (Kadath -> Supabase -> chart) with real data
