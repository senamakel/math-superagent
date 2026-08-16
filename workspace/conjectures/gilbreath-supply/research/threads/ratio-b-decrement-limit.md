# Ratio B decrement-ratio discriminator: does r_k keep falling or turn back to 1?

```thread
id: ratio-b-decrement-limit
question: >
  The prefix-variance null is log(N)/(4N); Ratio B = s2_N·4N/log N measures the
  primes' excess above it. Ratio B runs 1.443@1000 -> 1.392@4000 -> 1.361@10000
  -> 1.337@20000 -> 1.315@40000 -> 1.297@80000 — a persistent excess with
  per-doubling decrements whose consecutive RATIOS r_k = d_{k+1}/d_k are
  ≈0.623, 0.752, 0.899, 0.878 at full precision (the last step FALLS). The
  discriminator between the two limits is r_k: if r_k -> rho < 1 the decrements
  form a convergent geometric tail and Ratio B settles at a constant ABOVE 1
  (permanent structural excess); if r_k -> 1 the tail is non-summable and Ratio
  B tends to 1 (the primes become indistinguishable from uniform for this
  statistic). Which happens?
status: dead  (terminus — directive 33: hypothesis refuted by deliverable_3, run closes negative; see research/CONCLUSION.md)
rests-on: fair-variance-log-null-tail-clean-40000 (measured, mirrored in
  ROOT.md), extend-ratio-b-decade (N=80000, exact decrements)
blocked-by:
next: >
  Directive 30 — extend to N=160000 (one more doubling; this capture, or an
  unaffordable-runtime note, is the release condition for the absolute search
  freeze) with
  code/ratio_b/measure_ratio_b.py 160000, the existing capture pipeline. If
  unaffordable, report the projected runtime rather than substituting a
  smaller N: a smaller N cannot move the discriminator. Read only the
  full-precision decrement ratios; the rounded 0.875/0.905 set and the
  'rising toward 1' reading are operator artifacts, not data (directive 25).
```

## Why this question is the one that matters

The endpoint-sign investigation is abandoned (directive 29): its obstruction was
an instrument mismatch, not an open arithmetic question — see
`research/notes/endpoint-sign-abandoned.md`. This thread carries the redirect:
the decrement-ratio discriminator is the live question that already has a
working, guarded, streaming capture pipeline and whose answer decides the
meaning of the prefix-variance null. Ratio B tending to 1 would be the sharpest
possible framing of "the primes are asymptotically uniform for this statistic";
Ratio B settling above 1 would record a permanent structural excess. Either is
a genuine partial result; the current data cannot separate them.

The two extrapolations stated side by side, neither declared (measured, not
proved): geometric tail (ratio settled below 1) adds ≈0.171 for a limit ≈1.126;
a ratio drifting to 1 makes the tail diverge and Ratio B reach 1.
