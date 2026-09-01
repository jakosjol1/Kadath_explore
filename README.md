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
| Market level (OMXSPI) | daily index values | **Sourced from FRED/Nasdaq (web), not Kadath** -- Kadath's stock-level layers are down, so this is a genuine external substitute, not a Kadath pull. Stored under the synthetic MARKET portfolio row (migration 004). First real macro-vs-market comparison is now possible. |
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
- [ ] Widen the OMXSPI backfill to match/exceed the macro backfill's date
      range once the small-window pattern is validated further
- [x] Add synthetic "MARKET" row to `portfolios` table for macro-vs-benchmark
      comparisons independent of any specific portfolio
- [x] Validate full pipeline (Kadath -> Supabase -> chart) with real data
