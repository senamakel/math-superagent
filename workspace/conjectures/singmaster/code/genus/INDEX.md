# Index — code/genus

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `diag_families.sing` | _(undescribed)_ |
| `extend3_4.sing` | Extends k2=3,4,5 to k1=24, confirming the closed forms. |
| `extend_falsifiers.sing` | _(undescribed)_ |
| `famA2.sing` | _(undescribed)_ |
| `famB.sing` | _(undescribed)_ |
| `famC.sing` | _(undescribed)_ |
| `famD.sing` | _(undescribed)_ |
| `full_grid.sing` | Full grid 2<=k1,k2<=12 (Singular). Output matches Sage. |
| `genus_table.py` | **Library**: verified genus table + closed forms for the {2,n},{3,n},{4,n} families; the deliverable's source of exact genus values. |
| `small_column_genus_forms.md` | _(undescribed)_ |
| `test_range.sing` | Mid-range probe: (4..10,3), (5..9,4), and (k,k) diagonal (shows reducible → nonsense genus, excluded). |
| `test_singular.sing` | First Singular test (failed: `genus` not in `sing.lib`). Kept as the dead-end record. |
| `test_singular2.sing` | Correct Singular recipe: load `normal.lib`, call `genus(ideal)`. Reproduces cubic=1, quartic=3, (3,2)=1. |
| `test_slope_across_rows.py` | _(undescribed)_ |
| `test_slope_hypothesis.py` | _(undescribed)_ |
| `verify_closed.py` | Checks closed forms vs the computed table (k2=2,3,4 all match). |
| `verify_closed2.py` | Attempts a k2=5 pattern; the obvious 2*floor and 2k1-a guesses FAIL — k2=5 has periodic stalls at multiples of 5. |
| `verify_k2_5_row.py` | _(undescribed)_ |
