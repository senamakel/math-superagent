# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `cycles.py` | THE shelved exact oracle for the run (networkx-based): min_degree, girth, cycle_lengths (exact set via networkx.simple_cycles, exponential so small-graphs-only), has_power_of_two_cycle, power_of_two_cycle_lengths, and nauty-geng-driven exists_delta3_no_power2_cycle/report_delta3_no_power2. Single compute core that brute.py and lib/oracle.py now delegate to. Verified by code/verify_cycles.py and code/eg/hand_dfs_check.py on K4, K3,3, Petersen, cube Q3. |
| `oracle.py` | Adjacency-list twin of the DFS oracle: minimum_degree(adj), cycle_lengths(adj) (exact set of simple-cycle lengths by naive DFS over an adjacency-list graph, deduping cycles on frozenset of vertices; exponential, small-graphs only), powers_of_two_cycle_lengths(lengths, min_k=2) and has_power_of_two_cycle(lengths, min_k=2) which take a length *set* (not a graph), plus from_graph6 / from_networkx input helpers returning adjacency lists. Verified against code/brute.py and code/lib/cycles.py on K4, K3,3, Petersen, cube Q3 — all agree. |
