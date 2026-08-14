# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | _(undescribed)_ |
| `solution.py` | PE351 exact solution: prints parity table for n=5,10,1000 (identity H=3n^2+3n-6*Phi(n) vs embedded brute-force check), then computes Phi(10^8) via lib.totient.sum_phi (int32 sieve, ~400 MB) and prints Phi(10^8)=3039635516365908 and H(10^8)=11762187201804552. |
| `verify_mobius.py` | Independent verification of Phi(1e8): Möbius inversion Phi(N)=sum mu(k)*T(floor(N/k)) with a separate int8 mu sieve (step p^2 for squarefree zeroing). Agrees exactly with lib.totient.sum_phi; shares only the prime list. |
