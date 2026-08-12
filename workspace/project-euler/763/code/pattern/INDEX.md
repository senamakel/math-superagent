# Index — code/pattern

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `full_triangle_dump.py` | Builds the full R(N,M) max-level triangle (#distinct configs after N divisions with max level M) from data/level_N.txt (N=2..12) plus code/out/mhist_13_14.txt (N=13,14); verifies R(N,N)=3^(N-1) and D(N)=sum_M R(N,M), and prints each fixed-M column R(N,M) as N varies for transfer-structure hunting. Now imports sorted_key from lib/datafiles (its former local split('level_') copy was a fourth duplicate of the canonical definition, now consolidated). |
