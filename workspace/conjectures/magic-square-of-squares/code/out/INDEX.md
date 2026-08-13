# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `ap_structure2_output.txt` | _(undescribed)_ |
| `bremner2_quartics.txt` | Deliverable: exact quartics (12) and (13), the (13,9,2) square check (root 12682 = 34*373 = bottom-right 373^2 entry of the 7-square witness), and genus computations (all three (13) quartics genus 1, two routes). |
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
| `pell_record_seq.py` | Prints the record-denominator sequence P_{2k-1} (OEIS A001653), numerators, record f-decimals, and the growth ratio tending to 3+2sqrt2. |
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
| `prove_pell_record.py` | _(undescribed)_ |
| `reconciliation_2026-08-12.txt` | _(undescribed)_ |
| `run_k3_checks.sh` | _(undescribed)_ |
| `scholar_verify.py` | Scholar verification of the witness grids and source-reported numeric claims by exact integer arithmetic, so notes carry only program-checked numbers. |
| `seven_square_grids_audit.txt` | _(undescribed)_ |
| `verify_pell_argmax_unique.py` | _(undescribed)_ |
| `verify_pell_records.py` | _(undescribed)_ |
| `verify_pell_symbolic.py` | _(undescribed)_ |
| `verify_phi_doubling.py` | _(undescribed)_ |
| `verify_phi_doubling.py.captured.txt` | _(undescribed)_ |
| `witness_padic_falsification.captured.txt` | Captured stdout of code/witness_padic_falsification.py: both near-misses verified with exact verifier (neither is a full MSS), every positive fully-realised Phi element from a witness satisfies the proved p-adic facts (v2>=3, v3>=1, res=0 mod 3); RESULT ALL CONSISTENT — no residue/closure argument forbids either witness. |
