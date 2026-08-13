# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `ap_structure2_output.txt` | _(undescribed)_ |
| `bremner2_quartics.txt` | Deliverable: exact quartics (12) and (13), the (13,9,2) square check (root 12682 = 34*373 = bottom-right 373^2 entry of the 7-square witness), and genus computations (all three (13) quartics genus 1, two routes). |
| `candidate_verdict_math.py` | Verifies the two structural claims behind refuting the elimination-ideal and p-adic-valuation approaches: J=(0) over Qbar, and the Bremner witness q-values satisfy v2>=3, v3>=1 with no local contradiction. |
| `check_ferreira_proof.captured.txt` | _(undescribed)_ |
| `check_ferreira_proof.py` | Sympy verification that refutes Ferreira's claimed non-existence proof (arXiv:1506.06621): substituting z2 (a root of eqn 46) back into (46) gives the tautology 0=0, not the paper's (47); witness m=5,n=3,w=1 satisfies (46) but fails (47). Records the exact algebraic error. |
| `check_near_misses_latest.txt` | Fresh full stdout of `code/check_near_misses.py` (exit 0, ALL CHECKS PASSED): verifier cases, rerun worked examples, both near-misses, incidence rank, (c,u,v) extractions, Pythagorean pairs. |
| `checker_selftest_output.txt` | Task C deliverable: verbatim output of code/checker_selftest.py — checker-soundness self-test of is_magic_square_of_squares: relaxed True on genuine magic squares of squares with repeats ({1,25,49} family: all sums 75), rejection on the all-square-repeated non-magic control, Lo Shu, Sallows LS1 near-miss and Bremner 7-square; ALL CASES AS EXPECTED. |
| `ferreira_proof_refuted.md` | _(undescribed)_ |
| `k3_surface_check2.py` | Independent verification script for the Bremner II Category III six-square/K3 facts via lib/mss.py; superseded as primary evidence by reconciliation_2026-08-12.txt Task D (machine execution with exact construction + sympy). Kept as the independent second route; its brute-force point finder needs the parity-free (T±U) construction to avoid the [] parity artifact. |
| `k3_surface_check_note.md` | Claim note (id catIII-k3-has-q-point) recording the exact-arithmetic resolution that S(Q) is nonempty. Rewritten k3_surface_checks.py (exact) and independent k3_surface_check2.py agree on 64 S-points including P=(345,196,-304,255,-396,-25); the old float [] output is explained as a parity/half-integer artifact. Consequence: no Brauer-Manin obstruction can prove S(Q)=empty, closing the brauer-manin-k3-surface approach as formulated. |
| `k3_surface_checks.py` | _(undescribed)_ |
| `k3_surface_checks_exact.captured.txt` | _(undescribed)_ |
| `k3_surface_checks_output.txt` | _(undescribed)_ |
| `near_misses.json` | The run's witness set (GOAL.md contract): Sallows LS1 and Bremner's magic square, each with grid (printed orientation), square/non-square entries, the eight line sums, and provenance pointing at Bremner 1999 (local copy) / Sallows 1997. Written by code/check_near_misses.py. |
| `oracle_note.md` | Claim block for the oracle baseline: structural worked examples rerun fresh; the incidence-algebra results (rank 7 over Q, kernel dim 2, affine magic space dim 3, correcting the "dimension 4" misstatement); correction of the outdated "near-misses not yet reproduced" note; the (c,u,v) extraction table and the two realized Pythagorean relations; witness-set note directing every impossibility lemma at both near-misses (GOAL.md). |
| `oracle_output.txt` | _(undescribed)_ |
| `pattern_seq_output.txt` | _(undescribed)_ |
| `pell_record_seq.captured.txt` | _(undescribed)_ |
| `pell_record_seq.py` | Prints the record-denominator sequence P_{2k-1} (OEIS A001653), numerators, record f-decimals, and the growth ratio tending to 3+2sqrt2. |
| `pell_records_established.md` | _(undescribed)_ |
| `phi_2adic.captured.txt` | _(undescribed)_ |
| `phi_3adic_closure.captured.txt` | _(undescribed)_ |
| `phi_asymptotic_check.py` | _(undescribed)_ |
| `phi_asymptotic_findings.md` | _(undescribed)_ |
| `phi_canonical_check.py.captured.txt` | _(undescribed)_ |
| `phi_claim_blocks.md` | Claim blocks for the Φ/ |
| `phi_fibre_genus_check.py` | _(undescribed)_ |
| `phi_fibre_genus_check.py.captured.txt` | _(undescribed)_ |
| `phi_fibre_genus_run.py` | _(undescribed)_ |
| `phi_fibre_genus_run.py.captured.txt` | _(undescribed)_ |
| `phi_identity_verify.py.captured.txt` | _(undescribed)_ |
| `phi_mod3_check.captured.txt` | _(undescribed)_ |
| `phi_modular_obstruction.captured.txt` | _(undescribed)_ |
| `phi_padic_closure_all.captured.txt` | _(undescribed)_ |
| `phi_padic_closure_exact.captured.txt` | _(undescribed)_ |
| `phi_padic_valuation.captured.txt` | _(undescribed)_ |
| `phi_pattern_findings.md` | _(undescribed)_ |
| `phi_pell_record.md` | _(undescribed)_ |
| `phi_program_runs.txt` | Capture of fresh execution of the four never-run phi programs (phi_fibre_genus_run.py, verify_phi_doubling.py, phi_canonical_check.py, phi_identity_verify.py): commands, exit codes, full stdout, and per-program key conclusions. Fibre genus confirmed 0 (Faltings attack dead); two benign display artifacts; one program bug (phi_canonical_check orbit oracle, result independently confirmed); one genuinely false bound (phi_identity [5b]). |
| `phi_two_thirds_check.py` | Confirms |
| `prefilter_census_stages_M1000.jsonl` | _(undescribed)_ |
| `prefilter_census_stages_M200.jsonl` | _(undescribed)_ |
| `prefilter_census_stages_M500.jsonl` | _(undescribed)_ |
| `prefilter_census_stages_M700.jsonl` | _(undescribed)_ |
| `prove_pell_record.captured.txt` | _(undescribed)_ |
| `prove_pell_record.py` | _(undescribed)_ |
| `reconciliation_2026-08-12.txt` | _(undescribed)_ |
| `robertson_reduction_check.py` | Verifies the Robertson/Bremner elliptic reduction (E: y²=x(x²−c²), 2E-membership, doubling x-formula, AP of doubled x-coords) on Bremner's 7-square witness with exact integer arithmetic; confirms 2 of the 3 main-diagonal doubled x-coords lie in 2E (a near-miss, one short of an MSS). |
| `robertson_reduction_check.txt` | Full verbatim output (exit 0) of code/robertson_reduction_check.py: all 8 line sums 541875; reduction params a=425²=180625, b=41496 (main diag), c=138600 (anti-diag); exactly 2 of 3 main-diagonal x-coords (139129, 180625) pass the 2E(Q) test X, X−c, X+c all squares, 222121 fails (X and X+c=360721 not squares); doubling formula x(2Q)=(x²+c²)²/(4y²) verified symbolically, on a rational point, and against Sage 2P; rank of E: y²=x³−19209960000x is 2 (E.rank, algorithm='all', standalone mwrank — generators [−88200,315000], regulator 6.9103524178015, #E/2E=16, III[2]=1); 8 rational division preimages with quartics factoring completely exactly for X=139129, 180625 and having no rational root for X=222121; converse grid (4) = transpose of witness, all sums 3a, non-squares exactly {360721, 222121}. |
| `run_k3_checks.sh` | _(undescribed)_ |
| `scholar_verify.py` | Scholar verification of the witness grids and source-reported numeric claims by exact integer arithmetic, so notes carry only program-checked numbers. |
| `seven_square_grids_audit.txt` | _(undescribed)_ |
| `verify_a088959_records.py` | Cross-checks OEIS A088959 record-holder e (square with record # of sum-of-two-squares reps) against this run's own |
| `verify_pell_argmax_unique.captured.txt` | _(undescribed)_ |
| `verify_pell_argmax_unique.py` | _(undescribed)_ |
| `verify_pell_records.captured.txt` | _(undescribed)_ |
| `verify_pell_records.py` | _(undescribed)_ |
| `verify_pell_symbolic.captured.txt` | _(undescribed)_ |
| `verify_pell_symbolic.py` | Symbolic/exact verification of the Pell-record identity f(P_k,P_{k-1}) = 4P_k P_{k-1}(P_k^2−P_{k-1}^2)/(P_k^2+P_{k-1}^2)^2 = 1 − 1/P_{2k−1}² for the universal Φ-set: exact-reduced equality checks for k=2..39, sympy factor check of (a²+b²)²−4ab(b²−a²) = (a²+2ab−b²)², Pell-sign b²−2a²=±1 substitution, and the argmax-is-Pell probe. Ran 2026-08-16: exit 0, all PASS; independently cross-checked to k=200 (identity, convolution P_{2k−1}=P_k²+P_{k−1}², Pell sign n²+2mn−m²=±1, f<1, strictly increasing), see code/out/verify_pell_symbolic.captured.txt. Correctness anchor: the extracted exact fractions match the claim block phi-pell-record / note code/out/phi_pell_record.md. |
| `verify_phi_doubling.py` | _(undescribed)_ |
| `verify_phi_doubling.py.captured.txt` | _(undescribed)_ |
| `witness_padic_closure_claim.md` | _(undescribed)_ |
| `witness_padic_falsification.captured.txt` | Captured stdout of code/witness_padic_falsification.py: both near-misses verified with exact verifier (neither is a full MSS), every positive fully-realised Phi element from a witness satisfies the proved p-adic facts (v2>=3, v3>=1, res=0 mod 3); RESULT ALL CONSISTENT — no residue/closure argument forbids either witness. |
