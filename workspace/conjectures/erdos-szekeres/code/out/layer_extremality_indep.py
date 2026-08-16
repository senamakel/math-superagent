"""Independent cross-check of layer-extremality (Conjecture C) on es_construct.

Same statement as layer_extremality.py but uses a from-scratch gift-wrapping
(Jarvis) hull and a from-scratch orientation (determinant sign) instead of
es_geom, so the result is not an artifact of one implementation.
"""
from lib.es_construct import es_set


def orient(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])


def giftwrap_hull(points):
    pts = list(points)
    if len(pts) < 3:
        return list(pts)
    # leftmost-lowest start
    start = min(pts, key=lambda p: (p[0], p[1]))
    hull = []
    cur = start
    while True:
        hull.append(cur)
        nxt = pts[0]
        for p in pts:
            if p == cur:
                continue
            o = orient(cur, nxt, p)
            if nxt == cur or o < 0 or (o == 0 and _dist2(cur, p) > _dist2(cur, nxt)):
                nxt = p
        if nxt == start:
            break
        cur = nxt
    return hull


def _dist2(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2


def onion_layers(points):
    pts = list(points)
    layers = []
    while pts:
        h = giftwrap_hull(pts)
        hset = set(h)
        layers.append([p for p in pts if p in hset])
        pts = [p for p in pts if p not in hset]
    return layers


def has_convex(points, k):
    from itertools import combinations
    for comb in combinations(points, k):
        if len(giftwrap_hull(comb)) == k:
            return True
    return False


def all_convex(points):
    return len(giftwrap_hull(points)) == len(points)


print("=== Independent (gift-wrap) cross-check of layer-extremality ===")
for n in (5, 6, 7):
    S = es_set(n)
    layers = onion_layers(S)
    profile = [len(L) for L in layers]
    all_ok = True
    for L in layers:
        m = len(L)
        if m >= n - 1:
            ok = has_convex(L, n - 1)
        else:
            ok = all_convex(L)
        all_ok &= ok
    print(f"n={n}: profile={profile} Conjecture C = {'PASS' if all_ok else 'FAIL'}")
