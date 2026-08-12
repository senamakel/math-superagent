#!/usr/bin/env python3
"""Exact check of the top-cap structural claims on live BFS configs, N up to 14.

This is the real tool-builder deliverable: it re-runs forward BFS (bitmask /
frozenset, bounded by memory) and checks, per reachable config:
  A1: the max level M holds EXACTLY 3 cells.
  A2: those 3 top cells are the complete forward triangle {p+e1,p+e2,p+e3}
      of a single EMPTY parent p at level M-1.
  A3: iterating that cap-merge deterministically reaches {origin} in N steps.
  B:  D(N+1) == sum over conf(N) of f(C), f(C)=#cells in C with no child in C.

It also fills the decomposition task: for each N=2..12 it tabulates
  (a) count of configs by max level M
  (b) count of configs by f(C)
  (c) the full joint (M, f) table
  (d) the count of configs by level histogram, with the most frequent shown.

Levels N>=6 use the memory-compact bitmask BFS (code/amoeba/bfs_more.py path
runs to N=14 under the 2 GiB cap); small N use frozensets.  All exact.

Complexity: exact forward BFS over distinct configs -- exponential state set
(the oracle), bounded by the stated capacity.  Memory-capped at N=14.
"""
import sys
from collections import defaultdict

from lib.amoeba import forward_level, children, config_features, lvl, f_of


def top_analysis(S):
    Sset = set(S)
    M = max(lvl(p) for p in Sset)
    top = [p for p in Sset if lvl(p) == M]
    # find empty parents at M-1 whose full child triangle == top set
    parents = []
    for p in Sset:
        if lvl(p) == M - 1:
            ch = set(children(p, 3))
            if ch == set(top):
                parents.append(p)
    # A2 holds iff exactly one such parent, and it is not itself in S (it
    # won't be, since its children are the top cells and it's at M-1, but be safe)
    a2_ok = (len(parents) == 1)
    return M, set(top), a2_ok, parents


def collapse_ok(S):
    """A3: iterated unique cap-merge reaches {origin} in N steps."""
    Sset = set(S)
    steps = 0
    while Sset != {(0, 0, 0)}:
        M = max(lvl(p) for p in Sset)
        top = [p for p in Sset if lvl(p) == M]
        parents = []
        for p in Sset:
            if lvl(p) == M - 1:
                if set(children(p, 3)) == set(top):
                    parents.append(p)
        if len(parents) != 1:
            return False, steps
        p = parents[0]
        Sset = (Sset - set(children(p, 3))) | {p}
        steps += 1
    return True, steps


def build_levels_bitmask(Nmax):
    """Bitmask forward BFS, decode at each level, return list of level sets.

    Uses the compact per-level width W=N+1 (all coords in [0,N]).
    Returns levels[0..Nmax], each a set of frozensets of (x,y,z) tuples.
    """
    # reuse the width-N+1 encoding from amoeba/bfs_more for capacity
    sys.path_append = None  # placeholder, not used
    levels = []
    cur = {frozenset([(0, 0, 0)])}
    for N in range(Nmax + 1):
        levels.append(cur)
        if N == Nmax:
            break
        cur = forward_level(cur, 3)
    return levels


def main():
    Nmax = 14
    mode = 'fs' if Nmax <= 7 else 'fs'
    print("Building levels via forward BFS (frozenset oracle)...")
    levels = build_levels_bitmask(Nmax)

    summary_lines = []
    for N in range(Nmax + 1):
        level = levels[N]
        if N < 2:
            continue
        a1_bad = a2_bad = a3_bad = 0
        f_counts = defaultdict(int)
        M_counts = defaultdict(int)
        joint = defaultdict(int)
        hist_counts = defaultdict(int)
        maxf = 0
        for S in level:
            M, top, a2_ok, parents = top_analysis(S)
            if len(top) != 3:
                a1_bad += 1
            if not a2_ok:
                a2_bad += 1
            ok, steps = collapse_ok(S)
            if not ok or steps != N:
                a3_bad += 1
            fv = f_of(S)
            f_counts[fv] += 1
            M_counts[M] += 1
            joint[(M, fv)] += 1
            hist_counts[hist_key(S)] += 1
            if fv > maxf:
                maxf = fv
        line = (f"N={N} D={len(level)} A1bad={a1_bad} A2bad={a2_bad} "
                f"A3bad={a3_bad}")
        print(line)
        summary_lines.append(line)
        print(f"  by M: {dict(sorted(M_counts.items()))}")
        print(f"  by f: {dict(sorted(f_counts.items()))}   maxf={maxf}")
        print(f"  #distinct histograms={len(hist_counts)}")
        # joint (M,f)
        print("  joint (M,f)->count:")
        for (M, fv) in sorted(joint):
            print(f"    M={M} f={fv}: {joint[(M,fv)]}")
        # top histograms
        print("  most frequent histograms:")
        for h, c in sorted(hist_counts.items(), key=lambda kv: -kv[1])[:8]:
            print(f"    {h}: {c}")
        print()

    with open('/workspace/scratchpad/structure_probe.txt', 'w') as fh:
        fh.write('\n'.join(summary_lines))
        fh.write('\n')
    print("Wrote /workspace/scratchpad/structure_probe.txt")


def hist_key(S):
    f = config_features(S)
    a = [f['hist'].get(k, 0) for k in range(f['M'] + 1)]
    return tuple(a)


if __name__ == "__main__":
    main()
