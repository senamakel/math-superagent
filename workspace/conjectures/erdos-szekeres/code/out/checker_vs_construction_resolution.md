# Resolution: checker vs ES lower-bound construction — the construction is defective, the checker is correct

**Steering-directive response (code/out/commands.log).** The directive demanded
disambiguation before anything else: either the convex-position checker or the
block placement in `es_lower_set` is false. The captured machine output below
is the evidence. Verdict: **the checker is correct; every implementation of the
ES lower-bound construction present in this workspace is defective.**

## Step 1 — checker alone, on sets whose answer is known by hand

Captured output (exact integer arithmetic, `lib.es_geom`), from
`checker_disambiguation.py` run logged in `commands.log`:

```
=== checker self-test (exact integer arithmetic, es_geom) ===
circle k=4                              N=4 general=True maxConvex=4 want=4 -> PASS
circle k=5                              N=5 general=True maxConvex=5 want=5 -> PASS
circle k=6                              N=6 general=True maxConvex=6 want=6 -> PASS
circle k=7                              N=7 general=True maxConvex=7 want=7 -> PASS
parabola k=4 (4-convex cup)             N=4 general=True maxConvex=4 want=4 -> PASS
parabola k=5 (5-convex cup)             N=5 general=True maxConvex=5 want=5 -> PASS
tri(0,0)(1000,0)(0,1000)+inside(100,100) N=4 general=True maxConvex=3 want=3 -> PASS
square (4 convex)                       N=4 general=True maxConvex=4 want=4 -> PASS
tri + interior (4pts, 3 convex)         N=4 general=True maxConvex=3 want=3 -> PASS
circle k=12                             N=12 general=True maxConvex=12 want=12 -> PASS
circle k=16                             N=16 general=True maxConvex=16 want=16 -> PASS
```

Also captured from an earlier command run:
```
orient A,B,C: 1 (expect 1)
orient A,C,B: -1 (expect -1)
orient A,B,E: 0 (expect 0)
largest convex subset of triangle+interior: (3, [(0,0),(4,0),(0,4)])
largest convex subset (pentagon): (5, ...)
```

The predicate `in_convex_position(subset) == (len(convex_hull(subset)) == n)` with
an exact integer Andrew monotone-chain hull is the standard, correct definition
(points in convex position iff all are extreme vertices of their own hull), and
it reproduces every hand-known answer. **The checker is correct.** This is the
same definition GOAL.md item 3 requires and it is vindicated by the very sets the
directive names (k points on a circle, triangle-with-interior-point, 5-point
convex, Klein 4-point).

## Step 2 — therefore the construction is wrong

Every construction implementation in this workspace fails, and the failures
cluster in ways that identify the causes:

### (a) `lib/es_construction.es_lower_set` — radial placement, FLAGS EVERYTHING
Captured (`check_esz_construction.py`):
```
[es_lower_set] n=4: |S|=4 general=True largestConvex=4 (want 3) hasConvex4-gon=True  -> FAIL
[es_lower_set] n=5: |S|=8 general=False largestConvex=5 (want 4) hasConvex5-gon=True  -> FAIL
[es_lower_set] n=6: |S|=16 general=False largestConvex=8 (want 5) hasConvex6-gon=True  -> FAIL
[es_lower_set] n=7: |S|=32 general=False hasConvex7-gon=True (want False) -> FAIL
```
The blocks themselves fail their cup/cap bounds (want: T_i has no (i+2)-cap, no
(n-i)-cup), captured `largest_block_capcup`:
```
n=5: T_1 cap=3 (want <=2) ...
n=6: T_1 cap=3 (<=2) FAIL; T_2 cap=4 (<=3) FAIL   and T_1,T_2,T_3 general=False
n=7: T_1 cap=3 (<=2) FAIL; T_2 cap=5(<=3) FAIL; T_3 cup=4(<=3) FAIL; general=False
```
`es_lower_set` places blocks via `math.cos/math.sin` (FLOATING POINT) then rounds
to integers. This is exactly the directive's alert: a floating-point radial
placement destroys general position (collinear triples land on the same rays —
see the n=4 collinear-triple capture, points (1000,1000),(1000,0),(1000,-1000))
and, combined with rounding, destroys the intended cup/cap separation. The
block builder `cups_caps_block` is ALSO broken on its own terms (T_1 cap=3 but
the spec demands cap≤2), so no placement of these blocks can rescue the property.

### (b) `lib/es_construct.es_set_radial` — same floating-point radial idea
```
n=4: general=False maxConvex=3   n=5: general=True maxConvex=4 (want 4, OK)
n=6: slopes<1=False general=False maxConvex=6 (want <=5, FAIL)
```
Also the collinear capture shows three of the four n=4 radial points share
x=1000 → collinear triple.

### (c) `lib/esz` blocks + arc placement — exact fractions, the closest to working
Exact `Fraction` arc placement (block i at x≈i, y≈K−i²) — captured:
```
n=4: 4pts general=True maxConvex=3 (want 3) OK
n=5: 8pts general=True maxConvex=4 (want 4) OK
n=6: 16pts general=True maxConvex=6 (want 5) FAIL
```
n=6 exemplar (which 6 vertices, which blocks they came from):
```
point=(0.0000,100.0000) block~0   point=(1.0000,99.0000) block~1
point=(2.0000,96.0000) block~2   ... three more block~2
```
Four of the six convex vertices come from block T_2. This is NOT a sharp
contradiction of the no-4-cup/no-4-cap bound per se (a drawing whose interior
points cluster can put 4 of a 6-gon's vertices inside one shallow block when the
block sits on the same nearly-horizontal chain as the outer blocks), but it is a
real convex-6-gon in a set that must have none — so the exact-arc placement does
NOT realise the ES construction either. The blocks are mutually "flat", so a
convex polygon can pick a shallow block's points as vertices and the outer
blocks as the closing edges.

## Verdict / what is false

- **Convex-position checker (`lib/es_geom`): TRUE** (survived the directive's
  hand-known tests plus the full range of circle/parabola/triangle/quad cases).
- **`es_lower_set` block placement and `cups_caps_block` block builder: FALSE.** The
  construction must be rebuilt. The failure is structural, not a tuning issue:
  (1) radial placement via floating-point cos/sin destroys general position and
  cup/cap separation; (2) the block builder itself violates its own cap/cup
  bounds; (3) even the exact arc placement produces a convex-6 at n=6.

```claim
id: es-construction-defective-checker-correct
statement: In this workspace the ES lower-bound set es_lower_set(n) does NOT have the defining property (no convex n-gon at 2^{n-2} points). Captured: n=4 largestConvex=4 (want 3), n=5 largestConvex=5 (want 4), n=6 largestConvex=8 (want 5), n=7 hasConvex7=True. The convex-position checker lib/es_geom is CORRECT on hand-known cases (circle k -> k, triangle+inside -> 3, square -> 4). Therefore the construction is defective: floating-point radial placement (cos/sin, integer rounding) destroys general position and cup/cap separation, and cups_caps_block violates its own no-(i+2)-cap/no-(n-i)-cup bounds (n=6 T_1 cap=3 want<=2; T_2 cap=4 want<=3; several blocks non-general-position). The exact-fraction arc placement rescues n=4 (maxConvex 3) and n=5 (maxConvex 4) but still fails n=6 (maxConvex 6) with 4 of 6 convex vertices in one block.
hypotheses: planar point set in general position; the object is 2^{n-2} points with no convex n-gon; construction from Erdős–Szekeres 1961, Morris-Soltan Thm 2.5/2.6.
holds-here: yes — this is precisely the lower-bound construction GOAL.md and every later argument are measured against; it is currently defective and must be rebuilt with exact coordinates and correct block bounds before any structural claim is built on it.
status: checked (exact-arithmetic oracle lib/es_geom, captured output in code/out/commands.log)
bearing: GOAL.md item 2/3 — the oracle is validated; the construction must be replaced. No structural argument may cite the current es_lower_set.
anchor: code/out/checker_vs_construction_resolution.md
```

## What a correct rebuild needs (recorded for the coder, not yet done)

The official construction (Morris–Soltan Thm 2.5/2.6; primary source
`erdos-szekeres-1961` summary) is: X_n = ⋃_{i=0}^{n-2} T_i with |T_i| = C(n-2,i),
each T_i a block with no (i+2)-cap and no (n-i)-cup and internal slopes in
(-1,1); blocks placed on a convex arc so that the blocks are pairwise separated,
with a line through any two far-apart blocks leaving the intermediate blocks on
one side. The exact-arc attempt (c) got n=4,5 right but flattened the chain so a
convex-6 leaks through at n=6. The next attempt must: use exact rational
coordinates only; make the block builder actually meet its cap/cup bounds (the
current recursion's separation "cross slope > all within slopes" is not achieved
— verify by oracle per block); and choose a block placement whose separation
constant provably cuts every cross-block convex polygon to ≤ n-1 vertices. Record
this as a live task for the computational arm; the capture above is the ground
truth it must beat.
