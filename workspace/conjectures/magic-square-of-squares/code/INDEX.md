# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `ap_sequence.py` | _(undescribed)_ |
| `ap_structure.py` | _(undescribed)_ |
| `ap_structure2.py` | _(undescribed)_ |
| `audit_seven_grids.py` | Task B entry-repeat audit: exact re-run of code/brute.py near_miss_scan(80,120) with reproduction asserts against oracle_output.txt (kept 4052328, distribution incl. 7:4, best k=9, best distinct k=5), then extracts and audits the four k=7 grids — nine entries, distinctness with repeats reported, all-8-line-sums magic check, isqrt recount, and mutual distinctness of the four grids. Output code/out/seven_square_grids_audit.txt. Correctness established: scan distribution byte-matches the recorded oracle output; cross-checked by code/extract_sevens.py (independent isqrt sieve, 0 distinct 7/6-square grids, consistent with best distinct k=5). |
| `bremner2_genus.sage` | _(undescribed)_ |
| `bremner2_genus.sage.py` | _(undescribed)_ |
| `bremner2_quartics.py` | _(undescribed)_ |
| `bremner2_reconstruct.py` | _(undescribed)_ |
| `bremner2_verify.py` | Independent verification of the coefficient forms of the three (13) quartics and a second genus route (degree-4 squarefree, non-zero discriminant => genus 1). Agrees with Sage. |
| `bremner_deg4_check.py` | _(undescribed)_ |
| `bremner_phi_anchor.py` | _(undescribed)_ |
| `brute.py` | Naive oracle for the 3x3 magic square of squares: is_magic_square_of_squares verifier (failure_of diagnosis), grid_from_params, and a generator over the (c,u,v) parametrisation. Run against the statement's structural worked examples (parametrisation identity, centre-line AP structure, completeness) and small exhaustive scans (entries<=100, c=e^2 box). ALL TESTS PASSED, 6.9 s; exact output in code/out/oracle_output.txt. This is the ground truth every sieve/descent/structural lemma is measured against, and the pass criteria deliberately forbid treating repeated-entry grids (all-k^2, {1,25,49} family) as solutions. |
| `check_hilbert_splitness.py` | Verifies the refutation of the Hilbert-reciprocity/four-conics approach on Bremner's 7-square witness: that (c+d,c-d) with both c±d squares has Hilbert symbol 1 at all primes (so the quaternion algebra is trivially split), and that all four AP points lie on the conic X^2+Y^2=2c with rational point (e,e). STANDARD IDENTITY (A^2,B^2)_p=1 (bimultiplicativity) makes the refutation rigorous independent of the run; this script is a concrete residue-level check for a future executor. |
| `check_near_misses.py` | Oracle checker for the run: (1) verifier known-answer cases; (2) reruns the statement's structural worked examples fresh — parametrisation identity (585,640 grids), completeness (68,026 grids + Lo Shu), centre-line AP structure (65,025 grids); (3) constructs and verifies both 7-square near-misses (Sallows LS1: 7/8 sums 21609, non-principal diagonal 38307; Bremner magic square: all 8 sums 541875, 7 square entries, non-squares 360721, 222121) and writes code/out/near_misses.json with provenance; (4) exact Q-rank of the 8x9 incidence matrix (rank 7, kernel dim 2, affine magic space dim 3); (5) extracts (c,u,v)=(180625,-41496,138600), c=425^2=M/3, four differenced booleans [F,T,T,F]; (6) Pythagorean pairs (385,180)->v, (408,119)->u+v. Exit 0 only if everything passes; exact integer/Fraction arithmetic only. |
| `checker_selftest.py` | Task C checker-soundness self-test of is_magic_square_of_squares (lib/mss.py): exhibits the relaxed True branch on genuine magic squares of squares with repeated entries ({1,25,49} family, constants 75; nine 1s), a negative all-squares-repeated NON-magic control, and the rejection branches (Lo Shu, Sallows LS1 near-miss, Bremner 7-square). Output code/out/checker_selftest_output.txt. Correctness: every case as expected, exit 0; the magic family grids independently verified by sympy (all 8 sums 75). |
| `compute_sequences.py` | _(undescribed)_ |
| `extract_all_highk.py` | _(undescribed)_ |
| `extract_sevens.py` | _(undescribed)_ |
| `frac_phi_search.py` | _(undescribed)_ |
| `oeis_verify.py` | _(undescribed)_ |
| `pattern_seq.py` | _(undescribed)_ |
| `pattern_verify.py` | _(undescribed)_ |
| `phi_exact_search.py` | _(undescribed)_ |
| `phi_extend.py` | _(undescribed)_ |
| `scholar_parity_check.py` | Drop: a parity/3c-must-be-square-style argument (that a full MSS centre line X = 3c must have c/3 a square) is checked against the two near-misses and shown dead — 3·147² and 3·425² both have v2 = 1 and neither centre line is a full square AP; the 2E(Q) reduction needs B² = 3e² with B irrational. Kept as an explicit probe of a dead argument. |
