# Construction machinery: Minkowski sums and rotations of unit-distance graphs

**Subject:** The main construction engine for accumulating rigidity from small
unit-distance graphs. Task lead in `problem.md`.

## Sources (surfaced via server-side search; direct download of publisher
sites is blocked at the network boundary, so these records are syntheses of the
search-returned passages, each with its DOI/arXiv id):
- P. Engel, O. Hammond-Lee, Y. Su, D. Varga, P. Zsámboki, *Diverse Beam Search
  to Find Densest-Known Planar Unit Distance Graphs*, DOI
  10.1080/10586458.2025.2507956 (2025).
- B.V. Alexeev, D.G. Mixon, H. Parshall, *The Erdős unit distance problem for
  small point sets*, arXiv:2412.11914 (2024).
- F. Eisenbrand, J. Pach, T. Rothvoß, N.B. Sopher, *Convexly Independent
  Subsets of the Minkowski Sum of Planar Point Sets*, Electronic J. Combin.
  15 (2008), DOI 10.37236/883.

## What they establish (as derived from passages)

### Minkowski sums build dense unit-distance graphs
A large fraction of the densest-known small unit-distance graphs are Minkowski
sums: `A + B = { a + b : a in A, b in B }` of tiny unit-distance graphs.
- Example: the optimal 9-vertex UDG is a Minkowski sum of two unit triangles.
- The conjectured-optimal 21-vertex UDG is a disjoint Minkowski sum of a unit
  triangle and a 6-wheel (itself a non-disjoint Minkowski sum of three edges).
- A 49-vertex graph (G_49), a Minkowski sum of two 6-wheels, is a crucial
  ingredient in a `chi(R^2) >= 5` line of work — flagged because it shows sums
  genuinely used in attacking the bound.
- `A + B` is a *disjoint* sum when `|A+B| = |A||B|` (no colliding sums).

### Exact distance-1 condition in a Minkowski sum
Points of `A+B` are `a+b`. The pair `(a1+b1, a2+b2)` is at unit distance iff

    |(a1 - a2) + (b1 - b2)| = 1.

So a unit distance in the sum arises from pairs of difference-vectors from
`A - A` and `B - B` whose *sum* has length 1 — this is the calculation the whole
approach rests on, and the source of density: one unit distance in the sum can
come from many distinct pairs. Rotating one summand by an angle chosen so extra
such sums have length 1 creates still more unit distances.

### Spindling (rotation about a shared vertex)
The 7-vertex graph in `problem.md` is built from two unit rhombi sharing a
vertex, rotated so their far vertices are at distance 1. Generalised: given a
graph and two vertices forced to differ, rotate a copy about a shared vertex so
two far vertices coincide or become adjacent. The chromatic effect is to force
two specific vertices to receive different colours, increasing the colouring
constraint locally. Exact general statement of the chromatic-number effect is a
gap to derive (see REQUESTS).

### Convexly independent subsets bound
For planar point sets P, Q with |P|=m, |Q|=n, any convexly independent subset
of P ⊕ Q has size O(m^{2/3} n^{2/3} + m + n) (Eisenbrand–Pach–Rothvoß–Sopher).
This is an upper bound on how structured a sum's point set can be and links to
the unit-distance O(n^{4/3}) bound. Not a construction, but a control.

## Claim blocks
```claim
id: minkowski-sum-unit-distance-condition
statement: For finite point sets A, B in the plane, a pair of points
  a1+b1 and a2+b2 of A+B is at Euclidean distance 1 iff
  |(a1-a2) + (b1-b2)| = 1.
hypotheses: A, B finite point sets in R^2.
holds-here: YES — this is exactly the engine the run will use; the identity is
  a restatement of the definition of distance and holds for any A, B.
status: derived (immediate from |(a1+b1)-(a2+b2)| = |(a1-a2)+(b1-b2)|).
bearing: the exact condition to compute when building A+B; which pairs fall at
  unit distance is governed by sum-of-differences length 1.
anchor: research/sources/minkowski-sums-rotations-construction.md
falsifies: nothing — it is the definition of Euclidean distance applied to sums.
```

```claim
id: minkowski-sum-dense-graphs
statement: Minkowski sums of small unit-distance graphs produce larger
  unit-distance graphs with more unit distances per vertex than their size
  suggests; many densest-known small UDGs are such sums.
hypotheses: A, B are themselves unit-distance point sets (each realizes unit
  distances). The sums are formed in the Euclidean plane.
holds-here: YES (the sums of unit-distance graphs are unit-distance graphs; the
  point sets are the sums).
status: asserted-by-source (passages from search; the examples are those sources').
bearing: this is the promised structural route to rigidity — accumulate unit
  distances by summing structured small graphs rather than by random points.
anchor: research/sources/minkowski-sums-rotations-construction.md
falsifies: a proof that Minkowski sums of 4-colourable UDGs can never raise the
  chromatic number above 4 — not known; exactly what the run should test.
```
