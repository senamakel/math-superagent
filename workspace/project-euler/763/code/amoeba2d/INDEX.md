# Index — code/amoeba2d

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `d2d.py` | 2D BFS oracle for D_2D(N): an amoeba at (x,y) divides into (x+1,y) and (x,y+1) if both empty, parent disappears, after N divisions a config holds N+1 cells; D_2D(N)=#distinct reachable occupied-cell sets. Verified 0..14 by an independent int-encoded bitmask BFS (both give 1,1,2,4,9,20,46,105,243,561,1301,3014,6995,16227,37668). |
