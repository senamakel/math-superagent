# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `cycles.py` | THE shelved exact oracle for the run (networkx-based): min_degree, girth, cycle_lengths (exact set via networkx.simple_cycles, exponential so small-graphs-only), has_power_of_two_cycle, power_of_two_cycle_lengths, and nauty-geng-driven exists_delta3_no_power2_cycle/report_delta3_no_power2. Single compute core that brute.py and lib/oracle.py now delegate to. Verified by code/verify_cycles.py and code/eg/hand_dfs_check.py on K4, K3,3, Petersen, cube Q3. |
| `oracle.py` | Adjacency-list convenience layer over the shelved oracle: converts an adjacency-list graph to a networkx.Graph and delegates minimum_degree_and_cycle_lengths to lib.cycles (single compute core), plus power-of-two helpers and from_graph6/from_networkx input helpers. Supersedes the old independent DFS-copy of the oracle; core correctness rests on lib/cycles.py. |
