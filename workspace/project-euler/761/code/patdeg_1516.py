#!/usr/bin/env python3
"""Exact deg_Q(V(n)^2) for n=15,16 via sympy minimal_polynomial of cos(2a)."""
import sympy as sp

def deg_and_poly(n):
    th = sp.pi / n
    t = sp.tan(th)
    K = None
    for k in range(0, n + 1):
        if sp.sin(k * th) - (k + n) * t * sp.cos(k * th) < 0:
            K = k
    inner = sp.simplify(2 * sp.sin(K * th) / ((K + n) * t) - sp.cos(K * th))
    cos2a = sp.simplify(
        sp.cos(K * th) * inner - sp.sin(K * th) * sp.sqrt(1 - inner ** 2))
    x = sp.Symbol('x')
    p = sp.minimal_polynomial(cos2a, x)
    return K, sp.degree(p), sp.expand(p)

import sys
for n in [15, 16]:
    K, d, p = deg_and_poly(n)
    print(f"n={n}: K={K} deg_Q(V^2)={d} phi(n)={sp.totient(n)}")
    print(f"   poly={p}")
