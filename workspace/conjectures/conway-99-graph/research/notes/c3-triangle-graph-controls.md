# C3 triangle-graph claim — computed on both controls

```claim
id: c3-controls-verified
statement: The triangle graph C3(Gamma) of both control graphs is computed
  exactly (lib.triangles.triangle_graph over lib.srg). rook(3)=srg(9,4,1,2):
  C3 = K_{3,3} = srg(6,3,0,3) (the degenerate Thm-4.5 member). BvLS =
  srg(243,22,1,2): C3 is 30-regular on 891 vertices (13365 edges); NOT strongly
  regular, with all 26730 adjacent pairs sharing exactly 9 common neighbours
  (constant lambda sector) and non-adjacent pairs sharing {1:481140, 0:267300,
  3:17820} (non-constant mu sector). C3(BvLS) spectrum equals the Phillips eq
  4.3 prediction exactly: 30^1, 12^132, 3^110, (-3)^648; trace 0 and sum-of-
  squares 26730 match. So the C3-not-strongly-regular constraint is shared by
  99 and 243 (both fail s==-k/2 or k==6) — a constraint, not a rule-out; and at
  BvLS the failure is confined to the non-adjacent sector.
hypotheses: lambda=1 so distinct triangles share exactly one vertex (no edge
  sharing); C3 adjacency = share-at-least-one-vertex.
holds-here: yes — verifies `phillips-triangle-graph-not-srg` on both controls.
status: checked (exact common-neighbour counts; spectrum numerical).
anchor: code/out/check_triangle_graph.captured.txt, lib/triangles.py.
```

This was the named next step of thread `triangle-graph`. The exact conclusions
(triangle count nk/6, C3 degree 3(k/2-1), not-strongly-regular decided by exact
common-neighbour counts on both sectors, trace / sum-of-squares invariants) are
computed in integer/boolean arithmetic; only the eigenvalue multiset is
numerical (eigvalsh rounded) and matches the prediction exactly.
