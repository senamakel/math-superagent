"""MISSION 1, attack point 2: independent convex-position verifier built from
scratch (own monotone-chain + gift-wrapping over exact Fractions), in a NEW
file, NOT importing lib.es_geom for the hull.

Points come from lib.es_construct.es_set_blocks(7) (allowed by the mission).
The hull code here is entirely separate from lib.es_geom.

Checks on the wedge-witness bipartition:
  L = {1,2,3,4,5,16..26}, R = {0,6..15,27..31}
  (a) largest convex subset of L is exactly 5  (no convex 6-gon)
  (b) largest convex subset of R is exactly 5
  (c) whole 32-point set has no convex 7-gon; |L|+|R| = 32
Plus witness convex 5-gons in L and R.
"""
from fractions import Fraction
from itertools import combinations
from lib.es_construct import es_set_blocks


def _cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def monotone_hull(points):
    """Andrew monotone chain, exact Fraction arithmetic. Returns CCW hull."""
    pts = sorted(points)
    if len(pts) <= 1:
        return list(pts)
    lower = []
    for p in pts:
        while len(lower) >= 2 and _cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and _cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def in_convex_position(subset):
    if len(subset) < 3:
        return False
    return len(monotone_hull(subset)) == len(subset)

def has_convex_k(points, k):
    """Return (found, witness) for any k-subset in convex position.
    Brute force over C(N,k); correct but not the fastest."""
    N = len(points)
    for comb in combinations(range(N), k):
        sub = [points[i] for i in comb]
        if in_convex_position(sub):
            return True, sub
    return False, None

def largest_convex(points):
    """Exact largest convex subset (brute force, fine for size 16)."""
    N = len(points)
    for r in range(N, 2, -1):
        for comb in combinations(range(N), r):
            sub = [points[i] for i in comb]
            if in_convex_position(sub):
                return r, sub
    return 0, None


def main():
    pts, blocks = es_set_blocks(7)
    N = len(pts)
    L = set([1,2,3,4,5]+list(range(16,27)))
    R = set(range(N)) - L
    LLPts = [pts[i] for i in sorted(L)]
    RRpts = [pts[i] for i in sorted(R)]
    print("N =", N, "|L| =", len(LLPts), "|R| =", len(RRpts), "|L|+|R| =", len(LLPts)+len(RRpts))

    # (a) largest convex subset of L
    lk, lw = largest_convex(LLPts)
    print("L largest convex subset =", lk)
    print("   witness (convex %d-gon in L) = indices:" % lk, [sorted(L)[LLPts.index(p)] for p in lw])
    # explicit: no convex 6-gon
    f6, w6 = has_convex_k(LLPts, 6)
    print("   L has convex 6-gon:", f6)

    # (b) same for R
    rk, rw = largest_convex(RRpts)
    print("R largest convex subset =", rk)
    print("   witness (convex %d-gon in R) = indices:" % rk, [sorted(R)[RRpts.index(p)] for p in rw])
    f6r, w6r = has_convex_k(RRpts, 6)
    print("   R has convex 6-gon:", f6r)

    # (c) whole set: no convex 7-gon
    f7, w7 = has_convex_k(pts, 7)
    print("whole 32-point set has convex 7-gon:", f7)
    if f7:
        print("   witness 7-gon indices:", w7)
    print("union size:", len(LLPts)+len(RRpts), "(must equal 32)")


if __name__ == "__main__":
    main()
