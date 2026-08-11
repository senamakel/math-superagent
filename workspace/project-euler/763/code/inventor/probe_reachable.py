#!/usr/bin/env python3
"""Probe: 3D FE763 reachable configs, verified against Eriksson structure.

For N = 0..6:
  1. Forward BFS over distinct occupied-cube sets (exact, small-N).
  2. Reverse-merge check: every reachable config must reduce to {origin} by
     repeatedly replacing the three children of a common absent parent with
     that parent (Eriksson voidance/position characterization, n>=3).
  3. Collect the *voidance set* along the way: every cell that is a pebble at
     some stage but ends up empty.  Report its size distribution per N and how
     it relates to D(N).
"""
from itertools import product

DIM = 3
E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def children(p):
    return tuple(tuple(p[i] + e[i] for i in range(DIM)) for e in E)


def forward_level(level):
    nxt = set()
    for S in level:
        Sset = set(S)
        for p in Sset:
            ch = children(p)
            if all(c not in Sset for c in ch):
                nxt.add(frozenset((Sset - {p}) | set(ch)))
    return nxt


def mergeable(key, cand, memo):
    if key in memo:
        return memo[key]
    if key == frozenset([(0, 0, 0)]):
        memo[key] = True
        return True
    Sset = set(key)
    for p in cand:
        if p in Sset:
            continue
        ch = children(p)
        if all(c in Sset for c in ch):
            ns = frozenset((Sset - set(ch)) | {p})
            if mergeable(ns, cand, memo):
                memo[key] = True
                return True
    memo[key] = False
    return False


def main():
    level = {frozenset([(0, 0, 0)])}
    memo = {}
    Nmax = 6
    for N in range(Nmax + 1):
        maxc = max(max(pt) for S in level for pt in S)
        cand = [tuple(c) for c in product(range(maxc + 2), repeat=3)]
        fails = 0
        for S in level:
            if not mergeable(S, cand, memo):
                fails += 1
                print(f"  N={N} NOT mergeable: {sorted(S)}")
        print(f"N={N}: D={len(level)}  mergeable_ok={fails==0}  (fails={fails})")
        if N == Nmax:
            break
        level = forward_level(level)


if __name__ == "__main__":
    main()
