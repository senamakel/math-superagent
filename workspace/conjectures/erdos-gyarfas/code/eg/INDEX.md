# Index — code/eg

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `bruteforce_bound.py` | The verification-bound edge: uses nauty-geng to enumerate every connected min-degree-3 graph on n vertices (up to iso) and the exact oracle to test the Erdos-Gyarfas predicate, reporting counts and whether a counterexample exists. Shows where exhaustive generation stops being the method. Depends on lib.cycles. |
| `girth_survivors.py` | Sequence of obstruction survivors: counts connected min-degree-3 graphs on n vertices whose girth clears the first power-of-two barrier (girth >= 5, no 4-cycle). Shows how the first obstacle prunes the search space. Depends on lib.cycles (_geng_graph6, min_degree, girth). |
| `hand_dfs_check.py` | Independent-verification file: a fully hand-written DFS oracle (min_degree, girth, exact simple-cycle-length set, power-of-two lengths) with no imports from lib/cycles or lib/oracle, cross-checked against lib/cycles.py on K4, K3,3, cube Q3 and Petersen. A third, independent code path confirming the shelved oracle is not an artifact of one implementation. |
| `verify_cycles.py` | Verification harness for the shelved lib/cycles.py: asserts min_degree, cycle_lengths, girth and power-of-two predicates on K4, K3,3, cube Q3, Petersen plus extra graphs (K5, K2,3, triangle, C5+C6, path P6). The run's regression check for the oracle; depends on lib.cycles. |
