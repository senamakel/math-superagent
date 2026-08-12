#!/usr/bin/env python3
"""Dump the actual top-level structure of reachable configs at N=3,4,5.

For each reachable config, group cells by level and show the top level and
the candidate parents (empty cells at M-1 whose children lie in the top).
This shows exactly how A2 fails (top 3 are not a single triangle of one
empty parent).  Fixed BFS: levels advance correctly.
"""
from lib.amoeba import forward_level, children, lvl

def show(S):
    Sset = set(S)
    M = max(lvl(p) for p in Sset)
    top = sorted([p for p in Sset if lvl(p) == M])
    bylevel = {}
    for p in Sset:
        bylevel.setdefault(lvl(p), []).append(p)
    # candidate parents: cells at M-1 whose children are all in top level
    cands = []
    for p in Sset:
        if lvl(p) == M - 1:
            ch = set(children(p, 3))
            if ch.issubset(set(top)):
                cands.append((p, sorted(ch)))
    return M, top, bylevel, cands

def main():
    level = {frozenset([(0, 0, 0)])}
    for N in range(6):
        if N in (3, 4, 5):
            print(f"\n===== N={N}  D={len(level)}  showing all =====")
            for S in sorted(level, key=lambda s: sorted(s)):
                M, top, bylevel, cands = show(S)
                full_tri = None
                for p, ch in cands:
                    if set(ch) == set(top):
                        full_tri = p
                tag = "OK" if (len(cands) == 1 and full_tri is not None) else "BAD-A2"
                print(f"  [{tag}] M={M} top={top}")
                if len(cands) != 1 or full_tri is None:
                    print(f"        bylevel={ {k: sorted(v) for k,v in sorted(bylevel.items())} }")
                    print(f"        cands={[(tuple(p),ch) for p,ch in cands]}")
        level = forward_level(level, 3)

if __name__ == "__main__":
    main()
