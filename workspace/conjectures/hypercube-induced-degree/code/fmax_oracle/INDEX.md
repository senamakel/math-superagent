# Index — code/fmax_oracle

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `f5_independent.py` | Independent second route to f(5): ortools CP-SAT decision reproduces scipy/HiGHS result f(5)=3 (d=1,2 infeasible, d=3 feasible) and extracts an explicit witness S of 17 vertices with profile {1:2,2:3,3:12}, D(S)=3, verified by the pure-python exact oracle (third route). Confirms f(5)=3 by an independent solver. |
| `fmax_driver.py` | Driver that computes f(1..4) by the exhaustive oracle (n=4 profile {0:1,2:8} on S=[0,1,2,5,6,11,12,13,14]), validates the ILP decision against the exhaustive oracle on all n=1..4 (ALL AGREE), then runs the n=5 decision d=1,2,3 via scipy.optimize.milp finding f(5)=3 (d=1,2 infeasible, d=3 feasible). Captured in code/out/fmax_driver.captured.txt. |
| `indep_second_route.py` | Independent second route to small f(n) sharing no code with lib.fmax. n=4: hand-written exhaustive over all C(16,9)=11440 subsets gives min max internal degree = 2 (profile {0:1,2:8}). n=5: ortools CP-SAT decision (different solver tech than scipy milp) — d=2 infeasible, d=3 feasible; extracts witness written to code/out/witness_n5_alt.txt, re-verified by a local hand-written degree counter ( |
