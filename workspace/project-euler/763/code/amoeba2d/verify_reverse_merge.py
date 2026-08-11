#!/usr/bin/env python3
"""Standalone reverse-merge verification: confirm every config the forward
BFS reaches is reverse-merge-reducible to {origin}, in 2D and 3D.
"""
from itertools import product


def children(p, d):
    return [tuple(p[i] + (1 if i == j else 0) for i in range(d)) for j in range(d)]


def forward_level(level, d):
    nxt = set()
    for S in level:
        Sset = set(S)
        for p in Sset:
            ch = children(p, d)
            if all(c not in Sset for c in ch):
                nxt.add(frozenset((Sset - {p}) | set(ch)))
    return nxt


def merge(key, d, memo, cand):
    if key in memo:
        return memo[key]
    if key == frozenset([(0,) * d]):
        memo[key] = True
        return True
    Sset = set(key)
    for p in cand:
        if p in Sset:
            continue
        ch = children(p, d)
        if all(c in Sset for c in ch):
            ns = frozenset((Sset - set(ch)) | {p})
            if merge(ns, d, memo, cand):
                memo[key] = True
                return True
    memo[key] = False
    return False


def run(d, Nmax):
    level = {frozenset([(0,) * d])}
    memo = {}
    total = fails = 0
    for N in range(Nmax + 1):
        maxc = max(max(pt) for S in level for pt in S)
        cand = [tuple(c) for c in product(range(maxc + 2), repeat=d)]
        for S in level:
            total += 1
            if not merge(frozenset(S), d, memo, cand):
                fails += 1
                print(f"  d={d} N={N} FAILURE: {sorted(S)}")
        if N == Nmax:
            break
        level = forward_level(level, d)
    print(f"d={d}: checked {total} reachable configs (N<= {Nmax}); "
          f"reverse-merge failures={fails}")


if __name__ == "__main__":
    run(2, 8)
    run(3, 4)
