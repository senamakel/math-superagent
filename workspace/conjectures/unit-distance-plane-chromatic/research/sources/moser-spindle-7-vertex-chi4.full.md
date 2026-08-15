# Full text — Moser spindle (7-vertex unit-distance graph, χ = 4)

This file is the reference coordinate/construction record for the calibration
graph. It is the *computed* artifact, not a fetched publication.

## Exact coordinates in Q(sqrt3, sqrt11) — basis {1, sqrt3, sqrt11, sqrt33}

Each point is `(x, y)` with both coordinates 4-tuples of rationals over the
basis. These are the exact values used by `code/brute.py` and certified by
`code/out/brute_calibration.txt`.

```
O  = (0,                         0)
a1 = (1,                         0)
a2 = (1/2,                       sqrt3/2)
a3 = (3/2,                       sqrt3/2)
b1 = (5/6,                       sqrt11/6)
b2 = (5/12 - sqrt33/12,          5/12 + sqrt11/12)
b3 = (5/4 - sqrt33/12,           5/12 + sqrt11/4)      [ = b1 + b2 ]
```

Recovering the ordinary coordinates (basis coefficients give values):

- `a2 = (1/2, √3/2)`, `a3 = (3/2, √3/2)` — the unit rhombus (two unit equilateral
  triangles) `0,a1,a2,a3`.
- `b1 = (5/6, √11/6)`; `cos φ = 5/6`, `sin φ = √11/6`, so `b1` is the unit
  vector at angle `φ`.
- `b2` is `b1` rotated by the (flat) rhombus construction; `0,b1,b2,b3` is the
  second unit rhombus.
- The far tips are `a3` and `b3`, at distance exactly `1` (this is the choice of
  `cos φ = 5/6`).

## Certified edge list (11 edges)

```
0-1 0-2 0-4 0-5   1-2 1-3   2-3   3-6   4-5 4-6 5-6
```

## Certified chromatic data

- 4-colourable: yes (witness `[0,1,2,0,1,2,3]`).
- 3-colourable: **no** (complete backtracking test, symmetry-broken).
- **χ = 4.**

## Provenance

- Verification program: `code/brute.py` (exact arithmetic, field
  Q(√3,√11), complete colouring test).
- Verified output: `code/out/brute_calibration.txt`.
- Historical name/attribution: Moser & Moser (1961); see
  `research/summaries/moser-spindle-7-vertex-chi4.md` for the exact-arithmetic
  basis of the χ=4 claim and the attribution caveat.
