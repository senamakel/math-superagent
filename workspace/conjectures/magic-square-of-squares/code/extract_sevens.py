#!/usr/bin/env python3
"""Extract the 7-square and 6-square distinct-entry grids from the oracle's
near-miss box c = e^2, e <= 80, |u|,|v| <= 120, and classify each by the
difference-set structure:
   T: u, v, u+v all in S(e)   (7 squares: c+-u, c+-v, c+-(u+v), c)
   D: u, v, u-v all in S(e)   (7 squares: c+-u, c+-v, c+-(u-v), c)
All grids here are magic by the parametrisation; k = number of square
entries.  This is the ground truth my difference-sieve must reproduce.
"""
from math import isqrt
from collections import defaultdict
import sys

sys.path.insert(0, "/workspace/code")  # not needed: brute.py is not a module


def grid_from_params(c, u, v):
    return [
        [c + u, c - u - v, c + v],
        [c - u + v, c, c + u - v],
        [c - v, c + u + v, c - u],
    ]


def is_sq(x):
    return x > 0 and isqrt(x) ** 2 == x


def build_S_sieve(N):
    S = defaultdict(set)
    for m in range(2, isqrt(N) + 1):
        m2 = m * m
        for n in range(1, m):
            s0 = m2 + n * n
            if s0 > N:
                break
            for k in range(1, N // s0 + 1):
                e = k * s0
                d = 4 * k * k * m * n * (m2 - n * n)
                if d < e * e:
                    S[e].add(d)
    return S


def main():
    E_MAX, V_MAX = 80, 120
    S = build_S_sieve(E_MAX)
    sevens = []
    sixes = []
    for e in range(1, E_MAX + 1):
        c = e * e
        max_entry = c + 2 * V_MAX
        for u in range(-V_MAX, V_MAX + 1):
            for v in range(-V_MAX, V_MAX + 1):
                g = grid_from_params(c, u, v)
                entries = g[0] + g[1] + g[2]
                if any(x < 1 for x in entries):
                    continue
                if len(set(entries)) != 9:
                    continue
                k = sum(1 for x in entries if is_sq(x))
                if k >= 7:
                    sevens.append((e, u, v, k, g))
                elif k == 6:
                    sixes.append((e, u, v, k, g))

    print(f"7-square distinct grids: {len(sevens)}")
    for e, u, v, k, g in sevens:
        s = S.get(e, set())
        U, V = abs(u), abs(v)
        t_ok = (U in s and V in s and (U + V) in s)
        d_ok = (U in s and V in s and (U - V) in s and U != V)
        print(f"  e={e} c={e*e} u={u} v={v} k={k}  T(u,v,u+v in S)={t_ok} "
              f"D(u,v,u-v in S)={d_ok}  rows={g}")
    print(f"6-square distinct grids: {len(sixes)}")
    for e, u, v, k, g in sixes[:12]:
        s = S.get(e, set())
        U, V = abs(u), abs(v)
        t_ok = (U in s and V in s and (U + V) in s)
        d_ok = (U in s and V in s and (U - V) in s and U != V)
        print(f"  e={e} u={u} v={v}  T={t_ok} D={d_ok}  rows={g}")

    # for every 6-square grid record which of u,v,u+v,u-v lie in S
    print("\ndetail for all 6-square grids:")
    for e, u, v, k, g in sixes:
        s = S.get(e, set())
        U, V = abs(u), abs(v)
        print(f"  e={e} u={u} v={v}: u_in={U in s} v_in={V in s} "
              f"u+v_in={(U+V) in s} u-v_in={U != V and (U - V) in s} "
              f"|S(e)|={len(s)}")


if __name__ == "__main__":
    main()