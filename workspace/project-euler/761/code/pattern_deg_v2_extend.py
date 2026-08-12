#!/usr/bin/env python3
"""Extend deg_Q(V(n)^2) exact computation to n=15..20; conjecture deg = phi(n).

Route: sympy minimal_polynomial of cos(2a), exact. Prints n, K, deg, phi(n),
match flag, minpoly, wall time. n=17 and n=19 (phi = 16, 18) may be slow;
each n is computed independently so a timeout only loses that n.
"""
import time
import warnings
import sympy as sp
warnings.filterwarnings("ignore")


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


def main():
    print(f"{'n':>2} {'K':>2} {'deg':>3} {'phi(n)':>6}  match   sec   poly")
    for n in range(3, 21):
        t0 = time.time()
        try:
            K, d, p = deg_and_poly(n)
            phi = int(sp.totient(n))
            print(f"{n:2d} {K:2d} {d:3d} {phi:6d}   {str(d == phi):>5}  "
                  f"{time.time()-t0:5.1f}   {p}")
        except Exception as e:
            print(f"{n:2d}  FAIL {type(e).__name__}: {str(e)[:70]}  "
                  f"{time.time()-t0:5.1f}")

    print()
    degs = []
    for n in range(3, 21):
        try:
            K, d, p = deg_and_poly(n)
            degs.append(d)
        except Exception:
            degs.append(None)
    print("deg sequence n=3..20:", degs)
    print("phi sequence  n=3..20:", [int(sp.totient(n)) for n in range(3, 21)])


if __name__ == "__main__":
    main()