#!/usr/bin/env python3
"""Reproduce the powers-of-2 sparse-string fold weight and locate the drops.

The sparse-fold thread claims: powers-of-2 support string (density 0) has
wt(Phi_n h)/n ~ 2/3 along n = 2^k+1 but ~0 at every exact n = 2^k, so
liminf ratio = 0. Before trusting that, reproduce it and understand the
drop mechanism.

h[j] = 1 iff j is a power of two, else 0.  nu2(n) = #{d in [2,n-1]:
T(n,d)=1}, T(n,d) = XOR over bitwise submasks o of d of h[n-1-d+o].
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from lib.supply_fold import s_sos


def powers_of_two(n):
    h = [0] * n
    p = 1
    while p < n:
        h[p] = 1
        p <<= 1
    return h


def nu2(n, h):
    return s_sos(n, h)[1]


def report(N):
    print(f"{'n':>7} {'nu2':>7} {'nu2/n':>9}")
    for n in range(8, N + 1):
        h = powers_of_two(n)
        v = nu2(n, h)
        r = v / n
        mark = ""
        # power-of-two n?
        if n & (n - 1) == 0:
            mark = "  <-- exact 2^k" if r < 0.05 else "  <-- exact 2^k (high!)"
        else:
            for k in range(1, 20):
                if n == (1 << k) + 1:
                    mark = "  <-- 2^k+1"
        if r < 0.10 or mark:
            print(f"{n:7d} {v:7d} {r:9.4f}{mark}")


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 1024
    report(N)
