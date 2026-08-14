# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `totient.py` | Exact summatory totient: sum_phi(N) via incremental phi sieve on a numpy int32 table (memory-efficient at N=1e8), returns Python int; H_hexagon(n, Phi_n) applies H = 3n^2+3n-6*Phi. Correctness: parity checks against brute force at n=5,10,1000 and exact agreement with an independent Mobius-inversion computation at N=1e8. |
