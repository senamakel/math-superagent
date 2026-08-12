# Index — code/cutvertex

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `dimacs_shape.py` | _(undescribed)_ |
| `encode_shape.py` | _(undescribed)_ |
| `lobe_glue_machinery.py` | Independent validator of the J3 glue route used by lobe_probe.py. Since the real pair search is vacuous (no pow2-free lobes at n_H≤18), this proves the glue machinery is sound before it is trusted when a pow2-free lobe appears at larger n: glues 2500 pairs of arbitrary lobes by identifying their v-vertices and checks central-degree-4 + delta≥3 + connected + node-connectivity-1 structural invariants, oracle cycle set == networkx simple_cycles set, and the no-cross-cycles identity glued-set == union of the two lobe cycle sets. ALL PASS on 2500 pairs; both cycle routes always agree. |
| `lobe_probe.py` | Lobe probe for the (2,2) cut-vertex shape: for every connected cubic graph H on n_H=4..18 (A002851 counts asserted) and every edge e, forms the lobe L=H−e+v (v a fresh degree-2 vertex adjacent to the two endpoints of e) and tests for a C4 or C8 (J1/J2), then a J3 pair search by glueing two pow2-free lobes at their v's (central degree-4 cut vertex). **RESULT: zero pow2-free lobes — every one of the ~1.23M constructions (1,115,127 at n_H=18) contains a C4 or C8**; the zero rests on full distinct_cycle_lengths enumeration (complete for n_H≤14, sampled 16/18) independent of the early-exit oracle. Smallest pow2-free lobe: none in range. Log at code/out/cutvertex/lobe_probe/lobe_probe.log; full writeup in code/out/cutvertex/lobe_probe/README.md. |
| `shape_sat.py` | _(undescribed)_ |
| `surgery_verify.py` | Verifies the surgery identities behind the cut-vertex exclusion theorem, exactly with lib.cycle_oracle.all_simple_cycles. Bases K4, triangular prism, Petersen, random cubic n=8. CASE A (k≥3 all-single-edge): H=G−v+{u1u2,u1u3} is simple, n−1, δ≥3, and every H-cycle is a G-cycle (vertex set). CASE B (k=2,(1,2)): H=G−v+{xy1,xy2} has cycle-LENGTH multiset == G exactly. CASE C (k=2,(2,2)): G has no cross-cycle; H1=G−v+{x1y1,x2y2} is simple/n−1/δ≥3 and every H1-cycle is a G-cycle or a cross-cycle of length |
| `verify_cutvertex.py` | Machine-verification of the cut-vertex characterization's geometric clauses (all cycles intra-lobe; no lobe pow2-cycle if G is pow2-free; d_L(w)=d_G(w)) on glued and random forced-cut-vertex graphs, plus oracle worked-example reproduction. 14/14 PASS in code/out/cutvertex/verify_cutvertex.log. |
