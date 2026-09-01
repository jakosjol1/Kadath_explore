# Worked example: 2026-04-08 rally

First real (non-hypothetical) worked example of the "hover a date -> explain
what happened" concept from the long-term roadmap. Manually done in a Claude
chat session on 2026-09-01; the automated version would run this same
pattern (data lookup + scoped web search + LLM synthesis) on demand.

## Why this date

Biggest single-day OMXSPI move in the current Mar-Aug 2026 dataset, and a
sharp same-day VIX drop -- a natural candidate to check whether a real,
findable news event explains it.

## What the data shows (Supabase, `MARKET` + macro_observations)

| Metric | Apr 7, 2026 | Apr 8, 2026 | Change |
|---|---|---|---|
| OMXSPI | 1033.73 | 1074.22 | **+3.92%** (largest single-day move in the window) |
| VIX | 25.78 | 21.04 | **-4.74 points** (sharp drop) |
| US 10Y | 4.33% | 4.29% | -0.04pp (declined) |

## What web search found

Real, dated coverage of April 8, 2026 (TheStreet, Kalkine) describes a
broad US-led equity rally that day, driven by a decline in Treasury yields
(which lowers the discount rate applied to future corporate earnings) and
by easing geopolitical tensions -- specifically, markets reacted to reports
of a two-week ceasefire. Coverage described it as the Dow's best single day
since April 2025.

Sources:
- https://www.thestreet.com/latest-news/stock-market-today-apr-8-2026-updates
- https://kalkine.co.nz/news/general-news/what-sparked-the-us-stock-market-rally-on-april-8-2026

## The synthesis

All three signals from Supabase line up with the independently-reported
news, on the same day, in the expected direction:

- Falling yields -> matches the US10Y decline in Kadath's own data
- Easing fear/uncertainty -> matches the sharp VIX drop
- Broad equity rally -> matches the OMXSPI jump (Sweden moving with the
  global, US-led rally, not a Sweden-specific event)

This is a genuine (not cherry-picked-to-work) confirmation that the
macro data in this project reflects real market dynamics, and a template
for what the eventual automated hover-and-search feature should produce:
short, dated, sourced, and explicitly tying the local data movement to
the external event rather than just describing the event in isolation.

## Caveats

- One example, manually assembled -- not yet a repeatable, automated
  pipeline. The real feature needs to scope the search tightly (exact
  date range, relevant instruments) the way this one happened to be
  scoped by hand.
- The news event was global/US-led, not Sweden-specific -- worth keeping
  in mind that OMXSPI moves often reflect global risk sentiment more than
  local Swedish news, which matters for how the eventual feature should
  frame its explanations (don't overstate a Sweden-specific causal story
  when the driver is global).
