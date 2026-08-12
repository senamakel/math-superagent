#!/usr/bin/env python3
"""Trace the refined collapse on the N=4 configs where it FAILS, to understand
why.  For each failing config, print the full collapse trace (levels and the
parent chosen at each step) so we see whether it loops, diverges, or reaches a
non-origin fixed point.
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

def trace_collapse(S):
    Sset = set(S)
    trace = []
    while Sset != {(0, 0, 0)}:
        M = max(lvl(p) for p in Sset)
        top = [p for p in Sset if lvl(p) == M]
        entry = (M, sorted(top))
        if len(top) != 3:
            return False, trace + [("NON3", entry)]
        p = triangle_parent(sorted(top))
        if p is None:
            return False, trace + [("NOPARENT", entry)]
        if lvl(p) != M - 1:
            return False, trace + [("BADLEVEL", entry, p)]
        # guard against obvious looping: if p already in S (would re-create
        # a cell we just removed), still it might terminate; just record
        for t in top:
            Sset.discard(t)
        Sset.add(p)
        trace.append((M, sorted(top), p))
        # safety cap
        if len(trace) > 40:
            return False, trace + [("LOOP",)]
    return True, trace

def main():
    level = {frozenset([(0, 0, 0)])}
    for N in range(5):
        if N == 4:
            print(f"===== N={N} all configs =====")
            shown = 0
            for S in sorted(level, key=lambda s: sorted(s)):
                ok, trace = trace_collapse(S)
                status = "OK" if ok else "FAIL"
                if not ok and shown < 12:
                    print(f"  [{status}] cells={sorted(S)}")
                    for t in trace:
                        print(f"       {t}")
                    shown += 1
        level = forward_level(level, 3)

if __name__ == "__main__":
    main()
