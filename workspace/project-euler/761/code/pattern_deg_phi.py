#!/usr/bin/env python3
"""Test the conjecture deg_Q(V(n)^2) = phi(n) for n=3..24."""
import mpmath as mp
import sympy as sp
import warnings
warnings.filterwarnings("ignore")

totient = sp.totient


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
        mp.mp.dps = 500
        return None


def main():
    mp.mp.dps = 100
    print(f"{'n':>3} {'deg':>4} {'phi(n)':>7} {'match':>6}")
    for n in range(3, 25):
        d = v2_degree(n)
        phi = int(totient(n))
        print(f"{n:>3} {int(d):>4} {phi:>7} {str(d == phi):>6}")


if __name__ == "__main__":
    main()
