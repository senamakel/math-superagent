# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `configs_n3_n4.txt` | Output data: the actual reachable configurations of Project Euler 763 for N=3 (9 configs) and N=4 (30 configs), each a sorted set of (x,y,z) cubes, one per line; produced by code/amoeba/configs_n3_n4.py. |
| `d2_values.txt` | Output data: D2(N) for the 2D amoeba N=0..20 = 1,1,2,4,9,20,46,105,243,561,1301,3014,6995,16227,37668,87426,202961,471150,1093819,2539348,5895408, written by code/amoeba/d2_bfs.py using the compact bitmask encoding from lib/amoeba2d. Extends the D_2D sequence beyond the d2d_values.txt N=0..14 record. |
| `d2d_values.txt` | Output of the 2D analogue run: D_2D(N) for N=0..14 = 1,1,2,4,9,20,46,105,243,561,1301,3014,6995,16227,37668, verified by two independent BFS routes (frozenset and int-encoded). |
| `d_values.txt` | Oracle output: D(N) for N=0..13 (1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267), reproduced from the BFS oracles; D(2)=3 and D(10)=44499 confirm the statement's worked examples. Superseded as a record by d_values_more.txt (which also has D(14)). |
| `d_values_more.txt` | Output data: fresh complete BFS-oracle D(N) sequence D(0)..D(14) = 1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063. Produced by code/amoeba/bfs_more.py; D(14) independently confirmed. |
| `extension_summary.md` | Record of the extension run: method, per-level timings, which N failed (15 & 16 unreachable under the 5M cap), verification of D(14). |
| `recur.py` | Recurrence-search program (misfiled here from a shell): scans constant-coefficient linear recurrences (orders 1..7), holonomic forms, and an asymptotic ratio fit over the first 14 D(N) terms; found the order-7 linear recurrence confirmed by recur2.py/recur3.py. MISFILED — analysis program, not output data. |
| `recur2.py` | Companion recurrence program (misfiled here): verifies the order-7 constant-coefficient recurrence in integer form over all relations, factors the characteristic polynomial, and fits D(N)~C r^N N^alpha; confirms the recurrence from recur.py holds beyond the fitted range. MISFILED — analysis program, not output data. |
| `recur3.py` | Recurrence out-of-sample test (program, not output data — a third program that landed in code/out/ from a shell): fits the order-7 constant-coefficient linear recurrence to only the first 14 terms of D(N) (a 7x7 square system, unique coefficients), then predicts D(14)=5949063 and checks it matches; also fits to 12 terms leaving a 2-parameter family and checks the unfitted relations and D(14) are satisfied identically. Confirms the order-7 recurrence conjectured in recur.py/recur2.py generalizes beyond the fitted range. MISFILED here like recur.py/recur2.py; does not change what any other program computes. |
