#!/usr/bin/env python3
"""
frame_method.py - Validate the efficient frame-based method for PE 579.

Key idea (see memory.md / research notes):
  Every lattice cube factors uniquely as (primitive frame) x (integer scale t):
    a cube has edge vectors (u,v,w), pairwise orthogonal, |u|^2=|v|^2=|w|^2=ell^2,
    with gcd of all 9 coordinates equal to g.  Dividing by g gives the primitive
    frame (u0,v0,w0) (gcd of its 9 coords = 1) and scale t = g.

  For a fixed primitive frame the scaled cube (by t) has:
    - edge length  ell * t  where ell = primitive edge length,
    - x/y/z coordinate spans  t*A, t*B, t*C  where
        A=sum of |x| coords, B=sum of |y| coords, C=sum of |z| coords,
    - Ehrhart lattice-point count (Ionascu Thm 3.1) of the t-dilated cube:
        pts(t) = ell^3 t^3 + ell*D t^2 + D*t + 1,
      where D = sum of the three edge-gcds of the primitive frame.

  For a box [0,n]^3 the scaled cube fits iff t*A<=n, t*B<=n, t*C<=n, and the number
  of corner placements is T(t) = (n+1-tA)(n+1-tB)(n+1-tC).

  Then
    C-contribution = sum_{t=1..tmax} T(t)
    S-contribution = sum_{t=1..tmax} pts(t)*T(t)
  and C(n)=sum over distinct primitive frames of C-contribution, S(n) likewise.

This file enumerates primitive frames by the direct dependence
  u over integer vectors (coords in [-n,n], 1<=|u|^2<=n^2)
  v over vectors with same norm and u dot v = 0
  w = (u x v) / ell   (ell=isqrt(norm)), require w integer, |w|^2=norm, gcd(all 9)==1
then dedupes via a canonical (sign+permutation invariant) key.

Usage:  python3 frame_method.py
Writes stdout to /workspace/frame_method_output.txt and prints it.
"""
import math
import sys
import time


def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0])


def isqrt(n):
    x = math.isqrt(n)
    return x


def signed_canon(v):
    """Canonical sign representative of a nonzero vector up to negation."""
    nv = (-v[0], -v[1], -v[2])
    return v if v <= nv else nv


def canonical_key(u, v, w):
    """Frame identity up to permutation + independent sign flips of the 3 edges."""
    return tuple(sorted([signed_canon(u), signed_canon(v), signed_canon(w)]))


def gcd3(a, b, c):
    return math.gcd(math.gcd(abs(a), abs(b)), abs(c))


def enumerate_primitive_frames(n):
    """Return dict canon_key -> (ell, A, B, C, D) for every distinct primitive frame.

    ell = primitive edge length (isqrt of common norm).
    A,B,C = sums of |x|,|y|,|z| coordinates over the 3 edges.
    D = sum of edge-gcds.
    """
    vecs = [(x, y, z)
            for x in range(-n, n + 1)
            for y in range(-n, n + 1)
            for z in range(-n, n + 1)]
    bynorm = {}
    for v in vecs:
        m = v[0] * v[0] + v[1] * v[1] + v[2] * v[2]
        if m >= 1 and m <= n * n:
            bynorm.setdefault(m, []).append(v)

    out = {}
    for m, group in bynorm.items():
        ell = isqrt(m)
        if ell * ell != m:
            continue  # not a perfect square: cannot be a lattice cube's edge
        for u in group:
            for v in group:
                if u[0] * v[0] + u[1] * v[1] + u[2] * v[2] != 0:
                    continue
                cx, cy, cz = cross(u, v)
                if cx % ell or cy % ell or cz % ell:
                    continue
                w = (cx // ell, cy // ell, cz // ell)
                if w[0] * w[0] + w[1] * w[1] + w[2] * w[2] != m:
                    continue
                # primitive: gcd of all 9 coordinates must be 1
                g = 0
                for cc in (u[0], u[1], u[2], v[0], v[1], v[2], w[0], w[1], w[2]):
                    g = math.gcd(g, cc)
                if g != 1:
                    continue
                key = canonical_key(u, v, w)
                if key in out:
                    continue
                A = abs(u[0]) + abs(v[0]) + abs(w[0])
                B = abs(u[1]) + abs(v[1]) + abs(w[1])
                C = abs(u[2]) + abs(v[2]) + abs(w[2])
                D = (gcd3(u[0], u[1], u[2])
                     + gcd3(v[0], v[1], v[2])
                     + gcd3(w[0], w[1], w[2]))
                out[key] = (ell, A, B, C, D)
    return out


def enumerate_primitive_frames_lean(n):
    """Memory-leaner version: only group vectors by norm (no extra vecs list).
    Same return as enumerate_primitive_frames."""
    bynorm = {}
    for x in range(-n, n + 1):
        for y in range(-n, n + 1):
            for z in range(-n, n + 1):
                m = x * x + y * y + z * z
                if 1 <= m <= n * n:
                    bynorm.setdefault(m, []).append((x, y, z))

    out = {}
    for m, group in bynorm.items():
        ell = isqrt(m)
        if ell * ell != m:
            continue
        for u in group:
            for v in group:
                if u[0] * v[0] + u[1] * v[1] + u[2] * v[2] != 0:
                    continue
                cx, cy, cz = cross(u, v)
                if cx % ell or cy % ell or cz % ell:
                    continue
                w = (cx // ell, cy // ell, cz // ell)
                if w[0] * w[0] + w[1] * w[1] + w[2] * w[2] != m:
                    continue
                g = 0
                for cc in (u[0], u[1], u[2], v[0], v[1], v[2], w[0], w[1], w[2]):
                    g = math.gcd(g, cc)
                if g != 1:
                    continue
                key = canonical_key(u, v, w)
                if key in out:
                    continue
                A = abs(u[0]) + abs(v[0]) + abs(w[0])
                B = abs(u[1]) + abs(v[1]) + abs(w[1])
                C = abs(u[2]) + abs(v[2]) + abs(w[2])
                D = (gcd3(u[0], u[1], u[2])
                     + gcd3(v[0], v[1], v[2])
                     + gcd3(w[0], w[1], w[2]))
                out[key] = (ell, A, B, C, D)
    return out


def compute(n, frames):
    """Return (C(n), S(n)) from the primitive-frame dict."""
    C = 0
    S = 0
    for (ell, A, B, Cc, D) in frames.values():
        # tmax: largest integer t with t*A<=n, t*B<=n, t*C<=n
        tmax = n
        if A > 0:
            tmax = min(tmax, n // A)
        if B > 0:
            tmax = min(tmax, n // B)
        if Cc > 0:
            tmax = min(tmax, n // Cc)
        if tmax <= 0:
            continue
        # accumulate (loop t; fine for feasibility experiment)
        ccount = 0
        scount = 0
        for t in range(1, tmax + 1):
            tx = n + 1 - t * A
            ty = n + 1 - t * B
            tz = n + 1 - t * Cc
            T = tx * ty * tz
            if T <= 0:
                break
            pts = ell ** 3 * t ** 3 + ell * D * t * t + D * t + 1
            ccount += T
            scount += pts * T
        C += ccount
        S += scount
    return C, S


ORACLE_C = {1: 1, 2: 9, 4: 100, 5: 229, 10: 4469, 50: 8154671}
ORACLE_S = {1: 8, 2: 91, 4: 1878, 5: 5832, 10: 387003, 50: 29948928129}


def main():
    lines = []

    verify_ns = [1, 2, 4, 5, 10, 50]
    frame_counts = {}
    for n in verify_ns:
        t0 = time.time()
        frames = enumerate_primitive_frames(n)
        t_frames = time.time() - t0
        frame_counts[n] = len(frames)
        t1 = time.time()
        C, S = compute(n, frames)
        t_total = time.time() - t0
        mc = "OK" if (n in ORACLE_C and C == ORACLE_C[n]) else "?"
        ms = "OK" if (n in ORACLE_S and S == ORACLE_S[n]) else "?"
        line = (f"n={n:>3}: C={C:<12} S={S:<16} "
                f"primitives={len(frames):<6} "
                f"[C {mc}] [S {ms}]  wall={t_total:.2f}s (frames {t_frames:.2f}s)")
        print(line)
        lines.append(line)

    # growth data
    growth_ns = [20, 100, 200]
    for n in growth_ns:
        if n in frame_counts:
            continue
        t0 = time.time()
        try:
            frames = enumerate_primitive_frames_lean(n)
            wall = time.time() - t0
            frame_counts[n] = len(frames)
            line = (f"growth n={n:>3}: distinct_primitive_frames={len(frames):<8} "
                    f"wall={wall:.2f}s")
        except MemoryError:
            line = f"growth n={n:>3}: MemoryError (aborted)"
        print(line)
        lines.append(line)

    with open("/workspace/frame_method_output.txt", "w") as f:
        f.write("\n".join(lines) + "\n")
    print("Wrote /workspace/frame_method_output.txt")


if __name__ == "__main__":
    main()
