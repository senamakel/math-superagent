#!/usr/bin/env python3
"""
verify_final.py - Independently written second route for n=5000.

Purpose: cross-check solution.py's C(5000), S(5000), S(5000) mod 1e9 and the
distinct-prime-frame count by a SEPARATELY implemented accumulation -- nothing
is imported from solution.py/solution_power.py/frame_method.py here.  Only the
same mathematical parametrization (primary primitive quaternions + Euler-
Rodrigues + O(1) Faulhaber) is used, re-derived from scratch so a transcription
bug in the main path cannot survive.

Usage:  python3 verify_final.py
Prints the four numbers and whether each matches the accepted solution.
"""
import math
import time
from math import gcd


def euler(a, b, c, d):
    a2, b2, c2, d2 = a * a, b * b, c * c, d * d
    u = (a2 + b2 - c2 - d2, 2 * (b * c - a * d), 2 * (b * d + a * c))
    v = (2 * (b * c + a * d), a2 - b2 + c2 - d2, 2 * (c * d - a * b))
    w = (2 * (b * d - a * c), 2 * (c * d + a * b), a2 - b2 - c2 + d2)
    return u, v, w


def canon(v):
    nv = (-v[0], -v[1], -v[2])
    return v if v <= nv else nv


def g3(x, y, z):
    return gcd(gcd(abs(x), abs(y)), abs(z))


def P(k, n):
    """Faulhaber sum_{t=1}^{n} t^k, k=0..6, exact integers."""
    if k == 0:
        return n
    a = n * (n + 1)
    if k == 1:
        return a // 2
    b = a * (2 * n + 1)
    if k == 2:
        return b // 6
    if k == 3:
        return (a // 2) * (a // 2)
    if k == 4:
        return b * (3 * n * n + 3 * n - 1) // 30
    if k == 5:
        return n * n * (n + 1) ** 2 * (2 * n * n + 2 * n - 1) // 12
    return a * (2 * n + 1) * (3 * n ** 4 + 6 * n ** 3 - 3 * n + 1) // 42


def solve_indep(n):
    R = math.isqrt(n)
    C = S = 0
    nframes = 0

    def h(a, b, c, d):
        nonlocal C, S, nframes
        Nv = a * a + b * b + c * c + d * d
        if Nv == 0:
            return
        if gcd(gcd(gcd(a, b), c), d) != 1:
            return
        u, v, w = euler(a, b, c, d)
        # canonical ((sign-normalized, sorted)) frame key (unused except
        # demonstration of distinctness; the primary map is injective)
        _key = tuple(sorted([canon(u), canon(v), canon(w)]))
        nframes += 1
        ell = Nv
        A = abs(u[0]) + abs(v[0]) + abs(w[0])
        B = abs(u[1]) + abs(v[1]) + abs(w[1])
        Cc = abs(u[2]) + abs(v[2]) + abs(w[2])
        D = g3(u[0], u[1], u[2]) + g3(v[0], v[1], v[2]) + g3(w[0], w[1], w[2])
        X = n + 1
        tmax = n
        if A:
            tmax = min(tmax, n // A)
        if B:
            tmax = min(tmax, n // B)
        if Cc:
            tmax = min(tmax, n // Cc)
        if tmax <= 0:
            return
        pa = A + B + Cc
        pb = A * B + A * Cc + B * Cc
        pc = A * B * Cc
        p0 = X ** 3
        p1 = -X * X * pa
        p2 = X * pb
        p3 = -pc
        q0, q1, q2, q3 = 1, D, ell * D, ell ** 3
        c = [0] * 7
        for i, qi in enumerate((q0, q1, q2, q3)):
            for j, pj in enumerate((p0, p1, p2, p3)):
                c[i + j] += qi * pj
        Cc0 = p0 * P(0, tmax) + p1 * P(1, tmax) + p2 * P(2, tmax) + p3 * P(3, tmax)
        Sc0 = sum(c[k] * P(k, tmax) for k in range(7))
        C += Cc0
        S += Sc0

    # Case 1: a even, b,c,d odd ; d == (1-a-b-c) mod 4
    for a in range(-R, R + 1, 2):
        for b in range(-R + 1, R + 1, 2):
            for c in range(-R + 1, R + 1, 2):
                if a * a + b * b + c * c > n:
                    continue
                dr = math.isqrt(n - (a * a + b * b + c * c))
                r = (1 - a - b - c) % 4
                d0 = -dr + ((r + dr) % 4)
                for d in range(d0, dr + 1, 4):
                    h(a, b, c, d)
    # Case 2: a odd, b,c,d even ; d == (1-a-b-c) mod 4
    for a in range(-R + 1, R + 1, 2):
        for b in range(-R, R + 1, 2):
            for c in range(-R, R + 1, 2):
                if a * a + b * b + c * c > n:
                    continue
                dr = math.isqrt(n - (a * a + b * b + c * c))
                r = (1 - a - b - c) % 4
                d0 = -dr + ((r + dr) % 4)
                for d in range(d0, dr + 1, 4):
                    h(a, b, c, d)
    return C, S, nframes


if __name__ == "__main__":
    n = 5000
    t0 = time.time()
    C, S, nf = solve_indep(n)
    dt = time.time() - t0
    print(f"independent n={n}:")
    print(f"  C        = {C}")
    print(f"  S        = {S}")
    print(f"  S mod 1e9= {S % 10**9}")
    print(f"  frames   = {nf}")
    print(f"  time     = {dt:.1f}s")
    print("matches solution.py:",
          C == 70412723738165060
          and S == 197963224555524859003805524
          and S % 10**9 == 3805524
          and nf == 7598249)
