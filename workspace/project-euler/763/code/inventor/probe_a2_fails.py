#!/usr/bin/env python3
"""Pinpoint exactly which reachable configs fail A2 (top-3 is NOT the full
child-triangle of any single empty point at level M-1) and A3.

Uses the SAME top_caps definition as check_recurrence.py: search EVERY lattice
point p in the box with lvl(p)==M-1, p not in S, set(children(p))==set(top).
A candidate top 'cap' is such a p.

Prints, for N=1..5, the configs whose top set is not a unique single cap, with
their top set and all near-miss parents, so we can see the actual geometry of
the failure.
"""
from lib.amoeba import forward_level, children
from itertools import product

def lvl(p):
    return sum(p)

def top_caps(S):
    M = max(lvl(p) for p in S)
    Sset = set(S)
    top = [p for p in Sset if lvl(p) == M]
    caps = [p for p in product(range(max(1, M)), repeat=3)
            if lvl(p) == M - 1 and p not in Sset and set(children(p, 3)) == set(top)]
    return M, sorted(top), caps

def main():
    level = {frozenset([(0, 0, 0)])}
    for N in range(7):
        a1bad = a2bad = a3bad = 0
        fails = []
        for S in level:
            M, top, caps = top_caps(S)
            if len(top) != 3:
                a1bad += 1
            cap_ok = (len(caps) == 1)
            if len(top) == 3 and not cap_ok:
                fails.append((sorted(S), M, top, caps))
            if len(top) == 3 and not cap_ok:
                a2bad += 1
        if N >= 3:
            print(f"N={N} D={len(level)} A1bad={a1bad} A2bad(unique-cap-fail)={a2bad}")
            for (S, M, top, caps) in fails[:20]:
                print(f"   M={M} top={top}  caps={[tuple(c) for c in caps]}")
                # show which parents at M-1 have children intersecting top
        level = forward_level(level, 3)

if __name__ == "__main__":
    main()
