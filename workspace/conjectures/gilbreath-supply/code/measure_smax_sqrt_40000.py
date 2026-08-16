#!/usr/bin/env python3
"""Measure the random-walk vs mean-reversion question for S(n)=E2(n):
is max|S(n)|/sqrt(n) bounded (~3-4) or does it drift toward the random-walk
prediction (stdD*sqrt(n)/n = stdD/sqrt(n) -> large) out to N=40000?"""
import sys, math
sys.path.insert(0, "/workspace/code")
from lib.nu2 import fold_nu2
from lib.primes import h_string

def main(N):
    h = h_string(N + 2)
    cum = 0.0; cum_at = 0
    print("n       |S|     |S|/sqrt(n)   CUM max|S|/sqrt(n)")
    snap = set([100, 1000, 4000, 8000, 10000, 20000, 30000, 40000])
    for n in range(50, N + 1):
        v = fold_nu2(n, h)
        S = 2 * v - (n - 2)          # E2, and |S|=|E2|
        r = abs(S) / math.sqrt(n)
        if r > cum:
            cum = r; cum_at = n
        if n in snap:
            print(f"{n:6d}  {abs(S):6d}   {r:7.3f}   {cum:7.3f} @{cum_at}")
    print("done")

if __name__ == "__main__":
    main(40000)
