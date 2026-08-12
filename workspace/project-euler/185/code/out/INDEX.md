# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `solution2_run.log` | Captured stdout of the independent solution2.py (scipy MILP) run: confirms L=5 answer 39542 and reports the L=16 secret 4640261571849533 with all 22 counts verified and uniqueness confirmed via a no-good cut. This is the second, independent verification route for the backtracking solver. |
| `solution_run.log` | Output capture of a redirected run of solution.py (backtracking). Holds the L=5 confirmation (39542, 437 nodes, oracle agreement) and the L=16 section header, but no L=16 result: the solve had not produced output when the run was stopped after a 550 s window. Not a result-bearing artifact for L=16; that result lives in solution2_run.log. |
