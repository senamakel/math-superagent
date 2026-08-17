import time
from fractions import Fraction
from functools import cmp_to_key
from lib.es_construct import es_set_blocks
from lib.es_geom import orient, has_convex_k_subset

pts, blocks = es_set_blocks(7)
N = len(pts)
O = (Fraction(2400), Fraction(2725))

def circular_order(points, O):
    def half(idx):
        dx = points[idx][0] - O[0]; dy = points[idx][1] - O[1]
        return 0 if (dy > 0 or (dy == 0 and dx > 0)) else 1
    def cmp(a, b):
        ha, hb = half(a), half(b)
        if ha != hb: return -1 if ha < hb else 1
        return -1 if orient(O, points[a], points[b]) > 0 else 1
    return tuple(sorted(range(len(points)), key=cmp_to_key(cmp)))

t0=time.time()
order = circular_order(pts, O)
target = 16
bips = []
seen = set()
for s in range(N):
    arc = frozenset(order[(s+k) % N] for k in range(target))
    comp = frozenset(range(N)) - arc
    key = frozenset((arc, comp))
    if key in seen: continue
    seen.add(key)
    bips.append((arc, comp))
valid = 0
for arc, comp in bips:
    if (not has_convex_k_subset([pts[i] for i in arc], 6)[0]
            and not has_convex_k_subset([pts[i] for i in comp], 6)[0]):
        valid += 1
t1=time.time()
print("distinct biparts:", len(bips), "valid:", valid, "time:", round(t1-t0,3), "s")
