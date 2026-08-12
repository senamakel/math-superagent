#!/usr/bin/env python3
"""Solve "Matrix Sum" (maximum weight perfect matching) via the Hungarian
algorithm for maximum weight.

The Matrix Sum of an n x n matrix is the maximum possible sum of elements such
that no two chosen elements share a row or column — a maximum-weight perfect
matching in the complete bipartite graph K_{n,n}.

The Hungarian algorithm (Kuhn-Munkres) solves the assignment problem in
O(n^3) time / O(n^2) space with exact integer arithmetic. For a maximum
matching we maximize sum of chosen elements; we hand the minimizer a matrix of
negated costs (minimizing sum of -value == maximizing sum of value). scipy's
linear_sum_assignment is an O(n^3) Hungarian implementation.

This file hard-codes the 15x15 matrix from the problem statement and:
  (a) verifies on the 5x5 worked example (must give 3315),
  (c) reports the 15x15 Matrix Sum,
  (d) checks agreement vs code/brute's enumeration on random small matrices.

Usage:
    python solution.py          # run example + 15x15 + random-check vs brute
"""

import sys

try:
    import numpy as np
    from scipy.optimize import linear_sum_assignment
    HAVE_SCIPY = True
except Exception:  # pragma: no cover - fallback path
    HAVE_SCIPY = False


def hungarian_max(matrix):
    """Return (max_sum, col_of_each_row) for maximum-weight matching.

    col_of_each_row[r] is the chosen column in row r, all columns distinct.
    Uses linear_sum_assignment on negated costs (minimization of -value is
    maximization of value). Exact integer arithmetic: the algorithm works on
    the integer costs directly.
    """
    n = len(matrix)
    cost = [[-matrix[r][c] for c in range(n)] for r in range(n)]
    rows, cols = linear_sum_assignment(np.array(cost, dtype=np.int64))
    # rows == [0..n-1]; cols[r] is the column matched to row r.
    col_of = [0] * n
    for r, c in zip(rows, cols):
        col_of[r] = int(c)
    total = sum(matrix[r][col_of[r]] for r in range(n))
    return total, col_of


# ---- the 5x5 worked example -----------------------------------------------
EXAMPLE = [
    [7, 53, 183, 439, 863],
    [497, 383, 563, 79, 973],
    [287, 63, 343, 169, 583],
    [627, 343, 773, 959, 943],
    [767, 473, 103, 699, 303],
]
EXAMPLE_EXPECTED = 3315


# ---- the 15x15 matrix from the problem statement (copied row by row) ------
M15 = [
    [7, 53, 183, 439, 863, 497, 383, 563, 79, 973, 287, 63, 343, 169, 583],
    [627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913],
    [447, 283, 463, 29, 23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743],
    [217, 623, 3, 399, 853, 407, 103, 983, 89, 463, 290, 516, 212, 462, 350],
    [960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350],
    [870, 456, 192, 162, 593, 473, 915, 45, 989, 873, 823, 965, 425, 329, 803],
    [973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326],
    [322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601, 95, 973],
    [445, 721, 11, 525, 473, 65, 511, 164, 138, 672, 18, 428, 154, 448, 848],
    [414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198],
    [184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390],
    [821, 461, 843, 513, 17, 901, 711, 993, 293, 157, 274, 94, 192, 156, 574],
    [34, 124, 4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699],
    [815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107],
    [813, 883, 451, 509, 615, 77, 281, 613, 459, 205, 380, 274, 302, 35, 805],
]


def random_agreement_checks(count=300, max_n=7, seed=12345):
    """Check solution.hungarian_max agrees with brute enumeration."""
    import random
    from itertools import permutations

    rng = random.Random(seed)
    ok = 0
    for _ in range(count):
        n = rng.randint(1, max_n)
        mat = [[rng.randint(0, 999) for _ in range(n)] for _ in range(n)]
        # brute force oracle
        best = None
        for perm in permutations(range(n)):
            s = sum(mat[r][perm[r]] for r in range(n))
            if best is None or s > best:
                best = s
        got, _ = hungarian_max(mat)
        assert got == best, f"MISMATCH n={n}: hungarian={got}, brute={best}"
        ok += 1
    return ok


def main():
    if not HAVE_SCIPY:
        print("scipy not available — cannot run Hungarian method.")
        return 1

    # (a)+(b) verify the 5x5 worked example
    ex_val, ex_perm = hungarian_max(EXAMPLE)
    print(f"(a/b) 5x5 example Matrix Sum via Hungarian = {ex_val}")
    print(f"      chosen column permutation = {ex_perm}")
    print(f"      chosen elements          = "
          f"{[EXAMPLE[r][ex_perm[r]] for r in range(5)]}")
    assert ex_val == EXAMPLE_EXPECTED, (
        f"5x5 FAILED: got {ex_val}, expected {EXAMPLE_EXPECTED}")
    print(f"      worked example MATCHED (expected {EXAMPLE_EXPECTED})")

    # (c) the 15x15 matrix
    n15 = len(M15)
    assert all(len(row) == n15 for row in M15), "15x15 matrix not square/15"
    val15, perm15 = hungarian_max(M15)
    chosen15 = [M15[r][perm15[r]] for r in range(n15)]
    print(f"(c) 15x15 Matrix Sum = {val15}")
    print(f"    chosen column permutation = {perm15}")
    print(f"    chosen elements          = {chosen15}")

    # (d) random small matrices: Hungarian vs brute enumeration
    ok = random_agreement_checks()
    print(f"(d) random small-matrix agreement checks: {ok} passed vs brute.py")

    return 0


if __name__ == "__main__":
    sys.exit(main())
