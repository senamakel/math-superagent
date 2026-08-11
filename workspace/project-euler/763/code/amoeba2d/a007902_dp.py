#!/usr/bin/env python3
"""Exact DP for OEIS A007902 (2D amoeba / chessboard-pebbling counts).

Imports the canonical G(k,m)/a(n) from lib/amoeba2d (single shared
definition) and prints a(1..N) with the OEIS match check.

Run: python code/amoeba2d/a007902_dp.py [max_n]
"""
import sys
from lib.amoeba2d import G, a

A007902_FIRST_22 = [
    1, 1, 2, 4, 9, 20, 46, 105, 243, 561, 1301, 3014, 6995, 16227, 37668,
    87426, 202961, 471150, 1093819, 2539348, 5895408, 13686805,
]


def main():
    max_n = int(sys.argv[1]) if len(sys.argv) > 1 else 22
    seq = [a(n) for n in range(1, max_n + 1)]
    print(f"a(1..{max_n}) = {seq}")
    print(f"matches OEIS A007902 first {max_n}: "
          f"{seq == A007902_FIRST_22[:max_n]}")


if __name__ == "__main__":
    main()
