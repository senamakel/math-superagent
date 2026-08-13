# Verdict facts for circle-method-n3-threshold candidate.
# Rome-Yamagishi arXiv:2406.09364: the circle-method sufficiency condition is
#   min_sigma T_sigma >= min{2d, d(d+1)} + 1   (d=2: need >= 5)
# where T_sigma is the max number of PAIRWISE DISJOINT, each linearly-independent,
# sets of 2n+1 columns of the coefficient matrix M_sigma (7 columns when n=3).
# We compute, exactly, for n=3 (d=2):
#   (a) the rank of M0 (7x9),
#   (b) the maximum number T0 of disjoint 7-column subsets that are each of full
#       rank 7 (an upper bound is floor(9/7) = 1).

import itertools
import numpy as np

def coefficient_matrix(n):
    # variables ordered row-major: x_11,x_12,...,x_1n,x_21,...,x_nn
    # equations: n row sums, (n-1) column sums, 2 diagonal sums  -> 2n+1 rows
    rows = []
    # n row sums
    for i in range(n):
        r = [0]*(n*n)
        for j in range(n):
            r[i*n+j] = 1
        rows.append(r)
    # n-1 column sums (omit last)
    for j in range(n-1):
        r = [0]*(n*n)
        for i in range(n):
            r[i*n+j] = 1
        rows.append(r)
    # two diagonal sums
    r = [0]*(n*n)
    for i in range(n):
        r[i*n+i] = 1
    rows.append(r)
    r = [0]*(n*n)
    for i in range(n):
        r[i*n+(n-1-i)] = 1
    rows.append(r)
    return np.array(rows, dtype=int)

for n in [3, 4, 8]:
    M = coefficient_matrix(n)
    R = 2*n+1
    N = n*n
    rank = np.linalg.matrix_rank(M)
    print(f"n={n}: M0 is {R}x{N}, rank={rank}")

# For n=3, count the maximum number of pairwise-disjoint 7-column subsets each of rank 7.
# Upper bound = floor(9/7) = 1, so T0 <= 1 < 5. Confirm at least whether one such 7-set exists.
n = 3
M = coefficient_matrix(n)
R = 2*n+1
cols = range(n*n)
best = 0
# greedy/brute: since bound is 1, check if any single 7-subset of columns has rank 7
found_one = False
for subset in itertools.combinations(cols, R):
    if np.linalg.matrix_rank(M[:, list(subset)]) == R:
        found_one = True
        break
print(f"n=3: exists a linearly-independent {R}-column set? {found_one}; "
      f"max disjoint such sets <= floor(9/{R}) = {9//R} (so T0 <= {9//R})")
print(f"n=3: circle-method sufficiency for d=2 requires min_sigma T_sigma >= 5; "
      f"T0 <= 1, so the criterion FAILS at n=3 (as Rome-Yamagishi state n=3 is excluded).")
