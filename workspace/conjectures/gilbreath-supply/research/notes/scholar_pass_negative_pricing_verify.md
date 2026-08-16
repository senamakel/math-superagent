# Scholar pass — verify the two new Thue–Morse sources and persist findings

Reviewing the two primary sources added this cycle (`spiegelhofer_level_distribution_thuemorse`,
`mullner_spiegelhofer_normality_piatetski_II`) against their full texts, and storing the run's
durable findings in Cognee (which was **empty** despite two passes — nothing had ever been stored).

## What was verified against the full texts

- **Spiegelhofer 2020** (`spiegelhofer-thuemorse-level-1`): line 445-450 of the full text confirms
  Theorem 2.1 verbatim: level of distribution 1, `sum_{1<=d<=D} max_{y,z, z-y<=x} max_{0<=a<d}
  |A(y,z;d,a) - y/(2d)| <= C x^{1-eta}` for `x>=1, D = x^{1-eps}`. The digest's statement,
  hypotheses, and constants match the source. The theorem closes the normality gap to `1 < c < 2`
  (line 415-420: "finally closes the gap" from `[1.5,2)` and note `c>2` still open).
- **Müllner–Spiegelhofer 2017** (`mullner-spiegelhofer-normality-subsequence`): Corollary 2.3
  (every finite 0/1 word appears as an arithmetic subsequence of Thue–Morse) and the Piatetski-
  Shapiro normality (Theorem 1, `1 < c < 3/2`) are confirmed. The digest's `2/3` level of
  distribution is Theorem 2.1 of that paper.

Both digests are faithful; no corrections were needed.

## Contradiction check (none found)

The two new claims are **consistent** with the existing `konieczny-thuemorse-gowers-uniform-exponential`
(Konieczny 2019: Thue–Morse is Gowers-uniform of all orders with exponential dyadic decay). The three
are mutually reinforcing statements of the same "how random can the collapse witness be" fact across
three distinct notions of randomness (progressions / subsequence normality / Gowers uniformity). They
reinforce, rather than contradict, the negative pricing and the five closed doors.

## What I stored (Cognee)

Two durable, source-backed findings:
1. The **negative pricing** of the "h is well-distributed / random / normal" input family: Thue–Morse
   has level of distribution 1 AND is normal along Piatetski–Shapiro subsequences yet has sublinear
   fold weight, so no Walsh/subset-sum bound of that form can force linear supply. The needed weaker
   input must live in Φ's submask-XOR reading (`walsh-spectral-subset-b904`, still open).
2. The **proved core** of the fold: rank n−2 / nullity 2 kernel, exact Binomial(n−2,1/2) weight
   distribution under uniform h, E[S²]=n−2, and the single surviving open statement
   (E[S²]=O(n) for the prime h from an input weaker than switch density).

These are now recallable across runs. Nothing contradicts recalled memory (the store was empty).
