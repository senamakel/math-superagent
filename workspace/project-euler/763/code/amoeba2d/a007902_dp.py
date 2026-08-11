#!/usr/bin/env python3
"""Print the full G(k,m) table and a(n) for 2D chessboard pebbling.

Run: python code/amoeba2d/a007902_dp.py
"""
from functools import lru_cache


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


if __name__ == "__main__":
    for k in range(1, 9):
        row = [G(k, m) for m in range(0, 6)]
        print(f"k={k}: m=0..5 {row}   a({k})={a(k)}")
