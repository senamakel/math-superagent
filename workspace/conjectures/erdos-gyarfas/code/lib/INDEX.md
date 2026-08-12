# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `cycle_oracle.py` | Exact oracle for the Erdős–Gyárfás conjecture. `minimum_degree(G)->int`, `distinct_cycle_lengths(G)->frozenset[int]`, `all_simple_cycles(G)->list`, `has_cycle_of_length(G,L)->bool`, `oracle(G)->(min_deg, sorted tuple of lengths)`. Small-instance cycle oracle: min degree by counting neighbours; cycle lengths by brute-force enumeration of every simple cycle with a canonical-start DFS (a cycle basis is NOT enough — see module docstring). **Verified**: reproduces K4 {3,4}, K3,3 {4,6}, cube {4,6,8}, Petersen {5,6,8,9}; `has_cycle_of_length` cross-checked against exhaustive `distinct_cycle_lengths` on a spread of small graphs (complete, bipartite, cycles, hypercubes, Petersen, Markström graph, wheels, random) for every length 3..n — all MATCH; also cross-checked against networkx `simple_cycles` in `__main__`. |
| `k4expansion.py` | Membership test for the K4-triangle-expansion (cubic Apollonian dual) family, via recursion over clean-triangle contractions with memoisation; used for the Apollonian-family census against A027610. |
