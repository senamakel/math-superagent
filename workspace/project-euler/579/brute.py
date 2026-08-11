#!/usr/bin/env python3
"""
brute.py — naive but obviously-correct brute force for the "lattice cube"
counting problem (Project Euler 579).

A cube is determined by an integer corner P0 in Z^3 and three pairwise
orthogonal, equal-norm integer edge vectors u,v,w (|u|^2=|v|^2=|w|^2 = m).
Its 8 vertices are P0 + s1*u + s2*v + s3*w with s_i in {0,1}.

We enumerate:
  * every integer vector with each coordinate in [-n, n]  (a valid bound:
    any edge-vector coordinate has |u_c| <= n because the two vertices
    P0 and P0+u both lie in [0,n]^3),
  * every pair (u,v) with equal norm and u dot v = 0, where the third edge
    w = (u x v) / m is an integer vector (i.e. m divides u x v componentwise;
    this holds automatically for any genuine lattice cube).

For every corner P0 in [0,n]^3 and every frame (u,v,w) we build the 8 vertice
and keep the frozenset of those vertices as the cube identity.  Frozenset
deduplication collapses the same geometric cube found via different corners,
edge orderings and sign choices.  Counting distinct frozensets = C(n).

For S(n): for each distinct cube, count lattice points q contained in the
closed cube.  With P0 a corner and u,v,w the three edge vectors from it to its
neighbours, q is in the cube iff its affine coordinates satisfy
0 <= a,b,c <= 1.  Since u,v,w are orthogonal with |u|^2=m, we have
a = ((q-P0).u)/m exactly (integer arithmetic), and the exact integer test is
    0 <= (q-P0).u <= m   and  0 <= (q-P0).v <= m   and  0 <= (q-P0).w <= m.
This needs no floats.

Usage:  python brute.py [n1 n2 ...]
Writes output to /workspace/brute_output.txt and prints it.
"""

import sys
from collections import defaultdict

ORACLE_C = {1: 1, 2: 9, 4: 100, 5: 229, 10: 4469, 50: 8154671}
ORACLE_S = {1: 8, 2: 91, 4: 1878, 5: 5832, 10: 387003, 50: 29948928129}


def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0])


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]


def norm2(v):
    return dot(v, v)


def build_frames(n):
    """Return the set of all frames (u,v,w) whose 8 unit-cube offsets are
    integer triples each coordinate in [-n,n] and |u|^2=|v|^2=|w|^2=m>0,
    u.v=u.w=v.w=0."""
    vecs = [(x, y, z) for x in range(-n, n + 1)
            for y in range(-n, n + 1) for z in range(-n, n + 1)]
    bynorm = defaultdict(list)
    for v in vecs:
        m = norm2(v)
        if m > 0:
            bynorm[m].append(v)

    frames = set()
    for m, vl in bynorm.items():
        for u in vl:
            for v in vl:
                if dot(u, v) == 0:
                    cx, cy, cz = cross(u, v)
                    if cx % m == 0 and cy % m == 0 and cz % m == 0:
                        w = (cx // m, cy // m, cz // m)
                        # sanity: w must have norm m and be orthogonal
                        assert norm2(w) == m
                        assert dot(u, w) == 0 and dot(v, w) == 0
                        # include both w and -w sign (both valid cubes)
                        frames.add((u, v, w))
                        frames.add((u, v, (-w[0], -w[1], -w[2])))
    return frames


def offset_vertices(u, v, w):
    """8 vertex offsets s1*u+s2*v+s3*w for s_i in {0,1}."""
    offs = []
    for s1 in (0, 1):
        for s2 in (0, 1):
            for s3 in (0, 1):
                offs.append((s1 * u[0] + s2 * v[0] + s3 * w[0],
                             s1 * u[1] + s2 * v[1] + s3 * w[1],
                             s1 * u[2] + s2 * v[2] + s3 * w[2]))
    return offs


def corner_and_edges(vertex_set):
    """Given a frozenset of 8 vertices, return (P0, [u,v,w]) where P0 is the
    lexicographically smallest vertex (a corner) and u,v,w are the three edge
    vectors from P0 to its three nearest neighbours."""
    verts = list(vertex_set)
    P0 = min(verts)
    dsq = []
    for q in verts:
        if q == P0:
            continue
        d = sum((a - b) ** 2 for a, b in zip(q, P0))
        dsq.append((d, q))
    dsq.sort()
    m = dsq[0][0]  # edge length squared
    edges = [tuple(q[i] - P0[i] for i in range(3))
             for (d, q) in dsq if d == m]
    assert len(edges) == 3, (vertex_set, edges)
    return P0, edges


def count_points_in_cube(vertex_set):
    """Exact number of lattice points in the closed cube, plus boundary count.
    Boundary = point lying on a face (edge/vertex included); interior =
    strictly inside.  Returns (total, boundary)."""
    P0, (u, v, w) = corner_and_edges(vertex_set)
    m = norm2(u)
    assert norm2(v) == m and norm2(w) == m
    assert dot(u, v) == 0 and dot(u, w) == 0 and dot(v, w) == 0

    xs = [p[0] for p in vertex_set]
    ys = [p[1] for p in vertex_set]
    zs = [p[2] for p in vertex_set]

    total = 0
    boundary = 0
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
                        boundary += 1
    return total, boundary


def compute(n):
    """Return (C(n), S(n))."""
    frames = build_frames(n)
    Ps = [(x, y, z) for x in range(n + 1)
          for y in range(n + 1) for z in range(n + 1)]

    cubes = set()
    # cache per-frame offsets to avoid rebuilding
    for (u, v, w) in frames:
        offs = offset_vertices(u, v, w)
        for P in Ps:
            ok = True
            pts = []
            for o in offs:
                x = P[0] + o[0]; y = P[1] + o[1]; z = P[2] + o[2]
                if not (0 <= x <= n and 0 <= y <= n and 0 <= z <= n):
                    ok = False
                    break
                pts.append((x, y, z))
            if ok:
                cubes.add(frozenset(pts))

    C = len(cubes)
    S = 0
    for cube in cubes:
        t, _ = count_points_in_cube(cube)
        S += t
    return C, S


def main():
    ns = [int(a) for a in sys.argv[1:]] or [1, 2, 3, 4, 5, 6, 10]
    lines = []
    for n in ns:
        C, S = compute(n)
        line = (f"n={n}: C(n)={C}  S(n)={S}")
        if n in ORACLE_C:
            mc = "OK" if C == ORACLE_C[n] else "MISMATCH"
            ms = "OK" if S == ORACLE_S[n] else "MISMATCH"
            line += f"   [C oracle {ORACLE_C[n]}: {mc}]  [S oracle {ORACLE_S[n]}: {ms}]"
        print(line)
        lines.append(line)
    with open("/workspace/brute_output.txt", "w") as f:
        f.write("\n".join(lines) + "\n")
    print("Wrote /workspace/brute_output.txt")


if __name__ == "__main__":
    main()
