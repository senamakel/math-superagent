#!/usr/bin/env python3
"""For the N=4 configs where the naive top-cap collapse fails, list ALL
legitimate reverse moves: empty p (p not in C) with children(p) all in C, and
their level.  This shows whether the true reverse structure is a clean top-cap
collapse or a lower-level balancing move (voidance/folded-polyominoid picture).
"""
from lib.amoeba import forward_level, children

def lvl(p):
    return sum(p)

def reverse_moves(S):
    Sset = set(S)
    M = max(lvl(p) for p in Sset)
    moves = []
    # search all lattice points p in [0..M] that are empty with children in S
    for x in range(M+1):
        for y in range(M+1):
            for z in range(M+1):
                p = (x, y, z)
                if p in Sset:
                    continue
                ch = set(children(p, 3))
                if ch.issubset(Sset):
                    moves.append((lvl(p), p, sorted(ch)))
    return moves

def main():
    level = {frozenset([(0, 0, 0)])}
    for N in range(5):
        if N == 4:
            print(f"===== N={N} =====")
            for S in sorted(level, key=lambda s: sorted(s)):
                Sset = set(S)
                M = max(lvl(p) for p in Sset)
                top = [p for p in Sset if lvl(p) == M]
                # naive empty-cap at top
                naive_caps = [p for p in Sset if lvl(p)==M-1 and set(children(p,3))==set(top) and p not in Sset]
                moves = reverse_moves(S)
                # focus on configs where top-3 parent is present (the A2 fail)
                # or where naive cap is missing
                if not (len(naive_caps) == 1):
                    print(f"  cells={sorted(S)}")
                    print(f"    M={M} top={sorted(top)}")
                    # top parent present?
                    if len(top)==3:
                        pts=sorted(top)
                        s=(pts[0][0]+pts[1][0]+pts[2][0]-1, pts[0][1]+pts[1][1]+pts[2][1]-1, pts[0][2]+pts[1][2]+pts[2][2]-1)
                        cand=None
                        if all(v%3==0 for v in s):
                            p=(s[0]//3,s[1]//3,s[2]//3)
                            if set(children(p,3))==set(top):
                                cand=p
                        print(f"    triparent={cand} present={cand in Sset}")
                    print(f"    all reverse moves (lvl,p,children): {moves}")
        level = forward_level(level, 3)

if __name__ == "__main__":
    main()
