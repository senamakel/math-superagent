# Index — code/bautin

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `generate_p30.py` | Sympy generator emitting the untrusted 30-monomial P30 data as Lean (Generated/P30Data.lean); deterministic lexicographic monomial order; same recurrence as verify_lu_core.py. |
| `verify_lu_core.py` | Clean-room re-derivation of the finite algebraic core of Lu arXiv:2607.13785 (H14^3 hemicycle): Bautin/Lyapunov recurrence (rotation operator, Q1,Q2, V2..V6, L4, L6), the degree-4 obstruction 8*L4=AC+CD+2DF-EF, degree-6 192*L6+P30=0, the four bridge parameter identities, and the Darboux cofactors X(L)=(x+dy)L, X(F)=(2Bx+dy)F, div X. Built from the paper's stated definitions only — does NOT import its scripts. Exact sympy arithmetic. Verified correct: executes with exit 0 printing "ALL ASSERTIONS PASS"; every identity ALSO confirmed independently by code/lyap_audit.py. Emits capture to code/out/lu_core.captured.txt and P30's 30 monomials to code/out/p30_coeffs.txt (temp file, moved on exit 0). |
