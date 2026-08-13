# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive oracle for Gilbreath's conjecture: exact-integer generator of iterated absolute-difference rows A_0..A_D of the primes (literal definition A_{k+1}(i)= |
| `lemma54_iff_check.py` | Operator-computed check of Granville Lemma 5.4 on real primes (sieve 2e6, columns n=20..2499): iff v<=2*nu2+2 <=> success, suff g*<=2*nu2+2 => success, and the discarded delta=0 case (row-level any-zero-in-block). REPRODUCED in-container this session (EXIT_CODE=0, capture overwritten with identical numbers: tested 2480, all successful, 0/0 violations, 100% delta=0 rows). |
| `nu2_granville_check.py` | Operator-computed nu_2 measurement of the prime right diagonal (sieve 3e6, columns to n=3999): nu2/n in 0.420..0.520, nu2=2048 at n=3999, n^0.525=77.8, Lemma 5.4 hypothesis holds at all sampled n. REPRODUCED in-container this session (EXIT_CODE=0, capture overwritten with identical numbers). |
| `run_verify_nu2.py` | Placeholder wrapper ("catches nothing - placeholder removed"); does nothing. Retained for provenance. |
| `verify_granville_nu2_independent.py` | Independent in-container verifier (second route) for the operator-computed numbers in research/notes/granville-2607-04166-actually-read.md and research/notes/lemma54-discarded-case-is-universal.md. Uses lib.gilbreath rows_generator + prefix-max g* (different code paths than the two host scripts it checks), reproduces nu2 for n in {50..3999} (sieve 3e6) and the Lemma 5.4 iff/suff/discarded-case counts for n=20..2499 (sieve 2e6), and adds an entry-level count of zeros inside the gray block (50.0% of 3,095,143 block entries are 0 — the discarded delta=0 case dominates entrywise, not just per-row). Output: code/out/verify_granville_nu2_independent.captured.txt. Exact integers; O(N loglog N) sieve + O(M^2) triangle. |
| `verify_nu2_claim.py` | Operator-written independent re-verification of the granville-nu2-density-measured claim (different sieve/row-order). EXECUTED in-container this session (EXIT_CODE=0, capture code/out/verify_nu2_claim.captured.txt) — reproduces nu2_granville_check.py exactly: nu2/n in 0.420..0.520, nu2=2048 at n=3999, g*=72/2*nu2+2=4098, 0 hypothesis failures. |
