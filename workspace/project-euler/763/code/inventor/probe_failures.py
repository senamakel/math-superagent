#!/usr/bin/env python3
"""Investigate why the top-cap collapse (A2/A3) fails for N>=4.

The simple claim -- that the 3 cells on the max level M always form the
complete forward-child triangle {p+e1,p+e2,p+e3} of one empty parent p at
level M-1 -- is FALSE for some configs from N=4 on.  This probe dumps a few
failing configs and characterises exactly how the top level breaks.

For each reachable config we print:
  - its occupied cells grouped by level
  - every parent p (at level M-1, empty) whose children are a subset of the
    top level, and what fraction of the top level they cover
  - whether the top 3 are a single full triangle

Declared infrastructure cost: exact BFS + per-config inspection, exponential
state set, bounded to N<=6 (oracle only).
"""
from lib.amoeba import forward_level, children

DIM = 3


def lvl(p):
    return sum(p)


def inspect(S):
    Sset = set(S)
    M = max(lvl(p) for p in Sset)
    top = [p for p in Sset if lvl(p) == M]
    by_level = {}
    for p in Sset:
        by_level.setdefault(lvl(p), []).append(p)
    for k in sorted(by_level):
        by_level[k].sort()

    # parents: level M-1, empty, whose full child triangle sits in the top level
    parents = []
    for p in Sset:
        if lvl(p) == M - 1:
            ch = set(children(p, DIM))
            if ch.issubset(set(top)):
                parents.append((p, ch))
    return M, top, by_level, parents


def main():
    level = {frozenset([(0, 0, 0)])}
    Nmax = 5
    for N in range(Nmax + 1):
        print(f"\n===== N={N}  D={len(level)} =====")
        bad = 0
        for S in sorted(level, key=lambda s: sorted(s)):
            M, top, by_level, parents = inspect(S)
            # A2: exactly one parent p at M-1 (empty) whose full triangle == top set
            unique_single = (len(parents) == 1 and
                             set(parents[0][1]) == set(top) and
                             parents[0][0] not in Sset_present(S))
            if not unique_single:
                bad += 1
                if bad <= 6:
                    print(f"  config cells={sorted(S)}")
                    print(f"    M={M} top={sorted(top)}  parents(covers-top-subset)={[(sorted(set(p[0])),sorted(p[1])) for p in parents]}")
            # Also check a weaker claim: top = full triangle of some (any) parent
    print(f"\nN={N}: A2bad count = {bad}")

def Sset_present(S):
    return S

if __name__ == "__main__":
    main()
