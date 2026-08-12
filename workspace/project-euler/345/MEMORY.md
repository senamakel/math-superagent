# Working memory

## Problem

Matrix Sum of an n×n matrix = max sum of elements, one per row and one per
column. This is maximum-weight perfect matching in K_{n,n} (assignment
problem). Solve PE 345's 15×15 matrix.

## Established results

- 5×5 worked example → 3315 (verified by brute enumeration and Hungarian).
- 15×15 Matrix Sum = **13938**, from two independent Hungarian
  implementations (scipy.optimize.linear_sum_assignment and a hand-written
  O(n³) version) that returned the identical assignment.
- Chosen column permutation (rows→cols): [9,10,7,4,3,0,13,2,14,11,6,5,12,8,1];
  elements sum directly to 13938.
- Hungarian agrees with brute on 300 random small matrices.

## Failed approaches

None. Brute force at n=15 (15! matchings) is the wrong method and was not run
at full size; it is used only as the n≤8 oracle.

## Open questions

None — answer verified by two independent implementation routes.
