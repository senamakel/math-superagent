# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `bound_tightness.py` | Pattern work: checks whether 123/59 (largest m) is a per-product box bound or is set by the overall subset-sum. Result: per-product alone permits 596 reduced m>123/59, so the answer is bound by the OVERALL condition, not per-product boxes. |
| `brute.py` | Naive brute-force oracle for PE236. Base set of achievable reduced m from the smallest (s,t)-pair product, then tests every m>1 against all six exact equalities via per-product minimal pair (c_i,d_i), bound K_i, and subset-sum on the overall constraint. Reproduces the statement's oracle: count 35 and smallest 1476/1475. |
| `brute_m.py` | _(undescribed)_ |
| `extra_prime_analysis.py` | _(undescribed)_ |
| `factor_analysis.py` | _(undescribed)_ |
| `m_minus_1_analysis.py` | _(undescribed)_ |
| `solution.py` | _(undescribed)_ |
| `structure_analysis.py` | _(undescribed)_ |
| `theory_check.py` | Verifies per-product gcd-threshold theorem (existence of k_i) and bounded-k_i subset-sum overall feasibility against the oracle m values. |
| `verify_largest.py` | _(undescribed)_ |
| `verify_oracle.py` | Independent verification of the brute.py oracle: (A) reconstructs an explicit spoilage witness for each of the 35 reported m via subset-sum backtracking and literally checks all six equalities with Fraction arithmetic; (B) recomputes the valid-m count from a different base product (product 0) and compares sets; (C) re-checks smallest/largest. |
