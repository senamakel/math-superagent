"""Refutation probe for R-k-interior at n=5, k=5.

Statement: every set of 2^{3}+1 = 9 points in general position with at most
5 interior points contains a convex pentagon.  Trivial hull-count argument
holds for k<=4 (hull has >=5 vertices); the first nontrivial instance is
exactly 5 interior points -> hull is a convex quadrilateral, need a convex
pentagon among the 9.

We test: does there exist a 9-point general-position set with a convex
quadrilateral hull (5 interior points) whose largest convex subset is only 4
(no convex pentagon)?  Use exact arithmetic via lib.es_geom.  Random exact-
rational search with perturbation to avoid collinearities.
"""
import sys, random
from itertools import combinations
sys.path.insert(0, "/workspace/code")
from lib.es_geom import in_general_position, convex_hull, in_convex_position, largest_convex_subset

def interior_count(points):
    hull = convex_hull(points)
    return len(points) - len(hull)

def try_hull_then_interior(A, B, C, D, inner):
    """Check inner as interior points of quadrilateral hull ABCD."""
    pts = [A, B, C, D] + inner
    if not in_general_position(pts):
        return None
    h = convex_hull(pts)
    if len(h) != 4:
        return None
    ic = interior_count(pts)
    if ic != 5:
        return None
    k, witness = largest_convex_subset(pts)
    return k, witness

def centered(scale=1.0):
    """A=(0,s),(s,0),(0,-s),(-s,0); inner points near center, random rational."""
    from fractions import Fraction as F
    def rnd():
        return F(random.randint(-3*scale, 3*scale), 100*scale)
    A = (F(0), F(10*scale))
    B = (F(10*scale), F(0))
    C = (F(0), F(-10*scale))
    D = (F(-10*scale), F(0))
    inner = []
    for _ in range(5):
        inner.append((rnd(), rnd()))
    return A, B, C, D, inner

def random_quad():
    from fractions import Fraction as F
    # random convex quadrilateral + 5 interior random points
    pts = []
    for _ in range(9):
        pts.append((F(random.randint(-30, 30)), F(random.randint(-30, 30))))
    # force a broad-hulled one later
    return pts

def main():
    random.seed(12345)
    best = None
    hits = 0
    for trial in range(20000):
        A, B, C, D, inner = centered(1.0)
        r = try_hull_then_interior(A, B, C, D, inner)
        if r is None:
            continue
        k, w = r
        if k < 5:
            hits += 1
            pts = [A, B, C, D] + inner
            print("COUNTEREXAMPLE (largest convex =", k, ") hull quad, 5 interior:")
            for p in pts:
                print("   ", float(p[0]), float(p[1]))
            if best is None or k < best[0]:
                best = (k, pts)
            if hits >= 5:
                break
    print("hits (no convex pentagon) :", hits)
    if best is not None:
        print("best largest-convex found:", best[0])
        # verify exact
        pts = best[1]
        h = convex_hull(pts)
        print("hull:", [ (float(p[0]),float(p[1])) for p in h ])
        print("interior count:", interior_count(pts))
        print("general position:", in_general_position(pts))
        print("largest convex subset:", largest_convex_subset(pts))
    else:
        print("no counterexample found in 20000 trials")

if __name__ == "__main__":
    main()
