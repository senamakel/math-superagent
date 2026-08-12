#!/usr/bin/env python3
"""Test the right conjecture: is V(n)^2 always a quadratic surd?
Known: n=3 -> V2=28+12sqrt5 (quadratic), n=4 -> V2=5/2(7+sqrt41) (quadratic),
n=6 -> V2=40/3+8sqrt21/3 (quadratic). Test n=5,7,8,... exactly with sympy."""
import sympy as sp

def V2_symb(n):
    th = sp.pi / n
    tan_th = sp.tan(th)
    K = None
    for k in range(0, n + 1):
        if sp.sin(k*th) - (k+n)*tan_th*sp.cos(k*th) < 0:
            K = k
    inner = 2*sp.sin(K*th)/((K+n)*tan_th) - sp.cos(K*th)
    inner = sp.nsimplify(sp.simplify(inner))
    alpha = sp.Rational(1, 2)*(K*th + sp.acos(inner))
    V2 = 1/sp.cos(alpha)**2
    return K, inner, alpha, sp.nsimplify(sp.simplify(V2))

for n in range(3, 13):
    K, inner, alpha, V2 = V2_symb(n)
    try:
        poly = sp.minimal_polynomial(V2, sp.Symbol('x'))
        deg = sp.degree(poly)
        is_quad = (deg <= 2)
        print(f"n={n}: K={K}  V^2 minpoly degree={deg}  quadratic={is_quad}")
        if is_quad:
            print(f"    minpoly: {poly}")
    except Exception as e:
        print(f"n={n}: K={K}  V^2 minpoly failed: {type(e).__name__}")
    print(f"    V^2 numeric = {sp.N(V2, 12)}")
