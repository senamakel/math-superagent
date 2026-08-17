from fractions import Fraction
from functools import cmp_to_key
from lib.es_construct import es_set_blocks
from lib.es_geom import orient, has_convex_k_subset

pts, blocks = es_set_blocks(7)
N = len(pts)
O = (Fraction(2500), Fraction(2750))

def circular_order(points, O):
    """CCW circular order of point indices around apex O, exact (half-plane+orient)."""
    def half(idx):
        dx = points[idx][0] - O[0]
        dy = points[idx][1] - O[1]
        return 0 if (dy > 0 or (dy == 0 and dx > 0)) else 1
    def cmp(a, b):
        ha, hb = half(a), half(b)
        if ha != hb:
            return -1 if ha < hb else 1
        c = orient(O, points[a], points[b])
        return -1 if c > 0 else (1 if c < 0 else 0)
    return tuple(sorted(range(len(points)), key=cmp_to_key(cmp)))

# pi-wedge (half-plane) sides through apex O: one per set-point direction.
# boundary ray through point b (exclusive), half-plane = {q : orient(O,b,q) > 0}
sides = set()
for b in range(N):
    side = frozenset(q for q in range(N) if orient(O, pts[b], pts[q]) > 0)
    if 0 < len(side) < N:
        sides.add(side)
print("pi-wedge sides through apex (2500,2750), n=7:", len(sides))
target = 16
checked = 0
valid = 0
for side in sides:
    if len(side) != target:
        continue
    comp = frozenset(range(N)) - side
    if len(comp) != target:
        continue
    checked += 1
    if (not has_convex_k_subset([pts[i] for i in side], 6)[0]
            and not has_convex_k_subset([pts[i] for i in comp], 6)[0]):
        valid += 1
print("pi-wedge checked(size-16) =", checked, " VALID =", valid)

# contiguous-arc (proper wedge) bipartitions
order = circular_order(pts, O)
bips = set()
for s in range(N):
    arc = frozenset(order[(s + k) % N] for k in range(target))
    comp = frozenset(range(N)) - arc
    bips.add(frozenset((arc, comp)))
print("contiguous-arc distinct bipartitions (size-16 arcs):", len(bips))
vvalid = 0
for bip in bips:
    arc, comp = bip
    if (not has_convex_k_subset([pts[i] for i in arc], 6)[0]
            and not has_convex_k_subset([pts[i] for i in comp], 6)[0]):
        vvalid += 1
print("contiguous-arc valid =", vvalid)
