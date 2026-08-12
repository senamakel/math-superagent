#!/usr/bin/env python3
"""Naive oracle for "Matrix Sum" (maximum weight perfect matching).

The Matrix Sum of an n x n matrix is the maximum possible sum of matrix
elements such that no two chosen elements share a row or column — i.e. the
maximum weight of a perfect matching in the complete bipartite graph K_{n,n}.

This brute.py is the obviously-correct slow method: it enumerates ALL n!
permutations of column indices (one chosen column per row, all distinct),
sums each, and takes the maximum. It is the oracle that the Hungarian-based
solution.py is checked against.

Usage:
    python brute.py            # run the hard-coded 5x5 worked example
    python brute.py "-" < file # read an n x n matrix from stdin
    python brute.py file       # read an n x n matrix from a file

It handles n up to ~8 (8! = 40320 permutations, fast). Beyond that the n!
enumeration blows up, which is exactly why the Hungarian method is needed.
"""

import sys
from itertools import permutations


def matrix_sum_brute(matrix):
    """Return (best_sum, best_perm) for the square matrix by enumeration.

    best_perm is the list perm where matrix[r][perm[r]] is the chosen element
    in row r, perm being a permutation of 0..n-1 (distinct columns).
    """
    n = len(matrix)
    best = None
    best_perm = None
    for perm in permutations(range(n)):
        s = sum(matrix[r][perm[r]] for r in range(n))
        if best is None or s > best:
            best = s
            best_perm = perm
    return best, best_perm


def read_matrix(stream):
    """Parse whitespace-separated integers from stream into an n x n matrix."""
    data = [int(tok) for tok in stream.read().split()]
    n = int(round(len(data) ** 0.5))
    if n * n != len(data):
        raise ValueError(
            f"Input has {len(data)} integers, which is not a perfect square."
        )
    return [data[i * n:(i + 1) * n] for i in range(n)]


# The 5x5 worked example from the problem statement; its Matrix Sum is 3315.
EXAMPLE = [
    [7, 53, 183, 439, 863],
    [497, 383, 563, 79, 973],
    [287, 63, 343, 169, 583],
    [627, 343, 773, 959, 943],
    [767, 473, 103, 699, 303],
]


def main(argv):
    if len(argv) > 1 and argv[1] != "-":
        with open(argv[1]) as f:
            matrix = read_matrix(f)
    elif len(argv) > 1 and argv[1] == "-":
        matrix = read_matrix(sys.stdin)
    else:
        matrix = EXAMPLE

    n = len(matrix)
    if n > 8:
        print(f"n = {n}: refused, n! = {n}! is too large for brute force.")
        return 1

    val, perm = matrix_sum_brute(matrix)
    chosen = [matrix[r][perm[r]] for r in range(n)]
    print(f"n = {n}")
    print(f"Matrix Sum = {val}")
    print(f"chosen column permutation = {perm}")
    print(f"chosen elements          = {chosen}")
    print(f"sum of chosen elements   = {sum(chosen)}")
    if matrix is EXAMPLE:
        print("expected from statement  = 3315")
        assert val == 3315, f"FAILED: got {val}, expected 3315"
        print("WORKED EXAMPLE MATCHED")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
