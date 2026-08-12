# code/out/expansion_census_26 — Index

Output of the level-n=26 K4-triangle-expansion census (driver `code/eg/expansion_resume_26.py`).

| File | Purpose |
| --- | --- |
| `level_26_pool.txt` | Phase A pool: every expanded candidate, one graph6 line per graph (8,454,672 lines, ~482 MB). |
| `level_26_pool_done` | Phase A checkpoint: number of source classes whose expansions are written (58713). |
| `level_26_classes.txt` | Phase B canonical classes: deduplicated canonical graph6, one per line (321,776 lines, ~18 MB). |
| `level_26_classes_done` | Phase B checkpoint: pool lines consumed (8,454,672). |
| `level_26_results.txt` | **Final census row** (also `level_26.txt`): `n=26 classes=321776 avoidsC4=3408 avoidsC4C8=0 avoidsC4C16=0 avoidsC4C8C16=0 c4free_hasC8_notC16=0`. |
| `run26.log` | Full console log with per-chunk progress and final wall time (837.9s total). |

## Result

- **Total classes = 321,776 = A027610(11)** exactly (sourced OEIS b-file; the A027610 12th term).
- **avoidsC4 = 3408**, **avoidsC4C8 = 0**, **avoidsC4C16 = 0**, **avoidsC4C8C16 = 0**, **c4free_hasC8_notC16 = 0**.
- All 321,776 members are cubic (degree 3 only).
- The **C16 cliff survives** at n=26: every C4-free member still contains a 16-cycle (avoidsC4C16=0).
- avoidsC4C8=0 confirms the family's only C4,C8-free member is at n=24; consistent with sourced f(4)≥54 (Exoo's smallest cubic with no C4/C8/C16 is order 78).
- Verified: an independent full re-scan (`code/eg/recount_26.py`) reproduces every count byte-for-byte.
- Wall time: **837.9s (~14 min)** on 28 cores (Phase A 307.8s, Phase B 496.4s, Phase C 33.7s), well within budget.
