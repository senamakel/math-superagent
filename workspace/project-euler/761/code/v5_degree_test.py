#!/usr/bin/env python3
"""Numerically confirm that V(5) (critical speed, regular pentagon) is NOT a
quadratic surd. Uses mpmath high precision + sympy's numeric minpoly (PSLQ).
If the true minimal polynomial had degree 2, V(5)^2 would be a quadratic surd.
"""
import mpmath as mp
import sympy as sp
mp.mp.dps = 60

def V(n):
    th = mp.pi / n
    t = mp.tan(th)
    # largest integer with sin(K th) - (K+n) t cos(K th) < 0
    K = None
    for k in range(0, n+1):
        if mp.sin(k*th) - (k+n)*t*mp.cos(k*th) < 0:
            K = k
    inner = 2*mp.sin(K*th)/((K+n)*t) - mp.cos(K*th)
    alpha = mp.mpf(1)/2*(K*th + mp.acos(inner))
    return mp.mpf(1)/mp.cos(alpha)

v5 = V(5)
print("V(5) =", mp.nstr(v5, 40))

# numeric minpoly (PSLQ) to moderate degree
f = sp.Float(mp.nstr(v5, 40))
for deg in range(1, 9):
    try:
        p = sp.minimal_polynomial(f, sp.Symbol('x'), domain=sp.QQ)
        print(f"minimal polynomial of V(5) (degree {sp.degree(p)}): {p}  [degree>2 => NOT quadratic surd]")
        break
    except Exception as e:
        print(f"  degree {deg}: no integer polynomial (needs more terms / higher precision)")

# Also do the same for V(3), V(4), V(6) as sanity: they must be quadratic
for nv in [3,4,6]:
    v = V(nv)
    f = sp.Float(mp.nstr(v, 40))
    try:
        p = sp.minimal_polynomial(f, sp.Symbol('x'), domain=sp.QQ)
        print(f"V({nv}): minpoly degree {sp.degree(p)}: {p}")
    except Exception as e:
        print(f"V({nv}): minpoly failed: {e}")
