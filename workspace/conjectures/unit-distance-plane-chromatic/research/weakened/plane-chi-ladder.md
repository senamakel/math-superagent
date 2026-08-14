# plane-chi-ladder

Weakened ladder for the full-strength plane chromatic-number goal.

```ladder
goal: determine chi(G) for the unit-distance graph on R^2 (known 4 <= chi(G) <= 7): either exhibit a unit-distance graph with chi >= 5 in exact algebraic coordinates, with every edge certified |x-y|^2 = 1 symbolically and non-4-colourability proven by a complete method, or prove that every unit-distance graph is 4-colourable, or give an explicit 6-colouring of the plane with a computed separation margin
difficulties: unbounded-n, continuum-space, sparse-random, nonlocal-obstruction, exp-colour-test, direction-unknown, upper-novelty, exactness-trap
status: open
```

```rung
id: R-moser-calibration
statement: reproduce the calibration pair in exact arithmetic: the 7-vertex graph from problem.md (two unit rhombi sharing a vertex, rotated so the far vertices are at unit distance) has all 11 claimed edges certified |x-y|^2 = 1 symbolically, and a complete k-colouring test reports 4-colourable and not 3-colourable (a witness colouring at k=4, UNSAT at k=3)
off: unbounded-n, continuum-space, sparse-random, nonlocal-obstruction, exp-colour-test, direction-unknown, upper-novelty
stance: open
merge: oracle pair exists and is trusted; next turn continuum-space back on by defining a construction family (Minkowski sums A+B of small seed graphs, rotations chosen for coincidence) and running its outputs through unit_graph — first move is the exact pair-distance theorem for Minkowski sums
```
