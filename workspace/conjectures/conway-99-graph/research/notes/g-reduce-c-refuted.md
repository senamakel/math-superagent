# G-reduce part (c) refuted on the BvLS control — checked negative

```claim
id: g-reduce-c-refuted-on-bvls
statement: The vertex-derived design reduction does NOT recurse: the outer
  design's collinearity graph is not itself an srg(*,*,1,2). On bvls(243) the
  outer collinearity graph has lambda=1 but mu in {0:330, 1:11880, 2:9900},
  not constant. Parts (a) and (b) of the reduction hold exactly on both
  controls (rook(3) and BvLS); only (c)-as-recursion fails.
hypotheses: srg(v,k,1,2); fix a vertex v0; "outer" = the distance-2 vertices
  with the triangle design induced on them.
holds-here: yes — this is a control-graph fact; the refutation closes the
  recursion route for the whole family, including any putative (99,14,1,2).
status: checked (exact integer common-neighbour and triangle counts in
  code/out/g_reduce_control.captured.txt, computed through lib.srg.is_srg on
  lib.srg.rook(3) and lib.srg.bvls_graph()).
bearing: the 84-point/140-block/replication-5 outer design at 99 is NOT the
  collinearity graph of a smaller member of the family. Nonexistence, if it
  comes from this line, must come from the mu=2 coupling of the whole
  structure through the 7K2, not from recursing the outer design. The correct
  (c) is the converse in research/backward/derived-design-at-a-vertex.md.
anchor: code/out/g_reduce_control.captured.txt
```

## Detail

`code/out/g_reduce_control.captured.txt` reports, for bvls_graph() (v=243,
k=22, fixed vertex 0):

- (a) HOLDS: N(0) induces 11 K2; the 220 distance-2 vertices biject with the
  220 non-edges of N(0), each with exactly 2 neighbours in N(0).
- (b) HOLDS: triangles partition through/cross/outer = 11/220/660, and the
  outer 660 blocks form a partial Steiner triple system of replication 9.
- (c) REFUTED: the outer collinearity graph has lambda distribution {1:1980}
  (so λ=1 holds) but mu distribution {0:330, 1:11880, 2:9900} — not constant,
  hence not srg(*,*,1,2).

rook(3) gives the same verdict structure: (a) and (b) hold, and (c) fails (its
outer design is empty, so the script's "lambda=1,mu=2" is trivially False; the
empty-design case is degenerate and not a recursion counterexample — BvLS is
the decisive one).
