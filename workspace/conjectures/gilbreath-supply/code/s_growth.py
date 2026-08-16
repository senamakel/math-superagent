#!/usr/bin/env python3
"""Quantify growth of |S(n)| where S(n) = -E2(n) = 2*nu2(n)-(n-2) reversed.

SUPPLY pointwise (nu2>=c n) <=> S(n) <= (1-2c)n - 2 eventually, i.e. limsup S/n < 1.
Measured max|S| sublinear; test |S| = O(n^beta) for beta in {0.5,0.55,0.6,0.65} and
report max|S(n)|/n^beta over a long range; also the mean of S(n) over the range,
and |S|/sqrt(n) boundedness (random-walk regime).
"""
import sys
sys.path.insert(0, "/workspace/code")
from lib.nu2 import fold_nu2
from lib.primes import h_string

def main(N):
    h = h_string(N + 2)
    S = {}   # S(n) = -(2*nu2 - (n-2))
    for n in range(2, N + 1):
        v = fold_nu2(n, h)
        S[n] = - (2*v - (n-2))
    mS = max(abs(S[n]) for n in S)
    print(f"N={N}  max|S(n)| = {mS}  at sqrt(N)={N**0.5:.1f}")
    for beta in [0.45, 0.5, 0.55, 0.6, 0.65]:
        mb = max(abs(S[n])/(n**beta) for n in S)
        print(f"  max|S|/n^{beta} = {mb:.3f}")
    # |S|/sqrt(n) bounded over whole range?
    rmax = max(abs(S[n])/(n**0.5) for n in S)
    print(f"  max|S|/sqrt(n) = {rmax:.3f}")
    # mean of S(n)/n and running
    mean_over = sum(S[n] for n in S)/len(S)
    print(f"  mean S(n) over [2,{N}] = {mean_over:.2f}")
    # how many n have |S(n)|/n > 0.05 ?
    cnt = sum(1 for n in S if abs(S[n])/n > 0.05)
    print(f"  count n with |S|/n > 0.05 = {cnt}")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 30000)
