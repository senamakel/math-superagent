# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive exact-arithmetic oracle for the unit-distance problem. Defines the field Q(sqrt3,sqrt11) with exact (rational) arithmetic, unit_graph(points) which certifies edges by squared distance exactly 1, and a complete backtracking k-colouring test with witness. Calibrated: reproduces the 7-point two-lozenges graph from problem.md with exactly 11 edges, chi=4, not 3-colourable — all in exact arithmetic, matching the worked example. |
| `sat_calibration.py` | Second, independent route to the Moser spindle calibration: CNF k-colourability encoding solved with real SAT solvers (PySAT Cadical153 and Minisat22), with exact reconstruction cross-check of the edge list and a pure-integer witness validator. Reproduces k=4 SAT with witness and k=3 UNSAT that brute.py's exhaustive route already established. |
| `sat_count_check.py` | Strengthened cross-check: compares the exact number of proper k-colourings of the 7-vertex Moser spindle obtained two independent ways — brute-force enumeration (oracle) vs SAT-based model enumeration via Cadical153 — agreeing exactly for every k (0,0,0,384,5040). No floats. |
