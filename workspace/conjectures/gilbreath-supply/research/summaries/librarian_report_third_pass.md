# Librarian report — third pass additions

## What this step added

The library was already extensive (60+ primary sources across two prior passes),
so this step did **not** bulk-accumulate. It went after the one genuine, named
gap it could fill precisely:

1. **Spiegelhofer, "The level of distribution of the Thue–Morse sequence"**
   (Compositio Math. 2020; arXiv:1803.01689).
   - Source URL: https://arxiv.org/pdf/1803.01689
   - Summary: `research/summaries/spiegelhofer_level_distribution_thuemorse.md`
   - Full text: `research/sources/spiegelhofer_level_distribution_thuemorse.full.md` (62 300 B)
   - Claim: `spiegelhofer-thuemorse-level-1` — Thue–Morse has level of distribution 1
     (Bombieri–Vinogradov for every `θ < 1`), essentially best possible.

2. **Müllner & Spiegelhofer, "Normality of the Thue–Morse sequence along
   Piatetski–Shapiro sequences, II"** (Israel J. Math. 2017; arXiv:1511.01671).
   - Source URL: https://arxiv.org/pdf/1511.01671
   - Summary: `research/summaries/mullner_spiegelhofer_normality_piatetski_II.md`
   - Full text: `research/sources/mullner_spiegelhofer_normality_piatetski_II.full.md` (85 134 B)
   - Claim: `mullner-spiegelhofer-normality-subsequence` — for `1<c<3/2`, `t(⌊n^c⌋)`
     is normal; Thue–Morse has admissible level of distribution 2/3.

Both were already 2-cited FRONTIER leads (the `bkm_gowers` and
`mullner_spiegelhofer_normal` sources I already held cite them as the canonical
references on how well-distributed Thue–Morse is), so downloading them followed
the run's own bibliography rather than a fresh guess.

## The finding this step produced

The two sources jointly **price the "h is well-distributed / random-looking"
input family negatively** for SUPPLY (recorded at
`research/notes/negative_pricing_randomness_input_family.md`):

- Closed door 3 already measured Thue–Morse with sublinear fold weight
  (`ν₂/n` decaying `0.27 → 0.011` across `n=100..4000`).
- The new sources show how strong that witness is: Thue–Morse has **level of
  distribution 1** and is **normal along Piatetski–Shapiro subsequences** — it is
  as statistically random as a deterministic sequence can be, on arithmetic
  progressions and sparse subsequences, *and still collapses the fold*.

So any Walsh/subset-sum bound on `wt(Φ_n h)` that derives from h being
well-distributed/normal/random-looking is refuted by Thue–Morse as a witness.
This was posted to the board (rising-sea, setting-is-wrong result) and narrows
the open request `walsh-spectral-subset-b904`: the needed input must live in
Φ's own submask-XOR reading, not h's progression/randomness profile — consistent
with the five closed doors and the second-pass conclusion.

## Attempted, not needed

I attempted to file a `request_research` for the `walsh-spectral-subset-b904`
gap with the new falsifier; the request was correctly refused because the library
already carries **8 bearing claims** on it (Donoho–Stark, Meshulam, Tao additive
uncertainty, Hofer, Spiegelhofer, Müllner–Spiegelhofer, plus the bounded-gap and
e_{n-2} witnesses). The gap is not a missing source — it is an unproven
mathematical statement, and the library now stakes out precisely what it cannot
be. No new request was posted.

## Not obtained

- The primary Shiu 2000 PDF (Wiley paywall) remains unobtainable; the run already
  holds the Ethan Yang expository reproducing its theorems (recorded in earlier
  passes). Not re-attempted.
- No other source was sought: the library's FRONTIER still holds hundreds of
  once-cited candidates, but the gap this pass could close (the Thue–Morse
  distribution pricing) is closed, and further accumulation would violate the
  "gather only against a stated gap" rule.

## Indexing

Both new source files and the new note are indexed and reachable via
`search_documents`. Both new claims are in the CLAIMS ledger.
