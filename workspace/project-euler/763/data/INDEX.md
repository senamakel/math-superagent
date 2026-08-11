# Index — data

Per-config structural-feature dumps for the PE763 3D amoeba problem, produced
by `code/amoeba_extend.py` (which uses the verified BFS from
`code/lib/amoeba.py`). Each file covers one level N and has exactly D(N) lines
(one per distinct reachable configuration after exactly N divisions).

Format per line (`|`-separated):
```
level_histogram_a_k (space separated, a_k = #cubes in level k) | M | dx dy dz
```
where M = max level present = max(x+y+z) and (dx,dy,dz) are the bounding-box
extents. This is the structural data GOAL.md asks for: the level histogram,
max level, and bounding-box dims of every distinct config.

| File | Lines (D(N)) | Purpose |
| --- | --- | --- |
| `level_2.txt` | 3 | Feature dump for N=2 (D(2)=3). |
| `level_3.txt` | 9 | Feature dump for N=3 (D(3)=9). |
| `level_4.txt` | 30 | Feature dump for N=4 (D(4)=30). |
| `level_5.txt` | 99 | Feature dump for N=5 (D(5)=99). |
| `level_6.txt` | 336 | Feature dump for N=6 (D(6)=336). |
| `level_7.txt` | 1134 | Feature dump for N=7 (D(7)=1134). |
| `level_8.txt` | 3855 | Feature dump for N=8 (D(8)=3855). |
| `level_9.txt` | 13086 | Feature dump for N=9 (D(9)=13086). |
| `level_10.txt` | 44499 | Feature dump for N=10 (D(10)=44499). |
| `level_11.txt` | 151263 | Feature dump for N=11 (D(11)=151263). |
| `level_12.txt` | 514419 | Feature dump for N=12 (D(12)=514419). |

Line counts equal the reproduced D(N) values, so the dumps are internally
consistent with the BFS oracle.
