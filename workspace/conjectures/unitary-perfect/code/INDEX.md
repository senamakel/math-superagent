# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `H_EVEN_VERIFY_SPEC.md` | _(undescribed)_ |
| `_run_v2check.py` | _(undescribed)_ |
| `biquadratic_table.py` | _(undescribed)_ |
| `brute.py` | Naive exact oracle for unitary perfect numbers: factors n by trial division, computes sigma_star(n) = prod_{p^a |
| `cunningham_appc_v2check.py` | Staged structural probe using the newly-held Cunningham Appendix C +1-side data: tabs v2(q-1) over prime divisors q of 2^m+1 for reachable even m and cross-references Appendix C 2,n+/2,nL,M cofactor entries to test the paper's v2∈{2,3}/no-r≡1-mod-16 claim on the reachable scale. Not a sixth-UPN search. Ready for coder to run under timeout 540; capture target code/out/cunningham_appc_v2check.captured.txt. |
| `equality_case.py` | _(undescribed)_ |
| `equality_case_verify.py` | Independent exact-Fraction re-verification of equality-case bound. Already had fix for admissible_sizes (sort-then-slice with BOUND=800 + safety assertion); docstring updated to remove old bug-narrative. Verifies 4 points: a=1 / 4/3, a=8 / 257 forced, 3 vs 9 admissibility, exclusion 2≤a≤28 with M(29)>T(29). Post-fix capture at code/out/equality_case_verify.captured.txt is correct. |
| `heven_classify.py` | Phase A worked examples + Phase B classification of H_even cap [2,1200]: reproduces every worked example of the spec/paper for the 3-Higgs machinery, then combines heven_sieve.py's witness tables with full factorization of survivors to compute H_even cap [2,1200] and compare with the ten candidates of arXiv:2605.20475 Theorem 8. |
| `heven_complete_verify.py` | _(undescribed)_ |
| `heven_gauss.py` | First concrete step of the adopted biquadratic-character approach: exact Gaussian factorization of 2^p + i in Z[i] for odd primes p <= 61 (Cornacchia + sympy factorint of 2^{2p}+1), computing (2/r)_4 per divisor r via quartic_char, Aurifeuillean half membership, and v2(r-1). Verifies the ord=4p primitive-divisor structure (with the LTE exception v_5(Phi)=1 at p=5, found by the check's own failure first run), the equivalence (2/r)_4=+1 <==> r==1 mod 16, and reproduces every H_even member 2p in {6,10,26,46,62,82,122} with all divisors 3-Higgs; finds a non-3-Higgs head r==1 mod 16 for every 3-Higgs p<=61 whose 2p is NOT in H_even. Output: code/out/heven_gauss_61.captured.txt (all checks C1-C7 pass, 71 divisor rows, none left unfactored). Correctness established by the run's own exact asserts plus code/heven_heads_verify.py (independent pow/isprime certification of all 12 heads). |
| `heven_heads_verify.py` | Independent certification of the 12 heads found by code/heven_gauss.py: for each (p, r) verifies r prime (isprime), r |
| `heven_patterns.py` | _(undescribed)_ |
| `heven_sieve.py` | Phase B2: threaded witness sieve for H_even ∩ [2,1200]. Scans odd primes by gmpy2.next_prime over disjoint worker ranges to bound (1e8 or 1e9), skips primes with pow(2,2400,r)!=1, computes ord_r(2) for passers, archives (r,ord) to ord_sieve_table.tsv and every (r,m,ord) with r |
| `pattern_extract.py` | _(undescribed)_ |
| `structural_search_CLOSED.py` | _(undescribed)_ |
| `verify_257_literal.py` | _(undescribed)_ |
| `verify_biquadratic_supplement.py` | Verifies the Williams (1976) primary closed forms for the quartic residue symbol on primary Gaussian primes against the definitional evaluation alpha^((N-1)/4) mod pi: [i/pi]=i^{-(a-1)/2}, [1+i/pi]=i^{(a-b-1-b^2)/4}, [-1/pi]=(-1)^{(a-1)/2}, and the derived [2/pi]=i^{-b/2}. Upgrades qr-supplementary-2 from asserted to primary-backed for the second-moment-character-mod16 approach. |
