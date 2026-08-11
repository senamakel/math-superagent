#!/usr/bin/env python3
"""Empirical probe of the 3D FE763 reachable-config structure (inventor).

Tests on ACTUAL forward-BFS config sets (small N):
  T1. Every reachable config: does its max level hold exactly 3 cells?
      (the "cap"; would make the reverse collapse canonical-deterministic)
  T2. Do those 3 top cells form the complete forward-child triangle of a
      single EMPTY parent at level M-1?
  T3. Reverse cap-merge: merge that cap into its parent, repeat to {origin}.
  T4. Determinism: is the cap unique at every collapse step?

Verbose per-N report; used as the tool_builder's oracle we intend to confirm.
Declared infrastructure cost: exact BFS + reverse cap-merge, exponential in
config size, bounded to N<=6 (configs of <=13 cells).  Oracle only.
"""
from itertools import product
from lib.amoeba import children

E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
DIM = 3


def level(p):
    return sum(p)


def forward_level(level):
    nxt = set()
    for S in level:
        Sset = set(S)
        for p in Sset:
            ch = children(p)
            if all(c not in Sset for c in ch):
                nxt.add(frozenset((Sset - {p}) | set(ch)))
    return nxt


def top_caps(S):
    """Parent cells p at level M-1 whose full child-triangle fills the top
    level of S (the only cells at level M=max)."""
    maxlvl = max(level(pt) for pt in S)
    Sset = set(S)
    top_cells = [pt for pt in S if level(pt) == maxlvl]
    caps = []
    for p in product(range(maxlvl), repeat=3):
        if level(p) != maxlvl - 1:
            continue
        ch = children(p)
        if p not in Sset and set(ch) == set(top_cells):
            caps.append(p)
    return caps


def collapse_to_origin(S):
    """Deterministic cap-merge until {origin} or stuck."""
    Sset = set(S)
    merges = []
    while Sset != {(0, 0, 0)}:
        caps = top_caps(Sset)
        if len(caps) != 1:
            return (False, merges)
        p = caps[0]
        ch = children(p, DIM)
        Sset = (Sset - set(ch)) | {p}
        merges.append(p)
    return (True, merges)


def main():
    level = {frozenset([(0, 0, 0)])}
    Nmax = 6
    for N in range(Nmax + 1):
        t1_bad = t2_bad = t3_bad = t4_bad = 0
        for S in level:
            M = max(level(pt) for pt in S)
            top3 = [pt for pt in S if level(pt) == M]
            if len(top3) != 3:
                t1_bad += 1
            cand = top_caps(S)
            if len(cand) != 1:
                t2_bad += 1
            else:
                ok, merges = collapse_to_origin(S)
                if not ok:
                    t3_bad += 1
                # determinism: each step had a unique cap (collapse aborts if
                # not), so reaching origin implies determinism on this path.
        print(f"N={N}: D={len(level)}  T1(top==3)bad={t1_bad}  "
              f"T2(unique_cap)bad={t2_bad}  T3(collapse)bad={t3_bad}")
        if N == Nmax:
            break
        level = forward_level(level)


if __name__ == "__main__":
    main()
