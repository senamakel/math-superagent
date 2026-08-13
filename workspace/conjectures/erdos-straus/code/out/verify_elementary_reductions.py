#!/usr/bin/env python3
"""Exact verification of the elementary reductions for Erdos-Straus:
1. n even is trivial.
2. n = 4k+3 is covered -- but NOT by the naive x=n,y=(n+1)/2,z=n(n+1)/2
   (that solves 3/n, not 4/n -- confirmed a bug already flagged in
   research/approaches/oracle-findings.md). The corrected identity is
   n=4k+3, x=(n+1)/4, y=n(n+1)/4+1, z=y(y-1).
Uses exact fractions.Fraction arithmetic; no sympy available in this sandbox.
"""
from fractions import Fraction as F

def check_even(m_max=2000):
    bad = []
    for m in range(1, m_max + 1):
        n = 2 * m
        lhs = F(4, n)
        rhs = F(1, m) + F(1, 2 * m) + F(1, 2 * m)
        if lhs - rhs != 0:
            bad.append(n)
    return bad

def check_naive_3mod4(k_max=2000):
    """The identity as literally stated in the task brief: x=n, y=(n+1)/2, z=n(n+1)/2."""
    bad = []
    for k in range(k_max):
        n = 4 * k + 3
        x = n
        y = F(n + 1, 2)
        z = F(n * (n + 1), 2)
        lhs = F(4, n)
        rhs = F(1, x) + F(1, y) + F(1, z)
        if lhs - rhs != 0:
            bad.append((n, lhs - rhs))
    return bad

def check_corrected_3mod4(k_max=2000):
    """n=4k+3, x=(n+1)/4, y=n(n+1)/4+1, z=y(y-1)."""
    bad = []
    for k in range(k_max):
        n = 4 * k + 3
        x = F(n + 1, 4)
        y = F(n * (n + 1), 4) + 1
        z = y * (y - 1)
        assert x.denominator == 1 and y.denominator == 1 and z.denominator == 1
        assert x > 0 and y > 0 and z > 0
        lhs = F(4, n)
        rhs = F(1, x) + F(1, y) + F(1, z)
        if lhs - rhs != 0:
            bad.append((n, lhs - rhs))
    return bad

if __name__ == "__main__":
    bad_even = check_even(5000)
    print(f"n-even trivial identity: checked m=1..5000, failures={len(bad_even)}")
    assert not bad_even

    bad_naive = check_naive_3mod4(50)
    print(f"BRIEF'S naive n=3mod4 identity (x=n,y=(n+1)/2,z=n(n+1)/2): "
          f"checked k=0..49, failures={len(bad_naive)} -- "
          f"sample diffs: {bad_naive[:5]}")
    print("  -> This identity solves 3/n, NOT 4/n. It is WRONG as a covering "
          "identity for the conjecture. Confirms research/approaches/oracle-findings.md.")

    bad_corrected = check_corrected_3mod4(5000)
    print(f"CORRECTED n=3mod4 identity (n=4k+3,x=(n+1)/4,y=n(n+1)/4+1,z=y(y-1)): "
          f"checked k=0..4999, failures={len(bad_corrected)}")
    assert not bad_corrected
    print("All positive-integer and diff==0 checks passed for the corrected identity.")
