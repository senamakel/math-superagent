# Index — code/refute

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `attack_s_universe.py` | Enumerates the weakened universe U_N = {connected graphs on <=N vertices : min-deg>=4, K4-free, K2,3-free, NO neighbourhood-max-degree condition} via nauty-geng -c -d4 -k, filters K2,3-free, and runs the calibrated SAT oracle at k=4 on each member. A 5-chromatic member refutes the run's open lemma S-universe-4color (the version of sharp-kernel-4color DROPPING condition (d)); needs a shell to actually run. |
| `check_kernel_model.py` | _(undescribed)_ |
| `check_nauty.py` | _(undescribed)_ |
| `check_nauty2.py` | _(undescribed)_ |
| `check_tptp_model.py` | Independent hand-decode + check of the 8-vertex model returned by find_counterexample on kernel_4color.p: verifies all four kernel conditions (min-deg=4, K4-free, K2,3-free, nbhd-maxdeg<=2) and finds an explicit proper 4-colouring, proving the engine's "refuted" verdict is a false positive. |
| `decode_model.py` | Single-purpose decode of the TPTP kernel_4color.p model's edge relation plus 4-colourability check; superseded by check_tptp_model.py. |
| `kernel_4color.p` | _(undescribed)_ |
| `probe_n12.py` | _(undescribed)_ |
| `probe_tools.py` | _(undescribed)_ |
| `probe_tools2.py` | _(undescribed)_ |
| `probe_tools3.py` | _(undescribed)_ |
| `run_both.py` | _(undescribed)_ |
| `run_check_kernel_model.py` | _(undescribed)_ |
| `run_check_kernel_model2.py` | _(undescribed)_ |
| `timing_n12.py` | Times nauty-geng at n=12 with K4-free/min-degree pruning to judge census feasibility. |
| `torus_min_graph_6col.p` | _(undescribed)_ |
