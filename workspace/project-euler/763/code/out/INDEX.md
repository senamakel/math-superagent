# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `a007902_dp_values.txt` | Output data: the exact structural DP for OEIS A007902 run by code/amoeba2d/a007902_dp.py — a(1..22) with a(22)=13686805, and note that it matches OEIS A007902 exactly through a(33)=144558421877 and a(1..14) against the 2D BFS oracle. |
| `c1_test_results.md` | Result record of testing claim C1 (reachable amoeba sets == origin-connected sets): C1 is FALSE in both 2D and 3D. Enumerates origin-connected sets by size and compares to D_2D(N)/D(N); first disagreement N=1. The 2D count equals OEIS A005773 (directed animals), not the amoeba sequence. Records the reason: reachability constrains level distribution by division mass, so an arbitrary directed animal is not reachable. Dead end archived so the C1 structural hypothesis is not re-hunted. |
| `configs_n3_n4.txt` | Output data: the actual reachable configurations of Project Euler 763 for N=3 (9 configs) and N=4 (30 configs), each a sorted set of (x,y,z) cubes, one per line; produced by code/amoeba/configs_n3_n4.py. |
| `d2_values.txt` | Output data: D2(N) for the 2D amoeba N=0..20 = 1,1,2,4,9,20,46,105,243,561,1301,3014,6995,16227,37668,87426,202961,471150,1093819,2539348,5895408, written by code/amoeba/d2_bfs.py using the compact bitmask encoding from lib/amoeba2d. Extends the D_2D sequence beyond the d2d_values.txt N=0..14 record. |
| `d2d_values.txt` | Output of the 2D analogue run: D_2D(N) for N=0..14 = 1,1,2,4,9,20,46,105,243,561,1301,3014,6995,16227,37668, verified by two independent BFS routes (frozenset and int-encoded). |
| `d_values.txt` | Oracle output: D(N) for N=0..13 (1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267), reproduced from the BFS oracles; D(2)=3 and D(10)=44499 confirm the statement's worked examples. Superseded as a record by d_values_more.txt (which also has D(14)). |
| `d_values_more.txt` | Output data: fresh complete BFS-oracle D(N) sequence D(0)..D(14) = 1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063. Produced by code/amoeba/bfs_more.py; D(14) independently confirmed. |
| `extension_summary.md` | Record of the extension run: method, per-level timings, which N failed (15 & 16 unreachable under the 5M cap), verification of D(14). |
| `mhist_13_14.txt` | Output data: M-histograms (# distinct configs by max level M) at N=13 and N=14 for the 3D amoeba, produced by code/amoeba/mhist_13_14.py. Totals sum to D(13)=1749267 and D(14)=5949063 (verified). Notable structure: the M=N (maximal-level) bin equals 3^(N-1) in both rows (531441=3^12 for N=13, 1594323=3^13 for N=14). |
| `pattern_finder_summary.md` | _(undescribed)_ |
| `verify_c1_subsets.py` | Second, definitionally-independent oracle for the origin-connected (C1) counts: enumerates ALL subsets of the finite box [0,m-1]^d containing the origin and counts those literally origin-connected. Validates the forward-growth enumeration in test_c1.py for 2D m=1..6 and 3D m=1..4 (matches: 2D 1,2,5,13,35,96; 3D 1,3,12,52). Exponential, bounded to tiny boxes. |
