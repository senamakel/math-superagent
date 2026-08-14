# Index — code/pe1006

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `analyze_pairs.py` | _(undescribed)_ |
| `order10.py` | _(undescribed)_ |
| `report_tasks.py` | Generates the consolidated printed report code/out/PE1006_report_tasks_ABC.txt. |
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
| `task_cmatrix.py` | _(undescribed)_ |
| `task_conjugate_structure.py` | Verifies on structure.json (k=1..60 factor sets) that the k+1 length-k Fibonacci factors are {k rotations of one base word} ∪ {one singular factor} iff k is a Fibonacci index. Establishes claim PE1006-conjugate-singular-iff-fibonacci: holds exactly at Fibonacci k (2,3,5,8,13,21,34,55), fails at all other k<=60; the base is a Christoffel word with F_{m-2} ones. Correct because it reproduces the known Perrin–Restivo conjugates-plus-singular fact where it holds and refutes it elsewhere; validated against the brute-oracle Psi values in structure.json. |
| `task_extensions.py` | _(undescribed)_ |
| `task_period_big.py` | _(undescribed)_ |
| `task_period_test.py` | _(undescribed)_ |
| `task_rightspecial.py` | _(undescribed)_ |
| `task_state_long.py` | _(undescribed)_ |
| `task_state_recurrence.py` | _(undescribed)_ |
