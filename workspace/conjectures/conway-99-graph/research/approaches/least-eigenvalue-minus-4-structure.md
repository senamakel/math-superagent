# Approach: least eigenvalue exactly -4 (Cameron–Goethals–Seidel–Shult / Hoffman-graph structure theory)

```approach
idea: Attack srg(99,14,1,2) through the structural theory of graphs with a
  prescribed small least eigenvalue, specifically -4: the Cameron–Goethals–
  Seidel–Shult "graphs with least eigenvalue >= -2 are generalized line
  graphs" theorem, the Woo–Neumaier Hoffman-graph framework, and the
  classification programmes for SRGs with smallest eigenvalue -2 and -3.
mechanism: The least eigenvalue of srg(99,14,1,2) is s = -4, and this is
  99-SPECIFIC: rook(9) has s = -2 and BvLS(243) has s = -5. An argument that
  uses "least eigenvalue equals -4" as a hypothesis and derives forced
  substructure (forbidden subgraphs from the -4 basis, a special/fat-graph
  decomposition, a root-lattice representation) cannot be refuted by the two
  controls, because the hypothesis itself fails on them — the opposite of the
  eigenvalue-only routes already closed (integrality, Krein, absolute bound),
  which survive verbatim on all three parameter sets. The gate admits 99 and
  excludes the controls, so the theory can bite there and only there.
status: grounded
speculative: high — the -3 and -4 cases are far less settled than -2; the
  leverage is exactly that -4 separates 99 from both controls, which no
  parameter-driven invariant tried so far does.
precedent:
  - Koolen, Cao, Yang, "Recent progress on graphs with fixed smallest
    eigenvalue" (arXiv:2011.11935), 2020 : the survey of the classification
    programme; Theorem 5.1 (Neumaier) states a primitive SRG with smallest
    eigenvalue -lambda is geometric (Latin-square or Steiner family) provided
    (lambda+1)(a+1) - k > (c-1)(lambda+1)/2. This is the named theorem the
    reformulation's "dichotomy" rests on, and its HYPOTHESIS FAILS at
    (99,14,1,2): lambda=4,a=1,c=2,k=14 gives (5)(2)-14 = -4 NOT > 2.5 = (1)(5)/2.
    So the geometric classification does not fire at 99.
  - Greaves, Koolen, Park, "Improving the Delsarte bound" (arXiv:2012.09391),
    2020 : does exactly the right kind of work — combines the Delsarte bound
    with a cubic maximal-clique constraint and the claw-bound to RULE OUT
    infinite families of feasible SRG parameters with smallest eigenvalue -4,
    -5, -6, -7, giving explicit nonexistence tables. This is a concrete,
    applicable tool: none of its excluded sets is (99,14,1,2) (which remains
    open in the tables), so it does not rule out 99 but shows the -4 repertoire
    has born fruit and the tables should be checked directly.
  - Bussemaker & Neumaier, "Exceptional graphs with smallest eigenvalue -2 and
    related problems" (Math. Comp. 1992), DOI 10.1090/S0025-5718-1992-1134718-6 :
    the exhaustive -2 theory (Seidel -2 classification into lattice / line /
    multi-partite families + exceptional graphs + forbidden-subgraph tables).
    Confirms the -2 machinery is complete and the -4 machinery is not — the
    speculativity flag. Shows the CGSS > -2 / >=-2 characterization (Seidel;
    Hoffman) that gates the reformulation.
  - Birkhoff-Jiang-Polyanskii (arXiv:2111.10366), "Forbidden induced subgraphs
    ... eigenvalues bounded from below" : sharp threshold. The class of graphs
    with smallest eigenvalue >= -lambda has a FINITE forbidden-induced-subgraph
    characterization iff lambda < lambda* ~ 2.0198. Since -4 corresponds to
    lambda=4 > lambda*, the class "smallest eigenvalue >= -4" has NO finite
    forbidden-subgraph characterization — so a forbidden-subgraph-basis plan
    for -4 graphs is refuted by this theorem. It also implies -4 is a limit
    point of smallest eigenvalues, so the -4 structure theory cannot be finitely
    axiomatized by subgraph exclusion.
verdict: The -4 gate is GENUINELY 99-specific (rook -2, BvLS -5) — no refuted
  parameter-driven route separates the three this way, so the approach is not
  refuted by the literature. BUT the promised mechanism is partly refuted:
  (a) Neumaier's geometric dichotomy does not fire at 99 (hypothesis fails), so
  the "forced substructure via geometric-SRG classification" plan is grounded;
  the Greaves-Koolen-Park Delsarte/claw/cubic repertoire is the sound remaining
  weapon and its -4 nonexistence tables should be checked against (99,14,1,2).
  (b) The CGSS Subgraph-basis plan for least eigenvalue -4 is refuted outright
  by Birkhoff-Jiang-Polyanskii (lambda=4 exceeds the finite-forbidden threshold
  2.0198). The live remainder is the -m = -4 geometric-SRG classification
  literature (van Dam, Koolen-Yang, Spence), where (99,14,1,2) is plausibly
  among the open cases the tables leave.
first-step: (1) Recompute (4,1,-2), (14,3,-4), (22,4,-5) exactly to pin the
  separation. (2) request_research: state of "strongly regular graphs with
  smallest eigenvalue -4" (van Dam / Koolen–Yang / Spence lineage; whether the
  Woo–Neumaier Hoffman-graph framework covers lambda_min = -4); obtain the
  forbidden-subgraph basis or special-graph description a -4 regular graph must
  satisfy. (3) Apply it to a 14-regular, lambda=1, mu=2, locally-7K2 graph.
```

## Why this is not an eigenvalue-only route

The closed routes use the spectrum only to produce a bound that holds for all
three parameter sets. This approach uses the spectrum as a *gate*: the value
-4 is asserted only for 99, and the structure theory fires only where that gate
is passed. The controls sit at -2 and -5, so the negative-control test is the
hypothesis itself, not the conclusion.
