#!/usr/bin/env python3
"""Extend the exact minimal-polynomial degree of V(n)^2 over Q, n=3..24,
with per-n flush and a per-n wall-clock alarm so slow primes don't stall the
whole range. Prints n, K, deg (exact sympy route), phi(n), match.

Method (same as pattern_deg_v2_exact.py route A, exact):
  cos(2a) = cos(K pi/n)*inner - sin(K pi/n)*sqrt(1-inner^2),
  inner   = 2 sin(K pi/n)/((K+n) tan(pi/n)) - cos(K pi/n),
  V(n)^2 = 2/(1+cos 2a), so deg_Q(V(n)^2) = deg_Q(cos 2a).
sympy.minimal_polynomial of the exact algebraic expression is authoritative.
"""
import signal
import sys
import time
import warnings

import sympy as sp

warnings.filterwarnings("ignore")


class Timeout(Exception):
    pass


def _alarm(sig, frame):
    raise Timeout


def K_of_n(n):
    th = sp.pi / n
    t = sp.tan(th)
    best = 0
    for k in range(0, n + 1):
        if sp.sin(k * th) - (k + n) * t * sp.cos(k * th) < 0:
            best = k
    return best


def v2_degree_exact(n):
    th = sp.pi / n
    t = sp.tan(th)
    K = K_of_n(n)
    inner = sp.simplify(2 * sp.sin(K * th) / ((K + n) * t) - sp.cos(K * th))
    cos2a = sp.simplify(
        sp.cos(K * th) * inner - sp.sin(K * th) * sp.sqrt(1 - inner ** 2))
    x = sp.Symbol('x')
    p = sp.minimal_polynomial(cos2a, x)
    return K, sp.degree(p), sp.expand(p)


def v2_degree_numeric(n):
    """Fast fallback: nsimplify the 300-dps value then minpoly."""
    import mpmath as mp
    mp.mp.dps = 300
    th = mp.pi / n
    t = mp.tan(th)
    K = 0
    for k in range(0, n + 1):
        if mp.sin(k * th) - (k + n) * t * mp.cos(k * th) < 0:
            K = k
    inner = 2 * mp.sin(K * th) / ((K + n) * t) - mp.cos(K * th)
    c = mp.cos(K * th) * inner - mp.sin(K * th) * mp.sqrt(1 - inner ** 2)
    x = sp.Symbol('x')
    expr = sp.nsimplify(sp.Float(mp.nstr(c, 250), 250), rational=False)
    p = sp.minimal_polynomial(expr, x)
    return K, sp.degree(p), sp.expand(p)


def main():
    print("n   K  deg  phi(n)  match    method   poly(cos 2a)", flush=True)
    print("-" * 100, flush=True)
    for n in range(3, 25):
        t0 = time.time()
        signal.signal(signal.SIGALRM, _alarm)
        signal.alarm(150)
        try:
            K, d, poly = v2_degree_exact(n)
            method = "exact"
        except Timeout:
            try:
                K, d, poly = v2_degree_numeric(n)
                method = "numeric"
            except Exception as e:
                print(f"{n:2d}  -  FAIL  -  -       {type(e).__name__}", flush=True)
                continue
        except Exception as e:
            print(f"{n:2d}  -  FAIL  -  -       {type(e).__name__}", flush=True)
            continue
        finally:
            signal.alarm(0)
        phi = int(sp.totient(n))
        phistr = poly if method == "exact" else f"(numeric) {poly}"
        print(f"{n:2d}  {K}  {d:3d}  {phi:5d}  {str(d == phi):>5}  "
              f"{method:>7}   {phistr}   [{time.time()-t0:.0f}s]", flush=True)
    print("done", flush=True)


if __name__ == "__main__":
    main()