"""Exact check of the rank-3 / planar circuit premise behind the
'radon-circuit-no-radon-4set' approach.

Claim tested (the approach's mechanism): "4 points are NOT in convex position
iff ... a dependent (circuit) set of size 4 in the rank-3 oriented matroid." And
"a set is convex iff it contains no circuit 4-subset" / "no convex n-gon
iff every n-subset contains a circuit 4-subset."

The point of this program: in the PLANE (rank-3 affine geometry), every 4 points
in general position are AFFINELY DEPENDENT => every 4-set is a circuit. The
distinction convex/non-convex is NOT circuit-membership (all 4-sets are
circuits) but the SIGNING / Radon partition type (1+3 vs 2+2). We verify this
exactly on a convex quadrilateral and on a non-convex (one point inside
triangle) 4-set: both are affinely dependent with no 3 collinear.
"""
import itertools

def det3(a, b, c):
    """2x boxed affine dependence: sign of the 3x3 determinant (ax,ay,1) etc."""
    (ax, ay), (bx, by), (cx, cy) = a, b, c
    return ax*(by - cy) - ay*(bx - cx) + (bx*cy - by*cx)

def in_general_position(pts):
    for tri in itertools.combinations(pts, 3):
        if det3(*tri) == 0:
            return False
    return True

def affine_dependent(pts):
    """4 points in the plane are affinely dependent iff the 3x4 incidence matrix
    has rank <= 3; since we work with homogeneous coords (x,y,1), 4 points in R^2
    are ALWAYS affinely dependent iff the 4x4 determinant of (x,y,1) rows is 0.
    Compute via the 4x4 determinant of lifted points."""
    # lifted rows (x, y, 1)
    rows = [(x, y, 1) for (x, y) in pts]
    # 4x4 determinant, exact
    a, b, c, d = rows
    def det4(r0, r1, r2, r3):
        # expand along first row
        val = 0
        for i in range(4):
            # minor 3x3
            rows_ = [r for j, r in enumerate([r0, r1, r2, r3]) if j != i]
            m = rows_[0][0]*(rows_[1][1]*rows_[2][2]-rows_[1][2]*rows_[2][1]) \
              - rows_[0][1]*(rows_[1][0]*rows_[2][2]-rows_[1][2]*rows_[2][0]) \
              + rows_[0][2]*(rows_[1][0]*rows_[2][1]-rows_[1][1]*rows_[2][0])
            sign = (-1)**i
            val += sign * r0[i] * m
        return val
    return det4(a, b, c, d) == 0

def is_convex_quad(pts):
    """4 pts (in the cyclic labeling) form a convex quadrilateral iff the four
    orientation signs are all the same (all CCW or all CW) for the cyclic tour."""
    n = len(pts)
    signs = []
    for i in range(n):
        s = det3(pts[i], pts[(i+1) % n], pts[(i+2) % n])
        signs.append(1 if s > 0 else (-1 if s < 0 else 0))
    return all(s > 0 for s in signs) or all(s < 0 for s in signs)

# A convex quadrilateral (square, no 3 collinear)
convex = [(0, 0), (4, 0), (4, 4), (0, 4)]
# A non-convex 4-set: one point inside the triangle of the other three
nonconvex = [(0, 0), (4, 0), (2, 4), (2, 1)]   # (2,1) inside triangle 0,0-4,0-2,4
# A set of 3 points (not a circuit individually)
three = [(0, 0), (1, 0), (0, 1)]

for name, pts in [("convex quad", convex), ("non-convex 4-set", nonconvex)]:
    gp = in_general_position(pts)
    dep = affine_dependent(pts)
    cq = is_convex_quad(pts)
    print(f"{name}: general_position={gp}, affinely_dependent(circuit)={dep}, "
          f"convex_quad={cq}")

# Every 4-subset of every general-position set of size 5..7 (random) is a circuit
import random
def rand_set(n, scale=100):
    pts = []
    while len(pts) < n:
        p = (random.randint(0, scale), random.randint(0, scale))
        if all(det3(p, q, r) != 0 for q, r in itertools.combinations(pts, 2)) and \
           all(det3(q, p, r) != 0 for q in pts for r in pts):
            if all(det3(p, q, r) != 0 for q in pts for r in pts):
                pts.append(p)
    return pts

random.seed(1)
for n in [5, 6, 7]:
    for trial in range(5):
        pts = rand_set(n)
        circuits = 0
        for quad in itertools.combinations(pts, 4):
            if affine_dependent(quad):
                circuits += 1
        # every 4-subset should be a circuit in rank 3
        assert circuits == len(list(itertools.combinations(pts, 4))), (n, circuits)
    print(f"n={n}: every 4-subset is affinely dependent (a circuit) in rank 3 "
          f"-- confirmed exact.")
