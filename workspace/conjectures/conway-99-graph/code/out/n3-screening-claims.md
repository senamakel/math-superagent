# Order-6 counting and the n3 pivot — checked screening results

Two computations this attempt, both exact integer/Fraction arithmetic over the
Reimbayev order-6 subgraph-count formulas and the two control graphs.

```claim
id: order6-n3-not-forced
statement: In the family srg(v,k,1,2), all 62 Reimbayev order-6 induced-subgraph
  counts are of the form (n,k)-term +/- c*n3 with c in {0, 1/3, 2/3, 4/3, 1, 2, 4,
  5, 6, 8, 10, 14}. Requiring every one to be a NONNEGATIVE INTEGER admits n3=0 for
  EVERY family member (9,4),(99,14),(243,22),(6273,112),(494019,994); the only
  residue class forced is n3 ≡ 0 (mod 3); at (99,14) the admissible interval is
  n3 in [0, 4158]. Hence the order-6 count identities ALONE do not force n3>=1 at
  99, and do not separate 99 from the n3=0 controls.
hypotheses: Reimbayev order-6 formula list (arXiv 2508.03377, full text in
  library) is correct; each n_i is a count so must be a nonneg integer.
holds-here: yes — the transcription is self-validated: k=4 (rook exists, n3=0)
  and k=22 (BvLS exists, n3=0) both admit n3=0, as they must.
status: checked (exact Fraction arithmetic, code/out/n3_order6_feasibility.py,
  capture code/out/n3_order6_feasibility.captured.txt; brute-force cross-check
  agrees wherever the cap is small).
bearing: closes 'order-6 counting forces n3>=1' as a dead end; forcing n3 (either
  way) at 99 needs a k=14-specific GEOMETRIC constraint, not the count identities.
  Both existing members escaping any such forcing (they have n3=0 and exist) is
  the admissibility screen every candidate must pass.
anchor: code/out/n3_order6_feasibility.py
```

```claim
id: n3-99-forced-at-least-3
statement: Combining (a) the order-6 integrality residue n3 ≡ 0 (mod 3) with
  (b) the sourced+re-derived Makhnev 1988 conditional n3 >= 1 (any putative
  srg(99,14,1,2) has n3 >= 1, since n3=0 would force the parameter-infeasible
  srg(33,12,1,6) subobject), a putative srg(99,14,1,2) must have n3 in
  {3, 6, 9, ...}, i.e. n3 >= 3 and n3 ≡ 0 (mod 3). The previously recorded
  bound n3 >= 1 is sharpened to n3 >= 3. The admissible set at (99,14) is
  exactly the 1387 multiples of 3 in [0, 4158] (cap = v*k*(k-2)/4 = 4158);
  n3=0 and n3=3 are both arithmetically admissible (integrality alone forces
  nothing), and n3=4158 is admissible while n3=4159 is not (sharp bound).
  The n3>=3 claim is CONDITIONAL on the Makhnev n3>=1 conditional being
  correctly stated; the residue and cap parts are unconditional exact-integer
  arithmetic over the sourced 62 Reimbayev order-6 formulas.
hypotheses: the 62 Reimbayev order-6 count formulas are correctly transcribed;
  n3>=1 conditional (Makhnev 1988 Thm 2, source in library) holds at 99.
holds-here: yes — n3>=3 is a constraint a hypothetical 99-graph must satisfy;
  both controls have n3=0 and exist, so they CANNOT refute an n3>=1/3 argument
  (they are the n3=0 witnesses, not counterexamples to it).
status: checked for the residue and admissible-set parts (exact Fraction
  arithmetic, code/out/n3_admissible_check.py, n3_upper_bounds_exact.py,
  n3_cap_crosscheck.py); the n3>=1 premise is sourced+re-derived (Makhnev).
bearing: gives the run's sharpest built-in constraint on a hypothetical 99-graph
  (n3>=3), a genuine sharpening of the recorded n3>=1. It is a CONSTRAINT, not a
  nonexistence proof — the n3>=3 case remains open — and it does not claim
  existence. Marks the sharpest computed boundary on the n3 axis.
anchor: code/out/n3_sharpen3.py, code/out/n3_admissible_check.py
follows-from: order6-n3-not-forced, makhnev99-shorter-proof-integrality
```

```claim
id: makhnev-condstar-gate-passed
statement: Makhnev 1988 condition (*) [no two triangles joined by >=2 edges are
  joined by != exactly 3 edges = n3=0] HOLDS on both control graphs: rook(3)
  (6 triangles, all 6 disjoint pairs 3-joined, n3=0) and bvls_graph() (891
  triangles, disjoint join histogram {0:133650,1:240570,3:8910}, n3=0). Both
  have mu=2<=3, so Makhnev Thm1's mu<=3 branch absorbs them, consistent with
  their existence. Thus Makhnev 1988 Thm2 (n3=0 => no srg(99,14,1,2)) may be
  cited for 99 without contradicting the positive controls.
hypotheses: Reimbayev/Makhnev convention that n3 counts pairs of triangles
  joined by exactly 2 edges (disjoint class); shared-vertex pairs are 4-joined
  and excluded.
holds-here: yes.
status: checked (exact integer counting via lib.srg.is_srg entry guard,
  code/out/check_makhnev_condition.py, capture code/out/makhnev-1988-condition-captured.txt).
bearing: the Makhnev n3=0 conditional is now sourced AND admits the controls;
  the live question remains whether n3>=1 is forced at 99 by k=14-specific
  geometry (n3=0 is family-realizable, so not settled).
anchor: code/out/check_makhnev_condition.py
```
