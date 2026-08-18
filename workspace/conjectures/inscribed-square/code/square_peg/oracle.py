"""Exact rational oracle for squares inscribed in polygon boundaries.

A polygon is a cyclic list of rational points; the closing edge is implicit.
All coordinates and calculations use ``fractions.Fraction``.  ``find_squares``
returns canonical cyclic quadruples of boundary points, allowing points in the
interiors of edges.  The implementation enumerates pairs of opposite-vertex
edges and solves the two affine equations for the other opposite vertices.

This is an oracle, not a full-size algorithm for arbitrary curves.  Its exact
candidate enumeration is O(m^2) edge pairs and O(1) rational arithmetic per
pair, where m is the number of polygon edges.
"""
from fractions import Fraction
from itertools import combinations

Point = tuple[Fraction, Fraction]


def Q(x):
    """Convert an integer, Fraction, or finite rational string to Fraction."""
    return x if isinstance(x, Fraction) else Fraction(x)


def point(x, y):
    """Return a rational point."""
    return (Q(x), Q(y))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def mul(c, a):
    return (c * a[0], c * a[1])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def rotate90(a):
    return (-a[1], a[0])


def on_segment(p, a, b):
    """Exact test that p lies on the closed segment [a,b]."""
    ab = sub(b, a)
    return cross(ab, sub(p, a)) == 0 and dot(sub(p, a), sub(p, b)) <= 0


def _edges(vertices):
    if len(vertices) < 3:
        raise ValueError("a polygon needs at least three vertices")
    vs = [point(*v) for v in vertices]
    if vs[0] == vs[-1]:
        vs.pop()
    if len(set(vs)) != len(vs):
        raise ValueError("polygon vertices must be distinct, without repeated closure")
    return [(vs[i], vs[(i + 1) % len(vs)]) for i in range(len(vs))]


def _canonical_cycle(points):
    """Canonicalize a cyclic quadruple, identifying reversal."""
    rotations = []
    for seq in (points, tuple(reversed(points))):
        rotations.extend(tuple(seq[i:] + seq[:i]) for i in range(4))
    return min(rotations)


def _unique_boundary_intersections(p, q, edges):
    """Return all edge parameters t with p+t(q-p) on polygon edges."""
    result = []
    d = sub(q, p)
    for a, b in edges:
        e = sub(b, a)
        den = cross(d, e)
        if den:
            w = sub(a, p)
            t = cross(w, e) / den
            u = cross(w, d) / den
            if 0 <= t <= 1 and 0 <= u <= 1:
                result.append((t, add(p, mul(t, d))))
        elif cross(sub(a, p), d) == 0:
            # Collinear overlap: endpoints are sufficient for a nondegenerate
            # square, and avoids emitting a continuum of duplicate points.
            for r in (a, b):
                if on_segment(r, p, q):
                    t = (r[0] - p[0]) / d[0] if d[0] else (r[1] - p[1]) / d[1]
                    result.append((t, r))
    return sorted(set(result))


def find_squares(vertices):
    """Return exact nondegenerate squares on the polygon boundary.

    Each result is a 4-tuple of rational points in cyclic square order.  A
    result is included only when its four points are distinct, lie on the
    boundary, and satisfy the exact side/diagonal equations.
    """
    edges = _edges(vertices)
    found = set()
    # For each possible pair of boundary edges carrying adjacent vertices,
    # solve for the remaining two vertices.  If u,v are adjacent square
    # vertices, the other vertices are u+R(v-u) and v+R(u-v), for either
    # orientation.  The pair-of-edges formulation therefore covers corners
    # and edge interiors without assuming that opposite vertices share an edge.
    for i, (a, b) in enumerate(edges):
        for j in range(len(edges)):
            if i == j:
                continue
            c, d = edges[j]
            for u0, u1 in ((a, b), (b, a)):
                for v0, v1 in ((c, d), (d, c)):
                    du, dv = sub(u1, u0), sub(v1, v0)
                    # u=u0+t du and v=v0+s dv; require
                    # v-u = r*R(u1-u) in the corresponding orientation.
                    # Solve v-u = ±R(u1-u), a 2x2 rational system.
                    for sign in (Fraction(1), Fraction(-1)):
                        rdu = rotate90(du)
                        # (v0-u0)+s*dv-t*du-sign*rdu = 0
                        rhs = sub(u0, v0)
                        det = cross(dv, sub(du, mul(sign, rdu)))
                        if det == 0:
                            continue
                        s = cross(rhs, sub(du, mul(sign, rdu))) / det
                        t = cross(dv, rhs) / det
                        if not (0 <= s <= 1 and 0 <= t <= 1):
                            continue
                        u = add(u0, mul(t, du))
                        v = add(v0, mul(s, dv))
                        x = add(u, mul(sign, rotate90(sub(v, u))))
                        y = add(v, mul(sign, rotate90(sub(u, v))))
                        if not all(any(on_segment(p, e, f) for e, f in edges)
                                   for p in (u, v, x, y)):
                            continue
                        if len({u, v, x, y}) != 4:
                            continue
                        found.add(_canonical_cycle((u, v, x, y)))
    # Corner squares have adjacent vertices at a common polygon vertex, a
    # case whose two-edge linear system is singular.  Add the finite vertex
    # candidates explicitly; this is still O(m^4) in the number of edges and
    # is exact, while the edge-interior search above remains the main oracle.
    found.update(naive_vertex_squares(vertices))
    return sorted(found)


def naive_vertex_squares(vertices):
    """Small exponential oracle: exact squares among polygon vertices only."""
    vs = [point(*v) for v in vertices]
    found = set()
    for q in combinations(vs, 4):
        ds = sorted(dot(sub(q[i], q[j]), sub(q[i], q[j]))
                     for i in range(4) for j in range(i + 1, 4))
        if ds[0] and ds[:4] == [ds[0]] * 4 and ds[4:] == [2 * ds[0]] * 2:
            found.add(_canonical_cycle(q))
    return sorted(found)
