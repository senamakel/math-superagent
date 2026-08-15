# Index — code/attempt2

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `dw_pairs.py` | Task B: sieve odd primes < 10^4 and find all ordered pairs p<q satisfying both double-Wieferich congruences q^(p-1)==1 mod p^2 and p^(q-1)==1 mod q^2 via exact pow(a,b,m); result exactly {(83,4871)}, with (2903,18787) verified outside the box; output captured at code/out/dw_pairs_1e4.captured.txt (EXIT 0). |
| `oracle_extend.py` | Task A: runs the exact-integer oracle solutions(N) at N=10^9 and N=10^10 via lib/valuation (reuses perfect_powers_upto/solutions), asserts result == {(3,2,2,3)}, prints wall runtime and an independent perfect-power count; output captured at code/out/oracle_1e10.captured.txt (EXIT 0). |
