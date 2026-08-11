# Index — code/inventor

Folded-polyominoid / reverse-merge structural investigations for PE763 (inventor thread).

| File | Purpose |
| --- | --- |
| `probe_reachable.py` | Recomputed 3D reachable configs by forward BFS for N=1..6; verifies (a) reverse-merge reduces every reachable config to {origin} (the Eriksson voidance characterization), (b) level histograms match the data/level_N.txt dumps. Pins down the exact counting object before building a DP. |
