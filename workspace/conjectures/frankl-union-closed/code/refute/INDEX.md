# Index — code/refute

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `REFUTER_REPORT.md` | Refuter's report: which statement was attacked, the four-answer outcome (refuted for the clause, open for the inequality), why find_counterexample was not applicable, and the status of the other candidate. |
| `__init__.py` | Makes code/refute importable (empty). |
| `_n2.py` | _(undescribed)_ |
| `_run_all.py` | Driver that runs the verification/analysis scripts in this folder (documentation). |
| `_run_checks.py` | Driver for the n=1 coupling checks (documentation). |
| `_run_n2.py` | _(undescribed)_ |
| `collapse_recheck.py` | Independent float recheck of the collapsed Gamma_hat(1/2)=phi/2 value. |
| `coupling_half_finiteD_refute.py` | High-precision recomputation of Gamma_hat(1/2)=phi/2 and t_max≈0.38234, killing the "constant exactly 1/2" clause of G-coupling-half. |
| `coupling_half_finiteD_refuted.md` | Refutation of the "finite-D Yu optimization constant exactly 1/2" clause of open lemma G-coupling-half: exact algebra showing Gamma_hat(1/2)=phi/2<1 and t_max~0.38234, noting the primary coupling inequality stays open. |
| `coupling_half_n1_check.py` | Correct n=1 analysis of G-coupling-half: over all couplings of Bernoulli(p) the mean of AvB ranges over [p,2p], reaching 1/2 for p>=1/4, so the lemma holds for every p in (0,1/2) — documents that the deleted n=1 'refutation' was an arithmetic bug. |
| `coupling_half_n1_verify.py` | Table of h(p) vs max H(AvB) over couplings for n=1 Bernoulli; shows the flawed 'max H=h(2p)' reasoning that led to the deleted n=1 refutation. |
| `coupling_half_n2.py` | n=2 exhaustive check (numeric SLSQP) of sup over all couplings of H(AvB) vs H(mu) for uniform supports with max marginal<1/2. |
| `coupling_half_small.py` | Small-n coupling-half verification helper. |
| `coupling_half_verify.py` | Independent high-precision recomputation of Gamma_hat(1/2) and t_max of Yu's finite-D relaxation. |
| `two_set_strong_check.py` | Refuter check on the strong form of settled rung R-uc-with-two-set: whether a UC family containing a 2-set always has one of that 2-set's elements abundant, over all UC families n<=4 via the canonical oracle's exact enumeration. |
| `uc_with_three_set.p` | TPTP encoding of the R-uc-with-three-set rung as a bounded finite fragment; the prior find_counterexample 'refuted' verdict on it was an encoding bug, not a refutation (see REFUTER_REPORT.md). |
| `uc_with_three_set_fixed.p` | Corrected TPTP encoding of the R-uc-with-three-set bounded fragment: forces the six member slots pairwise-distinct as objects AND as sets, so the sat-finder cannot collapse them (the bug in uc_with_three_set.p). find_counterexample returns undecided, confirming no bounded (4-element, 6-member) counterexample and that the old 'refuted' was the collapse artifact. |
