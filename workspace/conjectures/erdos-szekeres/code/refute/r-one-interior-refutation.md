# Refutation report — weakened rung `R-one-interior` (current rung)

**Refuter verdict: `proved` (hand + machine).** The statement as stated is
trivially true; no counterexample exists even in the weakest faithful abstract
encoding. This is a *positive* finding for the run: the rung needs no attack,
and its "merge" text (which treats it as the open entry point into the
interior-point regime) misdescribes it — that content belongs to `R-k-interior`
with k ≥ 2.

## Statement attacked

From `research/weakened/es-conjecture.md`, id `R-one-interior` (stance: open;
the weakened ledger currently still lists it `open` despite the earlier report):

> For every n >= 4, every set of 2^(n-2)+1 points in general position with at
> most one interior point (a point strictly inside the convex hull of the set)
> contains n points in convex position.

## Hand argument (one line, covers ALL n)

A set with at most one interior point has at least 2^(n-2) points ON its convex
hull. In general position every hull point is a vertex of the convex hull, and
the hull vertices of a finite planar set are in convex position. Since
2^(n-2) >= n for every n >= 4 (equality at n=4, strict above), the hull alone
supplies n points in convex position.

Crucially, this is the regime where there is NO chirotope/realizability gap:
hull vertices are extreme in every realization, so "hull vertices in convex
position" holds for every realizable order type. The tightest case n=4 (5
points, ≥4 hull vertices, need a convex quadrilateral) is exactly the proved
claim ES(4)=5 (library: `es-exact-values`, `es35-four-criterion`).

## Machine results (fresh runs, this session)

TPTP problems under `code/refute/`, both re-verified by `find_counterexample`
this session:

1. `r-one-interior-n4.p` — tightest case n=4 (5 points), weakest faithful
   fragment (general-position ccw totals + cyclic symmetry; inside/triangle;
   interior via Caratheodory — in hull iff in some triangle of the other
   points; at-most-one-interior; convex4 via the 4-point criterion).
   **Verdict: `proved`** (SZS Theorem) — no countermodel even abstractly in
   this faithful fragment. Capture: `code/out/refute/code_refute_r-one-interior-n4.p.json`
   (finding=proved, status=Theorem).

2. `r-one-interior-n4-fullcc.p` — the same n=4 case over the FULL Knuth
   CC-system axiom set (cyclic, antisymmetry, nondegeneracy, interiority,
   transitivity), convexity defined axiom-natively via hull edges (all four
   points extreme). **Verdict: `proved`** (SZS Theorem) — the abstract CC-system
   analogue of ES(4)=5 is true. Capture:
   `code/out/refute/code_refute_r-one-interior-n4-fullcc.p.json`
   (finding=proved, status=Theorem). This is also the run's first
   encoder-validation rung: the abstract statement agrees with the proved
   geometric claim.

3. `es4-equals-5-fragment.p` — diagnostic: the SAME 4-point-criterion fragment
   WITHOUT the at-most-one-interior axiom (so, over the weak axioms 1-3 only).
   **Verdict: `refuted`**: a 5-element abstract chirotope with no convex
   quadrilateral. This is NOT a real counterexample: it violates geometric
   possibility in the weak fragment (the model has two points each strictly
   inside the other's triangle — impossible in the plane), and ES(4)=5 is
   proved. It is a concrete witness of the abstract-vs-realizable trap from
   problem.md: the weak axioms (cyclic + antisymmetry + totality) already admit
   non-realizable order types at n=5. The full CC axioms (interiority +
   transitivity) exclude it, and with them the abstract statement proves.

## What the run should do with this

- Mark `R-one-interior` **settled/trivial** — it is the k=1 case of the
  hull-count argument, and it is TRUE with margin (ES(4..6)=3,5,9,17 already
  confirm it).
- The interior points do not begin to matter until k >= 2 — that is
  `R-k-interior`, whose content the merge text actually describes.
- Within `R-k-interior`, the genuinely first nontrivial regime is the smallest
  n,k with 2^(n-2)+1-k < n: that is 2^(n-2)+1-k < n, i.e. k > 2^(n-2)+1-n.
  First instance: n=5, k >= 9-5+1... compute: 2^(5-2)+1 = 9; hull has 9-k
  vertices; need 9-k < 5 i.e. k >= 5. So n=5, k=5 (9 points, hull <= 4, 5
  interior) is the first machine target, not k=1.

## Recoed via

Hand proof + two fresh `find_counterexample` runs (SZS Theorem x2). Existing
prior report `research/weakened/R-one-interior-refutation-report.md` reaches
the same verdict; this note re-confirms it and resolves the ledger's stale
`open` stance.
