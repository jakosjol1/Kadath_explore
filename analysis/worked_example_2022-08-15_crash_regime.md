# Worked example: 2022-08-15 to 2022-10-17 grinding bear market

Fourth worked example, and the first genuine **crash/bear-market regime**
in the library. Required widening the dataset back to 2022 -- nothing in
the current 2026 window is severe enough to represent this regime.

## Why this window

Captures the Fed's hawkish "Jackson Hole 2022" pivot (Aug 26) and the
resulting selloff to that cycle's market low (Sep 29), then early
stabilization into mid-October. The single most consequential macro
speech of the 2022 tightening cycle, with a clean before/after in the data.

## What the data shows (Supabase)

| Metric | Value |
|---|---|
| Window | 2022-08-15 to 2022-10-17 (46 trading days) |
| OMXSPI | 821.28 -> low of 690.07 on 2022-09-29 (**-15.98%**) -> 728.48 by
  window end (-11.30% vs start) |
| VIX | 19.95 (Aug 15) -> peak of 33.63 (Oct 11), a slow ~7-week climb, not
  a single spike |
| US 10Y | 2.79% -> 4.02% (**+123 basis points** over the same window) |
| Avg daily OMXSPI return | -0.254% (consistently negative, not one big
  crash day) |
| Std dev of daily returns | 1.543% (roughly 1.6x the calm-regime example) |
| Largest single day | +3.57% (a relief-rally day, not the crash itself --
  illustrating that even grinding bear markets have sharp counter-rallies) |

## What web search found

August 26, 2022: Fed Chair Jerome Powell delivered his Jackson Hole
speech, stating the FOMC's overarching focus was bringing inflation back
to the 2% target -- widely regarded as one of the most hawkish Powell
speeches of the entire tightening cycle, explicitly signaling continued
rate increases and warning of economic pain ahead. This is the single
most consequential day in the window: VIX jumped from 21.78 (Aug 25) to
25.56 the day of the speech, and the OMXSPI decline accelerated from
there through late September.

Source: https://www.federalreserve.gov/newsevents/speech/powell20220826a.htm

## The synthesis -- and why this regime is structurally different

This is the first example where **VIX and US 10Y rose together**, rather
than moving in the usual inverse relationship with rates as a flight-to-
safety signal. That's the defining signature of a genuinely Fed-driven
bear market: the same underlying cause (persistent inflation, a hawkish
central bank response) pushes both series up simultaneously --
higher-for-longer rate expectations directly raise yields, while the
resulting growth/earnings risk raises equity volatility. Compare this to
the March 2026 episode (worked_example_2026-03-27.md), where yields and
VIX did not move in lockstep, because that episode's driver (an oil-price
war shock) worked through a different channel.

## Comparing all four regimes now in the library

| Regime | Duration | OMXSPI move | VIX peak | US10Y behavior |
|---|---|---|---|---|
| Slow-building crisis (Mar 2026) | ~4 weeks | ~-9% | 31 | Flat/mixed |
| Sharp single-catalyst reversal (Apr 2026) | 1 day | +3.92% (single day) | Sharp drop | Declined with the rally |
| Calm/grinding (May-Jun 2026) | ~2.5 weeks | +2.5% (steady) | 15-18 (low) | N/A (calm) |
| **Grinding bear market (2022)** | **~7 weeks** | **-16% to the low** | **33.6 (slow climb)** | **+123bp, rising in lockstep with VIX** |

The 2022 episode is both **longer** and **deeper** than anything in the
current 2026 dataset, and it's the only one where rates and volatility
rose together -- a genuinely distinct fingerprint from a rates-driven
tightening cycle versus a geopolitical or single-headline shock.

## Caveats

- Same manual-assembly caveats as the other three examples.
- This window captures the acceleration and the low, but not the full
  2022 bear market's origin (which began in January 2022) or its eventual
  bottom (October 2022 was close to, but not exactly, the final low for
  the broader cycle) -- worth treating this as "the most intense stretch"
  rather than "the whole bear market."
- Sweden-specific dynamics aren't separated out here either -- OMXSPI's
  decline is presented as tracking the global, Fed-driven macro backdrop,
  consistent with the pattern seen in the other worked examples.
