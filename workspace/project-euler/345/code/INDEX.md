# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive oracle for PE345: computes Matrix Sum (max-weight perfect matching) by enumerating all n! column permutations. Verified: reproduces the statement's 5x5 example, returning 3315 = 863+383+343+959+767 with column permutation (4,1,2,3,0). Factorial method, oracle only (n=5). |
| `seq_extract.py` | _(undescribed)_ |
| `solution.py` | Solve "Matrix Sum" (max-weight perfect matching) with the Hungarian algorithm (scipy.optimize.linear_sum_assignment on negated costs, exact integer arithmetic, O(n^3)). Hard-codes the 15x15 matrix from the problem statement and the 5x5 example; verifies 5x5 = 3315 and reports the 15x15 Matrix Sum = 13938. Also checks agreement vs brute enumeration on 300 random small matrices. Established correct: 5x5 matches statement; random checks pass; the 15x15 result is independently confirmed by a separate O(n^3) Hungarian implementation and the brute oracle on small cases. |
