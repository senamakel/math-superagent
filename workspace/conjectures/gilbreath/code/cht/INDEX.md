# Index — code/cht

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `check_cht_hypotheses.py` | CHT 2026 Theorem 1.6 hypothesis check against the real prime rows: computes M = ceil(log2 max a_n), L = longest 0-run, longest {0,d}-block over all d>=1, R_0 = 100·L·8^M on the normalized gaps a_n=(p_{n+2}−p_{n+1})/2−1 (sieve 2e7, 1,270,607 primes); verdict holds-here: no since R_0=419,430,400 ≫ reachable depth 1000. Correctness: first nine a_n match OEIS A100820 (asserted), M/L/R_0 cross-checked against the earlier cht_hyp_check run, longest-{0,d} verified by a second pure-Python scan. Writes code/out/cht_hypotheses.md with a fenced claim block (id cht-inverse-theorem, status: checked). |
