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
- `worked_example_2026-04-08.md` -- a real, sourced example of connecting
  a specific date's data movement to external news, as a template for the
  eventual hover-and-search LLM feature.

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

## Open methodological question

Should significance testing / Newey-West-style correction be added before
trusting these numbers further? Kadath's own `l10_get_ic_decay` tool does
this properly for IC estimates -- worth mirroring that approach here
before this analysis is used for anything beyond exploration.
