#!/usr/bin/env python3
"""Test the REFINED collapse (A3): with the top-3 always being the full child
triangle {p+e1,p+e2,p+e3} of a single parent p (which may be PRESENT in the
config or empty), does iterating  S := (S - children(p)) | {p}  deterministically
reach {origin} in N steps for every reachable N-config?

This is the version that matters for a compressed DP: if it holds, positions
correspond bijectively to full ternary collapse trees regardless of whether
the cap parent is present.

Also verifies the refined A2 (top 3 is always a single parent's triangle).
Runs live BFS N<=7 (frozenset oracle).
"""
from lib.amoeba import forward_level, children, lvl

def triangle_parent(top):
    a, b, c = top
    s = (a[0]+b[0]+c[0]-1, a[1]+b[1]+c[1]-1, a[2]+b[2]+c[2]-1)
    if s[0] % 3 or s[1] % 3 or s[2] % 3:
        return None
    p = (s[0]//3, s[1]//3, s[2]//3)
    if set(children(p, 3)) == set(top):
        return p
    return None

def refined_collapse(S):
    """Refined unique-collapse to origin.  top-3 = triangle of parent p
    (present or not); S := (S - top) | {p}.  Return (ok, steps)."""
    Sset = set(S)
    steps = 0
    while Sset != {(0, 0, 0)}:
        M = max(lvl(p) for p in Sset)
        top = [p for p in Sset if lvl(p) == M]
        if len(top) != 3:
            return False, steps
        p = triangle_parent(sorted(top))
        if p is None:
            return False, steps
        # p must be at level M-1 (follows from the triangle identity) -- check
        if lvl(p) != M - 1:
            return False, steps
        for t in top:
            if t in Sset:
                Sset.discard(t)
        Sset.add(p)
        steps += 1
    return True, steps

def main():
    level = {frozenset([(0, 0, 0)])}
    for N in range(8):
        a2_refined_bad = 0
        a3_refined_bad = 0
        for S in level:
            Sset = set(S)
            M = max(lvl(p) for p in Sset)
            top = [p for p in Sset if lvl(p) == M]
            if N >= 1 and len(top) != 3:
                continue
            if N == 0:
                continue
            p = triangle_parent(sorted(top))
            if p is None:
                a2_refined_bad += 1
            ok, steps = refined_collapse(S)
            if not ok or steps != N:
                a3_refined_bad += 1
        print(f"N={N} D={len(level)} A2_refined_bad(non-triangle)={a2_refined_bad} "
              f"A3_refined_bad(collapse)={a3_refined_bad}")
        level = forward_level(level, 3)

if __name__ == "__main__":
    main()
