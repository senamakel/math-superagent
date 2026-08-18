# Index — code/refute

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `G2-slope-refutation.md` | Refutation of Open Lemma G2 as written: the stated slope a=F(n-1)/F(n) is wrong (produces non-Fibonacci words with the block 11 at k=3); correct slope is F(n-2)/F(n)=fib(n)/fib(n+2). By-hand counterexample checked against the problem's own length-3 factor set and corroborated by code/out/check_slope.captured.txt. |
| `REDUCTION_INDEXING_ATTACK.md` | _(undescribed)_ |
| `REDUCTION_INDEXING_RUN.md` | _(undescribed)_ |
| `_run_check.py` | _(undescribed)_ |
| `attack_adopted_diagonal_closure.py` | Re-runs the naive Psi examples and both smallest finite collision oracles against the adopted bivariate diagonal summary closure. |
| `attack_reduction_counterexample.py` | Bounded exact refuter for ueuclid 0-indexing, decimal exponents, and rational-slope stability; uses direct moments as oracle. |
| `bivariate_diagonal_closure.p` | Placeholder documenting that the fixed-degree closure thesis is not faithfully expressible in the finite first-order refutation format; no adjacent conjecture is encoded. |
| `bivariate_diagonal_oracle.py` | Naive bounded collision oracle attacking fixed-degree bivariate diagonal closure; finds smallest equal-summary words with different appended-boundary second moments. |
| `check_M_and_claim3.py` | _(undescribed)_ |
| `check_approximant_stability.py` | Small exact refuter for mechanical approximant stability and duplicate-orbit boundary cases; compares rational slopes against the existing mechanical oracle. |
| `check_d9_claim1.py` | _(undescribed)_ |
| `check_directive_claims.py` | _(undescribed)_ |
| `check_reduction_indexing.py` | Exact k<=20 refuter for mech_psi to ueuclid indexing, testing decimal/floor shifts and ue0 moment conventions against mechanical oracle. |
| `check_small_final_evaluator.py` | Bounded refuter of reduction indexing and the single-intercept final evaluator; compares brute, mech_psi, and ue0 at k=1,2,3. |
| `d9-claim1-k3.p` | _(undescribed)_ |
| `fib_block_state_counterexample.py` | Small exact oracle attacking fixed-dimensional Fibonacci-block summary closure by finding minimal boundary-state collisions. |
| `fibword_finite_count.p` | Small TPTP attack on the false finite-word strengthening that S4 has k+1 factors for every positive k. |
| `g2-slope-correct-k3.p` | TPTP encoding of claim G2 with the CORRECTED slope a=F(n-2)/F(n)=2/5 at k=3; sanity model showing the corrected slope matches the true factor set. |
| `g2-slope-fn-1-k3.p` | TPTP encoding of claim G2 with the STATED slope a=F(n-1)/F(n)=3/5 at k=3; expected `refuted` (mechanical words {011,101,110} do not equal the true factors {001,010,100,101}). |
| `g2_slope_check.py` | Independent exact check (Fractions) of the G2 slope claim at k=3,4,5 comparing arc-midpoint mechanical words for the stated slope F(n-1)/F(n) vs corrected F(n-2)/F(n) against the true factor set from S_n. |
| `g4-context-free.md` | Attack notes for the G4 thesis: context-free window-sum formulation, the O(1)-state rolling-recurrence analysis, and why the additive/single-intercept candidate families fail (recorded counterexamples). Verdict: thesis survives this attack. |
| `g4-thesis-attack-report.md` | Report of the G4 thesis attack: finds no counterexample to the claim that no fixed-dimensional O(log k) joint-intercept evaluator is available in this workspace. Thesis survives. The two adopted approaches are unimplemented. |
| `g4_joint_intercept.p` | TPTP refutation encoding of the smallest additive-summary collision relevant to the G4 joint-intercept aggregation claim. |
| `g4_single_intercept.p` | TPTP encoding of the single-intercept replacement claim. Too weak for finite-model search (floor arithmetic over Q not faithfully representable); undecided outcome. |
| `g4_verify_exact.py` | Refuter's own exact verification script for the G4 thesis attack. Computes the exact mechanical factor values, Psi(k), single-intercept comparison, and mod-100 cross-check from the workspace's own verified mech_psi module. |
| `reduction_boundary_harness.py` | Bounded decisive refutation harness: shows at k=1,2,3 that fixing ue0 z^0 indexing does not solve the missing k+1-intercept aggregation; compares the tempting single-intercept S2 against mech_psi. |
| `refuter-summary.md` | Refuter's summary of the run: refutes the checked claim `ueuclid-incontainer-fails-s1s2` (a 1-indexed vs 0-indexed quantity confusion — the module is sound on disk), and records the directive-9 Claim-1 spot-checks plus the note that the d9-claim1-k3.p counterexample is an encoding artifact. |
| `run_attack_adopted_diagonal_closure.py` | Workspace-root launcher for the adopted diagonal-closure attack. |
| `run_bivariate_diagonal_oracle.py` | Runner for the bounded bivariate diagonal closure collision oracle. |
| `run_fib_block_state_counterexample.py` | Runner for the fixed-dimensional Fibonacci-block boundary-state counterexample oracle. |
| `small_oracle_thesis_attack.py` | Small exact oracle for the G4 thesis attack. Reproduces both official anchors (F3, Psi(3), Psi(10) mod M), tests the additive summary collision and single-intercept replacement. exponential complexity, oracle_bound k <= 10. |
| `ueuclid-S1-index-refutation.md` | Refutation record of claim `ueuclid-incontainer-fails-s1s2`: shows the decisive (1,0,1,5,z=3) case under the module's 1-indexed convention gives S1=547/S2=2551 (correct), and the claim's 426/1578 are the 0-indexed ue0 quantity. |
