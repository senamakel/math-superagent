# Working memory

## Problem

The "Matrix Sum" of an n x n matrix is the maximum possible sum of elements
such that no two chosen elements share a row or column — i.e. the maximum
weight of a perfect matching in K_{n,n} (this is Project Euler 345). Given a
5x5 worked example (Matrix Sum = 3315) and a 15x15 matrix, find the 15x15
Matrix Sum. Do not search online for the published answer.

## Established results

- 5x5 worked example: Matrix Sum = 3315 (chosen: 863, 383, 343, 959, 767 =
  columns 4,1,2,3,0). Confirmed by both brute enumeration (code/brute.py) and
  the Hungarian solver (code/solution.py).
- 15x15 Matrix Sum = 13938 (chosen columns per row 1..15:
  9,10,7,4,3,0,13,2,14,11,6,5,12,8,1; chosen elements 973,957,993,853,962,
  870,992,972,848,976,969,901,823,966,883). Confirmed by two independent
  routes: scipy linear_sum_assignment and a separately written O(n^3) Hungarian
  implementation, which returned identical matchings (sum 13938).
- brute.py (n! enumeration) and solution.py (Hungarian) agree on 300 random
  small matrices and on three 8x8 matrices.

## Failed approaches

- None for this problem; the assignment/Hungarian method solved it directly.

## Open questions

- None.
