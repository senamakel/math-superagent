```thread
question: Keyed on MINIMAL period, why does the F₂ transfer die exactly on dyadic-periodic h (minimal period a power of 2), and what anti-dyadic property of the prime halved-gap bit string restores ν₂ ≥ c·n?
status: dead — Directive 74: the dyadic skeleton is CLOSED. SPAD-linearization discharged; SPAD-dyadic-collapse discharged (dyadic-collapse-proved); SPAD-anti-dyadic-linear REFUTED (spad-nondegenerate-linear-refuted); SPAD-prime-anti-dyadic proved-but-inert, CONDITIONAL on Shiu 2000 (asserted, paywalled). Every gap resolved and the route delivers nothing toward the supply bound; ν₂ ≥ c·n for the primes stays the named-open abgs-2011-s9-mod4-switch-limit-open.
rests-on: rule90-interior-xor, g-supply-transfer-universal-refuted, transfer-matrix-kernel-allones, g-supply-transfer-measured, granville-lucas-kummer-sierpinski, dyadic-collapse-proved, dyadic-oddfactor-infimum-bounded, thue-morse-sublinear-supply-witness
blocked-by: none yet
next: |
  CLOSED by Directive 74 — write the deliverable (solution.md), do not re-open
  this thread. Historical guidance below is superseded.
  Directive 72 — index forensics STOOD DOWN (root cause is the Rust deriver's
  MAX_FILES=400, operator fixing outside the mount). Return to the mathematics:
  the one rung of this skeleton neither proved nor refuted is
  SPAD-prime-anti-dyadic ('the prime switch bit h is not eventually 2^k-periodic'),
  which is open-but-VACUOUS for supply after the refutation below — discharging it
  closes the dyadic skeleton as a negative result only; ν₂ ≥ c·n stays
  abgs-2011-s9-mod4-switch-limit-open. Mersenne per-period supply density decays
  like (3/4)^k (see dyadic-mersenne-elementwise-constants.md) — even the linear
  families weaken.

  Directive 68 — the CONVERSE is REFUTED and written up (claim
  spad-nondegenerate-linear-refuted, research/notes/spad-nondegenerate-linear-refuted.md).
  Half-step strings h=1^{a}0^{a} are balanced AND anti-dyadic yet collapse on
  the power-of-two subsequence: wt(Φh)=1 exactly at a=2^k, ratio→0 there
  (0.125@8, 0.0625@16, 0.0313@32); at non-power-of-two a it is a LARGER power
  of two (m=18: wt 8, 0.444; m=34: wt 16, 0.471; m=66: wt 32, 0.485), so wt/m
  has NO limit (liminf 0, limsup 1/2) — the refutation stands via the 2^k
  subsequence only (see dyadic-halfstep-fold-classification-checked). Thus
  anti-dyadic does NOT imply linear supply; the fold matrix Φ has low-weight
  images on structurally rich inputs. The dyadic COLLAPSE theorem survives
  (dyadic-collapse-proved, period 2^k ⟹ ν₂ = O_k(1)); only its converse is dead.
  The original question of this thread ("which anti-dyadic property of the prime
  h restores ν₂ ≥ c·n") is ANSWERED in the negative: no structural property of h
  restores it. ν₂ ≥ c·n for the primes reverts to the named-open arithmetic
  hypothesis abgs-2011-s9-mod4-switch-limit-open.

  Housekeeping left open: dyadic_halfstep_large.captured.txt prints no depth
  bound (Directive 67 rule 3) — re-capture to a NEW file with depth/width/m
  printed. Task file-antidyadic-converse-refutation tracks it.

  (Historical, superseded by the refutation above.) Directive 67: stream the
  triangle, never materialise it. Directive 66: density gate CLOSED — inf_n
  nu2/n positive for P=3,5,7,9 to n=20000; the odd-factor converse is
  numerically supported but stays CONJECTURED, and by the refutation it does
  not bridge to the primes. Thue–Morse is aperiodic with nu2 = O(log n)
  (thue-morse-sublinear-supply-witness): aperiodicity was already insufficient.

  Directive 60. The collapse side is PROVED for power-of-2 periods (claim
  `dyadic-collapse-theorem`, status proved); the over-general "any period"
  claim is REFUTED (rule90-periodic-window-collapse-refuted): odd-factor
  periods grow (period 3 -> nu2=2666 at n=4000). G-supply (nu2 >= c*n for the
  aperiodic primes) stays the named-open two-point mod-4 hypothesis
  (abgs-2011-s9-mod4-switch-limit-open). Do not claim the dichotomy closes
  G-supply.
```
