# Index — code/amoeba2d

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `a007902_dp.py` | Exact DP for OEIS A007902 (2D amoeba/pebble-spreading counts). Imports the canonical `G(k,m)`/`a(n)` from lib/amoeba2d (single shared definition) and prints a(1..N) with main()'s OEIS match check. Correctness: reproduces OEIS A007902 first N terms (a(22)=13686805) and a(1..14) checked against the independent 2D BFS oracle code/amoeba2d/d2d.py (every value matches). This is the seed to be generalized to 3D for PE763. |
| `amoeba_2d.py` | 2D amoeba BFS oracle: amoeba at (x,y) divides into (x+1,y),(x,y+1) if both empty, counts distinct reachable occupied sets; compares to OEIS A007902. Imports its one-step successor next_level_fs2 from lib/amoeba2d.py. Canonical copy relocated from code/ root. |
| `check_a007902.py` | Verifies the canonical A007902 recurrence in lib/amoeba2d.G reproduces the 2D amoeba counts a(n)=A007902(n+1), importing the single shared definition. Canonical copy relocated from code/ root. |
| `check_ggm_recurrence.py` | Verifies two sourced facts: (1) the exact G(k,m) recurrence (CGMO eqs 2.1-2.3 = OEIS A007902, Alois P. Heinz) reproduces the run's independent 2D BFS oracle D2D(0..14) via a(n+1); (2) Eriksson Fig.3 identities — column n=2 equals Catalan C_{k+1} and row k=2 equals n(3n-1)/2. |
| `d2d.py` | 2D BFS oracle for D_2D(N): an amoeba at (x,y) divides into (x+1,y) and (x,y+1) if both empty, parent disappears, after N divisions a config holds N+1 cells; D_2D(N)=#distinct reachable occupied-cell sets. Verified 0..14 by an independent int-encoded bitmask BFS (both give 1,1,2,4,9,20,46,105,243,561,1301,3014,6995,16227,37668). |
| `verify_reverse_merge.py` | Verifies the reverse-merge (voidance-set) characterization of amoeba reachability for both 2D and 3D: every config reachable by forward BFS reduces to {origin} by repeatedly merging the d children of a common missing parent (Eriksson). Runs standalone over all reachable configs (d=2 to N=8, d=3 to N=4). Now imports the canonical children(p,d) from lib.amoeba (was a local copy). |
