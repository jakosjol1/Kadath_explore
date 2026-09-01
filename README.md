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
| L1 macro (vix, us_10y, se_policy) | daily observations | Live, confirmed working |
| L8 weights / L9 NAV / L10 attribution | all 4 portfolios | Returning empty/null -- Kadath side, not ours. Re-check before relying on portfolio sync. |

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
- [ ] Add synthetic "MARKET" row to `portfolios` table for macro-vs-benchmark
      comparisons independent of any specific portfolio
