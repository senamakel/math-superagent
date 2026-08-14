# Oracle calibration on the 7-vertex worked example

`code/brute.py` is the naive exact-arithmetic oracle for the Hadwiger-Nelson
unit-distance problem. It was written first and deliberately not optimised.

## What it computes

- `unit_graph(points)` — pair-by-pair certification of which pairs are at
  EXACTLY unit distance, i.e. `|p - q|^2 == 1` as an exact element of the
  field `Q(sqrt3, sqrt11)`. Four-tuples of Fractions, no floating point.
- `coloring_test(n, edges, k)` — exhaustive (symmetry-broken) k-colourability
  test, returns a witness when one exists.

## The worked example (problem.md)

Construction: two unit rhombi (each two equilateral triangles) sharing a vertex
`0`, the second rotated by angle `theta` so its far vertex is at unit distance
from the first's far vertex. Exact coordinates, `e^{i theta} = 5/6 + i sqrt11/6`,
with `sin(theta/2) = 1/(2 sqrt3)` giving `|(1+u) - e^{i theta}(1+u)| = 1`.

Points (index: coordinate):
- `0`: 0
- `1`: 1
- `2`: u = 1/2 + i sqrt3/2
- `3`: 1 + u = 3/2 + i sqrt3/2    (far vertex of rhombus 1)
- `4`: e^{i theta} = 5/6 + i sqrt11/6
- `5`: u * e^{i theta}
- `6`: (1+u) * e^{i theta}        (far vertex of rhombus 2)

Rhombus 1 = vertices {0,1,2,3} (5 unit edges: the 4 sides + short diagonal
1-2 giving two triangles). Rhombus 2 = vertices {0,4,5,6} (5 unit edges).
Plus the cross edge 3-6 between the two far vertices: total 11.

## Output (verbatim)

```
field self-check: OK
number of points: 7  (distinct: 7)
unit-distance edges certified: 11
  edge 0-1  edge 0-2  edge 0-4  edge 0-5
  edge 1-2  edge 1-3  edge 2-3
  edge 3-6  edge 4-5  edge 4-6  edge 5-6
chromatic number: 4
3-colourable? False
4-colourable? True  witness: [0, 1, 2, 0, 1, 2, 3]
CALIBRATION PASSED: 7 points, 11 certified unit edges, chi = 4 and not 3.
```

Every one of the 11 edges is certified `|p_i - p_j|^2 == 1` exactly in the
field; no tolerance. The graph is 4-colourable (witness shown) and NOT
3-colourable. This is exactly the calibration GOAL.md requires.

## Status

`status: checked` on the calibration claim: the edge verifier and the complete
colouring test both reproduce chi = 4 on the 7-vertex graph of problem.md.

```claim
id: G-oracle-calibrated
statement: the exact-arithmetic oracle pair unit_graph (symbolic |x-y|^2==1 in Q(sqrt3,sqrt11)) and coloring_test (complete symmetry-broken k-colourability) reproduces chi = 4 on the 7-vertex Moser-spindle-type construction of problem.md: 7 distinct points, 11 unit edges all certified exactly, 4-colourable and not 3-colourable.
hypotheses: coordinates lie in Q(sqrt3,sqrt11); equality is exact tuple equality of Fraction fields, never floating point.
holds-here: true
status: checked
bearing: the oracle is the one every lower-bound claim in this run must survive; this is its calibration.
anchor: code/out/oracle_calibration.md and code/brute.py
```
