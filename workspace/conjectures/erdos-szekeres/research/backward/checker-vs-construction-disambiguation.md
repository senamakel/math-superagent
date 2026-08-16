# Disambiguation: the es_geom checker is correct; the constructions are broken

```claim
id: es-construction-broken-integer
statement: The integer lower-bound construction `es_lower_set` (code/lib/es_construction.py)
      does NOT have the ES property. At n=4 it reports largest convex subset 4 (want 3); at
      n=5 it reports 8 points with general position FALSE (collinearities introduced by
      integer rounding) and largest convex subset 5 (want 4); at n=6, 16 points not in general
      position, largest convex subset 8 (want 5); at n=7, 32 points, hasConvex7-gon=True.
hypotheses: exact oracle (lib.es_geom) is correct
holds-here: yes -- the checker was independently verified on hand-known sets (below)
status: checked
bearing: the ES lower-bound construction that every later structural argument is measured
      against is broken and must be rebuilt before any argument rests on it.
anchor: code/out/check_esz_construction.py output, captured in commands.log and re-run
```

```claim
id: es-construction-broken-rational
statement: The rational reconstruction `es_set` (code/lib/esz.py) is also broken. At n=4 it
      correctly gives largest convex subset 3 (PASS: 4 points, no convex 4-gon); but at n=5 it
      gives largest convex subset 6 (want 4), and at n=6 gives 9 (want 5) with general position
      True -- so the failure is NOT collinearity but a genuine convex k-gon present. Even the
      block T_2 = g(4,4) at n=6 reports longest cup 4 when the construction requires "no (n-i)-cup"
      = "no 4-cup", i.e. the block-level cup bound is violated.
hypotheses: exact rational construction, exact oracle
holds-here: yes
status: checked
bearing: the recursive g(a,b) merge or its flatness/scale stage is wrong; the block's own
      no-cup/no-cap invariant fails.
anchor: code/lib/esz.py self-test output (n=5:6, n=6:9)
```

## The checker is exonerated (step 1 of the directive)

Ran `code/checker_disambiguation.py` against `lib.es_geom`, exact integer arithmetic, on sets
whose answers are known by hand. Every case passed:

| set | N | maxConvex | want | verdict |
| --- | --- | --- | --- | --- |
| circle k=4,5,6,7,12,16 | k | k | k | PASS |
| parabola k=4,5 (cup, all convex) | k | k | k | PASS |
| triangle + interior point | 4 | 3 | 3 | PASS |
| square (4 convex) | 4 | 4 | 4 | PASS |
| 4 pts one strictly inside | 4 | 3 | 3 | PASS |

So the error is not in `orient`/`convex_hull`/`in_convex_position`/`largest_convex_subset`.
By the directive's exclusion, the construction is at fault. For the integer builder the failure
is physical (rounding creates collinear triples AND a convex 4-gon at n=4); for the rational
builder the failure is logical (a real convex k-gon that should not exist, and a violated
block cup bound).

## What the run must do

Do NOT build any structural argument on these constructions until a correct one is produced,
verified against the (correct) oracle at n=4,5,6,7, and captured. Correctness criteria:
N=2^{n-2}, general position True, largest convex subset == n-1 (equivalently no convex n-gon).
