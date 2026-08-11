# Index — code/amoeba

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `bfs_more.py` | Level-by-level exact BFS oracle for D(N) of Project Euler 763 using a COMPACT per-level bitmask encoding (width W = level+1, keeping each int minimal; children re-encoded at width W+1). Own one-step successor next_level_compact, distinct from lib/amoeba.py's fixed-width routine. Stops on a time budget or state cap; writes D(0..Nmax) to code/out/d_values_more.txt. Reproduces D(0..14) incl. worked examples D(2)=3, D(10)=44499, extending D(14)=5949063 (independently matched by fixed-width extension and amoeba_verify.py). Oracle, not solver; limited by the 2 GB cgroup memory cap which forbids D(15) (~20M states). |
| `configs_n3_n4.py` | BFS oracle with exact frozenset-of-tuples arithmetic that prints the actual reachable configurations of Project Euler 763 for N=3 (9 states) and N=4 (30 states), sorted, one per line, to code/out/configs_n3_n4.txt. Asserts the counts match D(3)=9, D(4)=30 from the established d_values sequence (itself validated on D(2)=3, D(10)=44499). |
