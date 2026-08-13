# Index — code/cht_hyp

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `check_cht_hyp.py` | CHT Theorem 1.6 hypothesis check on real prime rows: sieves primes ≤ 2e7, computes normalized gaps a_n=(p_{n+2}−p_{n+1})/2−1 over the depth-1000 window, reports max a_n, M=ceil(log2 max), longest 0-run L, and R_0=100·L·8^M, concluding holds-here=no. Checked: first-nine a_n match the claim (0,0,1,0,1,0,1,2,0); max gap 180 (primes 17051707/17051887) and 0-run 2 independently recomputed by a second program. |
