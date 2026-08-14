# Index — code/brute

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `verify_brute.py` | Independent second route verifying code/brute.py's scan results. Uses the closed-form place-value counter (not string scanning) to confirm: (1) every one of the 14 oracle solutions 0..300000 has f(n,1)=n (all asserts passed); (2) 199981 is the third solution (no solution with 2<=n<=199980); (3) f(n,1)=3 never occurs in 0..300000; (4) no solution with 200002<=n<=300000. Also cross-checks place-value vs brute-force running total on all n in 0..20000. All checks passed — output is in the run transcript. |
