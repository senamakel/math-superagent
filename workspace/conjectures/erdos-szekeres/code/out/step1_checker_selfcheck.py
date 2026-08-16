#!/usr/bin/env python3
"""Step 1 of the steering directive: test the convex-position checker (es_geom)
alone, on sets whose largest-convex-subset is known BY HAND, before touching
the construction. If the checker is wrong here, nothing built on it is valid.

Known answers:
  * k points on a circle (no 3 collinear, e.g. regular k-gon) -> maxConvex = k
  * a triangle with one point strictly inside -> maxConvex = 3
  * a convex quadrilateral + 1 point strictly inside -> maxConvex = 4
  * 5 points with the "Klein" shape: a convex pentagon (maxConvex=5), and a
    convex quadrilateral with one point inside (maxConvex=4)
  * 3 points in convex position -> maxConvex = 3 ; 4 in convex -> 4
"""
from math import cos, sin, pi
from lib.es_geom import (
    in_general_position, largest_convex_subset, in_convex_position,
)

def circle(k):
    return [(round(100*cos(2*pi*i/k)), round(100*sin(2*pi*i/k))) for i in range(k)]

def rep(name, S, want):
    gp = in_general_position(S)
    k, wit = largest_convex_subset(S)
    ok = (gp and k == want)
    print(f"{name:45s} general={gp} maxConvex={k} want={want} -> {'OK' if ok else 'FAIL'}")

# n points on a circle
for k in (3, 4, 5, 6, 8, 12):
    rep(f"circle k={k}", circle(k), k)

# triangle with one point inside
rep("triangle + interior pt", [(0,0),(10,0),(0,10),(2,2)], 3)
rep("quad + interior pt", [(0,0),(10,0),(10,10),(0,10),(5,5)], 4)
# convex 4 / 5
rep("convex quad", [(0,0),(10,0),(10,10),(0,10)], 4)
rep("convex pentagon", [(0,0),(10,0),(12,6),(5,12),(-2,6)], 5)

# Klein 5-point shape: quadrilateral with one point inside -> maxConvex 4
rep("Klein 5 (quad+inside)", [(0,0),(10,0),(10,10),(0,10),(3,3)], 4)

# Odd/even check: 5 points with a convex 4 and a point inside, plus a 5th that
# restores a convex 5
rep("5 convex", [(0,0),(8,0),(10,6),(4,10),(-2,4)], 5)

print()
print("colinear handling (should report general=False):")
rep("3 collinear", [(0,0),(1,1),(2,2)], None)
s = [(0,0),(1,1),(2,2),(5,5)]
print("  in_general_position:", in_general_position(s), "(want False)")
