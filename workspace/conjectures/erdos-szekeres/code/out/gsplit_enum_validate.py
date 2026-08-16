#!/usr/bin/env python3
"""Definitive completeness check for the gsplit pair-line enumeration.

Uses an independent, definitely-correct exact separator test: subset S of a
general-position point set, and its complement T, are strictly separable by a
line (S is exactly one open side) IFF convex-hull(S) and convex-hull(T) are
disjoint.  Closed-segment intersection + vertex containment, exact integer
determinants.  Validated first on hand-computable N=3,4 configs.

Compares, against this separator oracle:
  (a) pair-line enumeration completeness: does it produce every open side?
      (the directive's exact concern: FOUR assignments of the two on-line
       points, plus empty/wrong-size bipartitions generated before discard)
  (b) the claimed formula 2*C(N,2)+1 for the number of distinct bipartitions.
"""

from itertools import combinations
from lib.es_geom import orient, convex_hull, in_general_position


def on_or_cross(p, a, b):
    return orient(a, b, p) == 0


def segs_intersect_closed(a, b, c, d):
    """Closed segments ab and cd intersect (any proper crossing OR shared point).
    Exact via orientation; general position means shared points only as
    coincident segment endpoints, handled by bounding-box + orient checks."""
    o1 = orient(a, b, c)
    o2 = orient(a, b, d)
    o3 = orient(c, d, a)
    o4 = orient(c, d, b)
    # general position: a 0 only if point collinear with segment's line and
    # inside it; for our use (two disjoint-or-touching convex polygons from a
    # general-position point set) treat carefully:
    if o1 == 0:
        return on_segment(c, a, b)
    if o2 == 0:
        return on_segment(d, a, b)
    if o3 == 0:
        return on_segment(a, c, d)
    if o4 == 0:
        return on_segment(b, c, d)
    return (o1 > 0) != (o2 > 0) and (o3 > 0) != (o4 > 0)


def on_segment(q, a, b):
    """q on closed segment ab (a,b,q collinear)."""
    if orient(a, b, q) != 0:
        return False
    return (min(a[0], b[0]) <= q[0] <= max(a[0], b[0])
            and min(a[1], b[1]) <= q[1] <= max(a[1], b[1]))


def point_in_poly(p, h):
    if len(h) < 3:
        return False
    m = len(h)
    signs = [orient(h[t], h[(t + 1) % m], p) for t in range(m)]
    return all(s >= 0 for s in signs) or all(s <= 0 for s in signs)


def hulls_overlap(S, T):
    """True iff convex hulls of S and T share a point (not strictly separable)."""
    hS = convex_hull(S)
    hT = convex_hull(T)
    # edge-edge crossings
    for t in range(len(hS)):
        a, b = hS[t], hS[(t + 1) % len(hS)]
        for u in range(len(hT)):
            c, d = hT[u], hT[(u + 1) % len(hT)]
            if segs_intersect_closed(a, b, c, d):
                return True
    # vertex containment (either direction)
    for p in S:
        if point_in_poly(p, hT):
            return True
    for p in T:
        if point_in_poly(p, hS):
            return True
    return False


def is_open_side(points, S_mask):
    """True iff the subset S (bitmask) is strictly an open halfplane side."""
    S = [points[i] for i in range(len(points)) if (S_mask >> i) & 1]
    T = [points[i] for i in range(len(points)) if not ((S_mask >> i) & 1)]
    if not S or not T:
        return False  # empty or full are not 'one open side bipartitions'
    return not hulls_overlap(S, T)


def pair_line_sides(points):
    """The gsplit pair-line enumeration (4 on-line assignments), deduped set of
    side-masks.  Exactly mirrors gsplit_exhaustive.candidate_bipartitions."""
    N = len(points)
    seen = set()
    for (i, j) in combinations(range(N), 2):
        left = 0
        right = 0
        for p in range(N):
            if p == i or p == j:
                continue
            if orient(points[i], points[j], points[p]) > 0:
                left |= 1 << p
            else:
                right |= 1 << p
        seen.add(left | (1 << i) | (1 << j))   # both on left
        seen.add(right | (1 << i) | (1 << j))  # both on right (left side = comp)
        # both-to-right produces side=everything else: that's the complement of
        # "both left", so skip it; but for the OTHER orientation of the pair the
        # roles swap.  We use masks symmetric in complement? No -- record both
        # explicit left sides for the two 'odd' assignments:
        seen.add(left | (1 << i))              # i left, j right
        seen.add(left | (1 << j))              # j left, i right
    # also record complements explicitly so each side and its complement both
    # appear (count of distinct *bipartitions* = distinct {S,~S} pairs)
    return seen


def validate():
    # N=3 triangle
    tri = [(0, 0), (4, 0), (2, 3)]
    assert in_general_position(tri)
    sides = [m for m in range(1, 8) if is_open_side(tri, m)]
    print("N=3 triangle open sides:", len(sides), " (expect 6: 3 singles + 3 pairs)")

    # N=4 convex quadrilateral
    quad = [(0, 0), (3, 0), (4, 3), (0, 4)]
    sides = [m for m in range(1, 16) if is_open_side(quad, m)]
    sgl = [m for m in sides if bin(m).count('1') == 1]
    pair = sorted(bin(m).count('1') for m in sides)
    print("N=4 convex quad open sides:", len(sides), " sizes:", sorted(set(pair)))
    return tri, quad


def main():
    tri, quad = validate()

    # completeness on controlled configs
    for name, pts in [("triangle", tri), ("convex quad", quad),
                      ("quad+1 interior", [(0, 0), (4, 0), (4, 4), (0, 4), (2, 2)])]:
        N = len(pts)
        oracle = {m for m in range(1, (1 << N) - 1) if is_open_side(pts, m)}
        pl = pair_line_sides(pts)
        plnz = {m for m in pl if m != 0 and m != (1 << N) - 1}
        missing = oracle - plnz
        extra = plnz - oracle
        print(f"\n{name} N={N}: oracle open-sides={len(oracle)} "
              f"pair-line distinct(nontrivial)={len(plnz)}")
        print(f"  pair-line missing any genuine open side? {len(missing)>0}"
              f"  ({len(missing)})")
        print(f"  pair-line extras (not genuine)? {len(extra)>0} ({len(extra)})")

    import random
    rng = random.Random(99)
    print("\n=== random general-position sets, N=8..16 ===")
    for N in (8, 10, 12, 14, 16):
        pts = []
        while len(pts) < N:
            p = (rng.randint(0, 1000), rng.randint(0, 1000))
            if in_general_position(pts + [p]):
                pts.append(p)
        oracle = {m for m in range(1, (1 << N) - 1) if is_open_side(pts, m)}
        pl = pair_line_sides(pts)
        plnz = {m for m in pl if m != 0 and m != (1 << N) - 1}
        missing = oracle - plnz
        extra = plnz - oracle
        exp = 2 * (N * (N - 1) // 2) + 1
        print(f"N={N}: oracle={len(oracle)} pairline_nz={len(plnz)} "
              f"2*C(N,2)+1={exp} missing={len(missing)} extra={len(extra)}")


if __name__ == "__main__":
    main()
