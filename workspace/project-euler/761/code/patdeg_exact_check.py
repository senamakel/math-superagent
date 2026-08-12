#!/usr/bin/env python3
"""Exact check: deg_Q(V(n)^2) = phi(n) for n=3..20, via sympy minimal_polynomial.

V(n)=1/cos(alpha), alpha=(K*theta+acos(inner))/2, theta=pi/n.
cos(2a) = cos(K th)*inner - sin(K th)*sqrt(1-inner^2).
We build cos2a as an exact algebraic element and take sympy's minimal
polynomial. Print n, K, degree, phi(n), and whether degree==phi(n).
"""
import warnings, time
import sympy as sp
warnings.filterwarnings("ignore")


def K_of_n(n):
    th = sp.pi / n
    t = sp.tan(th)
    K = None
    for k in range(0, n + 1):
        if sp.sin(k * th) - (k + n) * t * sp.cos(k * th) < 0:
            K = k
    return K


def cos2a_val(n):
    th = sp.pi / n
    t = sp.tan(th)
    K = K_of_n(n)
    inner = (2 * sp.sin(K * th)) / ((K + n) * t) - sp.cos(K * th)
    inner = sp.simplify(inner)
    cosKa = sp.cos(K * th)
    sinKa = sp.sin(K * th)
    sq = sp.sqrt(1 - inner ** 2)
    return sp.simplify(cosKa * inner - sinKa * sq), K


def main():
    print("n  K  deg_Q(V^2)  phi(n)  match   time(s)")
    for n in range(3, 21):
        t0 = time.time()
        try:
            cos2a, K = cos2a_val(n)
            x = sp.symbols('x')
            mpoly = sp.minimal_polynomial(cos2a, x)
            deg = sp.degree(mpoly)
            ph = sp.totient(n)
            print(f"{n:2d} {K:2d}     {deg:2d}      {ph:2d}     {str(deg==ph):5s}   {time.time()-t0:6.1f}")
        except Exception as e:
            print(f"{n:2d}  FAIL {type(e).__name__}: {str(e)[:70]}   {time.time()-t0:6.1f}")


if __name__ == "__main__":
    main()
