# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive oracle for Gilbreath's conjecture: exact-integer generator of iterated absolute-difference rows A_0..A_D of the primes (literal definition A_{k+1}(i)= |
| `lemma54_iff_check.py` | _(undescribed)_ |
| `nu2_granville_check.py` | _(undescribed)_ |
| `run_verify_nu2.py` | _(undescribed)_ |
| `verify_granville_nu2_independent.py` | Independent in-container verifier (second route) for the operator-computed numbers in research/notes/granville-2607-04166-actually-read.md and research/notes/lemma54-discarded-case-is-universal.md. Uses lib.gilbreath rows_generator + prefix-max g* (different code paths than the two host scripts it checks), reproduces nu2 for n in {50..3999} (sieve 3e6) and the Lemma 5.4 iff/suff/discarded-case counts for n=20..2499 (sieve 2e6), and adds an entry-level count of zeros inside the gray block (50.0% of 3,095,143 block entries are 0 — the discarded delta=0 case dominates entrywise, not just per-row). Output: code/out/verify_granville_nu2_independent.captured.txt. Exact integers; O(N loglog N) sieve + O(M^2) triangle. |
| `verify_nu2_claim.py` | Independent re-verification of the granville-nu2-density-measured claim (second route to the same numbers; written but not executed in this session — the on-disk nu2_granville_check.captured.txt is the executed evidence). |
