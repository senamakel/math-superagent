# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `check_library_values.py` | Library-value oracle: computes Phi(n) by a naive phi sieve and checks H(5)=30, H(10)=138, H(1000)=1177848 (statement oracles) plus Phi(10^k) k=0..8 against OEIS A064018, then prints the check anchor H(10^8) = 3·10^8·(10^8+1) − 6·Phi(10^8) = 11762189901804552 that solution.py must reproduce. Exact integer arithmetic; the final answer is anchored here. |
