# plane-chi-ladder — SUPERSEDED

This ladder is superseded by `unit-distance-chi.md`, which carries the full rung
ladder for the same goal. Kept only for its finer difficulty vocabulary
(`sparse-random`, `nonlocal-obstruction`, `direction-unknown`), which the
canonical ladder's merge notes reuse. Its single rung is settled.

```ladder
goal: determine chi(G) for the unit-distance graph on R^2 (known 4 <= chi(G) <= 7): either exhibit a unit-distance graph with chi >= 5 in exact algebraic coordinates, with every edge certified |x-y|^2 = 1 symbolically and non-4-colourability proven by a complete method, or prove that every unit-distance graph is 4-colourable, or give an explicit 6-colouring of the plane with a computed separation margin
difficulties: unbounded-n, continuum-space, sparse-random, nonlocal-obstruction, exp-colour-test, direction-unknown, upper-novelty, exactness-trap
status: abandoned
```

```rung
id: R-moser-calibration-granular
statement: reproduce the calibration pair in exact arithmetic: the 7-vertex graph from problem.md (two unit rhombi sharing a vertex, rotated so the far vertices are at unit distance) has all 11 claimed edges certified |x-y|^2 = 1 symbolically, and a complete k-colouring test reports 4-colourable and not 3-colourable (a witness colouring at k=4, UNSAT at k=3)
off: unbounded-n, continuum-space, sparse-random, nonlocal-obstruction, exp-colour-test, direction-unknown, upper-novelty
stance: settled
established-by: code/out/calibrate_moser.captured.txt (11 edges certified exactly |x-y|^2 = 1 over Q(sqrt3,sqrt11,sqrt33), k=4 SAT witness [0,1,2,0,1,2,3], k=3 UNSAT); code/out/brute_calibration.txt; code/out/sat_count_check.captured.txt (brute-force and SAT colouring counts agree exactly for k=1..5)
merge: superseded — the continuation lives in unit-distance-chi.md, where continuum-space is turned back on as the next difficulty (R-construction-census-small, after the standing-bounds rung). First move there: the exact pair-distance theorem for Minkowski sums.
```
