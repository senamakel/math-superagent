# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive exact-arithmetic oracle: unit_graph(points) certifies \ |
| `check_lenz_planar.py` | Exact sympy check of the planar restriction of the Lenz construction: unit chords on radius-1/sqrt(2) circles are exactly 90-degree chords, and cross-circle unit pairs between two concentric circles are at most 2 per vertex. Written by librarian; NOT yet executed (no shell tool). Tool_builder/coder should run it to certify the derived claim. |
| `check_scholar.py` | Scholar's independent verification harness: capture integrity (sha256), independent chromatic recomputation of the 7-vertex spindle, hand-derived census sample counts, and the K3-vs-Z^n lattice-criterion contradiction that the Chilakamarri pair poses. Not a construction tool; a check on what the ledger asserts. |
| `extend_spindle_census.py` | Counts-only extension of the A^k census beyond the coloured levels: reports n(k) and e(k) (exact is_unit) for k in a given range without running the colouring test. Produced k=7 (n=876, e=4694); skips colouring so no chi claim should be attached to its output. |
| `lattice_census.py` | Exact census of square (S_r: n=(2r+1)^2, e=4r(2r+1), chi=2) and triangular A2 hexagon (H_r: n=3r(r+1)+1 centered-hexagonal, e=3r(3r+1) hexagonal-matchstick, chi=3) lattice patches via a complete DSATUR colouring test cross-checked against the calibrated brute oracle. Scale calibration. |
| `minkowski_growth_fit.py` | Exact Fraction-arithmetic Lagrange interpolation over the measured census counts (k=1..6). Establishes n(k)=(k^4+6k^3+14k^2+15k+6)/6 on the six measured levels (out-of-sample n(6)=532 match, k^5 coeff 0) and that e(k) is not quartic (k^5 coeff -1/60). Correctness: reproduces the six measured data points exactly; capture in code/out/minkowski_growth_fit.captured.txt. |
| `run_scholar_bounded.sh` | Bounded launcher (timeout 120) per compute policy, invoking run_scholar_checks.py. |
| `run_scholar_checks.py` | Launcher that runs check_scholar.py and writes its captured output under code/out/ with the exit code, so the scholar's verification is recorded where the run reads it. |
| `spindle_minkowski_census.py` | _(undescribed)_ |
