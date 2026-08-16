"""Radial unit-circle ES construction, exact-oracle verified.

ROOT.md Theorem 2.6 (Morris-Soltan / ES61): place a small copy of each
T_i (|T_i| = C(n-2,i), no (i+2)-cap, no (n-i)-cup) in a neighbourhood of the
unit-circle point at angle theta_i = pi/4 - i*pi/(2(n-2)).  Blocks at distinct
angles, scaled tiny.  Interior blocks then contribute <=1 point to any convex
subset, so largest convex subset <= n-1.

All coordinates exact rationals.  Scaling/translation by integer-free rationals
kept as Fraction.  cos/sin at these angles are algebraic; to keep EXACT rational
coordinates I instead place the blocks on a parabola scaled huge and spread
apart (a strictly convex arc with rational points), OR use rational end-points.
For exactness use the exact-rational parabola arc but verify; if collinearity
arises, fall back to circle with rational approximations is NOT exact.
"""
import math
from fractions import Fraction
from lib.es_geom import largest_convex_subset, in_general_position
from lib.es_lower import g as block_g, _flatten


def radial_circle(n, eps=Fraction(1, 10 ** 4)):
    """Blocks on exact unit circle: but cos/sin are irrational -> coordinates
    would be floats.  This is a *search* probe only (floating point) to check
    the geometry's validity; the exact-oracle check below uses integer pts."""
    blocks = []
    for i in range(n - 1):
        T = block_g(i + 2, n - i)
        if i == 0 or i == n - 2:
            T = [(Fraction(0), Fraction(0))]
        else:
            T = _flatten(T, Fraction(1, 20))
        blocks.append(T)
    out = []
    for i, T in enumerate(blocks):
        th = math.pi / 4 - i * math.pi / (2 * (n - 2))
        cx, cy = math.cos(th), math.sin(th)
        tx, ty = -math.sin(th), math.cos(th)     # tangent
        nx, ny = math.cos(th), math.sin(th)      # normal
        for (px, py) in T:
            x = cx + float(eps) * (float(px) * tx + float(py) * nx)
            y = cy + float(eps) * (float(px) * ty + float(py) * ny)
            out.append((x, y))
    return out


def radial_parabola(n, scale=10 ** 8, sep=10 ** 7):
    """Blocks on a strictly convex rational arc: place block i centred at
    (i*sep, (i*sep)^2) scaled by scale; tiles are exact integers.  arc is
    strictly convex (parabola), block sizes tiny relative to curvature."""
    blocks = []
    for i in range(n - 1):
        T = block_g(i + 2, n - i)
        if i == 0 or i == n - 2:
            T = [(Fraction(0), Fraction(0))]
        else:
            T = _flatten(T, Fraction(1, 20))
        blocks.append(T)
    out = []
    for i, T in enumerate(blocks):
        cx, cy = i * sep, (i * sep) ** 2
        for (px, py) in T:
            out.append((cx + scale * int(px), cy + scale * int(py)))
    return out


for n in (4, 5, 6):
    S = radial_parabola(n)
    gp = in_general_position(S)
    k, why = largest_convex_subset(S)
    good = len(S) == 2 ** (n - 2) and gp and k == n - 1
    print(f"radial_parabola n={n}: |S|={len(S)} exp={2**(n-2)} gp={gp} maxConvex={k} expect {n-1} -> {'PASS' if good else 'FAIL'}")
