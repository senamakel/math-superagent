#!/usr/bin/env python3
"""Exact minimal-polynomial degree of V(n)^2 = 1/cos^2(alpha) over Q, n=3..14.

cos(2a) = cos(K*pi/n)*inner - sin(K*pi/n)*sqrt(1-inner^2),
inner   = 2 sin(K pi/n)/((K+n) tan(pi/n)) - cos(K pi/n),
a final result:  V(n)^2 = 2/(1+cos(2a)),  so deg_Q(V(n)^2) = deg_Q(cos 2a).

Two independent routes for every n:
  A) exact sympy minimal_polynomial of the algebraic expression;
  B) high-precision PSLQ on the numeric value (mpmath).
Report both; agreement is the check. n=5's value is the artifact the old
pattern_deg_fixed.py failed to find (it reported 'no relation to d=40').
"""
import mpmath as mp
import sympy as sp
import warnings
warnings.filterwarnings("ignore")

sp.init_printing(use_unicode=False)


def K_of_n_sympy(n):
    th = sp.pi / n
    t = sp.tan(th)
    best = None
    for k in range(0, n + 1):
        if sp.sin(k * th) - (k + n) * t * sp.cos(k * th) < 0:
            best = k
    return best


def exact_degree(n):
    """Route A: exact sympy minimal polynomial of cos(2a)."""
    th = sp.pi / n
    t = sp.tan(th)
    K = K_of_n_sympy(n)
    inner = sp.simplify(2 * sp.sin(K * th) / ((K + n) * t) - sp.cos(K * th))
    cos2a = sp.simplify(
        sp.cos(K * th) * inner - sp.sin(K * th) * sp.sqrt(1 - inner ** 2))
    x = sp.Symbol('x')
    p = sp.minimal_polynomial(cos2a, x)
    return K, inner, cos2a, sp.degree(p), sp.expand(p)


def numeric_degree(n, dps=400):
    """Route B: PSLQ on the numeric value with default tolerances."""
    mp.mp.dps = dps
    th = mp.pi / n
    t = mp.tan(th)
    K = 0
    for k in range(0, n + 1):
        if mp.sin(k * th) - (k + n) * t * mp.cos(k * th) < 0:
            K = k
    inner = 2 * mp.sin(K * th) / ((K + n) * t) - mp.cos(K * th)
    c = mp.cos(K * th) * inner - mp.sin(K * th) * mp.sqrt(1 - inner ** 2)
    # try PSLQ with default tol; then with explicit tight tolerance
    for d in range(1, 25):
        vec = [c ** k for k in range(d + 1)]
        rel = mp.pslq(vec, tol=mp.mpf(10) ** (-(dps - 40)), maxsteps=2000)
        if rel:
            res = abs(mp.fsum(mp.mpf(a) * c ** k for k, a in enumerate(rel)))
            return K, d, res, [int(a) for a in rel]
    return K, None, None, None


def main():
    print("n   K  | degA(exact)  degB(PSLQ)  residual      polyA")
    print("-" * 78)
    for n in range(3, 15):
        Ka, innerA, cos2aA, degA, polyA = exact_degree(n)
        Kb, degB, res, rel = numeric_degree(n)
        mark = "OK" if degA == degB else "MISMATCH"
        res_str = "-" if res is None else f"{float(res):.1e}"
        print(f"{n:2d}  {Ka}  |   {int(degA):2d}          {str(degB):>4}      "
              f"{res_str:>10}   {mark}")
        print(f"     polyA: {polyA}")
    print()
    # n=5 explicit verification of the hand-derived nested radical
    s5 = sp.sqrt(5)
    inner5 = (13 - 5 * s5) / 28
    assert sp.simplify(inner5 - (2 * sp.sin(2 * sp.pi / 5) /
                                 (7 * sp.tan(sp.pi / 5)) - sp.cos(2 * sp.pi / 5))) == 0
    c25 = sp.cos(2 * sp.pi / 5) * inner5 - sp.sin(2 * sp.pi / 5) * sp.sqrt(1 - inner5 ** 2)
    x = sp.Symbol('x')
    p5 = sp.minimal_polynomial(sp.simplify(c25), x)
    print("n=5 hand form: cos2a = (18*sqrt(5)-38-sqrt(6200+2280*sqrt(5)))/112")
    print("n=5 exact minpoly:", sp.expand(p5), " degree", sp.degree(p5))


if __name__ == "__main__":
    main()