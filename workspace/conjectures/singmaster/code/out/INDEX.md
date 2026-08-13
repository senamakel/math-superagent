# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `brute.captured.txt` | Brute-force oracle on the 7 witnesses: direct enumeration gives identical counts and occurrence sets (3003->8, rest->6), second independent route. |
| `brute_oracle.md` | _(undescribed)_ |
| `check_mason_stothers_bound.py` | _(undescribed)_ |
| `check_witnesses_vs_mrstt.captured.txt` | Full output of code/check_witnesses_vs_mrstt.py, EXIT_CODE=0: all 15 nontrivial witness occurrences classified BOUNDARY (MRSTT-OPEN) under the n-form threshold exp((log n)^(2/3+0.1)) — 0 of 15 interior; a-form bound B(a)=(log a)/(log_2 a)^1.4 reported with the asymptotic caveat; strengthening: 0 of 44 pairs (mirrors and trivial included) in the symmetric interior. |
| `commands.log` | _(undescribed)_ |
| `count_multiplicity.captured.txt` | Oracle run: 3003 verified 8 times; a<=10^7 scan reports exactly 7 values with N>=6 (3003:8; 120,210,1540,7140,11628,24310:6); every value cross-checked against the inversion multiplicity. |
| `diag_families.captured.txt` | _(undescribed)_ |
| `exitcode_sweep.captured.txt` | _(undescribed)_ |
| `famA2.captured.txt` | _(undescribed)_ |
| `famB.captured.txt` | _(undescribed)_ |
| `famC.captured.txt` | _(undescribed)_ |
| `famD.captured.txt` | _(undescribed)_ |
| `fam_seqs.captured.txt` | _(undescribed)_ |
| `family_pairs.json` | All collisions (values with >=2 canonical reps) for n<=1000, value<=1e18, plus the N>=6 values, exact. |
| `family_seq_err.txt` | _(undescribed)_ |
| `family_seq_raw.txt` | _(undescribed)_ |
| `family_sequences.captured.txt` | _(undescribed)_ |
| `genus_closed_forms.md` | _(undescribed)_ |
| `genus_falsify.captured.txt` | _(undescribed)_ |
| `genus_integrality_proved.captured.txt` | Operator-computed integrality verification — 1,121,253 pairs, four parity classes, all integral. Needs this run's independent verification before claiming established. |
| `genus_out_of_sample_verified.md` | Claim note recording the out-of-sample Singular falsification of the genus closed form (17/17 pairs, 0 mismatches); anchors claim genus-closed-form-out-of-sample-verified. |
| `genus_single_closed_form.md` | _(undescribed)_ |
| `genus_spotcheck_new_pairs.captured.txt` | _(undescribed)_ |
| `genus_symmetric_form.captured.txt` | _(undescribed)_ |
| `genus_symmetric_form.md` | _(undescribed)_ |
| `genus_table.captured.txt` | The deliverable: exact genus table for C(x,k1)=C(y,k2), the Faltings threshold (genus>=2 except {2,3},{2,4}), verified closed forms for the {2,n},{3,n},{4,n} families, and literature cross-checks. |
| `job3_exitcode_sweep.py` | Job-3 read-only sweep: last line and EXIT_CODE status of every capture in code/out/*.captured.txt; writes code/out/exitcode_sweep.captured.txt listing per-capture last lines, the 9 captures with EXIT_CODE, and the 22 without. Linear in capture size. |
| `mrstt_leaves_witnesses_open.md` | _(undescribed)_ |
| `pattern_extend_6_8.captured.txt` | _(undescribed)_ |
| `pattern_extend_7_10.captured.txt` | _(undescribed)_ |
| `pattern_extend_k2_6.captured.txt` | _(undescribed)_ |
| `pattern_fam_seqs.captured.txt` | _(undescribed)_ |
| `pattern_genus_residual.captured.txt` | _(undescribed)_ |
| `pattern_print_family.captured.txt` | _(undescribed)_ |
| `pattern_sage_check_k2_6.captured.txt` | _(undescribed)_ |
| `pattern_slope.captured.txt` | _(undescribed)_ |
| `pattern_verify_genus_formula.captured.txt` | _(undescribed)_ |
| `print_family.captured.txt` | _(undescribed)_ |
| `rep_pairs.captured.txt` | _(undescribed)_ |
| `test_slope_across_rows.captured.txt` | _(undescribed)_ |
| `test_slope_hypothesis.captured.txt` | _(undescribed)_ |
| `verify_family.captured.txt` | Equal-pair finder n<=1000: reproduces all 7 witnesses; Pell family C(n+1,k+1)=C(n,k+2) members j=1..4 (the infinite N>=6 family, Singmaster 1975). |
| `verify_genus_formula.captured.txt` | _(undescribed)_ |
| `verify_k2_5_row.captured.txt` | _(undescribed)_ |
| `verify_lane_clark_bound.captured.txt` | _(undescribed)_ |
| `verify_lane_clark_bound.newcaptured.txt` | Fresh operator re-run of code/lane_clark/verify_lane_clark_bound.py, EXIT_CODE=0: every witness in witnesses.json satisfies N(a) < 2log2(a)+2 (3003: N=8 < 25.104) and brute force over 2<=a<=60 passes. This capture is the sole evidence for claim lane-clark-normal-array-bound = checked; the earlier .captured.txt was deliberately not adopted. |
| `verify_lane_clark_bound.purpose.md` | Points to the live Lane Clark verification program in code/lane_clark/ and the claim it checks. |
| `verify_lane_clark_bound.py` | _(undescribed)_ |
| `verify_library_claims.py` | _(undescribed)_ |
| `verify_mrstt_witnesses.captured.txt` | Captured output of code/verify_mrstt_witnesses.py (final run, EXIT_CODE=0): 3003's four witness pairs all equal 3003 with exactly 8 pairs in the triangle (mirrors included); all six N=6 witnesses + 3003 (N=8) reproduced by direct enumeration; Fibonacci family holds j=1..12; k<=log2(a)=39 candidates per a up to 10^12 (~1560 comb evaluations). |
| `verify_superelliptic_formula.captured.txt` | _(undescribed)_ |
| `witnesses.json` | Repro of the witness list: 3003:8 and the six 6-fold values with nontrivial canonical reps; conventions and scan bounds recorded. |
