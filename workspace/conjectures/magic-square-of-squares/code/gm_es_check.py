#!/usr/bin/env python3
"""Check the Elekes-Szabo / sum-product-for-Gm literature against the Phi-set.

Phi = f(Q cap (0,1)), f(t) = 4t(1-t^2)/(1+t^2)^2 = sin(4 arctan t) = y([4] on
the circle).  The Phi-quadruple condition is a 3-term AP
{q1-q2, q1, q1+q2} inside f(Q).

Facts to verify mechanically:
[1] f(t)^2 + g(t)^2 = 1 identically, g(t) = (t^4 - 6t^2 + 1)/(1+t^2)^2
    = cos(4 arctan t).  (Every Phi-value pairs with a rational s on the
    unit circle: q^2 + s^2 = 1.)
[2] f: P^1 -> P^1 is a degree-4 covering (generic fibre = 4 points), so the
    graph correspondence C = {(x, f(x))} subset Gm x Ga has
    deg_L(C) = d_X deg(X) + d_Y deg(Y) = 1*1 + 4*1 = 5  (HMS Sec. 3.2/3.3),
    i.e. 'degree at most d' with d = 5.
[3] The graph of a non-constant rational f: Gm -> Ga is NOT a translate of an
    algebraic subgroup of Gm x Ga: the only connected 1-dim algebraic
    subgroups of Gm x Ga with dominant projection to Gm are translates of
    Gm x {0}, whose projection to Ga is a point (not dominant).  Hence
    HMS Corollary 2.2's hypotheses hold verbatim with G = Gm, H = Ga,
    C = graph f, Gamma = <preimages> of rank r <= 4.
[4] The bound Corollary 2.2 gives, |P| <= D(5)^{1+r}, is trivially true for
    the length-3 AP: D >= 1 (a constant from uniform Mordell-Lang /
    S-unit bounds), so 3 <= D^{1+r} always.  Even the *ideal* effective
    bound D^{1+r} < 3 would need D < 3^{1/(1+r)} <= 3^{1/5} ~= 1.245.
    Print these thresholds.
[5] Phi is dense in (0,1): f continuous, {t in Q cap (0,1)} dense in (0,1),
    f((0,1)) = (0,1].  Demonstrate: given any eps > 0 and x0 in (0,1),
    find rational t with |f(t) - x0| < eps (constructive search over
    Farey-ish rationals for a few samples).
"""
from fractions import Fraction
from math import isqrt

# --- [1] exact identity with sympy ---------------------------------------
import sympy as sp
t = sp.symbols('t')
f = 4 * t * (1 - t**2) / (1 + t**2)**2
g = (t**4 - 6 * t**2 + 1) / (1 + t**2)**2
ident = sp.simplify(f**2 + g**2 - 1)
assert ident == 0
print("[1] f(t)^2 + g(t)^2 == 1 identically: PASS (g = cos(4 arctan t))")

# --- [2] map degree: generic fibre size + behaviour at infinity -----------
# f(t) = (4t - 4t^3)/(1 + 2t^2 + t^4); numerator degree 3, denominator
# degree 4.  As t -> inf, f -> 0 like 4/t^3 -> 4/t -> 0 to order 1: so
# f(inf) = 0.  Generic fibre of f: y = f(t) has degree-4 numerator
# equation y(1+t^2)^2 = 4t(1-t^2) -> quartic in t for generic y.
# Verify the quartic generically has 4 distinct roots for a sample y.
import random
rng = random.Random(11)
ok = True
for _ in range(20):
    y = Fraction(rng.randint(1, 100), rng.randint(101, 200))
    # y(1+t^2)^2 - 4t(1-t^2) = 0  ->  poly in t
    # expand: y t^4 + y 2t^2 + y - 4t + 4t^3 = 0
    # y*t^4 + 4*t^3 + 2y*t^2 - 4t + y
    poly = sp.Poly(y * t**4 + 4 * t**3 + 2 * y * t**2 - 4 * t + y, t)
    # number of distinct complex roots = degree - gcd(poly, poly')
    gcdd = sp.gcd(poly.as_expr(), sp.diff(poly.as_expr(), t))
    distinct = sp.degree(poly.as_expr(), t) - sp.degree(gcdd, t)
    if distinct != 4:
        ok = False
        print(f"   y={y}: distinct roots = {distinct}")
print(f"[2] generic fibre of f over y has 4 distinct roots (deg f = 4): "
      f"{'PASS' if ok else 'FAIL'}; f(inf)=0 to order 1")
print("    deg_L(graph C) = d_X*1 + d_Y*1 = 1*1 + 4*1 = 5  -> d = 5 for "
      "HMS Cor 2.2")

# --- [4] thresholds --------------------------------------------------------
import math
print("[4] Cor 2.2 bound |P| <= D(5)^{1+r}: D>=1 so length-3 AP ALWAYS "
      "fits. Thresholds for a *non-trivial* bound on length-3 AP:")
for r in range(0, 5):
    thr = 3 ** (1 / (1 + r))
    print(f"    r={r}: need D(5) < {thr:.6f} to forbid |P|=3")
print("    (D(d) is an uncomputed 'effectively computable' constant built "
      "from David-Philippon uniform Mordell-Lang + ESS S-unit bounds; no "
      "value is ever exhibited in HMS 2603.06483)")

# --- [5] Phi dense in (0,1): constructive check ---------------------------
def f_rat(t_num, t_den):
    n = 4 * t_num * (t_den**2 - t_num**2)
    d = (t_num**2 + t_den**2)**2
    g = math.gcd(n, d)
    return Fraction(n // g, d // g)

# for x0 in {0.1, 0.5, 0.9, 0.99}, find t = a/b rational, a<b, with
# |f(t) - x0| < 1e-3  (density: such t exists; find it by scanning b)
targets = [Fraction(1, 10), Fraction(1, 2), Fraction(9, 10), Fraction(99, 100)]
ok5 = True
for x0 in targets:
    found = None
    for b in range(2, 300):
        for a in range(1, b):
            v = f_rat(a, b)
            if abs(float(v) - float(x0)) < 1e-3:
                found = (a, b, v)
                break
        if found:
            break
    if not found:
        ok5 = False
        print(f"   x0={x0}: no rational t with |f(t)-x0|<1e-3, b<300")
    else:
        print(f"[5] Phi dense in (0,1): x0={x0} ~ f({found[0]}/{found[1]})"
              f"= {float(found[2]):.6f}")
print(f"    f(Q cap (0,1)) = Phi is dense in (0,1] by continuity: "
      f"{'PASS (constructive samples)' if ok5 else 'check FAILED'}")

# --- [6] membership squares: q in Phi => (q,s) on unit circle, s rational,
# with s = g(t). Demonstrates the exact-membership structure from the run.
q = f_rat(3, 2)   # f(3/2) = sin(4 arctan(3/2))
s = Fraction(3**4 - 6*3**2 + 1, (3**2 + 2**2)**2)  # g(3/2)
check1 = q**2 + s**2 == 1
check2 = (1 - s) / 2
check3 = (1 + s) / 2
# (1±s)/2 both rational squares is the Phi membership criterion
from math import isqrt as _isqrt
def is_sq(Fr):
    return Fr > 0 and _isqrt(Fr.numerator)**2 == Fr.numerator \
        and _isqrt(Fr.denominator)**2 == Fr.denominator
print(f"[6] sample q=f(3/2)={q}: q^2+s^2=1 with s=g(3/2)={s}: "
      f"{'PASS' if check1 else 'FAIL'}; (1-s)/2={check2} square: "
      f"{is_sq(check2)}; (1+s)/2={check3} square: {is_sq(check3)}")