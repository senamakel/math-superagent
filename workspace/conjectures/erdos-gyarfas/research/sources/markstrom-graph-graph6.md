# Markström graph — canonical graph6 representation

**Graph:** Markstroem Graph (House of Graphs ID **51419**), the unique planar
cubic graph on 24 vertices with no cycle of length 4 or 8 (one of the four
extremal 24-vertex graphs in Markström 2004, Congressus Numerantium 171,
Fig. 14; built from K4 by repeated vertex-into-triangle expansion).

## Canonical graph6 string

```
Ws??W?@@?P?aA_?O?GG?a?@_?gA??a?@CO?CG?A@???a??D
```

(served as `entity.canonicalForm` by the House of Graphs API for graph 51419,
and identical to the string saved by the tool_builder's reconstruction.)

## Sources

- House of Graphs graph page: https://houseofgraphs.org/graphs/51419
- House of Graphs API (canonical graph6 + adjacency list + embedding):
  https://houseofgraphs.org/api/graphs/51419
- Full JSON served by the API: `research/sources/markstrom-houseofgraphs-api.full.md`
- Wolfram MathWorld entry (GraphData["MarkstroemGraph"]):
  https://mathworld.wolfram.com/MarkstroemGraph.html

## Invariants (House of Graphs, graph 51419)

| Invariant | Value |
| --- | --- |
| Vertices / Edges | 24 / 36 |
| Regularity | cubic (degree 3 everywhere) |
| Planar / Genus | Yes / 0 |
| Girth | 3 |
| Diameter / Radius | 6 / 5 |
| Circumference | 24 |
| Chromatic Number / Index | 3 / 3 |
| Independence / Vertex cover / Matching | 9 / 15 / 12 |
| Number of spanning trees | 31,059,336 |
| Algebraic connectivity | 0.33802 |
| Second / smallest eigenvalue | 2.66198 / −2.19869 |
| Hamiltonian | Yes |
| Group size (automorphism) | 3 |
| Triangles | 7 |

## Cycle profile (Mechanical check — see `code/librarian_verify_markstrom.py`
and `code/verify_literature/reproduce_markstrom.py`)

The oracle (exact all-simple-cycles enumeration, `lib.cycle_oracle`) applied to
this graph gives: **no cycle of length 4, no cycle of length 8, but a cycle of
length 16 present**. Full cycle-length set is {3,5,6,7,9,…,24} (matching the
MathWorld profile). Powers of two {4,8} absent, {16} present.

## Cross-checks

- The graph6 string decodes to 24 vertices / 36 edges / cubic.
- The decoded edge set equals the HoG API adjacency list exactly.
- The decoded edge set equals the tool_builder's reconstruction
  (`code/out/markstrom_reconstruction/markstrom.edgelist`).
- The graph6 string equals the tool_builder's saved string
  (`code/out/markstrom_reconstruction/markstrom.graph6`) byte-for-byte.
- Planarity confirmed independently via networkx `check_planarity`.
- Spanning-tree count 31,059,336 reproduced exactly via Kirchhoff (exact
  rational Laplacian cofactor).

This is the independent route requested: feed
`Ws??W?@@?P?aA_?O?GG?a?@_?gA??a?@CO?CG?A@???a??D`
to the cycle oracle; it must report min degree 3 and cycle lengths avoiding 4
and 8 but including 16.
