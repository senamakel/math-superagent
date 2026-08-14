# Index — code/brute

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `independ_check.py` | Second-route verification of solution.py's outputs, sharing no iteration/control flow with it: (1) exhaustive closed-form scan of 0..10^5 per digit, stored in one array, asserting equality with the reported n≤10^5 solutions; (2) rechecks count, sum, last-solution, and last ≤ d·10^10 from the solution files; (3) re-evaluates f_place_value(n,d)=n for every third reported solution. RESULT: ALL CHECKS PASSED; grand total 21295121502550 reproduced from the saved per-digit sums. |
| `verify_brute.py` | Independent second route verifying code/brute.py's scan results. Uses the closed-form place-value counter (not string scanning) to confirm: (1) every one of the 14 oracle solutions 0..300000 has f(n,1)=n (all asserts passed); (2) 199981 is the third solution (no solution with 2<=n<=199980); (3) f(n,1)=3 never occurs in 0..300000; (4) no solution with 200002<=n<=300000. Also cross-checks place-value vs brute-force running total on all n in 0..20000. All checks passed — output is in the run transcript. |
