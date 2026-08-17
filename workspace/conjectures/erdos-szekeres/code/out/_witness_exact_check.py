#!/usr/bin/env python3
"""Direct exact check of the wedge witness claim around apex O=(2400,2725).

Computes the exact circular angular order of the 32 es_construct(7) points
around O from scratch (half-plane + cross-product comparator, fractions), lists
the contiguous size-16 arcs, and tests each arc+complement for 6-avoidance with
the exact oracle.  Independent of any probe's angular sort.
"""
from fractions import Fraction
from functools import cmp_to_key
from lib.es_construct import es_set_blocks
from lib.es_geom import orient, has_convex_k_subset

pts, blocks = es_set_blocks(7)
N = len(pts)
O = (Fraction(2400), Fraction(2725))
target = 16

def half(idx):
    dx = pts[idx][0] - O[0]
    dy = pts[idx][1] - O[1]
    return 0 if (dy > 0 or (dy == 0 and dx > 0)) else 1

def cmp(a, b):
    ha, hb = half(a), half(b)
    if ha != hb:
        return -1 if ha < hb else 1
    c = orient(O, pts[a], pts[b])
    return -1 if c > 0 else (1 if c < 0 else 0)

order = sorted(range(N), key=cmp_to_key(cmp))
blk = [bi for b, blk in enumerate(blocks) for bi in [b] * len(blk)]
print("exact circular order around O=(2400,2725):")
print("  indices:", order)
print("  blocks :", [blk[i] for i in order])

# contiguous size-16 arcs
seen = set()
arcs = []
for s in range(N):
    arc = frozenset(order[(s + k) % N] for k in range(target))
    comp = frozenset(range(N)) - arc
    key = frozenset((arc, comp))
    if key in seen:
        continue
    seen.add(key)
    arcs.append((arc, comp))

valid = []
for arc, comp in arcs:
    A = [pts[i] for i in arc]
    C = [pts[i] for i in comp]
    ok = (not has_convex_k_subset(A, 6)[0]) and (not has_convex_k_subset(C, 6)[0])
    if ok:
        valid.append((sorted(arc), sorted(comp)))

print(f"\ncontiguous size-16 arcs: {len(arcs)}")
print(f"valid (both halves 6-avoiding): {len(valid)}")
for arc, comp in valid:
    print("  arc  :", arc)
    print("  comp :", comp)
    print("  blocks:", sorted({blk[i] for i in arc}), "|", sorted({blk[i] for i in comp}))

# The probe's documented half
L = set([1,2,3,4,5] + list(range(16,27)))
R = set(range(N)) - L
print("\nprobe documented half L=[1..5,16..26]:")
print("  is L a contiguous size-16 arc at O?", any(set(L) == a for a, _ in arcs) or any(set(L) == c for _, c in arcs))
print("  L 6-avoiding?", not has_convex_k_subset([pts[i] for i in L], 6)[0])
print("  R 6-avoiding?", not has_convex_k_subset([pts[i] for i in R], 6)[0])