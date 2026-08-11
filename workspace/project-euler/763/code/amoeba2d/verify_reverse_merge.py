#!/usr/bin/env python3
"""Reverse-merge verification of the structural characterization.

Claim (backed by CGMO Lemma 3 / Eriksson Prop 20): a set S is reachable in the
amoeba (forward) process iff it can be merged DOWN to the singleton {origin}
by repeatedly replacing the d forward-children of a common missing parent with
that parent.  Verify on all configs the forward BFS reaches, in d=2 and d=3.
Runs standalone.
"""
from itertools import product
from lib.amoeba import children, forward_level


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
