# Summary — Müllner & Spiegelhofer, "Normality of the Thue–Morse sequence along Piatetski–Shapiro sequences, II"

Source: C. Müllner, L. Spiegelhofer, *Normality of the Thue–Morse sequence along
Piatetski–Shapiro sequences, II*, Israel J. Math. (2017), DOI 10.1007/s11856-017-1531-x.
Full text: `research/sources/mullner_spiegelhofer_normality_piatetski_II.full.md`.
(Downloaded this run from arXiv:1511.01671.)

## What it establishes

- **Theorem 1 (normality along Piatetski–Shapiro).** For `1 < c < 3/2`, the sequence
  `u(n) = t(⌊n^c⌋)` is **normal**: for every `L ≥ 1` and every word `ω ∈ {0,1}^L`, the set
  of `n` for which `(t(⌊n^c⌋), …, t(⌊(n+L−1)^c⌋)) = ω` has asymptotic density `2^{-L}`.
  This improves the second author's earlier `1 < c < 4/3` and Mauduit–Rivat's `c < 1.42`
  (in the wider q-multiplicative setting).
- **Theorem 2.1 (level of distribution 2/3).** Thue–Morse satisfies a Bombieri–Vinogradov
  type theorem for each exponent `η < 2/3` — improving Fouvry–Mauduit's `0.5924`.
  (This is the precursor to Spiegelhofer's later level-1 result.)
- **Corollaries.** Every finite `{0,1}` word appears as an *arithmetic subsequence* of
  Thue–Morse (Cor 2.3); a quantitative two-parameter average version (Thm 2.4).

## Why it matters for SUPPLY / the reopened question

Together with `spiegelhofer-thuemorse-level-1`, this prices the "h is normal /
well-distributed" input family for the fold. Thue–Morse is not merely equidistributed —
it is **normal along fast-growing subsequences** (Piatetski–Shapiro, any `c < 3/2`), i.e.
as random-looking as a deterministic sequence can be, and its subword statistics match
the uniform model at every block length. Yet closed door 3 measures its fold weight
`ν₂/n` decaying `0.27 → 0.011` across `n = 100 → 4000`. So even a sequence that is normal
along arithmetic progressions *and* along Piatetski–Shapiro subsequences collapses the
fold. This is the strongest negative statement in the library about how "random" an
input can be while still refuting any linear-supply-from-randomness theorem.

```claim
id: mullner-spiegelhofer-normality-subsequence
statement: For 1 < c < 3/2 the sequence u(n) = t(⌊n^c⌋) is normal: each word ω ∈ {0,1}^L occurs along (t(⌊n^c⌋),…,t(⌊(n+L−1)^c⌋)) with asymptotic density 2^{−L}. Thue–Morse has an admissible level of distribution 2/3 (a Bombieri–Vinogradov theorem for each η < 2/3).
hypotheses: t the Thue–Morse sequence; Piatetski–Shapiro indices ⌊n^c⌋ with 1 < c < 3/2.
holds-here: Yes — t is closed door 3's model object (aperiodic, sublinear fold weight).
status: sourced (Müllner–Spiegelhofer 2017, Thm 1, Thm 2.1)
bearing: Strengthens the negative pricing: the sublinear-fold collapse witness Thue–Morse is normal along arithmetic AND Piatetski–Shapiro subsequences — as random as a deterministic sequence can be — yet its fold weight decays. No "h is normal / random / well-distributed" hypothesis can force linear supply. Reinforces request walsh-spectral-subset-b904: the needed input must be about Φ's submask-XOR reading, not h's raw distribution.
anchor: research/sources/mullner_spiegelhofer_normality_piatetski_II.full.md
```
