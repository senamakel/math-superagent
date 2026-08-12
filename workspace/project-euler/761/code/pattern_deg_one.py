#!/usr/bin/env python3
"""deg_Q(V^2) for n=15..20, one n per subprocess with a hard timeout
(route A: exact sympy minimal_polynomial). Prime n (17,19) may still be
slow but are independent of each other."""
import sys
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
    t0 = time.time()
    p = sp.minimal_polynomial(cos2a, x)
    return K, sp.degree(p), sp.expand(p), time.time() - t0


if __name__ == "__main__":
    n = int(sys.argv[1])
    try:
        K, d, p, dt = deg_and_poly(n)
        print(f"n={n} K={K} deg={d} phi={sp.totient(n)} match={d == int(sp.totient(n))} time={dt:.1f}s")
        print(f"poly: {p}")
    except Exception as e:
        print(f"n={n} FAIL {type(e).__name__}: {str(e)[:80]}")