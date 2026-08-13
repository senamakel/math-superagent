# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `boundary_cut_tabulation.md` | Records the boundary-cut tabulation result: every known witness + Fibonacci family occurrence lies in the MRSTT-open boundary under eps=1/2; family stays boundary forever iff eps>=1/3 (else leaves into interior). Pins lower bound C>=3 for G-boundary-uniform-count. Evidence class: computed. |
| `brute.captured.txt` | Brute-force oracle on the 7 witnesses: direct enumeration gives identical counts and occurrence sets (3003->8, rest->6), second independent route. |
| `brute_oracle.md` | _(undescribed)_ |
| `check_eras_refutation.captured.txt` | _(undescribed)_ |
| `check_eras_refutation.py` | Verification computations for the grounding pass of three inventor approaches (Erdős–Selfridge structural, Bombieri–Pila determinant, hypergeometric-WZ). Decisive exact facts it checks when run: (1) 8·9=72=2³·3² has no prime >2 to exponent 1, falsifying the exponent-1 premise of erdos-selfridge-structural; (2) the trivial root-count bound O((log a)²) beats the Bombieri–Pila a^{1/d} term; (3) 360360·720 = 2162160·120 = 259459200 with 360360=2³·3²·5·7·11·13 and 2162160=2⁴·3³·5·7·11·13, showing large primes 7,11,13 sit inside both 3003 blocks. |
| `check_mason_stothers_bound.captured.txt` | _(undescribed)_ |
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
| `fam_seqs.captured.txt` | Real capture of code/pattern/fam_seqs.py (Fibonacci/Pell infinite N>=6 family): i, n_i, k_i, u_i=5n+6, v_i=5k+9, and digit counts of C(n+1,k+1) for i=1..8, EXIT_CODE=0. This file is why pattern_fam_seqs.captured.txt was deleted: the stale placeholder claimed fam_seqs.py produced no output, contradicted by this capture (second independent run just now also EXIT_CODE=0, 285 bytes). |
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
| `ground_three_approaches.py` | _(undescribed)_ |
| `integrality_reproduced.captured.txt` | EXECUTED this run, EXIT_CODE=0: independent re-check of the genus-closed-form integrality lemma over 1 <= m,n <= 799 — 638401 pairs, ZERO odd values of N(m,n)=(m-1)(n-1)+1-gcd(m,n) in any of the four parity classes, and the two algebraic forms agree 159201/159201 on 1..399. Replaces the previous 2-byte placeholder; closes TASKS.md item 4 and independently re-verifies the operator-computed 1,121,253-pair check behind claim genus-closed-form-integrality (status: proved). |
| `job3_exitcode_sweep.py` | Job-3 read-only sweep: last line and EXIT_CODE status of every capture in code/out/*.captured.txt; writes code/out/exitcode_sweep.captured.txt listing per-capture last lines, the 9 captures with EXIT_CODE, and the 22 without. Linear in capture size. |
| `mrstt_leaves_witnesses_open.md` | _(undescribed)_ |
| `pattern_extend_6_8.captured.txt` | Singular genus re-extension of the m=6..8 rows (F(m,n) for m=6 n=19..24, m=7 n=16..21, m=8 n=17..24) confirming the closed form g(m,n)=((m-1)n-(m-2)-gcd(n,m))/2; restored by re-run. |
| `pattern_extend_7_10.captured.txt` | Singular genus extension of the m=7..10 rows (m=7 n=13..15, m=8 n=13..16, m=9 n=13..17, m=10 n=13..19) confirming the closed form; restored by re-run. |
| `pattern_extend_k2_6.captured.txt` | Singular re-run of code/genus/extend_k2_6.sing (m=6, n=13..18: 30,32,34,37,40,40) cross-checked against g(6,n)=(5n-4-gcd(n,6))/2; restored by re-run. |
| `pattern_genus_residual.captured.txt` | Table of R=2g-(m-1)n arranged by n mod m (the genus formula residual after removing the (m-1)n term), m=2..11; confirms residual = 2-(m-2)-gcd pattern. Restored. |
| `pattern_print_family.captured.txt` | Real capture of code/pattern/print_family.py: infinite N>=6 family i=1..12 with a_i given exactly for i=1..4 (3003, 6e28, 3.5e204, 4.6e1411). Restored verbatim. |
| `pattern_sage_check_k2_6.captured.txt` | Marker that the Sage check for the k2=6 row errored (NameError: PolynomialRing — sage absent); superseded by the Singular re-run in pattern_extend_k2_6. Restored. |
| `pattern_slope.captured.txt` | Test of the slope hypothesis: mean of first-diff of genus across n vs (m-1)/2 prediction, m=2..11. Restored verbatim. |
| `pattern_verify_genus_formula.captured.txt` | verify_genus_formula.py table: 91 points + 25 extensions, 0 mismatches against g(m,n)=((m-1)n-(m-2)-gcd(n,m))/2; per-row-extension predictions. Restored. |
| `print_family.captured.txt` | _(undescribed)_ |
| `rep_pairs.captured.txt` | _(undescribed)_ |
| `test_slope_across_rows.captured.txt` | _(undescribed)_ |
| `test_slope_hypothesis.captured.txt` | _(undescribed)_ |
| `verify_family.captured.txt` | Equal-pair finder n<=1000: reproduces all 7 witnesses; Pell family C(n+1,k+1)=C(n,k+2) members j=1..4 (the infinite N>=6 family, Singmaster 1975). |
| `verify_fibonacci_identity.captured.txt` | This run's capture of code/verify_fibonacci_identity.py, PYTHON_EXIT=0: Singmaster family identity C(n+1,m+1)=C(n,m+2) verified j=1..6 (a up to 66416 digits), six distinct occurrences each (N(a)>=6), exact N(a) via fast inversion for j=1..3: N(3003)=8, N=6 at 29 and 205 digits, the latter beyond the BBW 2017 10^60 verification bound; fast oracle == lib oracle on 10 values. |
| `verify_genus_formula.captured.txt` | _(undescribed)_ |
| `verify_k2_5_row.captured.txt` | _(undescribed)_ |
| `verify_lane_clark_bound.captured.txt` | _(undescribed)_ |
| `verify_lane_clark_bound.newcaptured.txt` | Fresh operator re-run of code/lane_clark/verify_lane_clark_bound.py, EXIT_CODE=0: every witness in witnesses.json satisfies N(a) < 2log2(a)+2 (3003: N=8 < 25.104) and brute force over 2<=a<=60 passes. This capture is the sole evidence for claim lane-clark-normal-array-bound = checked; the earlier .captured.txt was deliberately not adopted. |
| `verify_lane_clark_bound.purpose.md` | Points to the live Lane Clark verification program in code/lane_clark/ and the claim it checks. |
| `verify_lane_clark_bound.py` | _(undescribed)_ |
| `verify_library_claims.py` | _(undescribed)_ |
| `verify_mrstt_witnesses.captured.txt` | Captured output of code/verify_mrstt_witnesses.py (final run, EXIT_CODE=0): 3003's four witness pairs all equal 3003 with exactly 8 pairs in the triangle (mirrors included); all six N=6 witnesses + 3003 (N=8) reproduced by direct enumeration; Fibonacci family holds j=1..12; k<=log2(a)=39 candidates per a up to 10^12 (~1560 comb evaluations). |
| `verify_riemann_hurwitz.captured.txt` | _(undescribed)_ |
| `verify_riemann_hurwitz_full.captured.txt` | _(undescribed)_ |
| `verify_sdw_transformations.captured.txt` | _(undescribed)_ |
| `verify_sdw_transformations.py` | Exact symbolic verification that all eight Stroeker-de Weger 1999 Table 1 reductions C(n,k1)=C(m,k2) -> elliptic model (W23, Q24, W26, Q28, W34, C36, W46, Q48) are polynomial identities, and that the Table 3 Mordell-Weil basis points lie on their curves. Independent algebraic check of sdw-elliptic-logarithms-eight-pairs; NOT yet executed (needs coder: timeout 540 python3 code/out/verify_sdw_transformations.py |
| `verify_superelliptic_formula.captured.txt` | _(undescribed)_ |
| `witnesses.json` | Repro of the witness list: 3003:8 and the six 6-fold values with nontrivial canonical reps; conventions and scan bounds recorded. |
