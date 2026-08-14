# Ladder: colouring the plane at unit distance

Scope note, so the dials below are read correctly.

- By De Bruijn–Erdős (a proved input, needing a choice principle), `chi(G) >= 5`
  is equivalent to the existence of a *finite* unit-distance graph with
  chromatic number at least `5`. So the infinite vertex set is not a difficulty
  to dial off — it is already handled. `continuum-space` below means the space
  of *finite candidates*, which is a continuum of point sets and is the real
  obstacle to enumeration.
- `exact-coords` is **not** a dial and is never switched off. Adjacency is
  `|x-y| = 1` exactly, and any rung that relaxes it to a tolerance becomes a
  proximity-graph problem whose results do not transfer (a spurious edge can
  only raise the apparent chromatic number — the trap in `problem.md`). Exact
  algebraic coordinates are on in every rung, including the bottom one, because
  the bottom rung exists precisely to prove the exact path works.

```ladder
goal: determine chi(G) for the unit-distance graph on R^2 (known 4 <= chi(G) <= 7): either exhibit a unit-distance graph with chi >= 5 in exact algebraic coordinates with complete machine verification, or prove every unit-distance graph is 4-colourable, or give an explicit 6-colouring of the plane with a computed separation margin
difficulties: unbounded-n, continuum-space, sparse-random, nonlocal-obstruction, exp-colour-test, direction-unknown, upper-novelty
status: open
```

The seven dials, one line each:

- `unbounded-n` — no known bound on the size of a minimal 5-chromatic witness; the search is over unbounded n.
- `continuum-space` — candidate point sets fill R^2, so the search space is not enumerable; search must be over constructions, i.e. over ideas.
- `sparse-random` — random point sets have O(n^{4/3}) unit distances; density cannot be bought, it must come from algebraic coincidence (rigidity).
- `nonlocal-obstruction` — small unit-distance graphs are all 4-colourable, easily; the obstruction to 5 must be accumulated global rigidity, not a local gadget.
- `exp-colour-test` — complete k-colourability is exponential in the number of vertices, bounding how large a candidate can be checked.
- `direction-unknown` — chi could be 4, 5, 6 or 7; a lower-bound search may be chasing a graph that does not exist.
- `upper-novelty` — a 6-colouring of the plane needs a genuinely new colouring scheme; unlike the lower bound there is no structured search, only invention.

```rung
id: R-moser-calibration
statement: reproduce the calibration pair in exact arithmetic: the 7-vertex graph from problem.md (two unit rhombi sharing a vertex, rotated so the far vertices are at unit distance) has all 11 claimed edges certified |x-y|^2 = 1 symbolically, and a complete k-colouring test reports 4-colourable and not 3-colourable (a witness colouring at k=4, UNSAT at k=3)
off: unbounded-n, continuum-space, sparse-random, nonlocal-obstruction, exp-colour-test, direction-unknown, upper-novelty
stance: open
merge: oracle pair exists and is trusted; next turn continuum-space on by defining a construction family (Minkowski sums A+B of small seed graphs, rotations chosen for coincidence) and running its outputs through unit_graph — first move is the exact pair-distance theorem for Minkowski sums
```

```rung
id: R-construction-census
statement: census of constructed graphs: run the exact construction engine (Minkowski sums, rotations, spindling) over small seed graphs, prove the exact pair-distance structure of each construction, record the chromatic number of every resulting unit-distance graph, and report the maximum chi attained, the vertex count reached, and where the complete colouring test became infeasible
off: unbounded-n, nonlocal-obstruction, direction-unknown, upper-novelty
stance: open
merge: turn unbounded-n on by promoting the census into a universal claim — prove every unit-distance graph on at most N vertices is 4-colourable for the largest N the census supports; first move is classifying or exhausting the unit-distance graphs on small vertex counts (their rigidity constrains the embeddings enough to enumerate)
```

```rung
id: R-size-bound
statement: prove that every unit-distance graph on at most N vertices is 4-colourable, for the largest N the run can establish, by a complete classification or reduction of small unit-distance graphs; this is the proved lower bound on the size of any 5-chromatic witness
off: exp-colour-test, sparse-random, nonlocal-obstruction, direction-unknown, upper-novelty
stance: open
merge: turn nonlocal-obstruction on by accumulating rigidity past N — grow the rigid at-most-N configurations via spindling and Minkowski sums and test the offspring at k=4 with the complete oracle; first move is spindling the Moser spindle and testing the result
```

```rung
id: R-lower-bound-five
statement: exhibit a unit-distance graph with chi >= 5, given as an explicit vertex list in exact algebraic coordinates, every edge certified |x-y|^2 = 1 symbolically, and non-4-colourability verified by a complete method, with the verification re-done independently of the code that produced the graph
off: upper-novelty
stance: open
merge: if settled the lower bound moves from 4 to 5, leaving upper-novelty (R-upper-bound-six) as the only dial; if a candidate fails, record the failed construction and the reason, since the failure names exactly which rigidity the obstruction still lacks
```

```rung
id: R-upper-bound-six
statement: give an explicit 6-colouring of the plane — a covering by 6 colour classes with a computed positive separation margin proving no two points at distance exactly 1 share a colour, i.e. a genuinely new scheme beating the 7-colour hexagonal tiling
off: unbounded-n, continuum-space, sparse-random, nonlocal-obstruction, exp-colour-test, direction-unknown
stance: open
merge: if settled, combined with the known lower bound 4 (or with R-lower-bound-five) it determines chi; first move is searching periodic/tiling colourings and computing the exact separation margin of each candidate against the 7-colour benchmark
```
