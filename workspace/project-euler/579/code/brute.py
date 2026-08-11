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
    w = (u x v) / k with k^2 = m is an integer vector.  For any genuine
    lattice cube m = |u|^2 is a perfect square m = k^2 and u x v = +-k*w, so
    we only consider square m and require k to divide u x v componentwise.

For every corner P0 in [0,n]^3 and every frame (u,v,w) we build the 8 vertice
and keep the frozenset of those vertices as the cube identity.  Frozenset
deduplication collapses the same geometric cube found via different corners,
edge orderings and sign choices.  Counting distinct frozensets = C(n).

For S(n): for each distinct cube, count lattice points q contained in the
closed cube (exact integer test from toolkit.count_points, no floats).

Usage:  python brute.py [n1 n2 ...]
Writes output to /workspace/brute_output.txt and prints it.
"""

import sys
from collections import defaultdict

from toolkit import count_points, dot, norm2

ORACLE_C = {1: 1, 2: 9, 4: 100, 5: 229, 10: 4469, 50: 8154671}
ORACLE_S = {1: 8, 2: 91, 4: 1878, 5: 5832, 10: 387003, 50: 29948928129}


def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0])


def isqrt(n):
    x = int(round(n ** 0.5))
    while x * x > n:
        x -= 1
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x


def build_frames(n):
    """Return all frames (u,v,w): |u|^2=|v|^2=|w|^2=m>0, pairwise orthogonal.

    For a genuine lattice cube m = |u|^2 is a perfect square (m = k^2), because
    w is parallel to u x v and u x v = +-k*w (since |u x v| = m = k^2 = k|w|),
    forcing k = (u x v)_i / w_i to be rational, hence an integer.  So we only
    consider square m and take w = (u x v)/k."""
    vecs = [(x, y, z) for x in range(-n, n + 1)
            for y in range(-n, n + 1) for z in range(-n, n + 1)]
    bynorm = defaultdict(list)
    for v in vecs:
        m = norm2(v)
        if m > 0:
            bynorm[m].append(v)

    frames = set()
    for m, vl in bynorm.items():
        k = isqrt(m)
        if k * k != m:
            continue  # not a perfect square: cannot be a lattice cube's edge
        for u in vl:
            for v in vl:
                if dot(u, v) == 0:
                    cx, cy, cz = cross(u, v)
                    if cx % k == 0 and cy % k == 0 and cz % k == 0:
                        w = (cx // k, cy // k, cz // k)
                        # sanity: w must have norm m and be orthogonal
                        assert norm2(w) == m, (u, v, w, m)
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
    S = sum(count_points(cube)[0] for cube in cubes)
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
