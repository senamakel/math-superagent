#!/usr/bin/env python3
"""Exact degree of cos(2alpha) (hence of V(n)^2) over Q via PSLQ.

V(n) = 1/cos(alpha), alpha = (K*theta + acos(inner))/2, theta=pi/n.
cos(2alpha) = cos(K theta)*inner - sin(K theta)*sqrt(1-inner^2).
R = Q(cos(pi/n)) real cyclotomic, [R:Q] = phi(2n)/2.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 400


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


rows = []
for n in range(3, 21):
    cos2a = cos2a_value(n)
    Rdeg = sp.totient(2 * n) // 2
    x = sp.Symbol('x')
    try:
        mpoly = sp.minimal_polynomial(sp.N(cos2a, 300), x)
        deg = sp.degree(mpoly)
        rows.append((n, Rdeg, deg, sp.expand(mpoly)))
    except Exception as e:
        rows.append((n, Rdeg, 'FAIL', type(e).__name__))

for n, Rdeg, deg, poly in rows:
    print("n=%3d  [R:Q]=%3d  deg_Q(V^2)=%s  poly=%s" % (n, Rdeg, deg, poly))
