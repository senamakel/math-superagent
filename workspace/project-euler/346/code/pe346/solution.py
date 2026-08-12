"""Solve PE346: sum of strong repunits below N.

A strong repunit = repunit in >=2 bases. Every n>1 is "11" in base n-1, so a
number >1 is strong iff it is a repunit of length >=3 in some base b>1. Plus 1.

Enumerate distinct values (b^k-1)/(b-1) for b>=2, k>=3, <= N. Dedup via a set.

ceiling: bases satisfy b^2+b+1 <= N  =>  b <= ~sqrt(N). For b up to 1e6 this
loop body runs once per (b,k) pair that is in range, which is ~1e6 * small.
"""
import math

def solve(N):
    s = set()
    if N >= 1:
        s.add(1)
    b = 2
    while True:
        # smallest length-3 value is b^2+b+1
        if b*b + b + 1 > N:
            break
        pw = b*b*b          # b^k for k=3
        while True:
            val = (pw - 1)//(b - 1)
            if val > N:
                break
            s.add(val)
            pw *= b
        b += 1
    return sum(s), sorted(s)

if __name__ == "__main__":
    for N in (50, 1000, 10**12):
        tot, sr = solve(N)
        print("N =", N, " sum =", tot, " count =", len(sr))
