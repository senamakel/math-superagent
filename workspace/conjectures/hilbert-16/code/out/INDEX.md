# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `bautin_focal_values.captured.txt` | _(undescribed)_ |
| `cofactor_certificate.captured.txt` | Capture of code/bautin/cofactor_certificate.py: evaluation-witness certificate that L8 ∉ ⟨L4,L6⟩ (Bautin focal values over Q). Witness (a1,a2,a3,b1,b2,b3)=(-2,-2,1,-1,-1,1) with L4=0, L6=0, L8=25/64; cleared-integer evaluations V1num=0, V2num=0, V3num=7200; CERTIFICATE VALID: PASS; 11679 points searched. Independently recomputed by direct sympy. Evidence for proving L8∉⟨L4,L6⟩ in code/lean/Lib/Bautin.lean (task cofactor-certificate-L8-not-in-L4-L6). |
| `commands.log` | _(undescribed)_ |
| `lean_tables.captured.txt` | Capture of code/bautin/verify_lean_tables.py: second independent route to "L8 not in <L4,L6>", validating the data tables the Lean kernel sees in code/lean/Lib/Bautin.lean. Parses V1num (6 explicit terms), v2coeffs/v2ms, v3coeffs/v3ms, certPt from raw file text; reconstructs and evaluates the three polynomials at certPt=(-2,-2,1,-1,-1,1) with exact integer arithmetic: eval V1num=0, eval V2num=0, eval V3num=7200; monomial counts 6/56/220. No sympy/recurrence. CERTIFICATE VALID: PASS. Evidence for theorem V3_not_mem_span_V1_V2 (task cofactor-certificate-L8-not-in-L4-L6). |
| `lu-core-identity-checked.md` | Claim block: the identity half of the Lu H14^3 finite core is checked (executed capture, ALL CLEAN-ROOM CHECKS PASS). Filed so the goals ledger can mark G-lu-core identity-half discharged by a claim id, with scope-limits naming the still-open membership extension and analytic remainder. |
| `lu_core.captured.txt` | Capture of the clean-room verification run of code/bautin/verify_lu_core.py: names what ran, the definitions, the six identity groups, and shows the computed residuals 8*L4-(AC+CD+2DF-EF)=0, 192*L6+P30=0, P30 monomial count=30, ending "ALL ASSERTIONS PASS". Evidence for claim lu-finite-core-partially-verified (verified-computationally). |
| `membership.captured.txt` | Capture of the exact-over-Q ideal-membership run of code/bautin/verify_membership.py (Bautin focal-value obstructions of the chart family Q1=A u^2+C u v+D v^2, Q2=E u v+F v^2, rotation linear part). Recomputes L4..L12 (monomial counts 4,30,97,236,485), passes the held audit guards (8L4=AC+CD+2DF-EF, 192L6+P30=0), and settles the lex-Groebner memberships: L8 in <L4,L6> = False, L6 in <L4> = False, L10 in <L4,L6,L8> = True, L12 in <L4,L6,L8> = True — each triple-checked (remainder==0, contains(), cofactor identity) with positive controls all True. Evidence for claim: the Bautin-trick step (higher focal values in the ideal of the first three) survives; three generators genuinely needed. |
| `mono_counts.captured.txt` | _(undescribed)_ |
| `naive-oracle-notes.md` | _(undescribed)_ |
| `p30_coeffs.txt` | Machine-readable Python list literal P30_TERMS = [(coeff,(deg_A,deg_C,deg_D,deg_E,deg_F)), ...] of the 30 monomials of the degree-6 Bautin-obstruction polynomial P30=-12*weighted_g6, in deterministic lexicographic order on (deg_A,deg_C,deg_D,deg_E,deg_F). Emitted by code/bautin/verify_lu_core.py with a round-trip assert that rebuilds P30 from the literal. For a later Lean step over MvPolynomial. |
