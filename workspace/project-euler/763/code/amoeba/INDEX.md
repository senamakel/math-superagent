# Index — code/amoeba

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `bfs_more.py` | Level-by-level exact BFS oracle for D(N) using a fixed-width W bitmask encoding, pushing the exponential oracle as far as a ~90s time or ~2M-state budget allows; writes D(0..Nmax) to code/out/d_values_more.txt. Carries results: reproduces D(0..14) including the worked examples D(2)=3 and D(10)=44499. Bit encoding cross-checked in code/brute_bits.py against the frozenset oracle for N=0..12. Exponential state space; this is the oracle, not the solver. |
| `configs_n3_n4.py` | Exact frozenset-of-tuples BFS that enumerates and prints the actual distinct arrangements reachable for N=3 (9 configs) and N=4 (30 configs) of Project Euler 763, to stdout and code/out/configs_n3_n4.txt. Asserts those counts equal D(3)=9 and D(4)=30 from the established d_values sequence. Used to inspect concrete configurations, not as a solver (exponential state space). |
