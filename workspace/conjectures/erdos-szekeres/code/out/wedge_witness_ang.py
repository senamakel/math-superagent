"""MISSION 1, attack point 1: re-derive the circular angular order of the 32
es_construct points around apex O=(2400,2725) from scratch, and confirm that
L=[1,2,3,4,5,16..26] and R=[0,6..15,27..31] are exactly the two contiguous
size-16 arcs of the correct bipartition.

Uses ONLY cross-multiplication half-plane + orientation comparator defined in
this file (no lib.es_geom, no lib.es_construct).  Coordinates are taken fresh
from lib.es_construct.es_set_blocks (allowed: the mission says points come from
lib.es_construct.es_set_blocks; the comparator is from scratch).  To be fully
independent we re-emit the construction too and verify it matches.
"""
from fractions import Fraction
from math import comb


# ---------------- from-scratch re-emission of es_construct ----------------
# (re-emitted so the angular audit depends on nothing but integers/rationals
#  and the book construction; cross-checked against lib result below)

def _bbox(S):
    xs = [p[0] for p in S]; ys = [p[1] for p in S]
    return min(xs), max(xs), min(ys), max(ys)

def _flatten_y(S, target_max=Fraction(2, 10)):
    m = Fraction(0)
    for (a, b) in __import__('itertools').combinations(S, 2):
        if a[0] == b[0]:
            m = Fraction(2); break
        s = abs((b[1]-a[1])/(b[0]-a[0]))
        if s > m: m = s
    if m == 0: return S
    factor = target_max/(2*m)
    return [(x, y*factor) for (x, y) in S]

def _cup(n):
    c = Fraction(1, 20); return [(Fraction(i), c*i*i) for i in range(n)]
def _cap(n):
    c = Fraction(1, 20); return [(Fraction(i), -c*i*i) for i in range(n)]

def _merge_AB_above(A, B):
    Ax0,Ax1,Ay0,Ay1 = _bbox(A); Bx0,Bx1,By0,By1 = _bbox(B)
    gap = Fraction(8)
    shift_x = (Ax1-Bx0)+gap
    dy = Ay1 + Fraction(1,2)*gap - By1
    Bm = [(x+shift_x, y+dy) for (x,y) in B]
    return A+Bm

def cupcap(k, l):
    if k == 2 or l == 2: return [(Fraction(0), Fraction(0))]
    if k == 3: return _cap(l-1)
    if l == 3: return _cup(k-1)
    A = cupcap(k-1, l); B = cupcap(k, l-1)
    A = _flatten_y(A, Fraction(1,40)); B = _flatten_y(B, Fraction(1,40))
    return _flatten_y(_merge_AB_above(A,B), Fraction(1,20))

def es_block(n, i):
    k = n-i; l = i+2
    S = cupcap(k, l); S = _flatten_y(S, Fraction(1,20))
    x0,x1,y0,y1 = _bbox(S)
    return [(x-x0, y-y0+Fraction(1)) for (x,y) in S]

def _convex_arc_centers(n):
    m = n-1; start_y = Fraction(5000)
    diffs = [Fraction(-(1000-100*t)) for t in range(m)]
    centers = []; y = start_y
    for i in range(m):
        centers.append((Fraction(i*1000), y))
        if i < m-1: y = y + diffs[i]
    return centers

def rebuild_es_set_blocks(n):
    centers = _convex_arc_centers(n)
    scale = Fraction(1, 10**6)
    out = []; blocks = []
    for i in range(n-1):
        T = es_block(n, i)
        assert len(T) == comb(n-2, i)
        cx, cy = centers[i]
        block = [(cx + scale*px, cy + scale*py) for (px,py) in T]
        out.extend(block); blocks.append(block)
    return out, blocks


# ---------------- from-scratch exact angular comparator ----------------

def half(idx, pts, O):
    x, y = pts[idx]
    dx, dy = x - O[0], y - O[1]
    # upper half-plane incl. positive x-axis -> 0, else 1
    return 0 if (dy > 0 or (dy == 0 and dx > 0)) else 1

def orient3(O, a, b):
    # sign of (a-O) cross (b-O) via integer determinants, exact
    ax, ay = a[0]-O[0], a[1]-O[1]
    bx, by = b[0]-O[0], b[1]-O[1]
    v = ax*by - ay*bx
    if v > 0: return 1
    if v < 0: return -1
    return 0

from functools import cmp_to_key
def angular_order(pts, O):
    def cmp(i, j):
        hi, hj = half(i, pts, O), half(j, pts, O)
        if hi != hj:
            return -1 if hi < hj else 1
        c = orient3(O, pts[i], pts[j])
        if c > 0: return -1
        if c < 0: return 1
        return 0   # collinear with apex (caller excludes)
    return sorted(range(len(pts)), key=cmp_to_key(cmp))

def apex_generic(pts, O):
    for i in range(len(pts)):
        for j in range(i+1, len(pts)):
            if orient3(O, pts[i], pts[j]) == 0:
                return False, (i, j)
    return True, None


def main():
    O = (Fraction(2400), Fraction(2725))
    pts_mine, _ = rebuild_es_set_blocks(7)
    from lib.es_construct import es_set_blocks as lib_blocks
    pts_lib, _ = lib_blocks(7)
    assert pts_mine == pts_lib, "re-emission differs from lib (audit FAIL)"
    print("re-emitted es_construct(7) == lib es_construct(7): True; N =", len(pts_mine))

    pts = pts_mine
    # apex must not see two points on the same ray
    ok, bad = apex_generic(pts, O)
    print("apex O=%s generic wrt points (no two on a ray): %s" % (O, ok))
    if not ok:
        print("  BAD collinear-with-apex pair:", bad)

    order = angular_order(pts, O)
    print("circular order around O:", order)

    N = len(order)
    target = 16
    # all contiguous size-16 arcs and their complements
    L = [1,2,3,4,5]+list(range(16,27))
    R = [0]+list(range(6,16))+list(range(27,32))
    L = set(L); R = set(R)

    # Does some contiguous arc of length 16 in `order` equal exactly L?
    found = None
    for s in range(N):
        arc = set(order[(s+k) % N] for k in range(target))
        if arc == L:
            found = s
            break
    print("L is a contiguous size-16 arc starting at index", found)
    # complement automatically R?
    print("complement of L is exactly R:", (set(range(N)) - L) == R)

    # print all arcs and their complement to show bipartition structure
    print("\nAll size-16 arcs (sector -> complement):")
    seen = set()
    for s in range(N):
        arc = frozenset(order[(s+k) % N] for k in range(target))
        comp = frozenset(range(N)) - arc
        key = frozenset((arc, comp))
        if key in seen: continue
        seen.add(key)
        print("  sector=%s" % sorted(arc))
        print("       comp=%s" % sorted(comp))
        if arc == L:
            print("      <== THE CLAIMED L/R BIPARTITION")

    # check pair-count: how many distinct such bipars
    print("\n# distinct size-16 bipartitions (arc|comp):", len(seen))


if __name__ == "__main__":
    main()
