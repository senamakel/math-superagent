# Index — code/cht_hyp

CHT Theorem 1.6 hypothesis check against the real prime rows.

| File | Purpose |
| --- | --- |
| `check_cht_hyp.py` | Sieves primes ≤ 2e7, computes normalized gaps a_n=(p_{n+2}−p_{n+1})/2−1 over the 1,270,605-gap window, and reports max a_n, M=ceil(log2 max), longest 0-run L, and R_0=100·L·8^M, concluding holds-here = no. Established correct: reproduces the claim's first-nine a_n values (0,0,1,0,1,0,1,2,0) and the max-gap/0-run numbers are independently recomputed by a second program. |
