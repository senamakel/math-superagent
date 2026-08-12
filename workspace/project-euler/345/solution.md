# Solution — Project Euler 345 (Matrix Sum)

## The governing theory

The Matrix Sum is the **maximum-weight perfect matching in the complete
bipartite graph K_{n,n}**: one part is the rows, the other the columns, and the
edge (i,j) has weight A[i][j]. We must pick n elements, exactly one per row,
with all n columns used, maximizing the sum. This is the classical
**assignment problem**.

The named algorithm that controls it is the **Hungarian algorithm
(Kuhn–Munkres)**, which solves the minimum-cost assignment in **O(n³) time /
O(n²) space** with exact arithmetic. To maximize the sum we minimize the sum of
the *negated* entries — minimizing Σ(−A[i][p(i)]) equals maximizing
Σ A[i][p(i)]; this is exact because the entries are integers and the algorithm
works on those costs directly.

Why the bound is not a problem: n = 15 is fixed. A brute-force search over all
15! ≈ 1.3×10¹² permutations is infeasible and is the *wrong* method. The
Hungarian algorithm's cost grows with n³, not with n!, and gives the exact
answer. This is the structural fact that makes the search space unnecessary to
visit: it is a polynomial-time bipartite matching algorithm, not an
enumeration.

## Worked example (oracle)

The 5×5 matrix in the statement has Matrix Sum **3315** =
863+383+343+959+767 (column permutation rows→columns: 4,1,2,3,0). Both brute
force (all 5! = 120 matchings) and the Hungarian algorithm reproduce 3315 —
this is the check that the definition was read correctly.

## Method

1. `brute.py`: enumerate all n! column permutations, take the max sum. Used
   only as the small-case oracle (n ≤ 8).
2. `solution.py`: `scipy.optimize.linear_sum_assignment` (a robust O(n³)
   Hungarian implementation) on the negated cost matrix, giving the exact
   maximum.

## Result

For the given 15×15 matrix, the Matrix Sum is **13938** with column assignment
rows→columns `[9, 10, 7, 4, 3, 0, 13, 2, 14, 11, 6, 5, 12, 8, 1]` and chosen
elements `[973, 957, 993, 853, 962, 870, 992, 972, 848, 976, 969, 901, 823,
966, 883]`, whose sum is 13938.

## Verification (second independent route)

- **scipy Hungarian** gave 13938.
- A **separately written O(n³) Hungarian implementation** (independent of
  scipy) gave the *identical* assignment and sum 13938 — two distinct
  implementations agree.
- **brute force** reproduces the worked example (3315) and agrees with the
  Hungarian on 300 random small matrices and three 8×8 matrices.
- The chosen 15 columns are all distinct, and the sum recomputed directly from
  the matrix is 13938.

Answer: **13938**.
