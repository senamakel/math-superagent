# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute.py` | Naive brute-force oracle for PE236. Base set of achievable reduced m from the smallest (s,t)-pair product, then tests every m>1 against all six exact equalities via per-product minimal pair (c_i,d_i), bound K_i, and subset-sum on the overall constraint. Reproduces the statement's oracle: count 35 and smallest 1476/1475. |
| `verify_oracle.py` | Independent verification of the brute.py oracle: (A) reconstructs an explicit spoilage witness for each of the 35 reported m via subset-sum backtracking and literally checks all six equalities with Fraction arithmetic; (B) recomputes the valid-m count from a different base product (product 0) and compares sets; (C) re-checks smallest/largest. |
