# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `solution2_run.log` | Captured stdout of the independent solution2.py (scipy MILP) run: confirms L=5 answer 39542 and reports the L=16 secret 4640261571849533 with all 22 counts verified and uniqueness confirmed via a no-good cut. This is the second, independent verification route for the backtracking solver. |
| `solution_run.log` | 0-byte output capture from a redirected full-size run of solution.py that is still in progress or wrote nothing yet. Empty at this snapshot; expected to hold the L=16 solver run's stdout (solution string, node count, runtime, verification) once the run completes. |
