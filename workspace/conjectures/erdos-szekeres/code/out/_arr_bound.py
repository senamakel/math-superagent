from fractions import Fraction
from itertools import combinations
from lib.es_construct import es_set_blocks

pts, blocks = es_set_blocks(7)
N = len(pts)
# pair-lines
L = N * (N - 1) // 2
print("points N =", N, " pair-lines L =", L)

# triples of points: count concurrent triple concurrences (3 pair-lines through
# one point=the third's pair).  For arrangement cell count, general position
# of arrangement means no 3 lines concurrent, no 2 lines parallel.
# Count triples of points collinear (should be 0, general position).
coll = 0
for (i, j, k) in combinations(range(N), 3):
    from lib.es_geom import orient
    if orient(pts[i], pts[j], pts[k]) == 0:
        coll += 1
print("collinear point-triples:", coll)

# check for parallel pair-lines (same slope)
slopes = {}
def red(x, y):
    from math import gcd
    g = gcd(x, y)
    return (x // g, y // g)
for (a, b) in combinations(range(N), 2):
    dx = pts[a][0] - pts[b][0]
    dy = pts[a][1] - pts[b][1]
    if dx == 0:
        s = None
    elif dx < 0:
        dx, dy = -dx, -dy
        s = (dy, dx)
    else:
        s = (dy, dx)
    slopes[s] = slopes.get(s, 0) + 1
parallel_groups = sum(1 for s, c in slopes.items() if c > 1)
print("parallel pair-line groups (same slope appearing >1 times):", parallel_groups)

# three pair-lines concurrent at a common point => at least 3 lines through
# one interior intersection.  Generic arrangement: no 3 concurrent.
# Count pairwise-distinct intersection points that are shared by 3+ lines.
# A 3-line concurrence happens iff an intersection of two pair-lines lies on
# a third pair-line, i.e. 4 points with a cross-intersection point.  Hard to
# count cheaply for L=496; note it as a nonlinear realizable-grid situation.
print("L(L+1)/2+1 (generic arrangement region bound) =", L * (L + 1) // 2 + 1)
