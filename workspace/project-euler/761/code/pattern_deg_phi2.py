#!/usr/bin/env python3
"""Test deg_Q(V(n)^2) = phi(n) for a few n=17..22 using numerical PSLQ-style
minpoly (fast fallback) instead of fully symbolic cyclotomic reduction."""
import mpmath as mp
import sympy as sp
import warnings
warnings.filterwarnings("ignore")

mp.mp.dps = 300


def K_of_n(n):
    th = mp.pi / n
    t = mp.tan(th)
    best = None
    for k in range(0, n + 1):
        if mp.sin(k * th) - (k + n) * t * mp.cos(k * th) < 0:
            best = k
    return best


def cos2a_val(n):
    th = mp.pi / n
    t = mp.tan(th)
    K = K_of_n(n)
    inner = 2 * mp.sin(K * th) / ((K + n) * t) - mp.cos(K * th)
    return mp.cos(K * th) * inner - mp.sin(K * th) * mp.sqrt(1 - inner**2)


def v2_degree_num(n):
    v = cos2a_val(n)
    s = mp.nstr(v, 250)
    x = sp.symbols('x')
    try:
        expr = sp.nsimplify(sp.Float(s, 250), rational=False)
        mpoly = sp.minimal_polynomial(expr, x)
        return sp.degree(mpoly)
    except Exception as e:
        return f"FAIL:{type(e).__name__}"


def main():
    print(f"{'n':>3} {'deg':>4} {'phi(n)':>7}")
    for n in range(17, 24):
        d = v2_degree_num(n)
        phi = int(sp.totient(n))
        if isinstance(d, int):
            print(f"{n:>3} {d:>4} {phi:>7}  match={d==phi}")
        else:
            print(f"{n:>3} {d:>10} {phi:>7}")


if __name__ == "__main__":
    main()
