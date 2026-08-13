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
| `spotcheck_new_pairs.sing` | Job-2 spot check of the closed genus formula g(m,n)=((m-1)(n-1)+1-gcd(m,n))/2 at three pairs absent from genus_table.py TABLE and all captures: (11,17), (11,20), (12,20). Same incantation as full_grid.sing (ring r=0,(x,y),dp; poly CB; degree-max(m,n) curve; normal.lib genus). All three PASS with Singular genus 80/95/103, cross-verified by an independent Python computation of the formula. |
| `test_range.sing` | Mid-range probe: (4..10,3), (5..9,4), and (k,k) diagonal (shows reducible → nonsense genus, excluded). |
| `test_singular.sing` | First Singular test (failed: `genus` not in `sing.lib`). Kept as the dead-end record. |
| `test_singular2.sing` | Correct Singular recipe: load `normal.lib`, call `genus(ideal)`. Reproduces cubic=1, quartic=3, (3,2)=1. |
| `test_slope_across_rows.py` | _(undescribed)_ |
| `test_slope_hypothesis.py` | _(undescribed)_ |
| `verify_closed.py` | Checks closed forms vs the computed table (k2=2,3,4 all match). |
| `verify_closed2.py` | Attempts a k2=5 pattern; the obvious 2*floor and 2k1-a guesses FAIL — k2=5 has periodic stalls at multiples of 5. |
| `verify_k2_5_row.py` | _(undescribed)_ |
| `verify_superelliptic_formula.py` | Cross-checks the run's computed genus rows for C(x,k1)=C(y,k2) against the literature superelliptic genus formula g=((d-2)(m-1)+m-gcd(m,d))/2 (Sutherland 2020, Wikipedia Superelliptic curve). Checks {2,n} hyperelliptic (10 values) and {3,n} trigonal (21 values) against the recorded table; reports {4,n} as a 2:1 cover where the plain formula does not apply. Written by the librarian pass; NOT yet executed — run with timeout 540 and tee to code/out/ to make the hand-verified reproduction machine-checked. |
