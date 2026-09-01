# Analysis

Findings and worked examples from exploring the macro + OMXSPI dataset,
done manually via Claude chat sessions with live Supabase + web search
access. These are early, exploratory results -- not statistically
rigorous (no significance testing, no autocorrelation correction) --
but establish patterns worth building into the real product later.

## Files

- `correlation_analysis.py` / `correlation_results.txt` -- Pearson
  correlations between VIX/US10Y/EUR-SEK daily changes and OMXSPI daily
  returns, plus a rolling 20-day correlation, over Mar-Aug 2026.
- **Regime pattern library** (the long-term goal: build a reference set of
  what different market regimes actually look like, so live conditions can
  be compared against real historical analogs):
  - `worked_example_2026-03-27.md` -- **slow-building crisis**. VIX climbs
    steadily to a peak (21->31 over ~4 weeks) as a single deteriorating
    narrative (Iran war/oil spike) runs with no offsetting good news.
  - `worked_example_2026-04-08.md` -- **sharp single-catalyst reversal**.
    VIX drops sharply in one day (25.78->21.04) on a single de-escalating
    headline (ceasefire reports).
  - `worked_example_2026-05-18_calm_regime.md` -- **calm/grinding**. VIX
    stays low and flat (15-18) even with real concurrent risks (a live Fed
    rate-hike repricing, elevated oil) because offsetting good news
    (earnings, easing tensions) wins out. Key lesson: low VIX means risk
    is being *absorbed*, not that it's absent.
  - `worked_example_2022-08-15_crash_regime.md` -- **grinding bear
    market** (required widening the dataset back to 2022 -- nothing in
    the current 2026 window is this severe). Captures the Fed's hawkish
    Jackson Hole 2022 pivot (Aug 26) through that cycle's market low
    (Sep 29). OMXSPI fell ~16% over 7 weeks; VIX and US10Y rose
    *together*, a distinct fingerprint from the other three regimes,
    where the driver is monetary policy itself rather than a geopolitical
    or single-headline shock.

Regime comparison table:

| Regime | Duration | OMXSPI move | VIX peak | US10Y behavior |
|---|---|---|---|---|
| Slow-building crisis (Mar 2026) | ~4 weeks | ~-9% | 31 | Flat/mixed |
| Sharp single-catalyst reversal (Apr 2026) | 1 day | +3.92% (single day) | Sharp drop | Declined with the rally |
| Calm/grinding (May-Jun 2026) | ~2.5 weeks | +2.5% (steady) | 15-18 (low) | N/A (calm) |
| Grinding bear market (2022) | ~7 weeks | -16% to the low | 33.6 (slow climb) | +123bp, rising in lockstep with VIX |

Still needed for a fuller library: a **slow melt-up** (steady low-vol
rally with genuinely no fear at all, as opposed to the mild May 2026
drift, which still had real concurrent risks).

## Headline findings so far

- VIX daily change vs OMXSPI daily return: r = -0.38 (moderate negative,
  real but noisy)
- VIX level vs OMXSPI level: r = -0.82 (misleadingly strong -- mostly a
  shared-trend artifact, not a genuine daily relationship; see caveat in
  the conversation this was derived from)
- The VIX/OMXSPI relationship is **regime-dependent**: rolling correlation
  is strongest (~-0.55 to -0.59) during the actual March volatility event
  and weakens substantially (~-0.19 to -0.22) during the calm May period.
  This is the single most useful finding -- VIX is a much better signal
  during genuine stress than during quiet markets.
- April 8, 2026's rally (biggest single-day OMXSPI move in the window) is
  independently confirmed by real news: falling Treasury yields + easing
  geopolitical tensions (ceasefire reports), matching the data exactly.
- March 27, 2026's VIX peak (31.05, the window's high) is confirmed as
  the tail end of a multi-week escalating Iran conflict / oil price
  spike, not a single-day shock -- and US10Y notably *rose* into the
  peak rather than falling, since the driver was inflation fear rather
  than generic flight-to-safety. A useful nuance for any automated
  version to get right.
- The 2022 Fed tightening episode (Aug 15-Oct 17) is the deepest and
  longest regime in the library: OMXSPI fell ~16% over 7 weeks, VIX
  climbed slowly to 33.6, and -- unlike the 2026 examples -- US10Y rose
  *alongside* VIX rather than diverging from it, because both were
  driven by the same underlying cause (the Fed's hawkish pivot at
  Jackson Hole, Aug 26 2022). This is the clearest signature yet of a
  genuinely monetary-policy-driven bear market versus a geopolitical or
  single-headline-driven one.

## Open methodological question

Should significance testing / Newey-West-style correction be added before
trusting these numbers further? Kadath's own `l10_get_ic_decay` tool does
this properly for IC estimates -- worth mirroring that approach here
before this analysis is used for anything beyond exploration.
