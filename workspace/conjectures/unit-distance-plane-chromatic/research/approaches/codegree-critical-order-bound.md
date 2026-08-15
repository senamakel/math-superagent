# Codegree (Kővári–Sós–Turán / Zarankiewicz) order bound for 5-critical unit-distance graphs

```approach
idea: Prove a lower bound on the NUMBER OF VERTICES (order) of any 5-chromatic
  unit-distance graph by the Kővári–Sós–Turán / Zarankiewicz codegree method,
  applied to the two necessary conditions this run has ALREADY established for
  every unit-distance graph: K2,3-freeness (two vertices share at most two
  common neighbours) and K4-freeness. The named mathematics: the Zarankiewicz
  problem ex(n, K_{2,3}), the Kővári–Sós–Turán double-count
  Σ_v C(d(v),2) = Σ_{pairs} codeg(pair) ≤ 2·C(n,2), and the Ore/Gallai/Kostochka–
  Yancey potential method for k-critical graphs.
mechanism: The run's own certified lemma `sharp-nbhd-local` proved every UDG is
  K2,3-free, and it is EXACTLY this condition that excludes the known small
  5-chromatic abstract families: M^k(C5) for k≥2 (the Mycielski chain, 23 vertices
  and up) contains an explicit K2,3, so none of it is unit-distance realizable
  (verified in code/out/pattern_mycielski_*.txt). So a 5-chromatic UDG must live
  in the intersection "K4-free AND K2,3-free AND 5-critical", a far narrower class
  than the general critical graphs the killed lines considered. A 5-critical
  graph has min degree ≥ 4 (established), so |E| ≥ 2n by handshaking; Dirac 1957
  (already sourced) sharpens this to |E| ≥ 2n+1. A K2,3-free graph has codegree
  ≤ 2 at every vertex pair, giving the exact identity
  Σ_v C(d(v),2) ≤ 2 C(n,2). Together with the run's sharper LOCAL constraint —
  every vertex neighbourhood induces a max-degree-2 graph (a disjoint union of
  paths and 6-cycles), so every vertex has degree in {4,5,6} and its neighbours
  sit at 60°-spaced positions on the unit circle — these are a finite, exact,
  solvable constraint system over (n, degree sequence, local configuration).
  The line asks: what is the smallest n at which this system has a solution, and
  is it strictly above the census's n=11? The proof tool is a codegree potential
  double-count, not an asymptotic edge-density crossing: this is the difference
  from the closed `clique-free-critical-size-bound` line (which crossed an edge
  lower bound against the SST O(n^{4/3}) ceiling and stopped at N≈11) and the
  closed `discharging-minimal-counterexample` line (same crossing, N≤9).
  SPECULATIVE, stated as such: whether the codegree constraint alone forces
  n ≥ 12+, or must be combined with the local 60° neighbourhood structure; the
  honest outcome may be "n ≥ 11 is already sharp and the census is optimal for
  pure combinatorics", in which case the line's value is the exact certificate
  that shows geometry (not combinatorics) is the next necessary lever.
status: proposed
first-step: Implement `code/lib/codegree_bound.py` doing exact integer feasibility:
  for n = 7..20, enumerate degree sequences (d_1..d_n) with each d_i ∈ {4,5,6}
  (the run's neighbourhood lemma forces this), Σ d_i ≥ 4n+2 (Dirac, |E| ≥ 2n+1),
  Σ_v C(d_v,2) ≤ 2 C(n,2) (K2,3 codegree identity), and the additional constraint
  that the induced neighbourhood of every vertex is a subgraph of C6 (each vertex
  adjacent to at most 2 others inside its own neighbourhood, cycles only at 6).
  Report the smallest n with a feasible solution and the actual feasible degree
  sequences; contrast with the census (n=11 achieved by 228 abstract kernel
  graphs, all 4-colourable). No floats; pure integer/backtracking, trivially
  bounded (few degree sequences per n).
falsifies: a feasible degree sequence at n ≤ 11 whose 4-colourability contradicts
  the census would expose an error in the run's census; conversely if the system
  is infeasible for n ≤ 11, that is a NEW combinatorial certificate of the size
  bound independent of the SAT census. The line is dead if research shows the
  potential/codegree method yields no order bound better than what the naive
  KST edge count gives (2n+1 ≤ (1/√2)n^{3/2} ⇒ n ≥ 8, strictly weaker than the
  census), i.e. if no sharper codegree potential for K2,3-free critical graphs is
  known.
precedent: Kővári–Sós–Turán 1954 (ex(n,K_{s,t}) = O(n^{2−1/s}); for K2,3 this is
  O(n^{3/2}) with constant 1/√2 — research must pin the exact statement);
  the Zarankiewicz problem; Ore 1961/Gallai 1963/Kostochka–Yancey 2014 potential
  method for k-critical graphs (already sourced in research/sources/ as
  kostochka-yancey-2014-… and krivelevich-1997-…). The run's own inputs:
  `sharp-nbhd-local` (K2,3-free, K4-free, nbhd maxdeg ≤ 2 — checked), and the
  verified census (all UDGs on ≤ 11 vertices 4-colourable). NULL precedent for
  the specific question "minimum order of a K2,3-free 5-critical graph" — research
  must check; it is a standard-sounding but possibly unrecorded extremal quantity.
```
