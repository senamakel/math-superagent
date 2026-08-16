#!/usr/bin/env python3
"""Independent verification of es_construct.es_set using a from-scratch
gift-wrapping hull, completely separate from es_geom's Andrew monotone chain.
Cross-checks largest convex subset on n=5 (8 pts) by enumerating all subsets.
"""
from itertools import combinations
from lib.es_construct import es_set


def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])


def gift_hull(points, debug=False):
    """Convex hull via gift wrapping (Jarvis march). Returns CCW vertex set."""
    pts = list(set(points))
    if len(pts) <= 2:
        return set(pts)
    # leftmost-lowest start
    start = min(pts, key=lambda p: (p[0], p[1]))
    hull = []
    p = start
    while True:
        hull.append(p)
        q = pts[0]
        for r in pts[1:]:
            cr = cross(p, q, r)
            if cr > 0 or (cr == 0 and (r[0]-p[0])**2+(r[1]-p[1])**2 >
                          (q[0]-p[0])**2+(q[1]-p[1])**2):
                q = r
        p = q
        if p == start:
            break
    return set(hull)


def in_convex_gift(sub):
    """True iff all of sub are its own hull vertices (gift-wrapping)."""
    if len(sub) < 3:
        return False
    return gift_hull(sub) == set(sub)


def largest_convex_gift(points):
    for r in range(len(points), 2, -1):
        for comb in combinations(range(len(points)), r):
            if in_convex_gift([points[i] for i in comb]):
                return r, comb
    return 0, None


for n in (4, 5, 6):
    S = es_set(n)
    k, wit = largest_convex_gift(S)
    print(f"es_construct n={n}: |S|={len(S)} gift-wrapping largestConvex={k} "
          f"(want {n-1}) -> {'PASS' if k==n-1 else 'FAIL'}")

# independent general-position check via cross products
def genpos(points):
    for a, b, c in combinations(points, 3):
        if cross(a, b, c) == 0:
            return False
    return True

for n in (4, 5, 6):
    print(f"  n={n}: general position (cross-prod) = {genpos(es_set(n))}")
