#!/usr/bin/env python3
"""
pointcount.py — independent implementation of ONLY the lattice-point-count for
a given cube (given by its 8 integer vertices), validated on the two worked
examples in the problem statement.

Method (independently derived here):
  Choose the lexicographically-smallest vertex as corner P0.  The three edge
  vectors u,v,w from P0 to its three nearest neighbours are the edges of the
  cube; they are pairwise orthogonal with equal squared length m (these are
  verified as a sanity check).  A lattice point q is inside the CLOSED cube iff
  its affine coordinates relative to the frame (P0; u,v,w) lie in [0,1]^3.
  Because u,v,w are orthogonal with |u|^2=m, the affine coordinates are
     a = ((q-P0).u)/m, b = ((q-P0).v)/m, c = ((q-P0).w)/m
  and the exact integer condition is simply
     0 <= (q-P0).u <= m,  0 <= (q-P0).v <= m,  0 <= (q-P0).w <= m.
  (No floating point is used.)

  A lattice point is on the SURFACE (a face, edge or vertex) iff at least one
  of the three coordinates equals 0 or 1, i.e. one of the three dot products
  above equals 0 or m.  Otherwise it is strictly interior.

  We scan the integer bounding box of the 8 vertices and test each lattice
  point.  This is a deliberately naive, obviously-correct scan whose purpose
  is to validate the counting logic against the statement's worked examples.

Expected results (from the problem statement):
  Cube A: 64 total (56 surface incl. vertices + 8 interior)
  Cube B: 40 total (20 surface + 20 interior)
"""


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]


def norm2(v):
    return dot(v, v)


def count_points(vertices):
    """vertices: iterable of 8 integer triples.
    Returns (total, surface, interior)."""
    verts = list(vertices)
    assert len(verts) == 8
    P0 = min(verts)  # lexicographically smallest vertex is a corner

    # find the 3 edge-neighbours of P0 (the three vertices nearest to it)
    dsq = []
    for q in verts:
        if q == P0:
            continue
        d = sum((a - b) ** 2 for a, b in zip(q, P0))
        dsq.append((d, q))
    dsq.sort()
    m = dsq[0][0]  # squared edge length
    edges = [tuple(q[i] - P0[i] for i in range(3)) for (d, q) in dsq if d == m]
    assert len(edges) == 3, (verts, edges)
    u, v, w = edges

    # sanity: an actual cube's edges are pairwise orthogonal with equal norm
    assert abs(norm2(u) - m) == 0
    assert norm2(v) == m and norm2(w) == m
    assert dot(u, v) == 0 and dot(u, w) == 0 and dot(v, w) == 0

    xs = [p[0] for p in verts]
    ys = [p[1] for p in verts]
    zs = [p[2] for p in verts]

    total = 0
    surface = 0
    for x in range(min(xs), max(xs) + 1):
        for y in range(min(ys), max(ys) + 1):
            for z in range(min(zs), max(zs) + 1):
                q = (x - P0[0], y - P0[1], z - P0[2])
                a = dot(q, u)   # = m * affine coordinated
                b = dot(q, v)
                c = dot(q, w)
                if 0 <= a <= m and 0 <= b <= m and 0 <= c <= m:
                    total += 1
                    if a == 0 or a == m or b == 0 or b == m or c == 0 or c == m:
                        surface += 1
    return total, surface, total - surface


def main():
    cubeA = [(0,0,0),(3,0,0),(0,3,0),(0,0,3),(0,3,3),(3,0,3),(3,3,0),(3,3,3)]
    cubeB = [(0,2,2),(1,4,4),(2,0,3),(2,3,0),(3,2,5),(3,5,2),(4,1,1),(5,3,3)]

    for name, cube, exp_total, exp_surf, exp_int in [
            ("A", cubeA, 64, 56, 8),
            ("B", cubeB, 40, 20, 20)]:
        t, s, i = count_points(cube)
        ok = (t == exp_total and s == exp_surf and i == exp_int)
        print(f"Cube {name}: total={t} surface={s} interior={i}"
              f"  expected total={exp_total} surf={exp_surf} int={exp_int}"
              f"  -> {'OK' if ok else 'MISMATCH'}")


if __name__ == "__main__":
    main()
