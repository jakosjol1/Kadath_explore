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
| L1 macro (vix, us_10y, se_policy, eur_sek) | daily observations | **Pipeline validated end-to-end**: Kadath -> Supabase -> chart, using real Aug 2026 data (manually backfilled from a Claude chat session, see schema/001_init_schema.sql migrations 002-003) |
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
      per-symbol only. "Macro vs market" genuinely depends on the L9/L10
      pipeline coming back; "macro vs a specific portfolio" does too.
- [x] Add synthetic "MARKET" row to `portfolios` table for macro-vs-benchmark
      comparisons independent of any specific portfolio
- [x] Validate full pipeline (Kadath -> Supabase -> chart) with real data
