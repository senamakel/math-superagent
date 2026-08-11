#!/usr/bin/env python3
"""Board value V(n) from per-number game values G(k).

Model (sourced in research/: disjsum.md, surreal.md): each number whose binary
string has a 1-bits and b 0-bits is the surreal integer G = a - b
(= popcount(k) - zerocount(k)). The board is "k copies of k" for k=1..n, a
disjunctive sum, so its value is V(n) = sum_{k=1..n} k * G(k).

G(k) are integers, so V(n) is an integer; we print them as exact fractions as
the task requests, and also the integer form.

Method rests on the disjunctive-sum value-additivity fact (Conway; see
research/L1.0/disjsum.md). O(n) per call, O(1) space.

Run: python temperature.py
"""
from fractions import Fraction


def g_value(k: int) -> int:
    """Game value of a single copy of the number k: popcount - zerocount."""
    b = bin(k)[2:]               # binary string of k, no leading zeros
    pop = b.count('1')           # a = number of 1-bits
    zero = len(b) - pop          # b = number of 0-bits
    return pop - zero


def board_value(n: int) -> Fraction:
    """V(n) = sum_{k=1..n} k * G(k), exact (integer) as a Fraction."""
    return Fraction(sum(k * g_value(k) for k in range(1, n + 1)))


def main() -> None:
    gs = [g_value(k) for k in range(1, 41)]
    print("G(k) for k = 1..40 (game value of a single copy of k):")
    print("  ", gs)
    print()
    print("n : V(n) = sum k*G(k)  (as exact fraction)      (integer)")
    for n in range(1, 41):
        v = board_value(n)
        # it is an integer; show denominator to prove exactness
        assert v.denominator == 1
        print(f"{n:2d} : {v}   = {v.numerator}")


if __name__ == "__main__":
    main()
