# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute.py` | Naive oracle for the Erdős ternary conjecture. `digit_free(m)` decides — by exact integer arithmetic, O(log_3 m) — whether the base-3 expansion of m avoids digit 2; `to_base3(m)` gives the digit string; `check_witnesses()` and `scan(n_max)` reproduce the statement's worked examples. Ground truth to validate the sieve and every claimed obstruction against. Verified: n=0 (1_3), n=2 (11_3), n=8 (100111_3) are digit-free; n=3 (22_3), 5 (1012_3), 6 (2101_3) contain a 2; scan of n in [0,20] finds exactly {0,2,8}. |
| `erdos/` | The Erdős ternary oracle package: `digit_free`, `sieve_count`, `finite_check` (see `erdos/INDEX.md`). |
