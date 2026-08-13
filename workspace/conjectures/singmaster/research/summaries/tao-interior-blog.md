# Tao's blog post on MRSTT — Singmaster's conjecture in the interior

Source: https://terrytao.wordpress.com/2021/06/07/singmasters-conjecture-in-the-interior-of-pascals-triangle/
Author's own expository account of arXiv:2106.03335 (the run's primary source is the
paper; this is a secondary confirmation from a coauthor). [[tao-interior-blog]]

## Confirms (with the author's framing)

- The record: largest known multiplicity is 8, `t=3003` with the eight
  `(n,m)` listed. The symmetry `C(n,m)=C(n,n−m)` justifies restricting to the left
  half.
- **Theorem 1** = MRSTT Theorem 1.3 (≤2 per half, ≤4 total; ≤1 in the smaller
  sub-region).
- To prove Singmaster in full it suffices to handle the **boundary region**
  `2 ≤ m < exp((log n)^{2/3+ε})` (and its mirror); `m=1` is deleted as it always
  gives exactly one solution. Possible that for large `t` there are *no* further
  collisions in this region, which would give ≤8 solutions — this claim is known
  only for **bounded** `(m,m′)` via Beukers–Shorey–Tijdeman (Siegel's theorem).
- The two-bound is best possible (infinite Fibonacci family (4)).
- **Archimedean half**: `n = f_t(m)` real-analytic, `f''_t(m) ≍ f_t(m)(log t/m²)²`;
  convexity + **Pick's theorem**: a cluster of three graph lattice points would give
  an area between 0 and 1/2, contradiction. Yields Proposition 2 (≤1 other solution
  within distance `exp((log₂t)^{1−ε})`).
- **Non-Archimedean half**: p-adic valuations + Legendre; collision iff (6) holds
  for all primes; draw `p` random in `[P, P+P log^{-100} P]`, compare correlations.
  The exponential sums `Σ_{P≤p≤P+P log^{-100}P} e(N/p + M/p^j)` need Vinogradov,
  nontrivial in `N,M ≪ exp((log P)^{3/2−ε})`, giving the distance bound
  `m′−m ≪_ε exp((log(n+n′))^{2/3+ε})`.
- **Comment thread — the method's ceiling (author's own words, 16 Jun 2021)**: what
  is needed is `Σ_{P≤p≤2P} e(N/p) = o(P/log P)`; Vinogradov gives it for
  `N ≪ exp((log P)^{3/2−ε})`, pseudorandomness heuristics predict `N ≪ exp(P^c)`
  (would give interior range `log^C n ≤ m ≤ n − log^C n`). RH "morally" gives
  `Σ e(N log p) = o(P/log P)` for such a wide range — but that is a *different*
  phase, and **no direct connection** between the two estimates could be found.
  Also (9 Apr 2021 comment): for `(2,3)`-type small pairs and the boundary, Tao
  suggests the **determinant method** (Bombieri–Pila) as a possible route to
  improve the total bound, but notes the key difficulty is quantitative control of
  intersections of the solution set with algebraic curves.

## Bearing for this run

Reinforces MRSTT's `mrstt-method-limit`: the `2/3` interior exponent and the
`exp((log P)^{3/2−ε})` Vinogradov barrier are genuine, author-confirmed walls. The
boundary region `2 ≤ m ≤ (log t)/(log₂t)^{3/2−ε}` remains the entire open problem,
and the only known tool there (BST/Siegel) is ineffective. The determinant-method
comment is a recorded suggestion, not a result — no effective bound follows from it
here.

```claim
id: tao-boundary-and-method-ceiling
statement: Tao's blog (coauthor exposition) confirms: interior theorem reduces
  Singmaster to the boundary 2<=m<exp((log n)^{2/3+eps}) (mirror), where only
  ineffective BST/Siegel-known bounded-(m,m') results exist; the Vinogradov barrier
  N,M << exp((log P)^{3/2-eps}) in the exponential-sum method cannot be relaxed to
  exp(P^c) except by unproven randomness heuristics, and RH gives a different (log p)
  phase with no known connection.
hypotheses: 0<eps fixed; t large.
holds-here: yes.
status: asserted (author's expository account + comments; confirms the paper's own
  statements)
bearing: names the boundary region as the entire remaining gap and the method's
  ceiling; no effective bound is produced.
anchor: research/summaries/tao-interior-blog.md
```
