# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Working guidance for the code/ tree: package-tree conventions — one job per file, programs live here with their outputs in code/out/, shared imports in code/lib/, the naive program stays as oracle, exact arithmetic, no exponential time/space, never delete a program carrying a result. |
| `brute.py` | Naive brute-force oracle for Project Euler 185. Enumerates all 10^L digit strings and keeps those matching every (guess, c_i) constraint exactly. Verified: on the L=5 example it reports the unique string 39542 (checked against 100000 candidates). Deliberately does not run the 10^16-candidate L=16 instance. |
| `diag.py` | Diagnostic probe of the backtracking solver for PE 185: runs the L=5 instance to confirm the oracle (39542) and probes the L=16 instance's node count under a budget (500M), reporting solutions found and nodes visited. Used to judge whether the recursive solver is fast enough at full size before committing to it. |
| `diag16.py` | _(undescribed)_ |
| `diagL5.py` | Diagnostic probe confined to the L=5 PE 185 example: a standalone recursive backtracking solve (feasible-digit pruning) printing the solution and node count, giving the L=5 baseline. Head of the file has a half-written placeholder solver that is never run; only the bottom solve5() executes and is sound. Superseded for full runs by diag.py, which probes L=5 and L=16 together. |
| `out_solutionpy.txt` | Stray 0-byte capture from a redirected run of solution.py that wrote nothing (an empty shell redirect left in code/ rather than code/out/). Obsolete and carries no result; kept only for provenance. The real solution output is verified and printed by solution.py itself. |
| `solution.py` | Efficient recursive backtracking solver for PE 185 (constraint-satisfaction, most-constrained-variable heuristic with feasibility pruning). Reproduces L=5 oracle (39542) and reports the L=16 secret; the primary fast route. Cost scales with constraint structure, not 10^L. |
| `solution2.py` | Independent second route to PE185 via scipy.optimize.milp (branch-and-bound ILP). Builds binary vars x[p][d] (secret[p]==d), constraints sum_d x[p][d]==1 per position plus sum_p x[p][guess_i[p]]==c_i per guess, zero objective, all binary. L=5 reproduces 39542 (matches brute 100000-check and uniqueness by no-good cut); L=16 yields secret 4640261571849533 with all 22 counts verified and uniqueness confirmed (re-solve with a no-good cut infeasible). Runtime ~0.16 s for the solve. This is the independent verification of the backtracking solution.py. |
