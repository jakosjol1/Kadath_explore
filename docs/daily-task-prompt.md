# Daily scheduled-task prompt (MVP)

Paste this into a Claude scheduled task. Designed to be self-contained --
assumes no memory of prior conversations, pulls its own context from
GitHub each run. Requires the Kadath and Supabase connectors enabled for
the task.

---

You are running a daily market-regime check for a personal project called
Kadath_explore. Do the following steps in order.

**0. Load context**
Fetch these two files to load the current pattern library and schema
(they define what "regime" labels mean and how the tables are shaped):
- https://raw.githubusercontent.com/jakosjol1/Kadath_explore/main/analysis/README.md
- https://raw.githubusercontent.com/jakosjol1/Kadath_explore/main/docs/daily-service-design.md

Supabase project ID: `dfuqhspmstqcrurtdutu`. Determine "yesterday" from
today's actual date.

**1. Get yesterday's data -- Kadath first, web search as fallback per series**
For each of: `vix`, `us_10y`, `se_policy`, `eur_sek` -- call Kadath's
`l1_get_macro` for yesterday's date specifically. If a series returns no
observation for that exact date (empty result, or Kadath's data lags
behind), search the web for that specific series' real closing value on
that specific date instead (e.g. "VIX close [date]", "US 10 year Treasury
yield [date]"). Note which source (Kadath vs. web) each value came from --
this matters for data quality tracking.

Separately, get yesterday's OMXSPI value: try
https://fred.stlouisfed.org/data/NASDAQOMXSPI first (it may not have
yesterday's value yet depending on publish timing); if missing, web
search for "OMX Stockholm All Share index close [date]".

**2. Write to Supabase**
Upsert the macro values into `macro_observations` (series_id, obs_date,
value, as_of = today's date). Upsert OMXSPI into `portfolio_nav_history`
under `portfolio_id = 'MARKET'` (rebal_date = yesterday, nav = the index
value, gross_return_pct = computed vs. the prior stored value for MARKET).

**3. Classify the regime**
Using the thresholds and signatures described in the pattern library you
loaded in step 0, compare yesterday's VIX level and its recent multi-day
trend (query the last ~10 days of `vix` from `macro_observations`) against
the documented regime shapes. Produce a proposed label: one of
`slow_building_crisis`, `sharp_reversal`, `calm_grinding`,
`rate_driven_bear`, or `unclassified` if nothing fits cleanly.

Check whether a `regime_state` table exists in Supabase (create it per
the schema in `daily-service-design.md` if not). Compare your proposed
label to the current stored one:
- If it matches the existing label, just update `last_confirmed_on` to
  yesterday's date.
- If it differs, only flip the stored label if this is at least the 2nd
  consecutive day the new label would apply (for this MVP, checking
  yesterday's data against the trend is enough evidence -- don't
  overthink the confirmation logic, this is a test).
- If you flip it, set `started_on` to the date the new pattern actually
  began (look back at the trend, not just yesterday), and write a short
  `confidence_note` explaining why.

**4. Check for a notable single-day move**
If yesterday's OMXSPI move was larger than ~1.5% in either direction, or
VIX moved more than ~2 points, do a scoped web search for real news from
that specific date that plausibly explains it (the way the worked
examples in `analysis/` were built). Keep this search tight -- the date
and the likely topic (markets, Fed, geopolitical), not a vague query.

**5. Output the daily digest**
Produce a short, plain-language summary with:
- Yesterday's date and the key numbers (VIX, US10Y, OMXSPI, EUR/SEK) with
  day-over-day change, and which source each came from
- Current regime label and "since [date]"
- If applicable, the notable-move explanation from step 4, with the
  source cited
- Any data-quality flags (e.g. "Kadath's VIX data is still lagging,
  fell back to web search" or "OMXSPI not yet published on FRED for
  yesterday, used [source] instead")

Keep the whole digest under ~200 words. This is a daily check-in, not a
report.
