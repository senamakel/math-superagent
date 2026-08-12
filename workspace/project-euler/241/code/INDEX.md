# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive brute force for Project Euler 241: finds all n<=N with perfection quotient p(n)=sigma(n)/n equal to k+1/2 for integer k, i.e. 2*sigma(n)/n an odd integer. Sieves smallest-prime-factor up to N, computes sigma(n) from spf factorisation via the multiplicative formula, prints n with 2*sigma % n == 0 and odd (2*sigma//n). CLI arg = max N (default 1e6). Verified: sigma(6)=12; sigma values agree with independent trial-division sigma over 1..200000; the qualifying set {2,24,4320,4680,26208} (k = 1,2,3,3,3) reproduced by a direct trial-division oracle up to 1e6. |
| `out.md` | Output directory for program artifacts. |
| `seqgen.py` | _(undescribed)_ |
