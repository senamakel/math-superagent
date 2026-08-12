# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `exact_p3_extra.json` | Output of code/exact_p3_extra.py: exact rational p(3,L) for the 16 extra integer L values (120,...,5000), plus ncells from the exact arrangement enumeration. Cross-validated two independent enumerators + MC; anchors reproduced exactly before these were computed. |
| `exact_p4_extra.json` | Output of code/exact_p4_extra.py: exact rational p(4,L) (fraction even) plus ncells (1202 each) for the 12 extra integer L values (480..5000), written incrementally by the n=4 arrangement solver. Companion to exact_p3_extra.json extending the exact p(n,L) reference data beyond the anchor range. |
| `exact_pn.json` | Output of code/arrangement_pn.py: exact rational p(n,L) values (and their floats, and the cell counts) for n=3 and n=4 across a range of integer L, including the anchor checks p(3,160)=56/135 and p(4,400)=0.5107843137. The exact reference values produced by the arrangement solver. |
| `exact_small_n_results.json` | Structured results of the exact-integration task: exact rational p(n,L) for n=2,3,4 at L in {160,400,1800}, cell counts (n=3:32, n=4:1202, L-independent), verification summary (independent arrangement_pn.py + MC at 2-10M), and p(5,1800) MC-only value. Produced by code/cell_exact.py via toolkits/arr_enum.py + arr_polytope.py. |
| `purelimit_probe_run.txt` | Output of code/purelimit_probe.py (200k trials): the n=2..30 table of p(n,inf) (pure race) and p(n,1800) (finite race) with binomial SEs, self-checks OK (n=2,3,4 pure = 1/2, 7/18, 19/36; p(3,1800), p(4,1800) vs exact), and the near-target delta at n=11..15. |
| `verification_run.txt` | Timestamped report of the worked-example verification run (2026-08-12): the five n=3,L=160 rows reproduced through brute.py + exact_race.py (edges, new order, parity); the row probabilities 4/15, 8/45, 1/3, 4/27, 2/27 derived exactly from the 32-cell n=3,L=160 arrangement (sum 1, even total 56/135); and the four exact p-values p(3,160)=56/135, p(3,1800)=2237/5742, p(4,400)=521/1020, p(4,1800)=166802/317985 from cell_exact.p_exact. ALL CHECKS PASS. Produced by code/verify_worked_examples.py. |
