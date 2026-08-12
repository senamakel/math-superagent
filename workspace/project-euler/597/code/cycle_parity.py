#!/usr/bin/env python3
"""Exact cycle-parity probability for PE597-related question 2/3.

Over all n! permutations, weight each cycle of size k by w(k)=(-1)^C(k,2).
Ask: probability that prod over cycles of w(size) equals +1 (even).

EGF machinery: the exponential generating function weighted by cycle weights is
    A(z) = exp( sum_{k>=1} w(k) z^k / k )
and  sum over all n-permutations of prod w = n! [z^n] A(z) =: S_n.
Hence the count of permutations whose cycle-product is +1 is (n! + S_n)/2 and the
probability is  (1/2) * (1 + A_n),  A_n = S_n / n! = [z^n] A(z).

We compute A(z) as an exact rational power series to degree N and report
exact rational + float for n in the requested set.
"""
import sys
from fractions import Fraction


def comb2(k):
    return k * (k - 1) // 2


def w(k):
    """(-1)^C(k,2): +1,-1,-1,+1,+1,-1,-1,+1,... period 4."""
    return 1 if comb2(k) % 2 == 0 else -1


def egf_A_coeffs(N):
    """Return [A_0..A_N] where A_n = [z^n] exp(sum_{k>=1} w(k) z^k/k)."""
    # B = sum_{k>=1} w(k) z^k / k  as rational coefficients in z
    B = [Fraction(0)] * (N + 1)
    for k in range(1, N + 1):
        B[k] = Fraction(w(k), k)
    # exp via: A' = A * B'  =>  n*A_n = sum_{i=1..n} i*B_i*A_{n-i}
    A = [Fraction(0)] * (N + 1)
    A[0] = Fraction(1)
    dB = [Fraction(0)] * (N + 1)
    for i in range(1, N + 1):
        dB[i] = i * B[i]
    for n in range(1, N + 1):
        s = Fraction(0)
        for i in range(1, n + 1):
            s += dB[i] * A[n - i]
        A[n] = s / n
    return A


def main():
    ns = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [2, 3, 4, 5, 6, 8, 13]
    N = max(ns)
    A = egf_A_coeffs(N)
    print("n   exact even-prob              float            (1/2)(1+A_n)")
    for n in ns:
        # even-prob = (1/2)(1 + A_n)
        p_even = Fraction(1, 2) * (1 + A[n])
        print(f"{n:2d}  {p_even.numerator}/{p_even.denominator}  {float(p_even):.10f}")


if __name__ == "__main__":
    main()
