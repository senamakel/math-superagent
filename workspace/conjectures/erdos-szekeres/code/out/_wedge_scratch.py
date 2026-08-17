from fractions import Fraction
from functools import cmp_to_key
from lib.es_construct import es_set_blocks
from lib.es_geom import orient, has_convex_k_subset

pts, blocks = es_set_blocks(7)
N = len(pts)
print("N =", N, "block sizes:", [len(b) for b in blocks])
print("block size 1..6 (T0..T5):", [len(b) for b in blocks])
# block membership per point index
mp = []
for b, blk in enumerate(blocks):
    for _ in blk:
        mp.append(b)
print("block membership:", mp)
print("first few coords:", pts[:3])
O = (Fraction(2500), Fraction(2750))

def angular_order(points, O):
    def half(idx):
        x, y = points[idx]
        dx, dy = x - O[0], y - O[1]
        return 0 if (dy > 0 or (dy == 0 and dx > 0)) else 1
    order = list(range(len(points)))
    def cmp(a, b):
        ha, hb = half(a), half(b)
        if ha != hb:
            return -1 if ha < hb else 1
        c = orient(O, points[a], points[b])
        if c > 0: return -1
        if c < 0: return 1
        return 0
    return sorted(order, key=cmp_to_key(cmp))

def apex_general(points, O):
    from itertools import combinations
    for a, b in combinations(range(len(points)), 2):
        if orient(O, points[a], points[b]) == 0:
            return False
    return True

def is_avoiding(pts_sub, k):
    return not has_convex_k_subset(pts_sub, k)[0]

print("apex_general:", apex_general(pts, O))
order = angular_order(pts, O)
print("circular order:", order)

target = 16
# enumerate distinct bipartitions: all contiguous arcs of size 16
bips = set()
for s in range(N):
    arc = frozenset(order[(s+k) % N] for k in range(target))
    comp = frozenset(range(N)) - arc
    bips.add(frozenset((arc, comp)))
print("distinct bipartitions (size 16 arcs):", len(bips))

valid = []
for bip in bips:
    arc, comp = bip
    if is_avoiding([pts[i] for i in arc], 6) and is_avoiding([pts[i] for i in comp], 6):
        valid.append((sorted(arc), sorted(comp)))
print("valid:", len(valid))
for arc, comp in valid:
    print("  arc:", arc)
    print("  comp:", comp)
    print("  arc blocks:", [mp[i] for i in arc])
    print("  comp blocks:", [mp[i] for i in comp])
