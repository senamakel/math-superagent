# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `configs_n3_n4.txt` | Oracle output: the 9 distinct reachable arrangements for N=3 and the 30 for N=4 of Project Euler 763, each printed as a sorted set of (x,y,z) triples. Written by code/amoeba/configs_n3_n4.py, which asserts these counts match D(3)=9 and D(4)=30 from the established d_values sequence. |
| `d_values.txt` | Oracle output: D(N) for N=0..13 (1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267), reproduced from the BFS oracles; D(2)=3 and D(10)=44499 confirm the statement's worked examples. |
| `d_values_more.txt` | Oracle output: D(N) for N=0..14 (1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063), the full sequence written fresh on every run by code/amoeba/bfs_more.py. Extends d_values.txt (N=0..13) by one level (D(14)); D(2)=3 and D(10)=44499 confirm the statement's worked examples. |
| `recur.py` | Exploratory recurrence analysis (program, not output data — landed in out/ when a shell put it here): tries to fit D(N)=1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063 with (a) constant-coefficient linear recurrences of order 1..7, (b) holonomic (P-recursive) recurrences of small order/degree via nullspace, (c) asymptotic growth ratios D(N)/D(N-1). No solver result; a hypotheses-hunting aid. This file is MISFILED: it is a program and belongs in code/ (or a question folder), not code/out/ — kept in place because only write/edit tools are available (no move/delete), so relocating would leave a duplicate. It does not change what any other program computes. |
