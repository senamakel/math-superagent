# Index — code/amoeba

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `bfs_more.py` | Bitmask BFS that pushes the exact D(N) sequence for Project Euler 763 as far as feasible, driving one BFS step per level from N=0 up with a fixed grid width W, stopping when a single level exceeds a ~90s time budget or ~2M states, and writing a fresh complete file D(0)..D(Nmax) to code/out/d_values_more.txt. Correctness: the bit encoding was cross-checked in brute_bits.py against the frozenset oracle (validated on D(2)=3, D(10)=44499) for N=0..12. Used to extend the oracle sequence beyond what the frozenset versions reach. |
| `configs_n3_n4.py` | Exact frozenset-of-tuples BFS that enumerates and prints the actual distinct arrangements reachable for N=3 (9 configs) and N=4 (30 configs) of Project Euler 763, to stdout and code/out/configs_n3_n4.txt. Asserts those counts equal D(3)=9 and D(4)=30 from the established d_values sequence. Used to inspect concrete configurations, not as a solver (exponential state space). |
