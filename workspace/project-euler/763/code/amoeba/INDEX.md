# Index — code/amoeba

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `amoeba_extend.py` | _(undescribed)_ |
| `amoeba_verify.py` | Second, structurally independent 3D BFS oracle for PE763 D(N): builds a non-blocked-cube set and re-derives the successor step, verifying the primary bitmask D(14)=5949063 by a second route. Validated by reproducing D(0..13). Canonical copy relocated from code/ root. |
| `bfs_more.py` | Level-by-level exact BFS oracle for D(N) using COMPACT per-level bitmask (width = level+1) to extend the oracle; stops on time/state cap and writes D(0..Nmax). Carries extant results D(2)=3, D(10)=44499 and D(14)=5949063; exponential state space, it is the oracle not the solver. |
| `brute.py` | _(undescribed)_ |
| `brute_bits.py` | Memory-compact int-bitmask 3D BFS oracle for D(N): each config a fixed-width W bitmask so encoding is level-independent. Imports next_level_bits from lib/amoeba.py (not duplicated). Cross-checked against the frozenset oracle for N=0..12. Canonical copy relocated from code/ root. |
| `brute_capped.py` | _(undescribed)_ |
| `brute_extended.py` | _(undescribed)_ |
| `configs_n3_n4.py` | BFS oracle with exact frozenset-of-tuples arithmetic that prints the actual reachable configurations of Project Euler 763 for N=3 (9 states) and N=4 (30 states), sorted, one per line, to code/out/configs_n3_n4.txt. Asserts the counts match D(3)=9, D(4)=30. Now imports its one-step successor as next_level_fs from lib/amoeba.py (previously a local copy). |
| `d2_bfs.py` | Clean exact level-by-level BFS oracle for the 2D amoeba D2(N) using the compact bitmask encoding from lib/amoeba2d; pushes much higher than the d=3 ceiling of N=14 because the 2D state space grows far more slowly. Writes D2(0..Nmax) to code/out/d2_values.txt. Validated at small N against the frozenset oracle (d2_check.py). |
| `d2_check.py` | Frozenset oracle for the 2D amoeba; independent validation that the bitmask BFS matches for N=0..12 (D2 = 1,1,2,4,9,20,46,105,243,561,1301,3014,6995). |
| `mhist_13_14.py` | Level-by-level exact BFS for PE763 (lib/amoeba.next_level_bits, fixed-width bitmask) that also counts distinct configs at N=13 and N=14 grouped by max level M = max(x+y+z), saving the M-histograms to code/out/mhist_13_14.txt. Totals verified: N=13 sum 1749267 = D(13), N=14 sum 5949063 = D(14), both independently established. Does not write full config dumps. Runs ~69s total; needs explicit gc.collect() between levels to stay under the 2 GiB cgroup cap (first attempt OOM'd, fixed by the GC call). |
