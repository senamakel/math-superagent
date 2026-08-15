# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `coloring.py` | k-colourability oracle **unsound in the False direction** (documented) |
| `critoracle.py` | critical-graph oracle |
| `frac_chro_check.py` | flag: exact-LP check of chi_f (fractional chromatic number) for C5/diamond/Moser |
| `frac_chro_verify.py` | Independent check of chi_f (fractional chromatic number) via the LP over the independent-set polytope (primal + dual, scipy highs) on the calibration graphs C5/diamond/Moser with edge lists exactly matching code/frac_chro_calib.py. Verifies primal==dual (strong LP duality) and the expected values chi_f(C5)=5/2, chi_f(diamond)=3. NOT yet executed this session — scholar should run it as the independent route. |
| `gpu_determinism.py` | GPU determinism |
| `pdf_numbers.py` | PDF number extraction |
| `satcolor.py` | SAT k-colourability encoding |
| `torus_margin.py` | hexagon-tiling upper-bound margin |
| `torus_minsep.py` | torus minimum-separation |
| `unitfield.py` | Algebraic number field helpers (Q(sqrt3,sqrt11)); `minkowski_sum` |
| `unitgraph.py` | Exact unit-distance graph construction/verification |
