# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `lu_core.captured.txt` | Capture of the clean-room verification run of code/bautin/verify_lu_core.py: names what ran, the definitions, the six identity groups, and shows the computed residuals 8*L4-(AC+CD+2DF-EF)=0, 192*L6+P30=0, P30 monomial count=30, ending "ALL ASSERTIONS PASS". Evidence for claim lu-finite-core-partially-verified (verified-computationally). |
| `p30_coeffs.txt` | Machine-readable Python list literal P30_TERMS = [(coeff,(deg_A,deg_C,deg_D,deg_E,deg_F)), ...] of the 30 monomials of the degree-6 Bautin-obstruction polynomial P30=-12*weighted_g6, in deterministic lexicographic order on (deg_A,deg_C,deg_D,deg_E,deg_F). Emitted by code/bautin/verify_lu_core.py with a round-trip assert that rebuilds P30 from the literal. For a later Lean step over MvPolynomial. |
