# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `brute_oracle.captured.txt` | _(undescribed)_ |
| `classify_test_10000.captured.txt` | _(undescribed)_ |
| `classify_test_10000_FIXED.captured.txt` | _(undescribed)_ |
| `classify_test_10000_STALE_FAIL.captured.txt` | _(undescribed)_ |
| `commands.log` | _(undescribed)_ |
| `equality_case_elimination.captured.txt` | _(undescribed)_ |
| `equality_case_reproduced.captured.txt` | _(undescribed)_ |
| `equality_case_verify.captured.txt` | _(undescribed)_ |
| `equality_case_verify_BUG.captured.txt` | Rejected first draft of the equality-case independent verifier: built the admissible-size list by truncating in prime-count order, missed 37 and 41 in favour of 121=11^2 and 361=19^2, so point 4's M(29)>=T(29) failed. Kept as the record of the bug; the corrected run is equality_case_verify.captured.txt (all four points PASS). Do not cite this file as a result. |
| `heven_complete_verify.captured.txt` | _(undescribed)_ |
| `heven_gauss_61.captured.txt` | Gaussian-factorization / quartic-character run for all odd primes p<=61: per-p divisor table of 2^{2p}+1 (71 rows), all checks C1–C7 PASS, 12 heads r≡1 mod 16 (non-3-Higgs witnesses), character distribution by p mod 8 × Aurifeuillean half. Produced by code/heven_gauss.py (EXIT_CODE=0), heads recertified by code/heven_heads_verify.py (ALL HEADS CERTIFIED 12/12). |
| `heven_heads_verify.captured.txt` | Independent pow/isprime certification of the 12 heads from heven_gauss_61.captured.txt: r prime, r | 2^{2p}+1, r≡1 mod 16, (r-1)≡0 mod 4p — ALL HEADS CERTIFIED 12/12 (EXIT_CODE=0). |
| `heven_patterns.captured.txt` | _(undescribed)_ |
| `higgs_a057447.captured.txt` | First execution of code/higgs/check_a057447.py: literal OEIS A057447 recursion reproduces all 58 DATA terms exactly; all five unitary-perfect witnesses pass sigma_star(n)==2n; EXAMPLE factorization of the fifth term reproduces it; every witness prime divisor is 3-Higgs. ALL CHECKS PASSED (EXIT_CODE=0). |
| `known_five_verified.captured.txt` | _(undescribed)_ |
| `ord_sieve_table.tsv` | _(undescribed)_ |
| `sieve_pass_1e8.captured.txt` | _(undescribed)_ |
| `sieve_test_1000.captured.txt` | _(undescribed)_ |
| `sieve_test_10000.captured.txt` | _(undescribed)_ |
| `sieve_timing_1e5.captured.txt` | _(undescribed)_ |
| `sieve_timing_1e6.captured.txt` | _(undescribed)_ |
| `verify_257_literal.captured.txt` | _(undescribed)_ |
| `wall1988_budget_lower_bound.captured.txt` | _(undescribed)_ |
| `witnesses_1200.tsv` | _(undescribed)_ |
