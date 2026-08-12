#!/usr/bin/env python3
"""Numeric PSLQ degree of cos(2a) with a sane tolerance scheme.

The old pattern_deg_fixed.py failed on n>=5 because it demanded residual
< 10^-(dps/2) = 1e-200 with coefficients of a degree-10 integer relation
   whose true size is ~1e14: PSLQ at 400 dps with tol 1e-320 cannot certify
   (working precision is exhausted resolving 400-digit mantissas against a
   ~1e-400-background; and the relation's identity tolerance should scale
   with the coefficient size ~ 1e-14, nowhere near 1e-320).

Here: dps=300, and for d=1..DMAX try pslq with the *default* tolerance
(1e-60 at 300 dps scaled by mpmath — actually mpmath default is
10^(prec-30) ~ 1e-60, much more reasonable), accept the smallest d whose
relation residual < 1e-40 (residual scales as ~1e-60 for genuine relations
at this precision; random near-relations at smaller d have residual ~1e-18
at best). This is exactly the regime V(n) values live in.
"""
import mpmath as mp

mp.mp.dps = 300


def K_of_n(n):
    th = mp.pi / n
    t = mp.tan(th)
    best = 0
    for k in range(0, n + 1):
        if mp.sin(k * th) - (k + n) * t * mp.cos(k * th) < 0:
            best = k
    return best


def cos2a_val(n):
    th = mp.pi / n
    t = mp.tan(th)
    K = K_of_n(n)
    inner = 2 * mp.sin(K * th) / ((K + n) * t) - mp.cos(K * th)
    return mp.cos(K * th) * inner - mp.sin(K * th) * mp.sqrt(1 - inner ** 2)


def deg_pslq(n, dmax=30, res_tol=mp.mpf('1e-40')):
    c = cos2a_val(n)
    for d in range(1, dmax + 1):
        vec = [c ** k for k in range(d + 1)]
        rel = mp.pslq(vec, maxcoeff=10**6, maxsteps=3000, tol=mp.mpf(10) ** (-(mp.mp.dps - 60)))
        if rel:
            res = abs(mp.fsum(mp.mpf(a) * c ** k for k, a in enumerate(rel)))
            if res < res_tol:
                # normalize signs/content
                import math
                g = 0
                for a in rel:
                    g = math.gcd(g, abs(int(a)))
                if rel[-1] < 0:
                    rel = [-a for a in rel]
                if g > 1:
                    rel = [a // g for a in rel]
                return d, res, [int(a) for a in rel]
    return None, None, None


def main():
    print(f"{'n':>3} {'K':>3} {'deg':>4} {'phi':>4} match  residual    coeffs[end]")
    from sympy import totient
    for n in range(3, 25):
        d, res, rel = deg_pslq(n)
        phi = int(totient(n))
        if d is None:
            print(f"{n:3d} {K_of_n(n):3d}  FAIL (no relation to d=30)")
        else:
            print(f"{n:3d} {K_of_n(n):3d} {d:4d} {phi:4d}  "
                  f"{str(d == phi):>5}   {float(res):.1e}     {rel[-1]}")


if __name__ == "__main__":
    main()