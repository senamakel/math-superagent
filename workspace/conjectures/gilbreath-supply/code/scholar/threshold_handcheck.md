# Independent hand-verification of the threshold formula logic

The exact-mean closed form behind the third-pass threshold column
(`threshold-mean-exact-parity-formula`) was checked by hand arithmetic,
independent of the program, as an oracle check of its *logic*:

For weight-w strings of length n, a depth-d cell reads k = 2^popcount(d)
positions, and is odd (T(n,d)=1) for
`(C(n,w) − [z^w](1−z)^k(1+z)^{n−k}) / 2` of the weight-w strings. The n=8, w=1
case:

- cells d ∈ [2,7]: d=2,4 → pc 1, k=2 (two cells); d=3,5,6 → pc 2, k=4 (three
  cells); d=7 → pc 3, k=8 (one cell).
- `[z^1](1−z)^k(1+z)^{8−k} = (8−k) − k = 8−2k`, so
  `P_d(1) = (8 − (8−2k)) / 16 = 2k/16 = k/8`: k=2 → 1/4, k=4 → 1/2, k=8 → 1.
- `Σ_d P_d(1) = 2·(1/4) + 3·(1/2) + 1·1 = 0.5 + 1.5 + 1 = 3.0`; `mean = 3/8 =
  0.375`.

This reproduces the capture's `0.375` at n=8 and the exhaustive
`linear_supply_by_weight.txt` (8→3). The formula's arithmetic is therefore
matched by a route that does not share the program's code.

No mechanical re-run is recorded here: this environment cannot execute
scripts. The pass's full captures were already verified by tool_builder's
independent code path (`code/out/threshold_exact_mean_independent.txt`,
digit-for-digit to n=16384).

The surrounding third-pass findings and their durable statement are in
`research/notes/scholar_pass_third_presence.md` and the conclusion
`research/CONCLUSION-PASS3.md`.
