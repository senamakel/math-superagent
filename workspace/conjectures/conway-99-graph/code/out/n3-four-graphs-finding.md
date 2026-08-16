# n3 = 0 on all four classical λ=1 SRGs — the join-2 configuration is unwitnessed in the μ≤3-or-exception part of the family

Directive 12 asked for the four-graph n3 values to be read as a FINDING, not a
failed search. `code/out/n3_four_graphs.py` computed the triangle count T and
n3 (unordered pairs of DISJOINT triangles joined by exactly 2 edges) exactly,
through `lib.srg.is_srg` entry guards, on the four classical λ=1 strongly
regular graphs. All four have n3 = 0; disjoint triangle pairs are joined by 0,
1, or 3 edges, never 2.

```claim
id: n3-zero-four-classical-lambda1-srgs
statement: The four classical lambda=1 SRGs all have n3 = 0 (no two DISJOINT
  triangles joined by exactly 2 edges): rook(3)=srg(9,4,1,2) has T=6 with
  disjoint-join histogram {3:6}; the doily srg(15,6,1,3)=GQ(2,2) has T=15 with
  {3:60}; the GQ(2,4) point graph srg(27,10,1,5) has T=45 with {3:720}; and the
  Berlekamp-van Lint-Seidel graph srg(243,22,1,2) has T=891 with
  {0:133650, 1:240570, 3:8910}. Disjoint triangle pairs are joined by 0, 1, or
  3 edges — never 2. In particular BOTH known mu=2 lambda=1 SRGs (rook, BvLS)
  have n3=0, so there is NO mu=2 in-family positive control for an
  n3>=1-forcing argument: the join-2 configuration is absent in every lambda=1
  SRG with mu<=3 and in the Thm-1 exception GQ(2,4).
hypotheses: n3 counts unordered pairs of DISJOINT triangles joined by exactly 2
  edges (the "4"-joined shared-vertex class is excluded). The four graphs named
  are the four CLASSICAL lambda=1 SRGs, NOT the whole lambda=1 family.
holds-here: yes — computed exactly from the four adjacency matrices.
status: checked (exact integer join-edge counting through lib.srg.is_srg entry
  guards; code/out/n3_four_graphs.py, capture code/out/n3_four_graphs.captured.txt).
bearing: the join-2 configuration is absent everywhere it has been looked at in
  the mu<=3-or-exception part of the lambda=1 family (not merely at 99), which
  is a FINDING, not a failed search. SCOPE NOTE: n3>=1 IS witnessed in the mu>=4
  non-exception members srg(81,20,1,6) and srg(729,112,1,20) (claim
  bondarenko-radchenko-lambda1-gk together with Makhnev Thm 1's contrapositive),
  but those are mu!=2 and cannot gate the mu=2/locally-7K2-specific kill
  argument. The kill target is the finite local question of whether a
  2-edge-joined disjoint triangle pair extends at all in a locally-7K2 mu=2
  graph (task kill-n3-ge1-case).
anchor: code/out/n3_four_graphs.py
```

The capture's per-graph histograms include a "4"-joined class (shared-vertex
pairs: rook {4:9}, doily {4:45}, GQ(2,4) {4:270}, BvLS {4:13365}); these are
excluded from n3 by definition (disjoint class only), which is why the
disjoint-join histograms above read {3}-only for rook/doily/GQ(2,4).
