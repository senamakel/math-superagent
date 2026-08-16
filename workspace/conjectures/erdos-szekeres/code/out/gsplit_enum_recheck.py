#!/usr/bin/env python3
"""Enumeration-completeness recheck for the gsplit line-split test (steer directive).

Question: does the line-through-a-pair enumeration in gsplit_exhaustive.py
(with the two on-line points assigned to the two open sides in all four ways)
produce EVERY combinatorially distinct *open*-half-plane bipartition of the
point set?  And is the deduplicated count of such bipartitions 2*C(N,2)+1?

Definitions
-----------
An *open-half-plane bipartition* of a finite planar point set in general
position is an ordered/unordered partition (S, complement) such that some line
L (containing NO point of the set) has the points of S strictly on one side and
all others strictly on the other.  (This is exactly a "k-set" boundary cut,
for the k = |S|.)

Oracle (brute force, feasible for N<=~16 via 2^N subsets): a subset S is a
valid open-side iff there is a separating line.  Since points are in general
position, S is an open side iff the convex hulls of S and of complement are
disjoint with a separating line — equivalently, iff no point of the complement
lies inside or on the convex hull of S AND no point of S inside the hull of
complement, AND the two hulls can be strictly separated.  For finite point
sets, S and comp are strictly linearly separable iff their convex hulls are
disjoint (strict separation theorem).  We test by checking orient signs: S is a
side iff hulls disjoint.

BUT the line-through-pair enumeration uses a DIFFERENT notion: it enumerates
bipartitions of the form (set strictly on one side of the line through pair
(i,j), with i and j then placed in all 4 ways).  The question is whether every
open-side bipartition equals one of these.  The classical k-set fact says: every
open-half-plane bipartition is realizable with the separating line moved (by a
tiny perturbation, without crossing any point) to pass through two points of the
set; the two points sit on the line and can be pushed to either open side, which
is exactly the 4 assignments.  So the enumeration should be COMPLETE.  We verify
this against the brute-force oracle on general-position integer sets of sizes
8..16, and separately confirm the deduplicated count equals 2*C(N,2)+1.

The count 2*C(N,2)+1: there are C(N,2) pairs.  For each pair, the line through
it, perturbed a tiny epsilon one way or the other, gives two sides; but the two
points on the line must be assigned.  Classically, the number of k-sets summed
over k of a general-position point set is exactly N(N-1)+2 (this is the
"rotation" count: rotating a line 180 degrees cycles through N(N-1) + ... ; a
known result, e.g. Lovasz on k-sets).  We verify the number of DISTINCT
bipartitions produced by candidate_bipartitions equals 2*C(N,2)+1 = N(N-1)+2.

Exact integer arithmetic throughout (orient via determinants).  This is the
independent second route the directive asks for: an oracle that does NOT use
the pair-line construction, cross-checked against it.
"""

from itertools import combinations
from lib.es_geom import orient, convex_hull, in_general_position


def segments_intersect_proper(a, b, c, d):
    """Proper orientation-based check: open segment ab intersects open segment cd
    (endpoints strictly on opposite sides) .""" 
    o1 = orient(a, b, c)
    o2 = orient(a, b, d)
    o3 = orient(c, d, a)
    o4 = orient(c, d, b)
    return (o1 != 0 and o2 != 0 and o3 != 0 and o4 != 0
            and (o1 > 0) != (o2 > 0) and (o3 > 0) != (o4 > 0))


def hulls_disjoint(S, comp):
    """True iff convex hull of S and hull of comp are disjoint (no shared point).
    Exact: check edge crossing and vertex containment.  General position => no
    vertex sits on the other's edge."""
    hS = convex_hull(S)
    hC = convex_hull(comp)
    # edge crossings
    for t in range(len(hS)):
        a, b = hS[t], hS[(t + 1) % len(hS)]
        for u in range(len(hC)):
            c, d = hC[u], hC[(u + 1) % len(hC)]
            if segments_intersect_proper(a, b, c, d):
                return False
    # vertex containment
    for p in S:
        if point_in_convex_polygon(p, hC):
            return False
    for p in comp:
        if point_in_convex_polygon(p, hS):
            return False
    return True


def point_in_convex_polygon(p, h):
    """p inside or on convex polygon h (CCW/any orientation): consistent orient."""
    if len(h) < 3:
        return True
    m = len(h)
    signs = [orient(h[t], h[(t + 1) % m], p) for t in range(m)]
    return all(s >= 0 for s in signs) or all(s <= 0 for s in signs)


def is_open_side_oracle(pts, S):
    """True iff S is exactly the set of points strictly on one open side of
    some line containing no point.  Exact strict separation via disjoint hulls."""
    comp = [p for p in pts if p not in S]
    if not S or not comp:
        return False  # empty side: not an open-half-plane bipartition of the set
    return hulls_disjoint(S, comp)


def pair_line_bipartitions(pts):
    """The enumeration from gsplit_exhaustive.py: for each pair, assign the two
    on-line points to the two open sides in all 4 ways.  Returns the SET of
    frozensets (one side) reached, deduplicated."""
    N = len(pts)
    seen = set()
    for (i, j) in combinations(range(N), 2):
        left = set(); right = set()
        for p in range(N):
            if p == i or p == j:
                continue
            if orient(pts[i], pts[j], pts[p]) > 0:
                left.add(p)
            else:
                right.add(p)
        # four ways to assign the two on-line points to the two open sides;
        # record the 'left' side content in each case (right is complement).
        seen.add(frozenset(left | {i, j}))   # both on left
        seen.add(frozenset(right | {i, j}))  # both on right (complement recorded)
        seen.add(frozenset(left | {i}))      # i left, j right
        seen.add(frozenset(left | {j}))      # j left, i right
    return seen


def main():
    import random
    rng = random.Random(1234)
    print("=== Enumeration-completeness recheck ===")
    for N in (8, 10, 12, 14, 16):
        # make a general-position integer set in a box
        pts = []
        while len(pts) < N:
            p = (rng.randint(0, 1000), rng.randint(0, 1000))
            trial = pts + [p]
            if in_general_position(trial):
                pts.append(p)
        pair = pair_line_bipartitions(pts)
        # oracle: all true open-side bipartitions
        oracle = set()
        for mask in range(1, (1 << N) - 1):
            S = frozenset(i for i in range(N) if (mask >> i) & 1)
            if is_open_side_oracle(pts, [pts[i] for i in S]):
                oracle.add(S)
        exp = 2 * (N * (N - 1) // 2) + 1  # 2*C(N,2)+1
        print(f"N={N}: pair-line distinct={len(pair)}  expected {exp}"
              f"  oracle-open-sides={len(oracle)}")
        missing = oracle - pair
        extra = pair - oracle
        print(f"   oracle sides not produced by pair-line: {len(missing)}")
        if missing:
            print("     MISSING example:", sorted(missing)[:4])
        print(f"   pair-line sides not open-sides (false positives): {len(extra)}")

    # exact structural identity check: does 2*C(N,2)+1 hold on the construction sets?
    print("\n=== Check the count on the actual es_construct sets ===")
    from lib.es_construct import es_set
    for n in (5, 6, 7):
        pts = es_set(n)
        N = len(pts)
        pair = pair_line_bipartitions(pts)
        exp = 2 * (N * (N - 1) // 2) + 1
        print(f"n={n}: N={N} pair-line distinct={len(pair)}  expected 2*C(N,2)+1={exp}"
              f"  match={len(pair)==exp}")


if __name__ == "__main__":
    main()
