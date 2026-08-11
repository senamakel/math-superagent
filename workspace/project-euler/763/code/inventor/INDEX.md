# Index — code/inventor

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `_run_fig3.py` | _(undescribed)_ |
| `check_eriksson_fig3.py` | _(undescribed)_ |
| `check_recurrence.py` | Tool_builder target: CLAIM A (deterministic reverse cap-collapse, top cap = exactly 3 cells = full child-triangle of one empty parent) and CLAIM B (D(N+1) = sum over conf(N) of f(C) = #dividable cells). Both verified on BFS reachable configs. |
| `probe_reachable.py` | Forward-BFS 3D config probe: verifies reverse-merge reachability (Eriksson voidance characterization) and voidance-set structure for small N. |
| `probe_topcap.py` | Empirical probe testing the top-cap collapse structure (T1 top==3, T2 unique cap, T3 deterministic collapse to origin) on forward-BFS 3D configs N<=6. |
| `research_structure.py` | _(undescribed)_ |
| `test_c1.py` | Tests conjecture C1 (reachable amoeba config == origin-connected set) by enumerating origin-connected sets (positive directed animals) by size and comparing to D_2D(N) and 3D D(N). RESULT: C1 is FALSE (2D counts match A005773 directed animals, not the amoeba sequence). Verified by an independent subset-based checker (code/out/verify_c1_subsets.py). Canonical copy relocated from code/ root. |
