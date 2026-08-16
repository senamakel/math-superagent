#!/usr/bin/env python3
"""Sparse-fold probe: does a FIXED sparse-but-growing h give linear fold weight?

The candidate for G-weak-input-strictness: h with 1s at all powers of two
(j = 1, 2, 4, 8, ...), switch density 0. Hand-analysis (cross-checked in the
note) shows nu2(2^m) = O(m) = O(log n), i.e. SUBLINEAR, NOT linear.

This script is the machine cross-check the run should run; the hand values to
reproduce are: nu2(8)=4, nu2(12)=4, nu2(16)=4 for the powers-of-two h.
"""
from lib.supply_fold import s_sos


def powers_of_two_h(N):
    h = [0] * N
    p = 1
    while p < N:
        h[p] = 1
        p <<= 1
    return h


def count_ones(x):
    return sum(x)


if __name__ == "__main__":
    print("n   ones(h)  nu2       nu2/n")
    for n in [8, 12, 16, 32, 64, 128, 256]:
        h = powers_of_two_h(n)
        S, nu2 = s_sos(n, h)
        print(f"{n:4d} {count_ones(h):7d} {nu2:7d} {nu2/n:8.3f}")
