# Worked example: 2026-05-18 to 2026-06-04 calm/grinding regime

Third worked example, and the first non-crisis one -- a genuinely
different "shape" of market behavior from the other two, and arguably
the most common regime day-to-day.

## Why this window

Directly follows the March/April volatility episode (see the other two
worked examples) and shows what "normal" looked like once that resolved
-- useful as the baseline case the crisis examples are contrasted against.

## What the data shows (Supabase)

| Metric | Value |
|---|---|
| Window | 2026-05-18 to 2026-06-04 (14 trading days) |
| VIX range | 15.32 - 18.06 (avg 16.50) -- low and narrow |
| OMXSPI | 1065.26 -> 1092.23 (+2.53% total, steady upward drift) |
| Avg daily return | +0.197% |
| Largest single-day move | -1.55% (small compared to the +3.92%/-3.29%
  single-day moves seen during the March/April episode) |
| Std dev of daily returns | 0.961% (roughly half the volatility of a
  crisis period) |

## What web search found

This is the interesting part: it wasn't a *quiet* period in the sense of
nothing happening. Real coverage of May 2026 describes markets absorbing
real headwinds -- rising Treasury yields and a sharp shift in Fed rate
expectations (probability of a hike jumping from ~1% to over 45% within a
month, per CME FedWatch) -- without volatility spiking, because earnings
strength and growth visibility offset the concern. Coverage also notes
incremental easing of Middle East tensions and a pullback in oil prices
contributed to a more constructive backdrop during this window.

Separately, later-dated coverage (per a "Chart of the Day" piece) frames
this whole stretch as markets "grinding back down" from the spring's
Iran-war volatility spike over the following months.

Sources:
- https://www.nasdaq.com/articles/may-2026-review-and-outlook
- https://finance.yahoo.com/markets/article/wall-streets-summer-calm-is-colliding-with-the-years-most-volatile-stretch-chart-of-the-day-114901053.html

## The synthesis, and the key contrast with the other two examples

This is the pattern worth internalizing for "what does calm actually
mean": **low VIX doesn't mean no risk exists — it means the market is
currently absorbing risk without panic.** May 2026 had real, substantive
headwinds (a live Fed-hike repricing, still-elevated oil prices, ongoing
geopolitical tension) running in parallel with strong earnings and
resilient economic data. The offsetting good news won, for now, and VIX
stayed low as a result.

Compare to the other two examples:

| Regime | VIX behavior | Underlying driver |
|---|---|---|
| Slow-building crisis (Mar 27) | Steady climb to a peak (21->31 over ~4 weeks) | A single deteriorating narrative (Iran war) with no offsetting good news |
| Sharp single-catalyst reversal (Apr 8) | Sharp one-day drop (25.78->21.04) | A single de-escalating headline (ceasefire) |
| Calm/grinding (May 18-Jun 4) | Low and flat (15-18 range) | Multiple real risks running concurrently, but offset by good news (earnings, easing tensions) |

The practical implication for "understanding what's happening right now":
a low VIX reading alone doesn't tell you whether real risk is absent or
just currently being outweighed by good news. Worth checking what's
actually offsetting what, not just reading the VIX level in isolation.

## Caveats

- Same methodology caveats as the other two examples -- manually
  assembled, not yet a repeatable pipeline.
- "Calm" here is relative to the March/April episode in this same
  dataset, not to all of market history -- a genuine multi-year low-vol
  grind (e.g. 2017) would look calmer still. Worth keeping that
  perspective once the dataset widens further back.
