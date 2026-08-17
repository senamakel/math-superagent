"""MISSION 2 — cell-enumeration completeness premise audit for the wedge
diagonal on the n=7 es_construct point set.

All exact Fraction arithmetic (no floats).

(a) General position: no 3 collinear (orient != 0 on all triples).
(b) Count pairs of points with equal x (vertical pairs) and equal y
    (horizontal pairs) — a vertical/horizontal pair-line splits cells and its
    coordinate must be in the cell-enumeration event set. Report them.
(c) For every pair of set points, the line through them contains no other set
    point (restatement of (a)); so every open cell of the arrangement has
    constant angular order.
Plus: confirm the witness apex (2400,2725) lies on NO pair-line (is generic).
"""
from fractions import Fraction
from itertools import combinations
from lib.es_construct import es_set_blocks


def orient3(a, b, c):
    v = (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    if v > 0: return 1
    if v < 0: return -1
    return 0


def main():
    pts, blocks = es_set_blocks(7)
    N = len(pts)
    print("MISSION 2 — cell premise audit, n=7 es_construct, N =", N)

    # (a) general position
    bad = []
    for (i, j, k) in combinations(range(N), 3):
        if orient3(pts[i], pts[j], pts[k]) == 0:
            bad.append((i, j, k))
    print("(a) general position (no 3 collinear):", "PASS" if not bad else "FAIL")
    print("    collinear triples:", bad[:10], "count", len(bad))

    # (b) vertical / horizontal pairs
    vpairs = []
    hpairs = []
    for (i, j) in combinations(range(N), 2):
        if pts[i][0] == pts[j][0]:
            vpairs.append((i, j))
        if pts[i][1] == pts[j][1]:
            hpairs.append((i, j))
    print("(b) vertical pairs (equal x): count", len(vpairs), vpairs[:10])
    print("    horizontal pairs (equal y): count", len(hpairs), hpairs[:10])
    print("    -> event set needs %d extra x's, %d extra y's"
          % (len(vpairs), len(hpairs)))

    # (c) every pair-line contains no other set point  == no 3 collinear (a)
    # verify directly as a restatement
    on_other = []
    for (i, j) in combinations(range(N), 2):
        for k in range(N):
            if k == i or k == j:
                continue
            if orient3(pts[i], pts[j], pts[k]) == 0:
                on_other.append((i, j, k))
    print("(c) pair-line contains no other set point:",
          "PASS (== (a), collinear triples %d)" % len(bad) if not on_other
          else "FAIL", "violations:", on_other[:10], "count", len(on_other))

    # apex generic: lies on NO pair-line == no pair of points collinear with apex
    O = (Fraction(2400), Fraction(2725))
    on_apex = []
    for (i, j) in combinations(range(N), 2):
        if orient3(O, pts[i], pts[j]) == 0:
            on_apex.append((i, j))
    print("witness apex O=(2400,2725) lies on NO pair-line:",
          "PASS (generic)" if not on_apex else "FAIL — on pair-line(s)")
    print("    pairs collinear with apex:", on_apex[:10], "count", len(on_apex))
    print("AUDIT COMPLETE")


if __name__ == "__main__":
    main()
