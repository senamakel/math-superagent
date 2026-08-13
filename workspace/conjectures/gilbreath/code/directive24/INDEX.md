# Index — code/directive24

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `verify_directive24_compute.py` | Independent verification of compute_width_degradation_and_growth.py via numpy: recomputes k*, asserts flooring(r)=0 on every row 162..1000 (839 rows), re-derives the 13 giant landing floors against the characterization table, re-derives the 43 b-increasing steps and that exactly the 13 giants have jump > 1000, and re-runs both fits with numpy.polyfit (reproduces geometric slope +0.519764 / R² 0.943852, linear R² 0.783043 for genuine 12; +0.494241 / 0.942088 vs 0.807242 for all 13). Exits 0 only if every claimed number matches. |
