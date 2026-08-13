# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute.py` | Naive exact oracle for unitary perfect numbers: factors n by trial division, computes sigma_star(n) = prod_{p^a |
| `equality_case_verify.py` | INDEPENDENT exact-Fraction re-derivation of the equality-case bound, not trusting equality_case.py: (1) a=1: T(1) and (1+1/5)(1+1/9) equal Fraction(4,3) exactly, {5,9} odd part of 90; (2) 2^8+1=257 prime by trial division, forcing 257 as a component since (2^a+1)|n, and the 8 smallest admissible sizes excluding 257 times (1+1/257) = 4235328000/2498670421 < 512/257; (3) 3,7 not admissible (3 mod 4), 9,49 admissible (1 mod 4); (4) table a=2..30 with M(a)<T(a) for 2<=a<=28 and M(29)>=T(29). All 4 points PASS, exact arithmetic throughout, no search over n. Verified by agreement with the pre-existing claim research/notes/equality-case-eliminated.md (M(8)=1.695032672, T(8)=1.992217899, cross at a=29). |
| `heven_sieve.py` | Phase B2: threaded witness sieve for H_even ∩ [2,1200]. Scans odd primes by gmpy2.next_prime over disjoint worker ranges to bound (1e8 or 1e9), skips primes with pow(2,2400,r)!=1, computes ord_r(2) for passers, archives (r,ord) to ord_sieve_table.tsv and every (r,m,ord) with r |
