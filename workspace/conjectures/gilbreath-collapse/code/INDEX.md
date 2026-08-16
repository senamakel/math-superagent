# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute.py` | Naive definition-following oracle for COLLAPSE: M_d via submask comprehension, Phi rows via literal binomial coeffs, S(n,h), rank via naive Gauss over F2, the symmetric-difference size formula, the telescoping identity, and the endpoint-sign form (product over runs R=[u,v] of chi(r_u)chi(r_{v+1}), boundary position v+1 not v, no prefactor). Reproduces every worked example in problem.md at small n — rows==indicator, rank=n-2, E[w]=(n-2)/2, Var(w)=(n-2)/4, E[S^2]=n-2, size formula, telescoping, endpoint-sign with two-valued r — and carries the three-valued negative control that must (and does) break endpoint-sign. Cross-checked against the fast canonical oracle code/lib/collapse.py via code/out/verify_multiset.py and verify_E_S2.py. |
