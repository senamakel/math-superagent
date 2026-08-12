# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `bound_tightness.py` | Pattern work: checks whether 123/59 (largest m) is a per-product box bound or is set by the overall subset-sum. Result: per-product alone permits 596 reduced m>123/59, so the answer is bound by the OVERALL condition, not per-product boxes. |
| `brute.py` | Naive brute-force oracle for PE236. Base set of achievable reduced m from the smallest (s,t)-pair product, then tests every m>1 against all six exact equalities via per-product minimal pair (c_i,d_i), bound K_i, and subset-sum on the overall constraint. Reproduces the statement's oracle: count 35 and smallest 1476/1475. |
| `brute_m.py` | _(undescribed)_ |
| `extra_prime_analysis.py` | Pattern work: enumerates which of the 35 oracle m-values carry primes beyond the core {2,3,5} along with 41 (num)/59 (den), and confirms extremes (largest 123/59, gap to 2nd = 41/295). |
| `factor_analysis.py` | _(undescribed)_ |
| `m_minus_1_analysis.py` | Pattern work: factors m-1 for the smallest/largest oracle values; confirms top-six ordering and that 123/59 − 574/295 = 41/295. |
| `solution.py` | _(undescribed)_ |
| `structure_analysis.py` | Pattern work: verifies the 35 oracle values are distinct/sorted, denominator divisibility by 59 (34/35), prime support, and the structure-theorem decomposition (g_i,c_i,d_i,K_i,w_i) of the largest m=123/59. |
| `theory_check.py` | Verifies per-product gcd-threshold theorem (existence of k_i) and bounded-k_i subset-sum overall feasibility against the oracle m values. |
| `verify_largest.py` | _(undescribed)_ |
| `verify_oracle.py` | Independent verification of the brute.py oracle: (A) reconstructs an explicit spoilage witness for each of the 35 reported m via subset-sum backtracking and literally checks all six equalities with Fraction arithmetic; (B) recomputes the valid-m count from a different base product (product 0) and compares sets; (C) re-checks smallest/largest. |
