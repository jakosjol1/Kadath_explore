# Daily Service Design: "Today's Regime"

Status: **designed, not yet built**. Blocked on the same standalone Kadath
API credential noted in the main README -- everything else needed
(schema, worked examples as classifier signatures, sync script skeleton)
already exists in this repo.

## What it produces, daily

1. **Yesterday's update**: what the key macro/market series did (VIX,
   OMXSPI, US10Y, EUR/SEK), any single-day moves worth flagging, and a
   short grounded explanation (web-search-sourced) if a notable move
   happened -- same format as the manually-built worked examples in
   `analysis/`.
2. **Current regime + since when**: a label (one of the 4+ documented in
   `analysis/README.md`'s pattern library, or "developing/unclassified" if
   nothing fits cleanly yet) plus the date that regime started.

## Pipeline

```
GitHub Actions (daily cron, e.g. 07:00)
  |
  v
1. Pull yesterday's data
   - Kadath MCP (VIX, US10Y, se_policy, eur_sek) -- needs standalone
     KADATH_API_KEY, see sync/kadath_to_supabase.py docstring
   - OMXSPI from FRED's public CSV export (no API key needed --
     confirmed working via plain HTTP fetch, same URL pattern used
     manually throughout this project: fred.stlouisfed.org/data/NASDAQOMXSPI)
   - Write both into existing macro_observations / portfolio_nav_history
     tables via the sync script
  |
  v
2. Classify the regime (rule-based, NOT an LLM guess)
   - Compare yesterday's VIX level + N-day trend against the numeric
     signatures already documented in analysis/worked_example_*.md:
       - VIX climbing steadily, multiple consecutive days -> "slow-building crisis"
       - VIX low (roughly <18) and flat -> "calm/grinding"
       - Sharp single-day VIX drop after an elevated period -> "reversal"
       - VIX + US10Y rising together -> "rate-driven bear market" (2022 signature)
   - Write to a new `regime_state` table: (regime_label, started_on,
     last_confirmed_on). Only flip the label after several consecutive
     confirming days, to avoid noisy one-day whipsaws.
  |
  v
3. Generate the narrative (LLM step, Anthropic API)
   - Given yesterday's numbers + the regime classification + a scoped
     web search for that specific date, write a short update in the
     same style as the existing worked examples.
   - Prompt should reference the existing worked_example_*.md files as
     style/quality templates.
  |
  v
4. Deliver
   - Not yet decided. Options: commit a dated markdown file to the repo,
     email digest, Slack post, small static page. Pick one concrete
     channel before building -- the pipeline needs a real endpoint.
```

## New schema needed

```sql
create table regime_state (
    id bigint generated always as identity primary key,
    regime_label text not null,        -- e.g. 'slow_building_crisis', 'calm_grinding',
                                        -- 'sharp_reversal', 'rate_driven_bear', 'unclassified'
    started_on date not null,
    last_confirmed_on date not null,
    confidence_note text,              -- brief note on why this label, for auditability
    updated_at timestamptz not null default now()
);
```

## Open questions for when this gets built

- Exact numeric thresholds for the classifier (e.g. "VIX > X for Y
  consecutive days") -- should be tuned against the 4 documented regimes
  plus probably more historical examples once the pattern library grows.
- How many consecutive confirming days before flipping the regime label
  (avoiding whipsaw vs. reacting fast enough to be useful).
- Delivery channel (see step 4).
- Whether "unclassified/developing" is a real, displayed state (honest)
  or whether the classifier should always force-fit to the nearest known
  regime (simpler, but potentially misleading on genuinely novel days --
  see the Sept 1 2026 live check earlier in this project's history, which
  looked like the *early* stage of a slow-building crisis but wasn't
  confirmed yet).
