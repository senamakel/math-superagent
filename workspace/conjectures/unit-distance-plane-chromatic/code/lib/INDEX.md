# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `coloring.py` | Complete k-colourability test via exhaustive backtracking with symmetry breaking (DSATUR order, vertex 0 pinned to colour 0). `chromatic_colorable(n,edges,k)` returns (True,witness) or (False,None). `verify_coloring` independently checks a witness. Calibrated on the 7-vertex Moser spindle: k=4 SAT, k=3 UNSAT. |
| `satcolor.py` | Complete k-colourability via CNF + Cadical153. encode_kcol, is_k_colorable(edges,k,n)->(sat,witness), verify_witness. Calibrated: Moser k=3 UNSAT, k=4 SAT with proper-checked witness. |
| `unitfield.py` | Exact arithmetic in Q(sqrt3,sqrt11): add/sub/mul, sq_dist, unit_graph, all_sqdist, moser_spindle_points (7-vertex, 11 edges chi=4), diamond_points (4-vertex, tips at sqdist 3), minkowski_sum. Calibrated against code/brute.py. |
| `unitgraph.py` | Exact unit-distance graph construction. `unit_graph(points)` returns (n, edges) with every edge certified |
