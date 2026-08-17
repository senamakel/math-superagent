# Verdict — adjudication of "every full transversal of es_construct is convex"

Source run: `code/out/transversal_adjudication.py`, capture
`code/out/transversal_adjudication.captured.txt` (EXIT: 0).
Modules used (both VERIFIED, exact arithmetic throughout):
`lib.es_construct.es_set / es_set_blocks` and
`lib.es_geom.in_convex_position / largest_convex_subset /
in_general_position / convex_hull`. Quarantined modules
(`es_construction`, `es_lower`, `esz`) were NOT imported.

## Question

Is "every full transversal of `es_construct` is convex" —

- (a) a **structural consequence** of the construction's design (tiny
  clusters near distinct points on a strictly convex arc), or
- (b) a **genuine discovery** about extremal (n-avoiding) sets in general?

Full transversal = exactly one point from each block T_i, i = 0..n-2.

## Results (all exact, from the capture)

| Part | n=5 | n=6 |
| --- | --- | --- |
| A: point count | 8 | 16 |
| A: largest_convex_subset | 4 (=n−1) | 5 (=n−1) |
| B: full transversals, all convex? | 9, True | 96, True |
| C: hull vertices (= n−1), one per block in order | 4, True | 5, True |
| D: perturbed set, all transversals convex? (in GP) | 9, True | 96, True |
| E: circle-cluster set, largest_convex | 6 (≥5 ⇒ not 5-avoiding) | — |
| E: circle-cluster set, all full transversals convex? | 9, True | — |

- Part A reproduces the worked examples exactly (sanity: oracle + construction
  load correctly).
- Part B reproduces the transversal-convexity finding: n=5 → 9 transversals all
  convex; n=6 → 96 transversals all convex.
- Part C: `convex_hull(es_set(n))` has exactly n−1 vertices, taking exactly one
  point from each block, in block order [0..n-2]. This is the geometric basis
  (Conjecture A): centers on a strictly convex arc ⇒ hull picks one per block.
- Part D: replacing every point with an arbitrary tiny within-cluster offset
  (seeded, exact-scaled perturbation, set in general position) still yields all
  full transversals convex at n=5 and n=6. Convexity of transversals is stable
  under arbitrary within-cluster choice.
- Part E: moving the same cluster sizes (1,3,3,1) near 4 distinct points on a
  plain circle — NOT the ES arrangement — yields a set with largest convex
  subset 6 (so it is NOT 5-avoiding) yet ALL 9 full transversals convex.

## Statement of the lemma (verified)

> Clusters of points near distinct convex-position centers lying on a strictly
> convex arc ⇒ every full transversal (one point per cluster) is in convex
> position.

## Verdict

- **Parts C + D confirm this is a structural consequence of the construction's
  design — status: VERIFIED, NOT a discovery.** The mechanism is that the block
  centers lie on a strictly convex arc: the hull of the full set takes one
  point per block in block order, and convexity of a transversal is stable under
  arbitrary within-cluster choice, so any choice of one point per cluster yields
  a convex transversal.
- **Part E shows it does NOT characterize n-avoiding sets in general.** The
  forward direction fails: a generic tiny-cluster set on a convex arc has all
  full transversals convex without being n-avoiding (largest convex subset 6 at
  8 points). Hence transversal-convexity is a generic property of "tiny
  clusters on a convex arc", not a marker of n-avoidance.
- **No bearing on the ES upper bound.** The ES upper bound concerns *general*
  extremal sets, which are not confined to cluster-on-convex-arc configurations.
  This finding neither helps nor refutes ES(n) ≤ 2^{n-2}+1 for general sets.
