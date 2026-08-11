# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `configs_n3_n4.txt` | Output data: the actual reachable configurations of Project Euler 763 for N=3 (9 configs) and N=4 (30 configs), each a sorted set of (x,y,z) cubes, one per line; produced by code/amoeba/configs_n3_n4.py. |
| `d_values.txt` | Oracle output: D(N) for N=0..13 (1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267), reproduced from the BFS oracles; D(2)=3 and D(10)=44499 confirm the statement's worked examples. Superseded as a record by d_values_more.txt (which also has D(14)). |
| `d_values_more.txt` | Output data: fresh complete BFS-oracle D(N) sequence D(0)..D(14) = 1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063. Produced by code/amoeba/bfs_more.py; D(14) independently confirmed. |
| `extension_summary.md` | Record of the extension run: method, per-level timings, which N failed (15 & 16 unreachable under the 5M cap), verification of D(14). |
| `recur.py` | _(undescribed)_ |
| `recur2.py` | _(undescribed)_ |
| `recur3.py` | Recurrence out-of-sample test (program, not output data — a third program that landed in code/out/ from a shell): fits the order-7 constant-coefficient linear recurrence to only the first 14 terms of D(N) (a 7x7 square system, unique coefficients), then predicts D(14)=5949063 and checks it matches; also fits to 12 terms leaving a 2-parameter family and checks the unfitted relations and D(14) are satisfied identically. Confirms the order-7 recurrence conjectured in recur.py/recur2.py generalizes beyond the fitted range. MISFILED here like recur.py/recur2.py; does not change what any other program computes. |
