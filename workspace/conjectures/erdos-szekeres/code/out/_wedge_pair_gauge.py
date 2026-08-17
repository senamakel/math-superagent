#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from lib.es_construct import es_set_blocks
from lib.es_geom import orient

def ordered_pair_sides(points):
    N = len(points)
    res = set()
    for a in range(N):
        for b in range(N):
            if a == b:
                continue
            strict = frozenset(x for x in range(N)
                               if orient(points[a], points[b], points[x]) > 0)
            for extra in (frozenset(), frozenset([a]), frozenset([b]),
                          frozenset([a, b])):
                side = strict | extra
                if 0 < len(side) < N:
                    res.add(side)
    return res

n = 7
pts, blocks = es_set_blocks(n)
N = len(pts)
target = 2 ** (n - 3)   # 16
full = frozenset(range(N))

sides = sorted(ordered_pair_sides(pts), key=lambda s: (len(s), sorted(s)))
print("num sides:", len(sides), "N(N-1)=", N*(N-1))

L = frozenset([1, 2, 3, 4, 5] + list(range(16, 27)))
R = frozenset([0] + list(range(6, 16)) + list(range(27, 32)))
assert len(L) == 16 and len(R) == 16 and L | R == full and L & R == frozenset()
witness_bip = frozenset((L, R))

size16_pairs = 0
splits = set()
witness_seen = False
npairs = len(sides)*(len(sides)-1)//2
for s1, s2 in combinations(sides, 2):
    inter = s1 & s2
    if len(inter) == target:
        size16_pairs += 1
        comp = full - inter
        if frozenset((inter, comp)) == witness_bip:
            witness_seen = True
        splits.add(frozenset((inter, comp)))
print("pairs of sides:", npairs)
print("pairs with |inter|=16:", size16_pairs)
print("distinct size-16 splits:", len(splits))
print("witness bipartition appears among intersections:", witness_seen)
