#!/usr/bin/env python3
"""Degree of V(n)^2 over Q via exact cyclotomic representation.

cos(2a) = cos(K th)*inner - sin(K th)*sqrt(1-inner^2), th=pi/n.
The element lives in the real cyclotomic field Q(zeta_{2n})^+.

Strategy: represent using z = exp(i*pi/n). Build cos(2a) symbolically in
terms of z algebraically, then reduce mod the cyclotomic polynomial
Phi_{2n}(z), and check the resulting algebraic element's minpoly via
numerical evaluation + rational reconstruction (sympy minimal_polynomial
with high precision).

A cleaner route: since sin(K th)*sqrt(...) is generally NOT in Q(cos(2a))
independently, just evaluate cos(2a) to huge precision and ask sympy to
find its minimal polynomial treating the number as algebraic. Use
mpmath -> Decimal -> nsimplify with the cyclotomic generator as the
extension, which makes reconstruction reliable.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 600

def K_of_n(n):
    th = mp.pi / n
    t = mp.tan(th)
    K = 0
    for k in range(0, n + 1):
        if mp.sin(k*th) - (k+n)*t*mp.cos(k*th) < 0:
            K = k
    return K

def cos2a_val(n):
    th = mp.pi / n
    t = mp.tan(th)
    K = K_of_n(n)
    inner = 2*mp.sin(K*th)/((K+n)*t) - mp.cos(K*th)
    cosKa = mp.cos(K*th)
    sinKa = mp.sin(K*th)
    sq = mp.sqrt(1 - inner**2)
    return cosKa*inner - sinKa*sq

for n in range(3, 15):
    v = cos2a_val(n)
    s = mp.nstr(v, 250)
    x = sp.symbols('x')
    try:
        cf = sp.cos(sp.pi/n)   # generator of real subfield
        expr = sp.nsimplify(sp.Float(s, 250), [cf], rational=False, full=True)
        mpoly = sp.minimal_polynomial(expr, x)
        deg = sp.degree(mpoly)
        coeffs = sp.Poly(mpoly, x).all_coeffs()
        num = coeffs[0] if coeffs else 1
        print(f"n={n}: V^2 degree Q = {deg}  quadratic={deg==2}")
    except Exception as e:
        print(f"n={n}: FAIL {type(e).__name__}: {str(e)[:80]}")
        print(f"    cos2a={mp.nstr(v,12)}")
