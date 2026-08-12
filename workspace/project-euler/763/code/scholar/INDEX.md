# Index — code/scholar

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `verify_fig3_n3.py` | Scholar-role verification of the folded-polyominoid definition itself: reproduces Eriksson Fig.3's n=3 folded-polyominoid column (k=0..6 = 1,3,12,57,300,1680,9900) by brute enumerating label pairs (u,v) of length k with k total nonzero labels in {1..n} satisfying Theorem 9 conditions (a),(b),(c). Exponential enumeration, tiny k only; verifies the sourced Theorem 9 bijection against Fig.3's published counts (all OK). Also records intent to check the 2D G(k,m) recurrence (see verify_gkm_2d.py for that). |
| `verify_gkm_2d.py` | Scholar-role verification: confirms the CGMO/Zhen-Knessl G(k,m) recurrence reproduces OEIS A007902 a(1..14) (the 2D amoeba), and sanity-checks Fig.3's Catalan column and n(3n-1)/2 row. Validates the 2D template that a 3D lift would generalise, with the memoized G(k,m) recurrence definition (local copy, kept as the scholar's own check rather than importing lib/amoeba2d). |
