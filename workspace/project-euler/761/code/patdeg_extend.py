#!/usr/bin/env python3
"""Extend the exact check deg_Q(V(n)^2) = phi(n) to n=20..24.

For each n: build cos(2a) exactly (K from the sign condition), take
sympy.minimal_polynomial, print degree vs phi(n). Independent numeric
check: evaluate the minpoly at a 50-dp numeric value of cos(2a) and
report the residual (must be ~0). Also print minpolys for n=3,4,6 to
compare with the known exact anchors.
"""
import warnings, time
import sympy as sp
import mpmath as mp

warnings.filterwarnings("ignore")


def cos2a_exact(n):
    th = sp.pi / n
    t = sp.tan(th)
    K = None
    for k in range(0, n + 1):
        if sp.sin(k * th) - (k + n) * t * sp.cos(k * th) < 0:
            K = k
    u = (2 * sp.sin(K * th)) / ((K + n) * t) - sp.cos(K * th)
    u = sp.simplify(u)
    cosKa, sinKa = sp.cos(K * th), sp.sin(K * th)
    sq = sp.sqrt(1 - u ** 2)
    return K, sp.simplify(cosKa * u - sinKa * sq)


def cos2a_num(n):
    th = mp.pi / n
    t = mp.tan(th)
    K = None
    for k in range(0, n + 1):
        if mp.sin(k * th) - (k + n) * t * mp.cos(k * th) < 0:
            K = k
    u = 2 * mp.sin(K * th) / ((K + n) * t) - mp.cos(K * th)
    return K, mp.cos(K * th) * u - mp.sin(K * th) * mp.sqrt(1 - u ** 2)


def main():
    mp.mp.dps = 50
    x = sp.symbols('x')
    print("anchors (must match known exact minpolys of cos 2a):")
    for n in [3, 4, 6]:
        K, c2 = cos2a_exact(n)
        poly = sp.minimal_polynomial(c2, x)
        print(f"  n={n}: K={K}  minpoly={sp.expand(poly)}")
    print()
    print("n  K  deg  phi(n)  match   residual(poly@cos2a)")
    for n in range(20, 25):
        t0 = time.time()
        try:
            K, c2 = cos2a_exact(n)
            poly = sp.minimal_polynomial(c2, x)
            deg = sp.degree(poly)
            ph = sp.totient(n)
            _, c2n = cos2a_num(n)
            res = abs(complex(sp.N(sp.Poly(poly, x).as_expr().subs(x, sp.N(c2, 50)), 30)))
            print(f"{n:2d} {K:2d} {deg:3d}  {ph:3d}   {str(deg == ph):5s}   {res:.1e}  ({time.time()-t0:.1f}s)")
        except Exception as e:
            print(f"{n:2d} FAIL {type(e).__name__}: {str(e)[:60]} ({time.time()-t0:.1f}s)")


if __name__ == "__main__":
    main()