# Index — code/genus

Programs computing the genus of the curve `C(x,k1) = C(y,k2) = 0` and the
resulting table and closed forms. Genus is of the projective closure, computed
by two independent CAS methods that agree.

| File | Purpose |
| --- | --- |
| `test_singular.sing` | First Singular test (failed: `genus` not in `sing.lib`). Kept as the dead-end record. |
| `test_singular2.sing` | Correct Singular recipe: load `normal.lib`, call `genus(ideal)`. Reproduces cubic=1, quartic=3, (3,2)=1. |
| `test_range.sing` | Mid-range probe: (4..10,3), (5..9,4), and (k,k) diagonal (shows reducible → nonsense genus, excluded). |
| `full_grid.sing` | Full grid 2<=k1,k2<=12 (Singular). Output matches Sage. |
| `extend3_4.sing` | Extends k2=3,4,5 to k1=24, confirming the closed forms. |
| `verify_closed.py` | Checks closed forms vs the computed table (k2=2,3,4 all match). |
| `verify_closed2.py` | Attempts a k2=5 pattern; the obvious 2*floor and 2k1-a guesses FAIL — k2=5 has periodic stalls at multiples of 5. |
| `genus_table.py` | **Library**: verified genus table + closed forms for the {2,n},{3,n},{4,n} families; the deliverable's source of exact genus values. |

Result: `/workspace/code/out/genus_table.captured.txt`.

**What established the table is correct:** every entry computed by Singular
`genus(ideal)` and by Sage `Curve(f).genus()` independently, agreeing over
2<=k1,k2<=12 and (k2=3,4,5) up to k1=24; the closed forms for k2=2,3,4 match
every computed entry of their families; literature cross-checks (3,4)=3
(de Weger), (2,5)=2 (Bugeaud, hyperelliptic), (2,n)=floor((n-1)/2) hold.
