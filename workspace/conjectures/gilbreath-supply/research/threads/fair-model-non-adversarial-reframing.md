# Fair model is exact; the difficulty is non-adversariality (directive 10)

```thread
id: fair-model-non-adversarial-reframing
question: fair_model_exact.txt is stronger than labelled. Rank Φ_n = n−2 (full
  row rank, nullity 2) makes Φ_n surjective onto F₂^{n−2}, so every image has
  2² = 4 preimages and, for h uniform on the cube, wt(Φ_n h) is EXACTLY
  Binomial(n−2,1/2) — not a measured fit. Corollary (Chernoff): SUPPLY holds
  for a uniformly random h with probability 1−exp(−cn). The measured prime mean
  0.4977 sits on the random prediction 1/2. Therefore the entire difficulty is
  that the primes are not known to be non-adversarial for this fold. Which of
  the five closed doors does this reframing touch?
status: dead  (terminus — directive 33: hypothesis refuted by deliverable_3, run closes negative; see research/CONCLUSION.md)
rests-on: fold-rank-is-n-2-nullity-2-alternating (rank n−2, nullity 2),
  fair-model-exact-binomial (to be filed proved, directive 10)
blocked-by:
next: File `fair-model-exact-binomial` and `uniform-random-h-supply-w.h.p.` as
  proved (task establish-fair-model-exact-binomial-proved), print the ratio
  s2_N/(1/(4N)) (task fair-model-variance-ratio-null), and state the doors
  analysis: the reframing touches NONE of the five closed doors.
```

## Doors analysis (directive 10 asks this explicitly)

The five closed doors refute structural hypotheses of the form "h is
complicated enough" (weight alone, no-long-runs, aperiodicity, anti-dyadicity,
periodicity). The fair-model statement is about the fold on *uniform* input, so
it is orthogonal to all five and reopens none: all-ones remains in the kernel
(ν₂ = O(1)), Thue-Morse remains sublinear, anti-dyadic inputs remain bounded.
What it does is sharpen the target: a generic string already satisfies SUPPLY,
so the only open content is proving the prime string is not one of the rare
adversarial inputs — i.e. an arithmetic/correlation input on h (GOAL priority
2), or proving SUPPLY ⇔ switch density (GOAL priority 3). This does not touch
the switch-density reduction (still available-and-dead as a pointwise route).
