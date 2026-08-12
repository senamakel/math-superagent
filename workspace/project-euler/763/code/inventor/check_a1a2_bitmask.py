#!/usr/bin/env python3
"""Minimal A1/A2 check on the large N=14 frontier, working directly on
bitmask ints (no tuple decode, no f_of, no D(N+1) computation).

A1: every reachable N-config has EXACTLY 3 cells on its max level M.
A2_tri: those 3 top cells are {p+e1,p+e2,p+e3} for a single parent p at M-1.
A2_empty: (stronger) that parent p is absent from the config.

Uses lib.amoeba.next_level_bits to generate levels (the exact bitmask BFS);
reports D(N)=len(level) each level (re-confirming the exact-BFS D values),
and checks A1/A2 only on the requested final level (default N=14).

Frontier bounded by the 2 GiB cap (5.9M at N=14).  Exact arithmetic.
"""
import sys
import time

from lib.amoeba import next_level_bits


def check_level(level, W):
    """Return (D, A1bad, A2tri_bad, A2empty_bad) for a bitmask level set."""
    W2 = W * W
    a1 = a2tri = a2emp = 0
    for S in level:
        m = S
        top = []
        M = -1
        while m:
            low = m & -m
            i = low.bit_length() - 1
            m ^= low
            x, r = divmod(i, W2)
            y, z = divmod(r, W)
            k = x + y + z
            if k > M:
                M = k
                top = [(x, y, z)]
            elif k == M:
                top.append((x, y, z))
        if len(top) != 3:
            a1 += 1
        a, b, c = sorted(top)
        s = (a[0] + b[0] + c[0] - 1, a[1] + b[1] + c[1] - 1,
             a[2] + b[2] + c[2] - 1)
        if s[0] % 3 or s[1] % 3 or s[2] % 3:
            a2tri += 1
            a2emp += 1
            continue
        p = (s[0] // 3, s[1] // 3, s[2] // 3)
        # rebuild children presence test from bitmask
        bit_e1 = 1 << ((p[0] + 1) * W2 + p[1] * W + p[2])
        bit_e2 = 1 << (p[0] * W2 + (p[1] + 1) * W + p[2])
        bit_e3 = 1 << (p[0] * W2 + p[1] * W + (p[2] + 1))
        need = {bit_e1, bit_e2, bit_e3}
        have = set()
        for t in top:
            have |= {1 << (t[0] * W2 + t[1] * W + t[2])}
        if have != need:
            a2tri += 1
            a2emp += 1
            continue
        # parent present?
        if (S >> (p[0] * W2 + p[1] * W + p[2])) & 1:
            a2emp += 1
    return len(level), a1, a2tri, a2emp


def main(Nmax=14):
    W = Nmax + 1
    level = {1}
    for n in range(1, Nmax + 1):
        t0 = time.time()
        level = next_level_bits(level, W)
        D, a1, a2tri, a2emp = check_level(level, W)
        print(f"N={n} D={D} A1bad={a1} A2tri_bad={a2tri} "
              f"A2empty_bad={a2emp} t={time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 14)
