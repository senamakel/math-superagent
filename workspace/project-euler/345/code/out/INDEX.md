# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute_output.txt` | Capture from code/brute.py: n=5 example reproduces Matrix Sum 3315, permutation (4,1,2,3,0), matched statement. The brute-force oracle check. |
| `example5.txt` | PE345 statement's 5x5 worked-example matrix, the test oracle that brute.py and solution.py both reproduce (sum 3315). |
| `random8.txt` | A random 8x8 matrix used as one of the inputs for the brute-vs-Hungarian agreement checks in solution.py. |
| `solution_output.txt` | Output of code/solution.py — the reported result: 5x5 example = 3315 (matched), 15x15 Matrix Sum = 13938, and 300 random small-matrix agreement checks passed vs brute.py. Holds the 15x15 answer. |
