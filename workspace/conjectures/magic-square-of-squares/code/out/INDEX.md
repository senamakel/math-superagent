# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `ap_structure2_output.txt` | _(undescribed)_ |
| `bremner2_quartics.txt` | Deliverable: exact quartics (12) and (13), the (13,9,2) square check (root 12682 = 34*373 = bottom-right 373^2 entry of the 7-square witness), and genus computations (all three (13) quartics genus 1, two routes). |
| `check_near_misses_latest.txt` | Fresh full stdout of `code/check_near_misses.py` (exit 0, ALL CHECKS PASSED): verifier cases, rerun worked examples, both near-misses, incidence rank, (c,u,v) extractions, Pythagorean pairs. |
| `checker_selftest_output.txt` | Task C deliverable: verbatim output of code/checker_selftest.py — checker-soundness self-test of is_magic_square_of_squares: relaxed True on genuine magic squares of squares with repeats ({1,25,49} family: all sums 75), rejection on the all-square-repeated non-magic control, Lo Shu, Sallows LS1 near-miss and Bremner 7-square; ALL CASES AS EXPECTED. |
| `k3_surface_check2.py` | Independent verification script for the Bremner II Category III six-square/K3 facts via lib/mss.py; superseded as primary evidence by reconciliation_2026-08-12.txt Task D (machine execution with exact construction + sympy). Kept as the independent second route; its brute-force point finder needs the parity-free (T±U) construction to avoid the [] parity artifact. |
| `k3_surface_check_note.md` | _(undescribed)_ |
| `k3_surface_checks.py` | _(undescribed)_ |
| `k3_surface_checks_output.txt` | _(undescribed)_ |
| `near_misses.json` | The run's witness set (GOAL.md contract): Sallows LS1 and Bremner's magic square, each with grid (printed orientation), square/non-square entries, the eight line sums, and provenance pointing at Bremner 1999 (local copy) / Sallows 1997. Written by code/check_near_misses.py. |
| `oracle_note.md` | Claim block for the oracle baseline: structural worked examples rerun fresh; the incidence-algebra results (rank 7 over Q, kernel dim 2, affine magic space dim 3, correcting the "dimension 4" misstatement); correction of the outdated "near-misses not yet reproduced" note; the (c,u,v) extraction table and the two realized Pythagorean relations; witness-set note directing every impossibility lemma at both near-misses (GOAL.md). |
| `oracle_output.txt` | _(undescribed)_ |
| `pattern_seq_output.txt` | _(undescribed)_ |
| `phi_claim_blocks.md` | Claim blocks for the Φ/ |
| `reconciliation_2026-08-12.txt` | _(undescribed)_ |
| `run_k3_checks.sh` | _(undescribed)_ |
| `scholar_verify.py` | Scholar verification of the witness grids and source-reported numeric claims by exact integer arithmetic, so notes carry only program-checked numbers. |
| `seven_square_grids_audit.txt` | _(undescribed)_ |
