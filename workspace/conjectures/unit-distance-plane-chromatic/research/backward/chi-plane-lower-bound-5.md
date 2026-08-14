# Backward: proving chi(G) >= 5

The lower-bound direction of the plane-colouring conjecture. This is the
direction the run's oracle and construction machinery are pointed at, and it is
the one with a complete machine-checkable inference.

```skeleton
goal: chi(G) >= 5, where G is the unit-distance graph on R^2 (every pair at distance exactly 1 is an edge).
implies: >
  By G5-debruijn-erdos, chi(G) >= 5 iff some finite unit-distance subgraph of G
  has chromatic number at least 5, so it suffices to exhibit a finite point set
  S with chi(G[S]) >= 5. G5-construction supplies such an S in exact algebraic
  coordinates. G5-edge-cert returns a graph H on S in which every returned edge
  is certified |x-y|^2 = 1 symbolically, so H is a subgraph of the true
  unit-distance graph G[S]. G5-non4col runs a complete 4-colourability test on H
  and returns UNSAT (encoding calibrated on the 7-vertex graph: SAT at k=4,
  UNSAT at k=3). Any proper 4-colouring of G[S] restricts to a proper 4-colouring
  of H, so UNSAT on the subgraph H forces chi(G[S]) >= 5, hence chi(G) >= 5.
  Note the direction of the subgraph step: only the *claimed* edges need to be
  genuine, and it is exactly the trap in problem.md — a spurious edge raises the
  apparent chromatic number — which G5-edge-cert's exact arithmetic is there to
  close.
status: sketched
rests-on: none
```

```gap
id: G5-debruijn-erdos
lemma: >
  For the unit-distance graph G on R^2, chi(G) >= 5 if and only if some finite
  unit-distance subgraph of G has chromatic number >= 5, under the compactness /
  choice hypotheses the theorem actually requires (state them; the problem
  statement's De Bruijn-Erdos reduction is an input to verify, not quote).
status: open
next: >
  librarian: fetch de Bruijn-Erdos (1951, "A colour problem for infinite graphs
  and a problem in the theory of relations") and a standard textbook statement;
  scholar: record a claim block with the exact hypotheses and holds-here;
  lean_prover: formalise the finite-subgraph characterisation of the chromatic
  number of an infinite graph.
```

```gap
id: G5-construction
lemma: >
  There is a finite point set S in R^2, with coordinates in an exact algebraic
  number field, whose unit-distance graph G[S] has chromatic number >= 5 (i.e.
  a 5-chromatic unit-distance graph exists).
status: open
next: >
  tool_builder: reproduce the 7-vertex Moser spindle in exact coordinates
  (the calibration graph), then run the construction engine on it — Minkowski
  sums A+B of the spindle with itself and rotations, and spindling two copies
  about a shared vertex — and feed each candidate to G5-edge-cert and
  G5-non4col. First concrete target: the smallest candidate past the 7-vertex
  graph that the engine produces.
```

```gap
id: G5-edge-cert
lemma: >
  There is an exact-arithmetic unit_graph(points) that, for a finite point set
  with algebraic coordinates, returns a graph together with a symbolic
  certificate |x-y|^2 = 1 for every returned edge (no floats, no tolerance),
  so the returned graph is a subgraph of the true unit-distance graph.
status: open
next: >
  tool_builder: implement unit_graph over sympy algebraic number fields
  (QQbar or a tower of the needed quadratic fields), certifying each edge by
  exact polynomial arithmetic; verify against the 7-vertex graph's claimed 11
  edges and confirm no spurious edges appear.
```

```gap
id: G5-non4col
lemma: >
  There is a complete k-colourability test (SAT encoding or exhaustive search
  with symmetry breaking) that is correct and returns a witness colouring on
  SAT; run at k=4 it certifies non-4-colourability exactly when it returns UNSAT.
status: open
next: >
  sat_solver: write the CNF encoding (per vertex, at least one colour; per
  vertex-colour pair the edge constraints; at-most-one via the standard
  encoding) returning a model on SAT; calibrate on the 7-vertex graph: must
  report 4-colourable and not 3-colourable (SAT at k=4, UNSAT at k=3), with the
  output recorded.
```
