"""Step (1) of the steering directive: test the es_geom checker ALONE on sets
whose largest-convex-subset answer is known by hand, before attributing any
failure to the construction.

Hand-known cases:
  - k points on a circle  -> maxConvex = k (all in convex position)
  - triangle + one point strictly inside -> maxConvex = 3
  - 4 points in convex position -> 4
  - 4 points, one strictly inside the other 3's triangle -> 3
  - 5-point Klein configuration (the ES(5)=9 witness's inner structure)
  - points on a parabola (cup) -> all in convex position for any k
Uses only the EXACT integer/rational oracle in lib.es_geom.
"""
from lib.es_geom import (
    in_general_position, in_convex_position, largest_convex_subset,
    convex_hull,
)
import math

def circle(k, r=1000):
    return [(int(round(r*math.cos(2*math.pi*i/k))),
             int(round(r*math.sin(2*math.pi*i/k)))) for i in range(k)]

def parabola(k):
    return [(i, i*i) for i in range(k)]

def check(name, pts, want):
    gp = in_general_position(pts)
    k, wit = largest_convex_subset(pts)
    ok = (k == want)
    print(f"{name:38s} N={len(pts)} general={gp} maxConvex={k} want={want} -> "
          f"{'PASS' if ok else 'FAIL'}")

print("=== checker self-test (exact integer arithmetic, es_geom) ===")
check("circle k=4", circle(4), 4)
check("circle k=5", circle(5), 5)
check("circle k=6", circle(6), 6)
check("circle k=7", circle(7), 7)
check("parabola k=4 (4-convex cup)", parabola(4), 4)
check("parabola k=5 (5-convex cup)", parabola(5), 5)

# triangle + interior point -> 3
tri = [(0,0),(1000,0),(0,1000)]
inside = [(100,100)]
check("tri(0,0)(1000,0)(0,1000)+inside(100,100)", tri+inside, 3)

# triangle + point clearly outside -> 4 (all convex)
out = [(1000,1000)]
comb = tri+out
print("  (sanity) tri + outside point all convex:", in_convex_position(comb))

# 4 points convex vs 3+inside
sq = [(0,0),(100,0),(100,100),(0,100)]
check("square (4 convex)", sq, 4)
tri2 = [(0,0),(10,0),(0,10)]
check("tri + interior (4pts, 3 convex)", tri2+[(3,3)], 3)

# large circle k=12, k=16 -> exact maxConvex = k
check("circle k=12", circle(12), 12)
check("circle k=16", circle(16), 16)
