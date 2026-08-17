# Research findings — adjudication of three candidate approaches (durable record)

Status date: current run. These are source-backed findings. The memory server was
down, so this file is the durable record; re-file to Cognee when it recovers.

## 1. Convex-4-set supersaturation — REFUTED by a counting identity

**The covering inequality reduces to an always-true density floor and cannot force N.**
By the 4-point criterion (claim `es35-four-criterion`, proved) a set is in convex
position iff every 4-subset is convex. So an n-avoiding set's NON-convex 4-sets must
4-uniformly cover the n-subsets: every n-subset contains ≥1 non-convex 4-subset.
Double-counting gives (nnc = #non-convex 4-sets):

    nnc · C(N−4, n−4)  ≥  C(N, n)

But C(N,n)/C(N−4,n−4) = [N(N−1)(N−2)(N−3)]/[n(n−1)(n−2)(n−3)] = C(N,4)/C(n,4).
So the inequality is exactly

    nnc  ≥  C(N,4) / C(n,4)

i.e. "at least 1/C(n,4) of all 4-sets are non-convex". Since the maximum nnc is
C(N,4), this is automatically satisfied by ANY set with at least one non-convex
4-subset — for EVERY N (including N = 2^{n-2}+1). It never tightens; there is no
"strict violation at 2^{n-2}+1". To bound N from above one would need an UPPER bound
nnc < C(N,4)/C(n,4) for n-avoiding sets, but n-avoiding sets are the MOST
non-convex-rich (they avoid larger convex subsets precisely by making many 4-sets
non-convex), so no such bound exists. Wrong direction.

**The real convex-4-set density results are 4^k-type, not 2^{n-2}.**
- Balogh & Salazar, "k-Sets, Convex Quadrilaterals, and the Rectilinear Crossing
  Number of Kn", DCG 38 (2006), doi 10.1007/s00454-005-1227-6: every n-point set has
  ≥ 0.37553·n^4 + O(n^3) convex quadrilaterals (via k-sets / circular sequences).
- This is the k=4 instance of Erdős's minimum-number-of-convex-k-gons question
  (Morris–Soltan survey doi 10.1090/S0273-0979-00-00877-6, Problem 5.1), whose values
  are 4^k-type, never 2^{n-2}.

So the density counting surface the candidate names is real but gives ~4^k growth, and
the covering direction invoked is refuted on safety. Overlaps structurally with the
convexity-complex-fvector "Kruskal–Katona goes the wrong direction" verdict.

## 2. Layer transfer matrix — NOT grounded; silent literature; placement-dependence hazard

**Named machinery is real but never applied to ES/convex layers.** Transfer-matrix /
Fekete subadditivity is standard (used for the *asymptotic* ES bounds → 2^{n+o(n)},
Suk arXiv:1604.08657; Holmsen–Mojarrad–Pach–Tardos arXiv:1705.10795 — context-only, not
exact). A transfer matrix over convex-n-gon structures appears in Jiménez–Kiwi–Loebl
"Counting triangulations of a convex n-gon" (arXiv:0912.3514) — but that's a
triangulation state-count, not an ES upper bound.

**The onion-layer premise is placement-dependent.** The run's own layer-extremality
claim (es-construct-layer-extremality) verifies at n=5,6,7 that each onion layer of
es_construct is maximally convex, but the LAYER PROFILES are realized placement
artifacts ([3,1],[4,4],[5,5,3,3],[6,6,6,5,6,3]) and NOT the order-type-determined
binomial blocks. A DP over "the actual onion layers" is a function of placement, so it
cannot carry a universal ES bound over order types unless shown realization-independent
— neither established.

**No theorem delivers the eigenvalue-2/max-chain ≤ 2^{n-2} claim.** Literature is
silent on the specific claim (absence, not a refutation). Decisive empirical check: run
the same DP on a SECOND no-convex family (Károlyi–Tóth twin T_n, claim
karolyi-toth-twin-construction, |T_n|=2^n no 2^n+1 convex pts) and Aichholzer order
types (aichholzer-order-db) before any graduation. Status stays proposed.

## 3. Polar-arrangement Euler-levels — REFUTED (dual problem is different and 4^n)

**The polar dual is NOT the point-ES problem; its bounds are 4^n-type.**
- Bárány–Roldán-Pensado–Tóth, "Erdős–Szekeres theorem for lines", arXiv:1307.5666,
  Thm 1.1: for ES_L(n), least #lines forcing n lines bounding a convex n-cell,
  `2^{n-4}·⌊n/2⌋−1 ≤ ES_L(n) ≤ C(2n-4, n-2)`, i.e. lower ~4^n/n and upper ~4^n/√n.
- They state explicitly: in the AFFINE plane the point and line versions are NOT dual
  to each other — "the dual of the convex hull of n points is not a cell (or an n-cell)
  in the arrangement of lines dual to the points." Only caps/cups duality survives,
  giving ESl(n) ≤ ES(2n).
- Furukawa "Happy Ending or Many Concurrent Lines" arXiv:2409.03122: order of ES_L(n)
  is 4^n/n^α, 1/2 < α < 1.
- So an Euler-characteristic / zone / level / face-count argument in the dual
  reproduces exactly the known ~4^n loss (the mechanism's own predicted falsifier is
  CONFIRMED in the literature). There is no Euler/zone result improving this to
  2^{n-2}.

**The Goodman–Pollack pseudoline conjecture is itself open.** Nps(n) ≤ 2^{n-2}+1 is an
open conjecture (Morris–Soltan §5.5; claim ms-dual-esz-pseudoline-bound), and the
signotope analogue is open and equivalent (claim baek-balko-signotope-analogue-open).
So the dual formulation restates the difficulty rather than removing it — same
faithful-restatement verdict as convex-geometry-order-dimension and
convexity-complex-fvector.

## Status summary
- `layer-transfer-matrix`: proposed (not grounded, not refuted — literature silent,
  placement hazard) → file updated.
- `convex-4set-supersaturation`: REFUTED (covering identity always-true, wrong side) →
  file updated, killed-by.
- `polar-arrangement-euler-levels`: REFUTED (affine duality is not the point problem;
  dual bounds are 4^n; GP conjecture open) → file updated, killed-by.
