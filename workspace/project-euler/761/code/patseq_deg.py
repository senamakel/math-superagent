#!/usr/bin/env python3
"""Compute deg_Q(V(n)^2) for n=3..30 via sympy minimal_polynomial.

V(n) = 1/cos(alpha), alpha = (K*theta + acos(inner))/2, theta=pi/n,
inner = 2 sin(K theta)/((K+n) tan(theta)) - cos(K theta), and

    cos(2a) = cos(K theta)*inner - sin(K theta)*sqrt(1 - inner^2).

deg_Q(V(n)^2) = deg_Q(cos 2a). Same element as pattern_deg_single.py, run
over the range n=3..30; prints n, K, deg, phi(n) for comparison.
"""
import warnings
import sympy as sp
warnings.filterwarnings("ignore")


def K_of_n(n):
    th = sp.pi / n
    t = sp.tan(th)
    K = None
    for k in range(0, n + 1):
        if sp.sin(k * th) - (k + n) * t * sp.cos(k * th) < 0:
            K = k
    return K, th, t


def v2_degree(n):
    K, th, t = K_of_n(n)
    inner = (2 * sp.sin(K * th)) / ((K + n) * t) - sp.cos(K * th)
    inner = sp.simplify(inner)
    cosKa = sp.cos(K * th)
    sinKa = sp.sin(K * th)
    sq = sp.sqrt(1 - inner**2)
    cos2a = sp.simplify(cosKa * inner - sinKa * sq)
    x = sp.symbols('x')
    mpoly = sp.minimal_polynomial(cos2a, x)
    return K, sp.degree(mpoly)


def main():
    print("n   K  deg_Q(V^2)  phi(n)  match")
    for n in range(3, 31):
        try:
            K, d = v2_degree(n)
            ph = sp.totient(n)
            print(f"{n:2d}  {K}       {d:2d}       {ph:2d}    {d == ph}")
        except Exception as e:
            print(f"{n:2d}  FAIL {type(e).__name__}: {str(e)[:60]}")


if __name__ == "__main__":
    main()
