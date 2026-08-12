# Goal

Solve Project Euler 345.

**Problem restated.** Given an n×n matrix of non-negative integers, the
*Matrix Sum* is the maximum possible sum of selected elements such that no two
selected elements share the same row or the same column. Since there are n
rows and we must pick one element per row (each row can contribute at most one,
and to maximize we pick n elements, one per row) and all n columns get used,
this is exactly a **maximum-weight perfect matching in the bipartite graph**
whose left vertices are rows and right vertices are columns, with edge
(i,j) having weight A[i][j].

**Worked example / oracle.** The 5×5 example matrix:

```
7  53  183 439 863
497 383 563 79  973
287 63  343 169 583
627 343 773 959 943
767 473 103 699 303
```

Matrix Sum = **3315** = 863 + 383 + 343 + 959 + 767 (one per row/column).

**Task.** Compute the Matrix Sum of the given 15×15 matrix.

**Completion criteria.**
1. brute.py: a naive but obviously-correct program (enumerate all perfect
   matchings of the 5×5 case) reproducing 3315.
2. solution.py: exact Hungarian algorithm, agrees with brute on the 5×5 oracle
   and on small random cases brute can reach, then run on the 15×15 matrix.
3. Final answer verified by a second independent route.
