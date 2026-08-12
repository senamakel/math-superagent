# Index — code/inventor

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `_run_all.py` | _(undescribed)_ |
| `_run_fig3.py` | _(undescribed)_ |
| `check_eriksson_fig3.py` | Independent hand-arithmetic consistency check of the OCR'd Eriksson Fig.3 folded-polyominoid table (from research/L0.0/pebbling_ejc_survey.full.md): confirms column n=2 = Catalan C_{k+1} (1,2,5,14,42,132,429) and row k=2 = n(3n-1)/2 (1,5,12,22,35,51). Verifies internal consistency only, NOT that these are the true folded-polyominoid counts. Canonical copy relocated from code/ root (root check_eriksson_fig3.py is byte-identical and marked superseded). |
| `check_recurrence.py` | Tool_builder target verifying CLAIM A (deterministic reverse cap-collapse: every reachable 3D config has exactly 3 cells on its max level, forming the full child-triangle of one empty parent) and CLAIM B (D(N+1) = sum over conf(N) of f(C)=#dividable cells). One-step BFS now imported as canonical forward_level(level,3) from lib/amoeba (was a local hardcoded d=3 copy; identical semantics). |
| `probe_failures.py` | _(undescribed)_ |
| `probe_live.py` | _(undescribed)_ |
| `probe_reachable.py` | Forward-BFS 3D config probe: verifies reverse-merge reachability (Eriksson voidance characterization) and voidance-set structure for small N. |
| `probe_topcap.py` | Empirical probe of the 3D FE763 top-cap collapse structure on forward-BFS configs N<=6: T1 max level holds exactly 3 cells, T2 those 3 form the full child-triangle of a unique empty parent, T3 deterministic cap-collapse reaches origin. One-step BFS imported as canonical forward_level(level,3) from lib/amoeba (was a local hardcoded d=3 copy, identical semantics). |
| `research_structure.py` | Structural analysis of the PE763 growth rule: computes D(N) by exact BFS in d=2 and d=3 (importing canonical forward_level(level,d) from lib/amoeba) and verifies the reverse-merge characterization — every reachable config reduces to {origin} by replacing the d children of a common absent parent (Eriksson voidance picture). Prints d=2 D(0..14), d=3 D(0..12), and reverse-merge-vs-forward frontier agreement for d=2 N<=6. |
| `structure_probe.py` | _(undescribed)_ |
| `test_c1.py` | Tests conjecture C1 (reachable amoeba config == origin-connected set) by enumerating origin-connected sets (positive directed animals) by size and comparing to D_2D(N) and 3D D(N). RESULT: C1 is FALSE (2D counts match A005773 directed animals, not the amoeba sequence). Verified by an independent subset-based checker (code/out/verify_c1_subsets.py). Canonical copy relocated from code/ root. |
