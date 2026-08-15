# Schoenberg / Cayley–Menger semidefinite rank-2 realizability as the complete UDG generator

```approach
idea: Replace point-set construction with a change of representation to
  Euclidean distance matrices: a graph G on vertices 1..n is a unit-distance
  graph in R^2 iff there is a symmetric n×n matrix D with D_ij ∈ {0, 1},
  D_ii = 0, D_ij = 1 exactly on the edges of G, and D = pairwise-squared-
  distance matrix of n points in R^2 — equivalently, by Schoenberg's theorem,
  the matrix B = −(1/2) J D J (double-centred) is positive semidefinite of
  rank exactly 2. The graph's chromatic number is then a property of the
  adjacency pattern of a PSD rank-2 0/1-off-diagonal matrix. The named
  mathematics: Schoenberg's theorem on Euclidean-distance matrices,
  Cayley–Menger determinants, and the rank-constrained semidefinite program
  (rank-2 EDM completion).
mechanism: The run's named obstruction is that the search space is a continuum
  and edges are determined by the embedding. This reformulation turns the
  continuum into a FINITE, exact, algebraic feasibility problem: for a fixed
  candidate edge pattern (which pairs are at distance 1), Schoenberg gives the
  exact polynomial condition "the matrix B = −(1/2)J D J is PSD of rank ≤ 2",
  i.e. all principal minors of B are ≥ 0 (PSD) and all principal 3×3 minors of B
  are = 0 (rank ≤ 2 forces every 3×3 minor to vanish); the 4×4 minors are implied
  and redundant (the rank-2 + PSD + triangle-inequality constraints). So the search splits
  cleanly into (a) a discrete outer loop over 5-critical candidate graphs
  (kernel: K4-free, K2,3-free, min-degree ≥ 4, every neighbourhood a subgraph of
  C6 — exactly the class the run's census already enumerates), and (b) an exact
  inner feasibility check per candidate: does its 0/1 distance matrix admit a
  rank-2 PSD completion? This is a Gröbner-basis / quantifier-elimination query
  over the rationals, no floats, and it is COMPLETE in a way the generative
  engines are not — every candidate is tested, none is missed because the
  construction grammar could not express it. This is the duality the closed
  `hajos-generative-grammar` line wanted and failed to get (Hajós is not
  UDP-preserving and realizability is ∃R-complete): the ∃R-completeness is
  exactly why realizability must be pushed into a per-candidate algebraic
  decision, not a per-node grammar step.
  SPECULATIVE, stated as such: the inner check is a rank-constrained SDP which
  is itself the hard part (Burer–Monteiro-type non-convexity); the certain
  value is that the run can now ATTACK the question "is there a 5-chromatic
  member of the census kernel that is unit-distance realizable" as a finite
  exact query, and the first candidate is the census's own 228-member n=11
  kernel.
status: proposed
first-step: Write `code/lib/edm_feasibility.py`: (1) given a 0/1 adjacency
  matrix A (edges = forced distance 1) build the symbolic distance matrix D with
  D_ij = 1 on edges, D_ij = free variable s_ij ∈ [1, ∞) on non-edges (distinct
  non-adjacent points are at distance ≠ 1, so s_ij is a free positive variable
  ≠ 1); (2) impose Schoenberg exactly: B = −(1/2)J D J must be PSD of rank ≤ 2,
  i.e. every principal minor of B is ≥ 0 (PSD) and every principal 3×3 minor of B
  is = 0 (rank ≤ 2 forces ALL 3×3 minors to vanish; the 4×4 minors are implied
  and redundant), all as exact polynomial conditions over Q; (3) feed the resulting polynomial
  system to sympy Groebner/`solveset` to decide emptiness. Calibrate first: the
  Moser spindle's 11-edge pattern must be FEASIBLE (a solution exists in
  Q(√3,√11,√33)) and the K4 pattern must be INFEASIBLE (four pairwise-unit points
  do not exist in R^2 — the run's K4-free certificate re-derived by this route).
falsifies: a candidate whose Cayley–Menger system is decided feasible but whose
  reconstructed Gram matrix is not actually rank 2 (an error in the minor
  conditions), or the run finding the inner check infeasible-by-Gröbner-cost for
  every candidate beyond n=12, which would bound the method's reach and demote it
  to a correctness filter. The line's VALUE is falsified if no 5-chromatic
  census-kernel member exists at all (then the search has no target), or if the
  first n=12 kernel enumeration is infeasible to produce.
precedent: Schoenberg 1935 ("Remarks to Maurice Fréchet's article … on the
  determination of a bilinear form …", the EDM characterization: B = −(1/2)J D J
  PSD ⇔ D is a squared Euclidean distance matrix); Blumenthal 1953 ("Theory and
  Applications of Distance Geometry") and the Cayley–Menger determinant
  characterization of embeddability in R^d (rank ≤ d+2); Menger 1928; the EDM
  completion problem (Laurent 2001 survey, "A connection between positive
  semidefinite and Euclidean distance matrix completion problems"); the
  rank-constrained SDP literature. NULL precedent for using it as a UDG
  GENERATOR combined with the 5-critical kernel — research must check, but the
  chromatic side is the run's own census.
```
