"""NOT EXECUTED — DESIGN NOTE, DO NOT CITE AS A RESULT.

This file is a *design* for verifying Keramatipour Thm 3.4.2 (the claim that a
putative srg(99,14,1,2) cannot follow the Paley(9) pattern). It was drafted by
the scholar during the final integrity pass, who has NO execution tool, so it
has NEVER been run. Per the run's own standing rule (a written-but-never-run
script is a trap: see paley9_pattern_check.py, whose unrun state produced a
dangling crash capture), this file must NOT be taken as a verification.

It is left here only so a future role WITH an execution tool (tool_builder /
coder) can implement and run it. If you run it, capture the output to a
.captured.txt and only then may any claim about Theorem 3.4.2's soundness be
made.

Status of the Paley(9)-pattern line (recorded, not re-derived here):
  - Lemma 3.4.1 (pattern present in rook(3) and BvLS): CHECKED exact, in
    code/out/paley9_pattern_check_fixed.captured.txt (9/9 and 13365/13365
    configurations are Paley(9)).
  - Theorem 3.4.2 (pattern forbidden at 99): ASSERTED-BY-SOURCE (unrefereed
    MPhil thesis), NEVER verified. This is the run's single most valuable
    unverified 99-specific candidate configuration.
  - The turning point the proof rests on: vertex 5 must have two neighbours in
    N_{1,3} (k=14-specific); the forced triangle must be {5,(1,3,x),(2,4,y)};
    two vertices then share three common neighbours, contradicting mu=2.

KEY STRUCTURAL POINT the designer verified by arithmetic (NOT by running code):
the first-level Paley(9) pattern seed materialises exactly
    1 + 14 + C(7,2)*4 = 1 + 14 + 84 = 99 vertices
(vertex 0, its 14 neighbours, and for each of the C(7,2)=21 pairs of matching
edges the 4 distance-2 vertices). An SRG has diameter 2, so EVERY vertex is at
distance <= 2 from 0, hence this materialises the ENTIRE 99-vertex graph — there
is no ~90-vertex "outside" to absorb deficits. That is what makes Thm 3.4.2's
contradiction a *decidable finite* question at k=14, and it is exactly the
k=14-vs-k=22 difference the proof exploits (at k=22 the 1+22+C(11,2)*4 = 1+22+220
= 243 vertices also materialise everything, and BvLS realizes the pattern = no
contradiction there).
    Seed construction (each edge soundly justified): 0 with neighbours 1..14
forming the 7K2 matching (1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14) [c5];
N(0) non-edges = all non-matching pairs; for each pair of distinct matching
edges {a1,a2},{b1,b2} the four dist-2 vertices (a_i,b_j) adjacent to exactly
their two named endpoints, non-adjacent to 0 and to all other N(0) vertices
[mu=2: unique non-0 common neighbour], forming the Paley(9) C4 (same-a sharing
a, same-b sharing b). Materialises 99 vertices in total.
    Then run code/lib/localprop.py::PartialGraph.propagate to fixpoint. The
engine reports ONLY genuine (excess) contradictions: adjacent pair with >=2
established common neighbours, non-adjacent pair with >=3, or degree > 14.
Because all 99 vertices are materialised, a deficit is a REAL contradiction
here (no outside to absorb it) — unlike the n3 patch experiments where ~91
vertices were left out. A genuine contradiction => Thm 3.4.2 CORROBORATED (the
pattern cannot extend to a degree-14 lambda=1 mu=2 SRG). If NO contradiction
arises, first-level closure is consistent and the full second-level forcing
(the (1,3,x)-type vertices from the proof) is the next (larger) step.

What the run has NOT established and must not claim:
  - It did NOT verify Thm 3.4.2's soundness. Status remains asserted.
  - It did NOT establish that the pattern is forbidden at 99.
  - It did NOT re-derive the theorem's proof chain mechanically.
If a future role executes this design, the negative-control discipline from
paley9-pattern-99-verification-status.md applies: does the same case analysis,
run verbatim at k=22 (BvLS, which HAS the pattern), produce the SAME
contradiction? If it does, the theorem is refuted on the control, not verified.
"""
