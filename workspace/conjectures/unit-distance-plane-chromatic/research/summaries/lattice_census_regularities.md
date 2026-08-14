# Pattern-finder: structural regularities from the lattice census

Data source: exact run of `code/lattice_census.py` (captured output in
`code/out/lattice_census.captured.txt`). The colouring machinery was first
cross-checked two independent ways: it reproduces the calibrated 7-vertex
spindle (chi = 4, not 3) of `problem.md`, and it agrees with the calibrated
oracle `brute.coloring_test` on thå lattice patches r = 1,2,3. Every vertex
count and edge count is exact; every edge is certified by the integer norm
test; every chromatic number is decided by a complete symmetry-broken
backtracking test whose witness is re-verified before acceptance.

## The two families, exact over every term computed

**Square lattice patch** `S_r = {(i,j) : |i|,|j| <= r}`, n = (2r+1)^2,
unit edge iff |di|+|dj| = 1.

- vertex count `n = (2r+1)^2` (verified r = 0..25)
- edge count `e = 4r(2r+1) = 8r^2 + 4r` (verified r = 0..25);
  `e: [0,12,40,84,144,220,312,...]`, constant second difference 16 → quadratic
- chromatic number `chi = 2` for r >= 1 (complete test; witnesses are a
  proper 2-colouring). Agrees with the classical (i+j) mod 2 colouring.

**Triangular / A2 hexagon patch** `H_r = {(i,j) : |i|,|j|,|i+j| <= r}`,
unit edge iff `di^2 + di*dj + dj^2 = 1`.

- vertex count `n = 3r(r+1) + 1` — the **centered hexagonal numbers**
  (OEIS A003215, crystal-ball sequence for the hexagonal lattice). Verified
  r = 0..21. `n: [1,7,19,37,61,91,...]`.
- edge count `e = 3r(3r+1) = 9r^2 + 3r` — the **hexagonal matchstick numbers**
  (OEIS A045945, `3n(3n+1)`). Verified r = 0..21.
  `e: [0,12,42,90,156,240,342,...]`, constant second difference 18 → quadratic.
- degree classification (verified r = 2..14): 6 corner vertices of degree 3,
  6(r-1) side vertices of degree 4, the rest interior of degree 6. Handshake:
  2e = 6·3 + 6(r-1)·4 + (3r(r+1)+1 − 6r)·6 = 6r(3r+1), which is exactly the
  counted edge number — so the edge count is derivable from the vertex count
  and degree partition, not just fitted.
- chromatic number `chi = 3` for r >= 1 (complete test). Agrees with the
  classical (i+2j) mod 3 colouring.

These matched the OEIS on the first lookup each — the counts are catalogued,
so they are sourced closed forms rather than this run's discovery.

## What these are, and what they are not

Both families reproduce a **known** chromatic number (2 and 3) with a **known**
colour-partition witness. The sequence tools report the vertex/edge counts are
exactly quadratic, which is a **conjecture in the general-index sense** but here
it is a *proof*: the degree partition + handshake halves give the closed forms
by elementary counting, and they were verified against every computed term
(ranges above). The chromatic numbers 2 and 3 are proved (they are proper
colourings, and the non-(k-1)-colourability — a unit square forces ≥2, a unit
triangle forces ≥3 — is classical).

These are therefore **scale calibrations of the complete-colouring oracle**, not
new structural discoveries. They demonstrate the oracle at graph sizes up to
~2600 vertices (S) and ~1387 vertices (H) running in well under a second, and
cross-checked against the 4-chromatic spindle. That is the census deliverable of
GOAL.md in miniature, and it is the honest statement: the largest graph this run
has colour-tested is the S_25 patch at 2601 vertices (chi=2, 0.43 s) and H_21 at
1387 vertices (chi=3, 0.15 s).

## Why the lattice patches cannot beat the bound (why this is a calibration)

The full infinite lattices Z^2 and A2 are themselves 2- and 3-colourable (by the
(i+j) mod 2 and (i+2j) mod 3 colourings), so every finite patch inherits that
colouring: no lattice patch of either family can ever be non-4-colourable, and
the chromatic number is bounded by the lattice chroma. Consequently this
regularity carries no information for the lower-bound (5-chromatic) search. To
push χ past 4 the run must move to rigid algebraic constructions — spindle /
Minkowski-sum closures over rings of integers in quadratic or cyclotomic fields
— per research/backward/lower-bound-five.md gap G-five-chromatic-graph. The
lattice census is the costed, calibrated baseline underneath that search.

## First term that would falsify each regularity

None: every closed form was asserted by an elementary counting derivation
(vertex sets are finite arithmetic ranges; edge counts follow from the degree
classification and handshake), verified exactly over the full computed range,
and matched an OEIS catalogue entry. The appropriate falsifier, if the
continuation to larger r were ever in doubt, is the first r where e(H_r) ≠
3r(3r+1) or e(S_r) ≠ 4r(2r+1); no such term exists in r = 0..25 (S) / 0..21 (H).

```claim
id: lattice-census-regularities
statement: for the square lattice patch S_r (n=(2r+1)^2, edges iff |di|+|dj|=1) the exact counts are n=(2r+1)^2 and e=4r(2r+1) and chi=2 for r>=1; for the triangular A2 hexagon patch H_r={|i|,|j|,|i+j|<=r} (edges iff di^2+di dj+dj^2=1) the exact counts are n=3r(r+1)+1 (centered hexagonal, OEIS A003215) and e=3r(3r+1) (hexagonal matchstick, OEIS A045945) and chi=3 for r>=1, with degree partition 6 corners deg 3, 6(r-1) sides deg 4, interior deg 6 (handshake gives 2e=6r(3r+1)).
hypotheses: full lattice Z^2 is 2-colourable and A2 is 3-colourable, so every finite patch inherits chi 2 and 3; edge norms are exact integers (|di|+|dj|=1 resp. di^2+di dj+dj^2=1).
holds-here: yes (these are scale calibrations of the colouring oracle, reproducing the classical lattice colourings; they cannot supply a 5-chromatic graph)
status: checked
bearing: the complete-colouring machinery is validated at size up to 2601 vertices (S_25) and 1387 (H_21), each under ~0.4 s, cross-checked against the calibrated 7-vertex spindle; it is the baseline the spindle/Minkowski-sum construction search builds on.
anchor: code/lattice_census.py, code/out/lattice_census.captured.txt, research/summaries/lattice_census_regularities.md
```

