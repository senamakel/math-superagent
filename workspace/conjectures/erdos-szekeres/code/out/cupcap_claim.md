# Cup–cap convex-position characterization (G-cupcap) — verified

This run's own exact-arithmetic check of the Erdős–Szekeres (1935) cups-and-caps
characterization of convex position. Output of the run: `code/out/cupcap_verify.txt`.

```claim
id: g-cupcap-verified
statement: For any planar point set X in general position with distinct x-coordinates,
  X contains n points in convex position iff there exist k in {2..n}, a k-cup C and
  an (n+2-k)-cap D in X that share their leftmost and rightmost points (by x) and
  whose union is exactly n points in convex position.
hypotheses: general position (no 3 collinear), distinct x-coordinates, n in 3..|X|.
holds-here: true
status: checked
bearing: confirms the classical cup/cap route to convexity that everything in ES uses;
  also shows "sharing both x-extreme points" was sufficient for convexity in every
  observed case (0 nonconvex shared-extreme pairs seen, though such pairs are plentiful).
anchor: code/out/cupcap_verify.txt -- 624 sets, 1220 (set,n) cases, 1220 agreement, 0 mismatch.
```

## Numbers

- sets checked: **624** (58 exhaustive subsets of {0,1,2}² in general position
  with distinct x, 202 + 364 random small sets)
- (set, n) cases: **1220**
- agreement between oracle (`largest_convex_subset(X) >= n`) and the
  cupcap predicate (`exists_cupcap(X,n)`): **1220 / 1220**
- mismatches: **0**
- disagreements between the lib helpers `is_cup`/`is_cap` and an independent
  Fraction-from-definition reference, over every subset of every tested set: **0**

## Method

- `is_cup` / `is_cap` (exact, `lib/cupcap.py`): sort by x, compare consecutive
  slopes with rational arithmetic (Fraction); require distinct x.
- `exists_cupcap(X, n)` (exact): brute force over all subsets, checking
  existence of a k-cup C and (n+2−k)-cap D sharing leftmost and rightmost
  indices by x with C∪D = n points in convex position (hull test from
  `lib/es_geom`).
- Oracle side: `largest_convex_subset` (exact hull test, `lib/es_geom`).
- Both directions compared for EVERY (set, n); the program exits non-zero if
  any mismatch or any lib-vs-reference cup/cap disagreement is found.

## Independent confirmation of both directions

Two independent routes agree everywhere: the convex-position hull oracle and the
explicit cup/flat-cap decomposition. This is brute-force on small sizes only (a
legitimate oracle; sets up to 8 points, all their subsets), not a search over the
answer space of the conjecture.
