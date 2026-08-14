# Lower bound: chi(G) >= 5

```skeleton
goal: prove chi(G) >= 5 for the unit-distance graph G on R^2, by exhibiting a finite unit-distance graph that is not 4-colourable
implies: G-dbe states chi(G) = sup over finite subgraphs, so chi(G) >= 5 holds iff some finite unit-distance graph is not 4-colourable. G-five-chromatic-graph supplies such a finite graph as an exact point set; G-oracle certifies it is genuine: every asserted edge satisfies |x-y|^2 = 1 exactly, and a complete method returns UNSAT for 4-colourability. Therefore chi(G) >= 5. With the standing upper bound chi(G) <= 7 (hexagonal tiling, reproduced separately) this narrows the known gap to 5 <= chi(G) <= 7.
status: sketched
rests-on: none
```

```gap
id: G-dbe
lemma: chi(G) = sup_H chi(H) over all finite subgraphs H of the unit-distance graph on R^2 (de Bruijn-Erdos compactness); in particular chi(G) >= 5 iff some finite unit-distance graph is not 4-colourable. The hypothesis to record is the choice principle the compactness argument uses.
status: open
next: theorem_prover: state and prove de Bruijn-Erdos for an arbitrary graph under AC, then instantiate to H ranging over finite point sets of R^2; or librarian: locate a primary source and scholar: record a claim block with id, hypotheses, holds-here.
```

```gap
id: G-oracle
lemma: there is a correct oracle pair with a recorded calibration: unit_graph(points) certifies |x-y|^2 = 1 symbolically in the exact algebraic field of the coordinates; chromatic_number(graph,k) is a complete k-colourability test returning a witness colouring; on the 7-vertex graph of problem.md both report all 11 edges certified, 4-colourable, and not 3-colourable.
status: open
next: tool_builder: write unit_graph and a SAT encoding of k-colourability; sat_solver: run the calibration pair on the 7-vertex graph and record the output verbatim.
```

```gap
id: G-five-chromatic-graph
lemma: there exists a finite unit-distance graph with chi >= 5, given as an exact-algebraic point list, with every unit edge certified exactly and non-4-colourability certified by a complete method, re-verified independently of the producing code.
status: open
next: inventor/tool_builder: implement the Minkowski-sum + spindling/rotation engine over algebraic point sets (rings of integers in Q(sqrt d), cyclotomic fields), run G-oracle on each construction, and report the maximum chi attained; the target instance is one on which the 4-colouring SAT test returns UNSAT.
```
