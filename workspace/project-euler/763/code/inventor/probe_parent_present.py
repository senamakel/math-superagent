#!/usr/bin/env python3
"""Resolve the A2 failure: for each config where top-3 is NOT a triangle of an
EMPTY parent, check whether it IS the triangle {p+e1,p+e2,p+e3} of a parent p
that is PRESENT in the config (the top-3 was produced by p, and p got
re-created afterward), or something else entirely.

A2_refined (conjecture): the top 3 cells {a,b,c} always satisfy
    p = (a+b+c-(1,1,1))/3  is integer,  lvl(p)=M-1,  and
    {a,b,c} = {p+e1,p+e2,p+e3}.
Report how often this holds, and whether p is present/absent in S.
"""
from lib.amoeba import forward_level, children, lvl

def triangle_parent(a, b, c):
    """Return p if {a,b,c}={p+e1,p+e2,p+e3}, else None."""
    s = (a[0]+b[0]+c[0]-1, a[1]+b[1]+c[1]-1, a[2]+b[2]+c[2]-1)
    if s[0] % 3 or s[1] % 3 or s[2] % 3:
        return None
    p = (s[0]//3, s[1]//3, s[2]//3)
    if set(children(p, 3)) == {a, b, c}:
        return p
    return None

def main():
    level = {frozenset([(0, 0, 0)])}
    for N in range(8):
        a1bad = 0
        not_triangle = 0
        parent_present = 0
        parent_absent = 0
        examples = []
        for S in level:
            Sset = set(S)
            M = max(lvl(p) for p in Sset)
            top = [p for p in Sset if lvl(p) == M]
            if len(top) != 3:
                a1bad += 1
                continue
            p = triangle_parent(*sorted(top))
            if p is None:
                not_triangle += 1
                examples.append(('NOTRI', sorted(S), M, sorted(top)))
            else:
                if p in Sset:
                    parent_present += 1
                else:
                    parent_absent += 1
        print(f"N={N} D={len(level)} A1bad={a1bad} not_a_triangle={not_triangle} "
              f"parent_PRESENT={parent_present} parent_absent={parent_absent}")
        if N >= 3:
            for e in examples[:5]:
                print(f"    {e}")
        level = forward_level(level, 3)

if __name__ == "__main__":
    main()
