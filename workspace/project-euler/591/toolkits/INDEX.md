# Index — toolkits

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `analyze_Id_b.py` | Tests the exact-integer relation abs(I_d) = nint(b_d*sqrt(d) - pi) = nint(b_d*sqrt(d)) - 3 across all non-square d in [2,99] at n=10^4, re-scanning b when needed. Established the uniform I/b relation used to derive a from b. |
| `check_divisibility_rule.py` | Verifies the m^2*d0 rule on results_full.txt (n=1e13): abs(I at m^2*d0) equals abs(I at d0) iff m divides b_{d0}; and when equal, b_{m^2*d0} = b_{d0}/m. |
| `check_scaling_symmetry.py` | Tests the scaling symmetry d1=m^2*d2 on results_full.txt: whether abs(I_d1) equals abs(I_d2) and b_d1 = m*b_d2; also checks distinct abs(I) counts and the S sum. |
| `compare_signs.py` | _(undescribed)_ |
| `final_check.py` | Final independent checks on results_full.txt: re-sums S from the file, verifies each row has b in [0,L], a = nint(pi-b*sqrt(d)) at high precision, checks the d=2 oracle row, and cross-checks against results_independent.txt if present. Targets the positive-b results_full.txt. |
| `ostrowski_verify.py` | Small-scale brute-force check that the Cabanillas Prop 9/10 candidate set contains the argmin of the distance of n*alpha-beta to nearest integer over n in [0,L], for several alpha,beta and L. First validation of the candidate structure. |
| `print_record_sequences.py` | Prints the record-holding b sequence for d in {2,5,7} up to N=10^7 (exact distances via mpmath). Evidence for the structure of record b's. |
| `recheck_laws_corrected.py` | Re-runs on the CORRECTED both-sign data (results_full_bothsides.txt): (1) checks |I| == |nint(b*sqrt(d)-pi)| for every d; (2) re-verifies the m^2*d scaling law (|I at m^2*d0| equals |I at d0| iff m divides b_{d0}) and that when equal b_{m^2*d0}=b_{d0}/m. Confirms the uniform I/b relation and divisibility law survive the both-sides correction. |
| `test_method_scale.py` | Full-method test at n=10^6 for d in {2,3,5,6,7,8,10,11,13,92,83,57}: compares brute-force argmin b to the Cabanillas-candidate argmin, and checks the abs(I) and a relations. The brute comparison here scans b in [0,L] (positive only). |
| `validate_all_d.py` | Independent cross-check for ALL non-square d less than 100 at n=10^6: brute-force argmin b (positive-only scan) vs Cabanillas-candidate argmin, zero mismatches (~47s). Uniform correctness check of the positive-b method across every d. |
| `validate_bothsides.py` | Validates the corrected both-sign solver solution_bothsides.py against brute force for ALL d at n=10^6, where the brute scan covers b in [-L,L] (both signs). Confirms where the both-sides result differs from the positive-only one. |
| `verify_cabanillas_exact.py` | Verifies Cabanillas Prop 9/10 exactly on record holders: every record-holder of the distance of n*alpha-beta to nearest integer over [0,N] is in the candidate set, and the global min value matches the candidate min, for d in {2,3,5,7,11}, N in {200,1000,5000}. |
| `verify_oracle_d2.py` | Cross-checks the PE591 d=2, n=10^13 oracle with exact/mpmath arithmetic: a + b*sqrt(2) - pi about -4.29e-15; confirms abs(a) and nearby-integer relations; shows b=4375636191520 is NOT a sqrt(2) semiconvergent denominator. |
20 is NOT a sqrt(2) semiconvergent denominator. |
