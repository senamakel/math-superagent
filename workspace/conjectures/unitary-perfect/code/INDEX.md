# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute.py` | Naive exact oracle for unitary perfect numbers: factors n by trial division, computes sigma_star(n) = prod_{p^a |
| `heven_sieve.py` | Phase B2: threaded witness sieve for H_even ∩ [2,1200]. Scans odd primes by gmpy2.next_prime over disjoint worker ranges to bound (1e8 or 1e9), skips primes with pow(2,2400,r)!=1, computes ord_r(2) for passers, archives (r,ord) to ord_sieve_table.tsv and every (r,m,ord) with r|2^m+1 to witnesses_1200.tsv incrementally. Marks each witnessed m killed iff its witness r is 3-Higgs-checked non-Higgs. Validated at bound 1000 against heven_classify's full factorization oracle. |
