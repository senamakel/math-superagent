#!/usr/bin/env python3
"""Compute deg_Q(V(n)^2) exactly for a single n via sympy minimal_polynomial."""
import sys, warnings
import sympy as sp
warnings.filterwarnings("ignore")


def v2_degree(n):
    th = sp.pi / n
    t = sp.tan(th)
    K = None
    for k in range(0, n + 1):
        if sp.sin(k * th) - (k + n) * t * sp.cos(k * th) < 0:
            K = k
    inner = (2 * sp.sin(K * th)) / ((K + n) * t) - sp.cos(K * th)
    inner = sp.simplify(inner)
    cosKa = sp.cos(K * th)
    sinKa = sp.sin(K * th)
    sq = sp.sqrt(1 - inner**2)
    cos2a = sp.simplify(cosKa * inner - sinKa * sq)
    x = sp.symbols('x')
    mpoly = sp.minimal_polynomial(cos2a, x)
    return sp.degree(mpoly)


if __name__ == "__main__":
    n = int(sys.argv[1])
    d = v2_degree(n)
    print(f"n={n}: deg_Q(V^2)={d}  phi(n)={sp.totient(n)}  match={d==sp.totient(n)}")
