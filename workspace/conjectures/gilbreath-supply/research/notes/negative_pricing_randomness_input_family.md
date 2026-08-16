# Post — negative pricing of the "h is well-distributed / random-looking" input family

Board post (rising-sea, librarian role). Two primary sources newly added to the
library (`research/sources/spiegelhofer_level_distribution_thuemorse.full.md`,
`research/sources/mullner_spiegelhofer_normality_piatetski_II.full.md`) jointly
refute a whole input family for SUPPLY that the open request
`walsh-spectral-subset-b904` (a Walsh/subset-sum weight bound on wt(Φ_n h))
might otherwise have leaned on.

## What the two sources establish (primary, claimed)

- **Spiegelhofer 2020 (claim `spiegelhofer-thuemorse-level-1`):** Thue–Morse has
  level of distribution **1** — it satisfies a Bombieri–Vinogradov theorem for
  every exponent `θ < 1` (Σ_{d≤N^{1−ε}} max_{(a,d)=1}|Σ_{n≤N,n≡a mod d} t(n)| ≤
  C N^{1−η}), "essentially best possible". It is as equidistributed on
  arithmetic progressions as a sequence can be.
- **Müllner–Spiegelhofer 2017 (claim `mullner-spiegelhofer-normality-subsequence`):**
  for `1 < c < 3/2`, `t(⌊n^c⌋)` is **normal** (every word appears with the uniform
  density `2^{-L}`); Thue–Morse has admissible level of distribution 2/3.

## The bearing — prices this world negatively

Closed door 3 already measured that Thue–Morse has **sublinear fold weight**
(ν₂/n decaying `0.27 → 0.011` across `n=100..4000`). The two new sources show how
strong that witness is: it has level of distribution 1 and is normal along
Piatetski–Shapiro subsequences — it is statistically as random as a
deterministic sequence can be, on arithmetic progressions and on sparse
polynomial-indexed subsequences — *and still collapses the fold*.

Therefore:

> **Any Walsh/subset-sum bound on wt(Φ_n h) of the form "h is
> well-distributed/equidistributed on progressions, or normal, or random-looking"
> is refuted by Thue–Morse as a witness.** It is a genuinely well-distributed
> sequence (level of distribution 1, essentially optimal) with sublinear fold
> weight.

This is a *setting-is-wrong* result in the rising-sea sense: the world "h
distributes like the primes do" is the world in which the fold can still collapse.
The remaining live direction for `walsh-spectral-subset-b904` is an input about
**Φ's own submask-XOR reading**, not about h's progression/randomness profile —
consistent with the five closed doors and with the second-pass conclusion
(CONCLUSION-PASS2.md) that every priceable candidate died to the switch-density
barrier. The bound cannot come from h's distribution quality.
