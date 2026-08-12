# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `gears.py` | The meshing model under test for PE620: continuous centre-distance d parameterization, planets forced to circle(O,R-rho) ∩ circle(S,r+rho), valid iff eliminated phase conditions 2Fp, 2Fq, H are integers mod 1 (sign convention F = R*beta - r*gamma - T). g_count scans the d interval at grid_points; G_sum sums over the s+p+q<=n pairs. FAILED the oracle: g(16,5,5,6)=0 vs 9, G(16)=0 vs 9, G(20)=0 vs 205 (see code/out/oracle_test.txt). Do not extend; the discrete least-mesh-angle lattice model is the next route. |
