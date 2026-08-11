# Index — code/amoeba

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `bfs_more.py` | Level-by-level exact BFS oracle for D(N) using COMPACT per-level bitmask (width = level+1) to extend the oracle; stops on time/state cap and writes D(0..Nmax). Carries extant results D(2)=3, D(10)=44499 and D(14)=5949063; exponential state space, it is the oracle not the solver. |
| `configs_n3_n4.py` | BFS oracle with exact frozenset-of-tuples arithmetic that prints the actual reachable configurations of Project Euler 763 for N=3 (9 states) and N=4 (30 states), sorted, one per line, to code/out/configs_n3_n4.txt. Asserts the counts match D(3)=9, D(4)=30 from the established d_values sequence (itself validated on D(2)=3, D(10)=44499). |
| `d2_bfs.py` | Clean exact level-by-level BFS oracle for the 2D amoeba D2(N) using the compact bitmask encoding from lib/amoeba2d; pushes much higher than the d=3 ceiling of N=14 because the 2D state space grows far more slowly. Writes D2(0..Nmax) to code/out/d2_values.txt. Validated at small N against the frozenset oracle (d2_check.py). |
| `d2_check.py` | Frozenset-of-tuples oracle for the 2D amoeba D2(N) that also cross-checks the compact bitmask BFS (lib/amoeba2d next_level_bits2_compact) against it for N=0..max_n. Simple and obviously faithful; the independent small-N oracle that validates d2_bfs.py. |
