#!/usr/bin/env python3
"""deg_Q(V(n)^2) = deg_Q(cos 2alpha) for n=3..20 via PSLQ (fixed version).

Why the original pattern_deg_exact.py fails: sympy.minimal_polynomial raises
NotAlgebraic for numeric Floats; it needs exact algebraic expressions. Also its
premise cos(2a) in Q(cos pi/n) is false in general (hexagon: cos 2a =
-(1+3sqrt21)/16 in Q(sqrt21), not Q(sqrt3) = Q(cos pi/6)).

Method: c = cos 2a at 400 dps; for d = 1..D_MAX, mp.pslq([1,c,...,c^d]).
First d with an integer relation of small norm is the degree. Minimality then
follows: no relation exists in smaller dimension (PSLQ returned empty there).
Verification: (i) residual |P(c)| after reconstruction; (ii) known exact
anchors n=3,4,6 (closed forms below) reproduced exactly as minpolys of cos 2a.
"""
import mpmath as mp

mp.mp.dps = 400


def K_of_n(n):
    th = mp.pi / n
    t = mp.tan(th)
    K = 0
    for k in range(0, n + 1):
        if mp.sin(k * th) - (k + n) * t * mp.cos(k * th) < 0:
            K = k
    return K


def cos2a_value(n):
    th = mp.pi / n
    t = mp.tan(th)
    K = K_of_n(n)
    inner = 2 * mp.sin(K * th) / ((K + n) * t) - mp.cos(K * th)
    cosKa = mp.cos(K * th)
    sinKa = mp.sin(K * th)
    return cosKa * inner - sinKa * mp.sqrt(1 - inner ** 2)


def minpoly_pslq(c, d_max, tol):
    """Smallest d with an integer relation sum a_k c^k = 0; return (d, coeffs)."""
    for d in range(1, d_max + 1):
        vec = [c ** k for k in range(d + 1)]
        rel = mp.pslq(vec, tol=tol)
        if rel:
            # sanity: residual must be tiny relative to coefficient size
            res = mp.fsum(mp.mpf(a) * c ** k for k, a in enumerate(rel))
            if abs(res) < mp.mpf(10) ** (-mp.mp.dps // 2):
                return d, [int(a) for a in rel]
    return None, None


# exact anchors: cos 2a for n=3,4,6 as closed forms
# n=3: V^2=28+12sqrt5 -> cos2a=(-1-3sqrt5)/8, minpoly 16x^2+4x-11
# n=4: V^2=(5/2)(7+sqrt41) -> cos2a=(-3-sqrt41)/10, minpoly 25x^2+15x-8
# n=6: V^2=(40+8sqrt21)/3 -> cos2a=(-1-3sqrt21)/16, minpoly 64x^2+8x-47
print("exact anchors (check):")
import sympy as sp
xa = sp.Symbol('x')
for n, expr in [(3, (-1 - 3 * sp.sqrt(5)) / 8),
                (4, (-3 - sp.sqrt(41)) / 10),
                (6, (-1 - 3 * sp.sqrt(21)) / 16)]:
    p = sp.minimal_polynomial(expr, xa)
    print("  n=%d  deg=%d  poly=%s" % (n, sp.degree(p), sp.expand(p)))

print()
D_MAX = 40
TOL = mp.mpf('1e-320')
print("n    [R:Q]=phi(2n)/2   deg_Q(V^2)   poly(cos 2a)          residual")
for n in range(3, 21):
    c = cos2a_value(n)
    Rdeg = sp.totient(2 * n) // 2
    d, coeffs = minpoly_pslq(c, D_MAX, TOL)
    if coeffs is None:
        print("n=%3d  [R:Q]=%3d        FAIL(no relation to d=%d)" % (n, Rdeg, D_MAX))
        continue
    # normalize: make leading coeff positive and divide content
    import math
    g = 0
    for a in coeffs:
        g = math.gcd(g, abs(a))
    if coeffs[-1] < 0:
        coeffs = [-a for a in coeffs]
    if g > 1:
        coeffs = [a // g for a in coeffs]
    res = mp.fsum(mp.mpf(a) * c ** k for k, a in enumerate(coeffs))
    poly = " + ".join(
        ("%d" % a if k == 0 else
         ("" if abs(a) == 1 else "%d*" % a) + "x" + ("" if k == 1 else "^%d" % k))
        for k, a in enumerate(coeffs) if a)
    print("n=%3d  [R:Q]=%3d      deg_Q(V^2)=%2d%s  %s   res=%.1e"
          % (n, Rdeg, d, "" if d <= Rdeg else "  (>[R:Q]!)", poly, abs(res)))