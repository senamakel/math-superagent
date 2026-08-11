# Index — code/amoeba2d

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `a007902_dp.py` | Exact DP for OEIS A007902 (2D amoeba/pebble-spreading counts). a(1)=1, a(n)=G(n,0) via the auxiliary G(k,m) recurrence translated from the OEIS entry (Alois P. Heinz). Functions: G(k,m) memoized, a(n), a_seq(max_n), g_table(k_max). Correctness: reproduces OEIS A007902 a(1..33) exactly (incl. a(22)=13686805), and a(1..14) checked against the independent 2D BFS oracle code/amoeba2d/d2d.py (every value matches). This is the seed to be generalized to 3D for PE763. |
| `check_ggm_recurrence.py` | _(undescribed)_ |
| `d2d.py` | 2D BFS oracle for D_2D(N): an amoeba at (x,y) divides into (x+1,y) and (x,y+1) if both empty, parent disappears, after N divisions a config holds N+1 cells; D_2D(N)=#distinct reachable occupied-cell sets. Verified 0..14 by an independent int-encoded bitmask BFS (both give 1,1,2,4,9,20,46,105,243,561,1301,3014,6995,16227,37668). |
| `verify_reverse_merge.py` | Verifies the reverse-merge (voidance-set) characterization of amoeba reachability for both 2D and 3D: every config reachable by forward BFS is also reducible to {origin} by repeatedly merging the d children of a common missing parent (Eriksson's Fact 5). Runs standalone over all reachable configs for small N (d=2 to N=8, d=3 to N=4). Supports the run's structural reverse-merge claim. |
