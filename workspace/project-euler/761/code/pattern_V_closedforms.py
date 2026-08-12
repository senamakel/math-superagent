#!/usr/bin/env python3
"""Compute alpha and V(n) for n=3..40 exactly-ish with sympy, and try to
produce a closed form in radicals for each n where the acos argument and
angle yield one. Focus: does V(n) have a simple surd / algebraic form for
small n (3: sqrt2(3+sqrt5), 4: sqrt(5/2(7+sqrt41)), 6: 2+2sqrt21/3)?"""
import sympy as sp

def critical(n):
    theta = sp.pi/n
    tan_th = sp.tan(theta)
    K = None
    for k in range(0, n+1):
        if sp.sin(k*theta) - (k+n)*tan_th*sp.cos(k*theta) < 0:
            K = k
    inner = 2*sp.sin(K*theta)/((K+n)*tan_th) - sp.cos(K*theta)
    inner = sp.Max(sp.Min(sp.simplify(inner), 1), -1)
    alpha = sp.Rational(1,2)*(K*theta + sp.acos(inner))
    V2 = 1/sp.cos(alpha)**2
    return K, alpha, sp.simplify(V2), inner

print(" n   K   inner(acos)            V^2 (simplified)              V(10dp)")
for n in range(3, 17):
    K, alpha, V2, inner = critical(n)
    inner_s = sp.simplify(inner)
    # try N() forms
    V = sp.sqrt(V2)
    print(f"{n:3d} {K:3d}  {sp.nsimplify(sp.N(inner_s,12))!s:<24s} {sp.simplify(sp.nsimplify(V2))!s:<30s} {sp.N(V,10)}")
