# Index — code/out/expansion_census

Census output of the K4-triangle-expansion family (`code/eg/expansion_census_fast.py`),
levels n=4,6,...,24.

| File | Purpose |
| --- | --- |
| `level_<n>.txt` | One-line summary per level: `n classes avoidsC4 avoidsC4C8`, plus the cumulative history. |
| `level_<n>.canon` | Canonical graph6 of each isomorphism class at level n (missing for n=24; see level_24_classes.txt). |
| `level_24_classes.txt` | Canonical graph6 of all 58713 classes at n=24 (identity with A027610(10) verified). |
| `level_24_pool.txt` / `level_24_pool_done` / `level_24_classes_done` | Intermediate work files from the level-24 run (pooled expansion graphs, completion markers). |
| `level_24_results.txt` | `n=24 classes=58713 avoidsC4=807 avoidsC4C8=1` — the only n=24 result row. |

## Key verified facts (pattern_finder, this run)

- Total classes at n=24 = 58713 = A027610(10): the Apollonian/planar-3-tree identity now
  holds for 11 terms. Sequence 1,1,1,3,7,24,93,434,2110,11002,58713.
- avoidsC4C8 is 0 for every n=4..22 and 1 at n=24.
- The single C4,C8-free member of the family is byte-for-byte the Markström graph
  HoG 51419 (graph6 `Ws??W?@@?P?aA_?O?GG?a?@_?gA??a?@CO?CG?A@???a??D`), confirmed by
  exact graph6 identity and by reverse-expansion BFS to K4 at depth 10.
