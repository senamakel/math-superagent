# Which h have linear supply — the weight threshold where it becomes typical

Directive 38 names this as the productive next step of the second pass: the
fold's supply class, characterised by Hamming weight. One extreme point is
pinned (h = e_{n-2}: switch density 0, linear supply via the odd-depth
mechanism). The question is where the class's bulk begins.

```thread
id: supply-class-characterisation
question: Which binary strings h have linear supply nu2(h)/n bounded below by
  c > 0 for all large n? With one extreme point known (per-window h = e_{n-2}:
  switch density 1/n -> 0, nu2(n) = ceil((n-2)/2) ~ n/2), what is the minimum
  weight w at which linear supply becomes typical rather than exceptional among
  weight-w strings? If linear supply is generic even at very low weight, the
  arithmetic input the primes need is correspondingly weak — and naming how
  weak is the deliverable this pass exists to produce.
status: live
rests-on: enminus2-linear-supply-switch-density-not-necessary,
  fixed-single-1-fold-weight-bounded-by-j,
  single-boundary-one-refutes-switch-equivalence-as-stated
blocked-by:
next: Directive 39 — the class's bulk begins near w/n ≈ 0.125: linear supply is
  typical (mean nu2/n >= 0.40, frac >= 0.5) at w/n = 0.375@8 falling 0.300,
  0.250, 0.188, 0.156 to 0.125@64 and 0.125@128 (two consecutive n). Two tasks
  in order: (1) task linear-supply-threshold-limit — push n as far as the
  sampled method allows (300 samples per weight bounds the frac column) and
  say whether the threshold ratio tends to 0 or plateaus near 1/8, without
  declaring beyond the data; (2) task linear-supply-threshold-claim-block —
  file the claim block stating in ONE sentence the gap: typical is not this
  string — being above the threshold does not prove the primes' h has linear
  supply (the first pass's genericity gap). The result is a density bound near
  1/8 instead of full switch density. problem.md result type 4, NOT type 1;
  never SUPPLY-solved or prime-specific.
```
