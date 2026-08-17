# Refutation report — weakened rung `R-one-interior` (current rung)

**Refuter verdict: `proved` (hand + machine). The statement as stated is
trivially true; no counterexample exists even in the weakest abstract
encoding that is faithful.** This is a *positive* finding for the run: the
rung needs no attack, and its "merge" text (which treats it as the open entry
point into the interior-point regime) misdescribes it.

## Statement attacked

From `research/weakened/es-conjecture.md`, id `R-one-interior` (stance: open):

> For every n >= 4, every set of 2^(n-2)+1 points in general position with at
> most one interior point (a point strictly inside the convex hull of the set)
> contains n points in convex position.

## Hand argument (one line)

A set with at most one interior point has at least 2^(n-2) points ON its
convex hull; for n >= 4, 2^(n-2) >= n (equality at n=4; strict above), and any
n vertices of the convex hull of a general-position set are in convex
position. So the statement is TRUE with margin — the tightest case is n=4
(5 points, >= 4 hull vertices, need a convex quadrilateral = ES(4)=5, a proved
library claim).

The "content" the rung's merge text gestures at (hull has 2^(n-2)+1-k vertices,
trivial hull argument dies when k > 2^(n-2)+1-n) only engages at k >= 2
interior points — i.e. it belongs to `R-k-interior` with k >= 2, not to
`R-one-interior`. R-one-interior is the k=1 case and is a theorem.

## Machine results

TPTP problems under `code/refute/`:

1. `r-one-interior-n4.p` — tightest case n=4: 5 points, full general-position
   fragment (ccw totals antisym, cyclic), inside/triangle, interior
   (Caratheodory: in hull iff in some triangle of the other four), at-most-one
   interior, convex4 via the 4-point criterion.
   **Verdict: `proved`** (SZS Theorem) — the tool proved the conjecture from
   the axioms; no countermodel exists even abstractly in this faithful
   fragment.

2. `r-one-interior-n4-fullcc.p` — same case over the FULL Knuth CC-system
   axiom set (cyclic, antisymmetry, nondegeneracy, interiority, transitivity),
   convexity defined axiom-natively via hull edges (all-four-points-extreme).
   **Verdict: `proved`** (SZS Theorem). This is exactly the run's first
   encoder-validation rung: the abstract CC-system analogue of ES(4)=5 is
   true, consistent with the library's proved claims `es-exact-values`,
   `es35-four-criterion`.
   *(A previous buggy version returned `refuted`; the model was an artifact of
   contradictory guards making hull_edge/hull_vertex vacuous — diagnosed and
   fixed, re-proved. See call log.)*

3. `es4-equals-5-fragment.p` — diagnostic: same 4-point-criterion fragment
   WITHOUT the at-most-one-interior axiom. **Verdict: `refuted`**: a
   5-element abstract chirotope with no convex quadrilateral. NOT a real
   counterexample: it violates geometric possibility in the weak fragment
   (two points each strictly inside the other's triangle — impossible in the
   plane), and ES(4)=5 is proved. It is a concrete witness of the
   abstract-vs-realizable trap from problem.md: the weak axioms (cyclic +
   antisymmetry + totality, i.e. axioms 1-3) already admit non-realizable
   order types at n=5. The full CC axioms (interiority + transitivity, axioms
   4-5) exclude it, and with them the abstract statement proves.

## What the run should do with this

- `R-one-interior` should be marked **settled/trivial** (k=1 case of the
  hull-count argument; ES(4..6)=3,5,9,17 already confirm it). The interior
  points do not begin to matter until k >= 2 — that is `R-k-interior`, whose
  content the merge text actually describes.
- Within `R-k-interior`, the genuinely first nontrivial regime is NOT k=1 but
  the smallest n,k with 2^(n-2)+1-k < n and still (the interesting part)
  k *small relative to the hull deficit*: e.g. n=5, k=5? then hull >= 4 < 5,
  no hull argument... — the actual first case where the trivial argument dies
  is n=5, k >= 5? No: 2^(5-2)+1-k = 9-k; need 9-k < 5 i.e. k >= 5. So the
  first nontrivial regime is n=5, k>=5 interior points (hull <= 4 vertices),
  or n=4 (k>=2, hull <= 4... but n=4, hull>=5-2=3, need convex 4-gon in 3+2
  points — the tiny regimes are worth an exact enumeration as the first real
  rung after this one). Suggest making n=5, k=5 (9 points, >=4 hull, 5
  interior) the next machine target, not k=1.