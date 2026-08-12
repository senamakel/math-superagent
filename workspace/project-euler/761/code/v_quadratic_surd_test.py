#!/usr/bin/env python3
"""Test whether V(n)^2 for the regular n-gon critical speed is always a
quadratic surd (degree-2 algebraic number). It holds for n=3 (sqrt2(3+sqrt5)),
n=4 (sqrt(5/2(7+sqrt41))), n=6 (2+2sqrt21/3)^... -- actually V itself is
quadratic in those. Question: what is the field degree of V(n) for small n?

V(n)=1/cos(alpha), alpha=1/2*(K*theta + acos(inner)),
inner = 2*sin(K*theta)/((K+n)*tan(theta)) - cos(K*theta), theta=pi/n.

We compute V(n) symbolically with sympy, then find its minimal polynomial
over Q and its degree. Quadratic surd  <=>  minpoly degree 2.
"""
import sympy as sp

def V_symb(n):
    th = sp.pi / n
    tan_th = sp.tan(th)
    K = None
    for k in range(0, n + 1):
        if sp.sin(k*th) - (k+n)*tan_th*sp.cos(k*th) < 0:
            K = k
    inner = 2*sp.sin(K*th)/((K+n)*tan_th) - sp.cos(K*th)
    inner = sp.nsimplify(sp.simplify(inner))
    alpha = sp.Rational(1, 2)*(K*th + sp.acos(inner))
    V = 1/sp.cos(alpha)
    return K, inner, alpha, V

for n in range(3, 13):
    K, inner, alpha, V = V_symb(n)
    Vs = sp.nsimplify(sp.simplify(V))
    # minpoly of V (should be algebraic if we can express acos of constructible)
    try:
        poly = sp.minimal_polynomial(Vs, sp.Symbol('x'))
        deg = sp.degree(poly, sp.Symbol('x'))
        print(f"n={n}: K={K}  V^2-degree(minpoly of V)={deg}")
        print(f"    minpoly: {poly}")
    except Exception as e:
        print(f"n={n}: K={K}  minpoly failed: {type(e).__name__}: {e}")
    print(f"    numeric V = {sp.N(V, 14)}")
