#!/usr/bin/env python3
"""Regenerate the deg_Q(V(n)^2) sequence exactly for small n (via exact minpoly
over Q(cos(pi/n))), and print the degree values for the pattern tools."""
import mpmath as mp
import sympy as sp
import warnings

warnings.filterwarnings("ignore")


def K_of_n(n):
    th = mp.pi / n
    t = mp.tan(th)
    best = None
    for k in range(0, n + 1):
        if mp.sin(k * th) - (k + n) * t * mp.cos(k * th) < 0:
            best = k
    return best


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
    try:
        mpoly = sp.minimal_polynomial(cos2a, x)
        return sp.degree(mpoly)
    except Exception:
        # numerical fallback
        mp.mp.dps = 400
        val = complex(sp.N(cos2a, 350))
        return None


def main():
    mp.mp.dps = 100
    print("deg_Q(V(n)^2) for n=3..16:")
    degs = []
    for n in range(3, 17):
        d = v2_degree(n)
        degs.append(d)
        print(f"  n={n}: deg={d}")
    print("sequence:", degs)


if __name__ == "__main__":
    main()
