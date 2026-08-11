# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `ccsum.json` | Output of code/ccsum.py: conjugacy-class f_n(k) rows for n=2..16. CONFLICTS with the oracle-verified rows of out/extend_f.json (e.g. n=3 here is [13,8] vs verified [10,11], giving Q(3)=91 != 88) — UNTRUSTED, do not use until ccsum.py is re-validated; extend_f.json remains the trustworthy source for n=2..11. |
| `ccsum_ab.json` | Output of code/ccsum.py: derived A_n=f(1), B_n=f(2)-f(1) for n=2..16 from ccsum.json. CONFLICTS with the oracle-verified A_n/B_n (extend_f.json) — UNTRUSTED, do not use; see ccsum.json and code/ccsum.py. |
| `explore.out.txt` | Saved stdout of explore.py (n=2..7): M_j vectors and N(j,m) matrices exposing the translation-invariant gap function f(k)=N(j,j+k) |
| `extend_f.json` | Output of extend_f.py: exact rows {n: [f(1),...,f(n-1)]} of the gap function f_n(k)=#{(pi,i):0<=i<n!,(pi^i)(k)<(pi^i)(0)} for n=2..11, computed by the period formula (row j=0). Shows f_n exactly arithmetic in k with A_n=f(1), step B_n=f(2)-f(1); input for the closed-form hunt (fit*.py, aj3.py) and verify_f_method2.py |
| `fdtable.json` | Output of fdtable.py: per-n rows {n, d, phi(n!/d), F(d)} for n=4,5,6 plus totals; the verified F(d)/phi divisor table for the Q(n) structure |
| `rerun_output.txt` | Verbatim console output of the fresh re-run of brute.py then brute2.py (18 Sep 2025): rank check, Q(n) tables, oracle checks, cross-check lines; both exit 0 |
| `results.json` | Output of brute.py (method 1, literal): exact Q(n) and Q mod p for n=2..7; n=8 skipped (budget estimate exceeds cap) |
| `results2.json` | Output of brute2.py (method 2, period formula): exact Q(n) and Q mod p for n=2..8 (n=8 reached by method 2 only, 24768798220800); rewritten by the rerun |
