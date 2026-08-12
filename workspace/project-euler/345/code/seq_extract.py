#!/usr/bin/env python3
"""Extract the one natural integer sequence hidden in PE345's 15x15 matrix:
the Matrix Sum of each leading principal submatrix of size k (k=1..15).

This is a pattern-extraction aid: it turns the single-instance problem into
a 15-term sequence (Matrix Sum as a function of matrix size k) and hands it
to analyze_sequence / find_linear_recurrence. Uses the same Hungarian solver
as solution.py so the terms are what the run actually computes.
"""
import numpy as np
from scipy.optimize import linear_sum_assignment

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


def hungarian_max(mat):
    n = len(mat)
    cost = [[-mat[r][c] for c in range(n)] for r in range(n)]
    rows, cols = linear_sum_assignment(np.array(cost, dtype=np.int64))
    col_of = [0] * n
    for r, c in zip(rows, cols):
        col_of[r] = int(c)
    return sum(mat[r][col_of[r]] for r in range(n))


if __name__ == "__main__":
    seq = []
    for k in range(1, 16):
        sub = [row[:k] for row in M15[:k]]
        seq.append(hungarian_max(sub))
    print("Matrix Sum of leading principal kxk submatrix, k=1..15:")
    print(seq)
    print("full 15x15 (k=15) =", seq[-1], "(should be 13938)")
    assert seq[-1] == 13938
    # also first differences
    print("first differences:", [seq[i+1]-seq[i] for i in range(len(seq)-1)])
