#!/usr/bin/env python3
"""Ad-hoc cross-check of the incidence-algebra dimensions for the 3x3 magic
square: rank over Q of the 8x9 line-incidence matrix, its kernel (all eight
line sums zero), the single Q-relation among the eight line-vectors, and the
rank of the 7x9 difference matrix whose kernel is the affine space of magic
assignments.  Exact integer/Fraction arithmetic; sympy rank/nullspace as the
second, independent route.  This is a scratch probe, superseded by the
corresponding section of code/check_near_misses.py."""
from fractions import Fraction
from sympy import Matrix

inc = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 0],
]

M = Matrix([[Fraction(x) for x in row] for row in inc])
print("rank (sympy):", M.rank())
print("nullspace (sympy), dim:", len(M.nullspace()))
for v in M.nullspace():
    print("  ", list(v))

T = M.T
print("nullspace of transpose (row relations), dim:", len(T.nullspace()))
for v in T.nullspace():
    print("  ", list(v))

# difference rows: line_i - line_1 for i = 2..8  -> kernel = equal-sums space
diff = Matrix([[Fraction(inc[i][j] - inc[0][j]) for j in range(9)]
               for i in range(1, 8)])
print("rank difference 7x9 (sympy):", diff.rank(),
      "-> affine magic space dim =", 9 - diff.rank())

# shuffle: does the row-relation involve only rows+cols, or diagonals too?
rel = [v for v in T.nullspace()][0]
print("relation coefficients (L1..L8):", [int(v) for v in rel])