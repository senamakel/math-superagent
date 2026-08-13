# Negative finding: no proved theorem for a deterministic general Gilbreath-like class

Searched July 2026, several phrasings (research paper category): "Gilbreath conjecture
proved theorem deterministic sequence first entry 1 eventually stays odd gaps bounded not
random", "deterministic sequence class bounded gaps odd numbers", "Gilbreath-like
sequences theorem". **Nothing found** — no paper proves GC, or even the eventual-persistence
claim `A_k(1) = 1 for all large k`, for any genuinely deterministic class of integer
sequences.

## What the literature actually offers (all held in the library)

- **Random analogue, almost-sure eventual persistence**: Chase 2024 (Math. Ann. 388,
  arXiv:2005.00530) and CHT 2026 Thm 1.3 — i.i.d. or 2-separated-non-concentrating gap
  models give `{0,1}` left diagonal a.s. These are statements about *random* sequences,
  not fixed deterministic ones.
- **Inverse/obstruction classification (deterministic, but conditional)**: CHT 2026 Thm
  1.6 — if initial data ≤ 2^M and no long zero-block and no long shallow {0,d}-block then
  decay to {0,1}. This is a true theorem about deterministic arrays, but its hypotheses
  for the primes are exactly the unproved Cramér-type conjectures. It is the only
  deterministic general result in the library, and it is conditional on unproved input.
- **Conjectural postulates**: Croft's bounded-gap postulate (refuted in its blanket form by
  Eppstein 2011 — anti-Gilbreath construction), Gatti 2023's "sequences starting 2 + odds
  not growing too fast/slow satisfy GC" (postulate, no proof held), Odlyzko's "sufficiently
  random" heuristic.
- **Restricted classes actually proved**: only the trivial ones in
  `research/ROOT.md` — consecutive odds, constant-2 first-difference tail, and reaching a
  row (1, c, c, ...) — all "regeneration already complete" corner cases, proved by this
  run from the reduction mechanism.

## Consequence for this run's GOAL

A theorem covering "2 followed by odd numbers with gaps bounded by g" is **not in the
literature and (by Eppstein's construction) is false without an extra non-concentration
hypothesis**. The clean realistic targets remain what GOAL.md lists: a proved invariant
forcing A_k(1) ∈ {0,2} (nothing in the library approaches this), a proved statement about
the regeneration rate, or a general-class theorem carved down to beat Eppstein (e.g.
2-separated non-concentration, or gaps avoiding a fixed 2-separated set — the CHT form).
Anyone proposing a "deterministic bounded-gap theorem" should be pointed at Eppstein's
construction first.