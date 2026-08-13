# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `H_EVEN_VERIFY_SPEC.md` | _(undescribed)_ |
| `brute.py` | Naive exact oracle for unitary perfect numbers: factors n by trial division, computes sigma_star(n) = prod_{p^a |
| `equality_case.py` | _(undescribed)_ |
| `equality_case_verify.py` | Independent exact-Fraction re-verification of equality-case bound. Already had fix for admissible_sizes (sort-then-slice with BOUND=800 + safety assertion); docstring updated to remove old bug-narrative. Verifies 4 points: a=1 / 4/3, a=8 / 257 forced, 3 vs 9 admissibility, exclusion 2≤a≤28 with M(29)>T(29). Post-fix capture at code/out/equality_case_verify.captured.txt is correct. |
| `heven_classify.py` | Phase A worked examples + Phase B classification of H_even cap [2,1200]: reproduces every worked example of the spec/paper for the 3-Higgs machinery, then combines heven_sieve.py's witness tables with full factorization of survivors to compute H_even cap [2,1200] and compare with the ten candidates of arXiv:2605.20475 Theorem 8. |
| `heven_complete_verify.py` | _(undescribed)_ |
| `heven_patterns.py` | _(undescribed)_ |
| `heven_sieve.py` | Phase B2: threaded witness sieve for H_even ∩ [2,1200]. Scans odd primes by gmpy2.next_prime over disjoint worker ranges to bound (1e8 or 1e9), skips primes with pow(2,2400,r)!=1, computes ord_r(2) for passers, archives (r,ord) to ord_sieve_table.tsv and every (r,m,ord) with r |
| `structural_search_CLOSED.py` | _(undescribed)_ |
