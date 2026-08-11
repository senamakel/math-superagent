#!/usr/bin/env python3
"""Exact DP for OEIS A007902 (2D amoeba / chessboard-pebbling counts).

G(k, m) = number of 2D reachable configs with k pebbles whose top structure
sits at level m (the CGMO auxiliary, encoded by Alois P. Heinz on OEIS).
a(n) = A007902(n) offset 1: a(1)=1, a(n)=G(n,0) for n>=2.

Recurrence (from CGMO eqs 2.1-2.3, verified against the run's 2D BFS oracle):
  G(k, m):
    k < 1          -> 0
    m = 0          -> 2*G(k-1,0) + G(k,1) + (1 if k==2 else 0)
    m = 1          -> G(k-3,0) + 2*G(k-2,1) + G(k-1,2) + G(k-4,1)
    m >= 2         -> G(k-m-2,m-1) + 2*G(k-m-1,m) + G(k-m,m+1)
  a(1)=1; a(n)=G(n,0).

Run: python code/amoeba2d/a007902_dp.py [max_n]
"""
import sys
from functools import lru_cache

A007902_FIRST_22 = [
    1, 1, 2, 4, 9, 20, 46, 105, 243, 561, 1301, 3014, 6995, 16227, 37668,
    87426, 202961, 471150, 1093819, 2539348, 5895408, 13686805,
]


@lru_cache(maxsize=None)
def G(k, m):
    if k < 1:
        return 0
    if m == 0:
        return 2 * G(k - 1, 0) + G(k, 1) + (1 if k == 2 else 0)
    if m == 1:
        return G(k - 3, 0) + 2 * G(k - 2, 1) + G(k - 1, 2) + G(k - 4, 1)
    return G(k - m - 2, m - 1) + 2 * G(k - m - 1, m) + G(k - m, m + 1)


def a(n):
    return 1 if n == 1 else G(n, 0)


def main():
    max_n = int(sys.argv[1]) if len(sys.argv) > 1 else 22
    seq = [a(n) for n in range(1, max_n + 1)]
    print("a(1..N) =", seq)
    print("matches OEIS A007902 first N:", seq == A007902_FIRST_22[:max_n])


if __name__ == "__main__":
    main()
