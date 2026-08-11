"""Reusable helpers for Project Euler 579 (lattice cubes)."""


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]


def norm2(v):
    return dot(v, v)


def corner_and_edges(vertex_set):
    """Given a frozenset/list of the 8 integer vertices of a cube, return
    (P0, [u, v, w]) where P0 is the lexicographically smallest vertex and
    u,v,w are the three unit-cube edge vectors from P0 to its three nearest
    neighbours (each to a vertex at squared distance m = edge length^2)."""
    verts = list(vertex_set)
    P0 = min(verts)
    dsq = []
    for q in verts:
        if q == P0:
            continue
        d = sum((a - b) ** 2 for a, b in zip(q, P0))
        dsq.append((d, q))
    dsq.sort()
    m = dsq[0][0]
    edges = [tuple(q[i] - P0[i] for i in range(3))
             for (d, q) in dsq if d == m]
    assert len(edges) == 3
    return P0, edges


def count_points(vertex_set):
    """Exact lattice-point count in the closed cube: returns (total, surface).

    For a cube with corner P0 and pairwise-orthogonal equal-norm edge vectors
    u,v,w (|u|^2=|v|^2=|w|^2=m), a lattice point q is inside the closed cube
    iff its affine coordinates are in [0,1]^3, i.e. exactly
        0 <= (q-P0).u <= m  and  0 <= (q-P0).v <= m  and  0 <= (q-P0).w <= m.
    It is on the surface iff at least one of those dot products equals 0 or m.
    All-integer arithmetic.  Scans the integer bounding box of the vertices.

    Verified against the statement's two worked cubes.  See pointcount.py."""
    P0, (u, v, w) = corner_and_edges(vertex_set)
    m = norm2(u)
    assert norm2(v) == m and norm2(w) == m
    assert dot(u, v) == 0 and dot(u, w) == 0 and dot(v, w) == 0

    xs = [p[0] for p in vertex_set]
    ys = [p[1] for p in vertex_set]
    zs = [p[2] for p in vertex_set]

    total = 0
    surface = 0
    for x in range(min(xs), max(xs) + 1):
        for y in range(min(ys), max(ys) + 1):
            for z in range(min(zs), max(zs) + 1):
                q = (x - P0[0], y - P0[1], z - P0[2])
                a = dot(q, u)
                b = dot(q, v)
                c = dot(q, w)
                if 0 <= a <= m and 0 <= b <= m and 0 <= c <= m:
                    total += 1
                    if a == 0 or a == m or b == 0 or b == m or c == 0 or c == m:
                        surface += 1
    return total, surface
