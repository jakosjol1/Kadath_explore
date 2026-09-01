# Worked example: 2026-03-27 VIX peak

Second worked example of the hover-to-analyze concept. Unlike the 2026-04-08
example (a single clean catalyst), this one is a slow-building, multi-week
crisis -- a more realistic test of what the automated feature needs to
handle.

## Why this date

VIX peaked at 31.05 on this date -- the highest point in the entire
Mar-Aug 2026 dataset -- at the tail end of a steady climb from ~21 that
began Mar 2.

## What the data shows (Supabase)

| Metric | Context | Value |
|---|---|---|
| VIX | Peak of the whole window | 31.05 (up from ~21 on Mar 2) |
| OMXSPI | Day-of move | -1.03% (Mar 26: 1007.80 -> Mar 27: 997.42) |
| OMXSPI | Cumulative into the peak | ~-9% from the Mar 2 starting level |
| US 10Y | Day-of move | Rose slightly, 4.42% -> 4.44% (not a flight-to-bonds pattern) |

## What web search found

Real, dated coverage confirms an escalating Iran conflict was driving oil
prices sharply higher (Brent crossed $110-112/barrel) through late March
2026, fueling inflation fears and a broad equity selloff. US markets
recorded their fifth consecutive losing week -- the longest such streak
since early 2022 -- with the Nasdaq falling into full correction territory.
Coverage specifically cited incidents in the Strait of Hormuz as
intensifying energy-supply concerns on top of weeks of accumulating
war-related anxiety.

Sources:
- https://www.bloomberg.com/news/articles/2026-03-26/stock-market-today-dow-s-p-live-updates
- https://finance.yahoo.com/markets/world-indices/articles/major-us-stock-indexes-fared-202545953.html
- https://www.goodmanfinancial.com/march-2026-market-commentary/

## The synthesis

This is a genuinely different shape of event from the 2026-04-08 example:

- **2026-04-08** = single clean catalyst (ceasefire headline) -> sharp
  one-day reversal, easy to explain in one sentence.
- **2026-03-27** = slow-building, multi-week narrative (escalating war,
  rising oil, compounding inflation fear) -> a gradual VIX climb peaking
  on this date, not a single-day shock.

The US10Y move is the interesting wrinkle: yields *rose* slightly into
the VIX peak rather than falling (the usual flight-to-safety pattern),
consistent with the reported driver being inflation fear (from oil
prices) rather than a generic risk-off flight into bonds. This is a
useful nuance an automated feature would need to get right -- not every
VIX spike has the same bond-market signature, and naively assuming
"VIX up -> yields down" would have been wrong on this specific date.

## Caveats

- Same as the 2026-04-08 example: manually assembled, not yet a
  repeatable pipeline.
- The war/oil narrative is global, not Sweden-specific -- OMXSPI's move
  here is again best read as "Sweden moving with global risk sentiment,"
  not a locally-driven event.
- Worth testing whether an automated version would correctly surface the
  US10Y nuance (yields rising, not falling) rather than defaulting to a
  generic "risk-off" explanation template.
