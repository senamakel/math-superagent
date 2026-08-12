#!/usr/bin/env python3
"""Naive oracle for Project Euler 345 (Matrix Sum).

The Matrix Sum of a square matrix is the maximum possible sum of matrix
elements such that no two chosen elements share a row or column — i.e. the
maximum weight of a perfect matching in the complete bipartite graph, found
here by enumerating every permutation of column indices (one chosen element
per row, distinct columns).

This is deliberately the obviously-correct slow method: enumerate all n!
permutations and take the max sum. It is only run on the small worked
example (n = 5), where n! = 120, to pin down what the statement means.
"""

from itertools import permutations


def matrix_sum_brute(matrix):
    """Return the Matrix Sum of a square matrix by full permutation search."""
    n = len(matrix)
    best = None
    best_perm = None
    for perm in permutations(range(n)):
        s = sum(matrix[r][perm[r]] for r in range(n))
        if best is None or s > best:
            best = s
            best_perm = perm
    return best, best_perm


# The worked example from the statement: the 5x5 matrix shown.
EXAMPLE = [
    [7, 53, 183, 439, 863],
    [497, 383, 563, 79, 973],
    [287, 63, 343, 169, 583],
    [627, 343, 773, 959, 943],
    [767, 473, 103, 699, 303],
]

if __name__ == "__main__":
    val, perm = matrix_sum_brute(EXAMPLE)
    chosen = [EXAMPLE[r][perm[r]] for r in range(5)]
    print("n =", len(EXAMPLE))
    print("Matrix Sum =", val)
    print("chosen column permutation =", perm)
    print("chosen elements          =", chosen)
    print("sum of chosen elements   =", sum(chosen))
    print("expected from statement  = 3315")
    assert val == 3315, f"FAILED: got {val}, expected 3315"
    print("WORKED EXAMPLE MATCHED")
