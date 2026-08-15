# Index — code/scholar_oracle

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `_run.py` | Placeholder only. This session has no execution tool; the ramification check must be run by a role that can execute. |
| `oracle.py` | Exact-integer naive oracle. solutions(N) returns every (x,p,y,q) with x^p,y^q<=N and x^p-y^q=1 by enumerating the set of perfect powers and checking consecutive values. Verified correct by (a) reproducing worked example (3,2,2,3), (b) matching a direct pairwise enumerator for N in {9,100,1000}, (c) all N up to 1e8 returning exactly (3,2,2,3). |
| `verify_ramification.py` | Exact sympy check of the three direct consequences of cyclotomic ramification: N(1-zeta_p)=Phi_p(1)=p, prod(1-zeta^j)=p, Phi_p(X) ≡ (X-1)^(p-1) mod p, for p in {3,5,7,11,13,17,19}. Previously written-but-never-run; executed this run, ALL PASS, captured at code/out/scholar_ramification_check.captured.txt. Third route for claim ramification-check-exact. |
