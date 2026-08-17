#!/usr/bin/env python3
from fractions import Fraction
from lib.es_construct import es_set_blocks
from lib.es_geom import orient, in_general_position

n = 7
pts, blocks = es_set_blocks(n)
N = len(pts)
print("N =", N)
xs = [p[0] for p in pts]
ys = [p[1] for p in pts]
print("x range:", min(xs), max(xs))
print("y range:", min(ys), max(ys))
print("distinct x count:", len(set(xs)))
print("distinct y count:", len(set(ys)))
print("block sizes:", [len(b) for b in blocks])
print("general position of set:", in_general_position(pts))
# sample points
print("first 8 pts:", pts[:8])

# witness
W = (Fraction(2400), Fraction(2725))

def apex_general(points, O):
    for a in range(N):
        for b in range(a + 1, N):
            if orient(O, points[a], points[b]) == 0:
                return False
    return True

print("apex_general(witness):", apex_general(pts, W))
