#!/usr/bin/env python3
"""Verify the exact G(k,m) recurrence (CGMO/OEIS A007902) reproduces the 2D
amoeba BFS oracle, and cross-check Eriksson Fig.3 identities.
"""
from functools import lru_cache
from math import comb


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


# 2D amoeba BFS oracle values D2D(N) (the run's own verified counts).
D2D = [1, 1, 2, 4, 9, 20, 46, 105, 243, 561, 1301, 3014, 6995, 16227, 37668]
ok = all(a(n + 1) == D2D[n] for n in range(len(D2D)))
print("G(k,m) recurrence a(n+1) == 2D BFS oracle D2D(n):", ok)

# Eriksson Fig.3 folded-polyominoid table, row/col identities.
fig3 = {
    0: [1, 1, 1, 1, 1, 1],
    1: [1, 2, 3, 4, 5, 6],
    2: [1, 5, 12, 22, 35, 51],
    3: [1, 14, 57, 148, 305, 546],
    4: [1, 42, 300, 1126, 3045, 6756],
    5: [1, 132, 1680, 9220, 32985, 91236],
    6: [1, 429, 9900, 79972, 368665, 1228575],
}


def catalan(j):
    return comb(2 * j, j) - comb(2 * j, j + 1)


col2 = [fig3[k][1] for k in range(7)]
print("Fig3 col n=2 == Catalan C_(k+1):",
      col2 == [catalan(k + 1) for k in range(7)], col2)
row2 = fig3[2]
print("Fig3 row k=2 == n(3n-1)/2:",
      row2 == [n2 * (3 * n2 - 1) // 2 for n2 in range(1, 7)], row2)
