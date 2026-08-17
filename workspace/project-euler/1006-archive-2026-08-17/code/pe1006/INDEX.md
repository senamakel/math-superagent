# Index — code/pe1006

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `analyze_pairs.py` | _(undescribed)_ |
| `cgeometry.py` | _(undescribed)_ |
| `cintervals_print.py` | _(undescribed)_ |
| `csteps.py` | _(undescribed)_ |
| `cstructure.py` | _(undescribed)_ |
| `debug_affine5.py` | _(undescribed)_ |
| `diag_fib_subseq.py` | _(undescribed)_ |
| `final_check_fib_subseq.py` | _(undescribed)_ |
| `order10.py` | _(undescribed)_ |
| `report_tasks.py` | Generates the consolidated printed report code/out/PE1006_report_tasks_ABC.txt. |
| `state_component_bm.py` | Independent Berlekamp–Massey cross-check over F_M per state component (P,S,N1,N0,P1,vR): BM on first half gives order ~ n/2=50, coefficients fail on first untrained term k=101; full-200 BM order = n/2=100 (degenerate ceiling). Confirms no low-order constant linear recurrence, agreeing with the Gaussian tester. Correctness: reuses lib/recurrences.berlekamp_massey and reproduces the n/2 degeneracy signature of the prior 150-term finding. |
| `state_recurrence_enriched.py` | Tests whether the extension-formula state [P,S,vR,vR^2,P1,N1,N0] (vR^2 carried explicitly) closes under a constant linear/affine map mod M, orders 1..6, using the Gaussian tester in state_recurrence_test. All configurations INCONSISTENT. Builds on the verified extension recurrence P(k+1)=100(P+vR^2)+20P1+N1; establishes the nonlinear-in-state barrier to a fixed linear matrix. |
| `state_recurrence_test.py` | Modular Gaussian-elimination tester deciding whether the PE1006 state vector evolves under a constant-coefficient linear/affine recurrence mod M=101001001, orders 1..6, any column subset, optional skip-window. Returns consistent/inconsistent per (cols, order, affine). Validated on a synthetic known constant-recurrence sequence (order 2, 3 cols): reported consistent with 0 verify-errors. Used to establish the negative result that no such recurrence fits the 5/6-dim state from psi_state_1_200.txt. |
| `task_a_modular.py` | Task A: factor M, ord_10(M), Pisano period. Establishes M prime, ord_10=50500500, pi=101001000. |
| `task_b_period.py` | Task B first pass: r(k) table, naive (vacuous) pure-period probe. |
| `task_b_rigorous.py` | Task B rigorous: genuine eventual-period search (>=40 aligned comps) -> none <150. |
| `task_c_ceilset.py` | Characterize the ceil (+1) column sets per k; tests mechanical threshold forms. |
| `task_c_fit.py` | Fit N(i;k) ceil-column set vs candidate mechanical forms (all fail). |
| `task_c_fit2.py` | Fit ramp form N=floor((k-i)a+const): FAILS (N nearly constant, not ramp); confirms two-value N. |
| `task_c_intervals.py` | Extract (start, length) circular-interval representation of each column. |
| `task_c_rigorous.py` | Task C: verify columns are circular intervals, N in {floor/floor+1((k+1)a)}, pair-var list. |
| `task_c_starts.py` | Probe column-start patterns (arithmetic rotation / two-increment walk). |
| `task_c_structure.py` | Task C: k=1..12 factor values, diffs, string transitions, raw N(i;k). |
| `task_c_validate_intervals.py` | VALIDATES circular-interval representation reconstructs Psi exactly (k=3,4,5,6,8,10,12,15) and that intervals[i]&intervals[l] = A(i,l). |
| `task_chain.py` | _(undescribed)_ |
| `task_christoffel_psi.py` | _(undescribed)_ |
| `task_cmatrix.py` | _(undescribed)_ |
| `task_conjugate_structure.py` | Verifies on structure.json (k=1..60 factor sets) that the k+1 length-k Fibonacci factors are {k rotations of one base word} ∪ {one singular factor} iff k is a Fibonacci index. Establishes claim PE1006-conjugate-singular-iff-fibonacci: holds exactly at Fibonacci k (2,3,5,8,13,21,34,55), fails at all other k<=60; the base is a Christoffel word with F_{m-2} ones. Correct because it reproduces the known Perrin–Restivo conjugates-plus-singular fact where it holds and refutes it elsewhere; validated against the brute-oracle Psi values in structure.json. |
| `task_extensions.py` | _(undescribed)_ |
| `task_fib_subseq.py` | _(undescribed)_ |
| `task_fib_subseq_exact.py` | _(undescribed)_ |
| `task_period_big.py` | _(undescribed)_ |
| `task_period_test.py` | _(undescribed)_ |
| `task_rightspecial.py` | _(undescribed)_ |
| `task_state_long.py` | _(undescribed)_ |
| `task_state_recurrence.py` | _(undescribed)_ |
