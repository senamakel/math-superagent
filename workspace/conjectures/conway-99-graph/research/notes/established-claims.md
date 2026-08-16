# Established claims from the reference library

<!-- These are claim blocks. The ledger in research/CLAIMS.md is derived from
them. Each states its hypotheses, its holds-here status, and its status. -->

```claim
id: c1
statement: A strongly regular graph with lambda=1, mu=2 has v equal to one of
  9, 99, 243, 6273, 494019.
hypotheses: srg(v,k,1,2) exists; the counting identity v=1+k+k(k-2)/2; and
  eigenvalue-multiplicity integrality / the Makhnev-Minakova classification k
  = u^2+u+2 with u in {1,3,4,10,31}.
holds-here: yes — the 99 case is exactly this problem.
status: sourced (van Lint, A survey of perfect codes, Rocky Mountain J. Math.
  5 (1975), states n must be 9,99,243,6273 or 494019; Makhnev-Minakova 2004
  classification quoted in Cesarz-Woldar 2025).
base: research/sources/van-lint-perfect-codes-survey-1975.full.md; also
  re-derived by exact multiplicity arithmetic in code/out/feasibility-candidates.md
  and confirmed against Brouwer's table (research/sources/brouwer-srg-table-*.full.md).
bearing: corrects problem.md, which listed k=8 (v=33), 32 (v=513), 44 (v=969)
  as candidates. Those fail eigenvalue-multiplicity integrality: k=8 gives
  multiplicity numerator -16/5 (non-integer). The literature's five-member list
  is the correct one.
```

```claim
id: c2
statement: srg(33,8,1,2) does not exist; it is excluded by
  eigenvalue-multiplicity integrality.
hypotheses: srg(v,k,lambda,mu) multiplicity f = (k - (v-1)s)/(r-s) must be a
  nonnegative integer; r=3,s=-4 here.
holds-here: yes (it is the "nearest precedent" member's infeasibility).
status: computed-checked (exact integer arithmetic, code/out/feasibility.py and
  feasibility-candidates.md: f = (-8 + 4*32)/7 = 120/7 non-integer with the
  standard formula; equivalently (2k-(v-1))/sqrt(4k-7) = -16/5 non-integer).
  NOT an oracle verdict (no matrix), but a pure feasibility statement.
base: code/out/feasibility-candidates.md
bearing: problem.md asked for the mechanism that rules out srg(33,8,1,2). The
  mechanism is multiplicity integrality, not a structural argument. This means
  the 33 case is NOT a useful structural precedent: it dies on an
  arithmetic condition that 9 and 243 (and 99) all satisfy.
```

```claim
id: c3
statement: The automorphism group G of a putative srg(99,14,1,2) has the
  following constraints, all sourced:
  - |G| divides 2*3^3*7*11 (Makhnev-Minakova 2004).
  - If 7 divides |G| then G is Z_7; if 2 divides |G| then |G| divides 6
    (Cesarz-Woldar 2025, computer-free proofs).
  - There is no srg(99,14,1,2) with automorphism group of order 6 or 9; if the
    graph exists the order of its full automorphism group is 2^a 3^b with
    b in {0,1} (Crnkovic-Maksimovic 2020, Theorem 7.2 & 7.3).
hypotheses: existence of srg(99,14,1,2) assumed (these are constraints on the
  hypothetical graph).
holds-here: yes.
status: sourced (Cesarz-Woldar 2025; Crnkovic-Maksimovic 2020 abstract).
base: research/sources/automorph-putative-conway-99-graph.full.md;
  research/sources/crnkovic-maksimovic-composite-automorphism.full.md.
bearing: directly answers GOAL's "exactly which automorphism orders are
  excluded, by whom". Prime orders/group orders excluded: 7-valent sorts
  handled; order 6, 9 (Z9, E9), S3 excluded. Result holds without a computer
  (Cesarz-Woldar), so it is not a computer-assisted claim.
```

```claim
id: c4
statement: srg(9,4,1,2) (the 3x3 rook's graph = Paley(9)) and srg(243,22,1,2)
  (Berlekamp-van Lint-Seidel graph, from the perfect ternary Golay code) both
  exist.
hypotheses: none — existence.
holds-here: yes; these are the two negative controls every nonexistence
  argument must fail on.
status: checked (exact integer verification through the canonical oracle
  lib/srg.is_srg: rook(3) confirmed srg(9,4,1,2), bvls_graph() confirmed
  srg(243,22,1,2) with 2673 edges, capture in
  code/out/oracle_verification.captured.txt).
base: research/sources/brouwer-srg-table-1-50.full.md (row 9: "Paley(9)"),
  van-lint-perfect-codes-survey-1975.full.md (lines 605-622),
  wikipedia-berlekamp-vanlint-seidel-graph.full.md.
bearing: any nonexistence argument in this workspace must be run against these
  two before effort is spent; GOAL.md's hard rule.
```

```claim
id: c5
statement: The neighbourhood of every vertex of a putative srg(99,14,1,2) is a
  perfect matching (7 disjoint edges).
hypotheses: lambda=1, k=14.
holds-here: yes.
status: checked (direct from parameters lambda=1,k=14; the same fact verifies
  on the two control graphs rook(3) and BvLS through the oracle — every
  neighbourhood is a disjoint union of edges — capture in
  code/out/oracle_verification.captured.txt).
base: problem.md derivation; wikipedia-conway-99-graph summary.
bearing: basis of the partial-linear-space reformulation.
```

```claim
id: c6
statement: A strongly regular graph with mu=2 is either a grid graph or
  satisfies k >= 12*lambda*(lambda+3) (Bagchi 2006, improving Brouwer-Neumaier).
hypotheses: srg with mu=2.
holds-here: for (99,14,1,2), 12*1*4 = 48 > 14, so a non-grid such graph would
  violate the bound. If the bound is sound, (99,14,1,2) would have to be a
  grid graph, which is impossible (grids have v a product and specific k).
status: sourced (Bagchi, "On strongly regular graphs with mu<=2", Discrete Math.
  2006, abstract) — NOT yet fully verified in this library's full text; the
  abstract states the theorem. This is a lead with high potential: it would
  immediately rule out (99,14,1,2).
base: exa summary of ScienceDirect S0012365X06002056.
bearing: THIS IS THE MOST PROMISING ROUTE FOUND. Needs verification: is there a
  subtlety (e.g. does the grid branch use v=99,k=14 being impossible)? The
  bound k>=12*lambda*(lambda+3)=48 and k=14 < 48 would force the graph to be a
  grid graph. A grid graph srg has v = a*b, k = (a-1)+(b-1), lambda=2, mu=2...
  which contradicts lambda=1. So (99,14,1,2) appears ruled out IF the Bagchi
  theorem holds here. But 9 and 243 exist with k=4<... wait: for the 9-graph
  k=4, 12*lambda*(lambda+3)=48, k=4 < 48, so the theorem would force the 9-
  graph to be a grid graph — and the 3x3 rook's graph IS a grid graph (3x3)!
  For 243: k=22 < 48 forces it to be a grid graph — but BvLS is NOT a grid
  graph. CONTRADICTION. So either the theorem statement is misread (likely: the
  grid branch may have parameters lambda=2 not 1), or it does not apply. MUST
  be resolved before relying on c6.
bearing2: This is exactly the kind of claim GOAL says to hunt for a
  counterexample. The BvLS graph (243,22,1,2) with k=22<48 not being a grid
  graph is the counterexample. Record as CONTRADICTION, unresolved filter: the
  Bagchi mu<=2 theorem must be read carefully (its `grid` may mean
  Hamming-type with specific parameters, or the bound's lambda is different).
```

<!-- c6 needs the oracle/scholar to resolve: the Bagchi theorem as summarised
appears to contradict the existence of BvLS (243,22,1,2). Most likely the
summary garbles the hypothesis (the "grid or k>=12lambda(lambda+3)" statement
is a known result; the grid graph there is the Hamming graph H(2,q) which has
lambda attributes). Flag for resolution, do not rely on c6 as stated. -->

```claim
id: c8-induced-hexagon-count-bvls
statement: The number of induced 6-cycles (induced hexagons) in the BvLS
  graph srg(243,22,1,2) is exactly 4,980,690, equal to the Reimbayev-style
  closed form (1/12) n k (k-2) (2k^2 - 21k + 53) = (1/12)*243*22*20*559.
hypotheses: the BvLS graph is built correctly (srg(243,22,1,2), verified by
  the canonical oracle lib.srg.is_srg, 2673 edges).
holds-here: yes (this is a control-graph measurement, not a 99 statement).
status: computed-checked by two independent exact routes — (1) the
  P4-anchored counter lib/hexagons.count_induced_C6 (O(n^4), boolean matvec
  completion) runs in 116.5s giving 4,980,690; (2) an independent directed-
  edge-anchored counter (O(n^5)) in code/out/verify_hexagons_edge_anchor.py
  gives directed 59,768,280 = 12*4,980,690. Both validated on rook(3)=6
  (which attains its formula value 6) and on a bare C6 (=1).
base: code/out/hexagon_count_bvls.py, code/out/verify_hexagons_edge_anchor.py,
  code/lib/hexagons.py.
bearing: confirms the Reimbayev closed-form value for the 243 control -- i.e.
  the 243 graph ATTAINS the hexagon lower bound, consistent with the
  thread-hexagon-bound expectation. This gives the oracle a measured
  invariant the 99 case (and any candidate argument) must reproduce or fire
  against: for n=99,k=14 the closed form predicts (1/12)*99*14*12*(2*196-294+53)
  = (1/12)*99*14*12*151 = 16632*151 /12 ... = 1,386*151 = 209,286. Whether the
  99 value equals its formula (and whether that is consistent with the 243
  control, which equals it) is the open structural question.
```
