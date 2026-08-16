# SUPERSEDED / DISCARDED (directive 42 + solver) — do not read as a result

The claim this note once filed (`kstar-budget-not-ceil-n-over-2`) is
**wrong and discarded**. Its irregular `B(n) = 1,1,2,2,4,5,5,7,8,8,10,11,8,13,14,12,16`
sequence came from the single-`(K+1)`-gram histogram `C_K` taken alone as the
fiber, not the cumulative `C_1..C_K` reading that `REOPENED.md`'s own correction
established as authoritative. Its output is self-refuting: `B(14)=8 < B(13)=11`
violates the monotonicity the definition provably forces, which is proof of the
wrong fiber definition, not a new finding.

The operative budget is settled: **`K*(n) = floor(n/2)`**, `n=2..18`, by five
captures (`kstar_exact`, `kstar_settle`, `kstar_resolve`,
`kstar_structural_capture`, `cum_floor18`) and two independent cumulative
implementations. The imported `⌈n/2⌉` table had already been superseded to
`floor(n/2)` before this note was written. Nothing in this file is citable.
