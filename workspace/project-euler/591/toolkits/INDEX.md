# Index — toolkits

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

These are standalone verification/analysis scripts (not importable reusable helpers). Each builds on the Cabanillas (arXiv:1904.01874) candidate-set method and/or checks a relation against the brute-force oracle.

| File | Purpose |
| --- | --- |
| `analyze_Id_b.py` | Tests the exact-integer relation |I_d| = nint(b_d*sqrt(d) - pi) = nint(b_d*sqrt(d)) - 3 across all non-square d in [2,99] at n=10^4, re-scanning b when needed. Established the uniform I/b relation used to derive a from b. |
| `ostrowski_verify.py` | Small-scale brute-force check that the Cabanillas Prop 9/10 candidate set contains the argmin of ||n*alpha - beta|| over n in [0,L], for several alpha,beta and L. First validation of the candidate structure. |
| `print_record_sequences.py` | Prints the record-holding b sequence for d in {2,5,7} up to N=10^7 (exact distances via mpmath). Evidence for the structure of record b's. |
| `test_method_scale.py` | Full-method test at n=10^6 for d in {2,3,5,6,7,8,10,11,13,92,83,57}: compares brute-force argmin b to the Cabanillas-candidate argmin, and checks the |I|/a relations. Validated the method at moderate scale for a representative d subset. |
| `validate_all_d.py` | Independent cross-check for ALL non-square d<100 at n=10^6: brute-force argmin b vs Cabanillas-candidate argmin, zero mismatches (~47s). This is the uniform correctness check of the scalable method across every d we need. |
| `verify_cabanillas_exact.py` | Verifies Cabanillas Prop 9/10 exactly on record holders: every record-holder of ||n*alpha - beta|| over [0,N] is in the candidate set, and the global min value matches the candidate min, for d in {2,3,5,7,11}, N in {200,1000,5000}. |
| `verify_oracle_d2.py` | Cross-checks the PE591 d=2, n=10^13 oracle with exact/mpmath arithmetic: a + b*sqrt(2) - pi ~ -4.29e-15; confirms |a| = nint(...) relations; shows b=4375636191520 is NOT a sqrt(2) semiconvergent denominator. |
