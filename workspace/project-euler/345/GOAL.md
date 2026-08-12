# Goal

## Objective
Solve Project Euler problem 345: compute the "Matrix Sum" of a given 15x15
matrix.

## Definitions
- **Matrix Sum** of a matrix M: the maximum possible sum of matrix elements
  such that none of the selected elements share the same row or column.
- That is, choose exactly one element from each row and each column (a
  perfect matching in the complete bipartite graph on rows/columns),
  maximizing the sum of the chosen elements. Equivalent to a maximum-weight
  assignment problem and to finding a maximum weight perfect matching.
- For an n x n matrix, a selection is described by a permutation π of
  {0,...,n-1}: element M[r][π(r)] is chosen from row r.

## Worked example (test oracle)
Given 5x5 matrix:

```
7 53 183 439 863
497 383 563 79 973
287 63 343 169 583
627 343 773 959 943
767 473 103 699 303
```

The statement says its Matrix Sum = 3315 = 863 + 383 + 343 + 959 + 767.
These are elements (0,4), (1,1), (2,2), (3,3), (4,0) — one per row and column.

## Completion criteria
- code/brute.py (naive oracle) reproduces 3315 for the 5x5 example. DONE.
- code/solution.py (efficient, exact) agrees with brute.py on reachable
  cases and reproduces the example, then computes the 15x15 answer.
- Final answer verified by an independent route.
