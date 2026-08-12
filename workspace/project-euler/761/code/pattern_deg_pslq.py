#!/usr/bin/env python3
"""deg_Q(V(n)^2) via mpmath pslq minimal-polynomial detection.

V(n) = 1/cos(alpha), alpha = (K*theta + acos(inner))/2, theta=pi/n.
cos(2alpha) = cos(K theta)*inner - sin(K theta)*sqrt(1-inner^2),
a real algebraic number (in Q(cos(pi/n), sqrt terms)).  We detect its
integer minimal polynomial by PSLQ over 1, v, v^2, ..., v^d for increasing d.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 500


def K_of_n(n):
    th = mp.pi / n
    t = mp.tan(th)
    K = 0
    for k in range(0, n + 1):
        if mp.sin(k * th) - (k + n) * t * mp.cos(k * th) < 0:
            K = k
    return K


def cos2a_value(n):
    th = mp.pi / n
    t = mp.tan(th)
    K = K_of_n(n)
    inner = 2 * mp.sin(K * th) / ((K + n) * t) - mp.cos(K * th)
    cosKa = mp.cos(K * th)
    sinKa = mp.sin(K * th)
    return cosKa * inner - sinKa * mp.sqrt(1 - inner ** 2)


def minpoly_pslq(val, maxdeg, tol=mp.mpf('1e-120')):
    """Return (degree, coeffs[leading..0]) of integer poly val satisfies,
    or None if no relation of degree<=maxdeg with small coefficients found."""
    for d in range(1, maxdeg + 1):
        powers = [mp.power(val, k) for k in range(d + 1)]
        rel = mp.pslq(powers, maxcoeff=10 ** 6, maxsteps=10 ** 5, tol=tol)
        if rel is not None:
            # rel[0]*1 + rel[1]*v + ... + rel[d]*v^d = 0
            # make it a monic-ish minimal polynomial (leading coeff may be!=1)
            # degree = highest index with nonzero coeff
            deg = max(i for i, c in enumerate(rel) if c != 0)
            return deg, [rel[i] for i in range(deg + 1)]
    return None


for n in range(3, 21):
    cos2a = cos2a_value(n)
    Rdeg = sp.totient(2 * n) // 2
    res = minpoly_pslq(cos2a, 2 * Rdeg + 4)
    if res is None:
        print("n=%3d K=%3d  [R:Q]=%3d phi(2n)=%3d  deg=VFAIL(no small rel)" % (
            n, K_of_n(n), Rdeg, sp.totient(2 * n)))
    else:
        deg, coeffs = res
        poly = " + ".join("%d*x^%d" % (c, i) for i, c in enumerate(coeffs))
        print("n=%3d K=%3d  [R:Q]=%3d phi(2n)=%3d  deg_Q(V^2)=%3d  %s" % (
            n, K_of_n(n), Rdeg, sp.totient(2 * n), deg, poly))
