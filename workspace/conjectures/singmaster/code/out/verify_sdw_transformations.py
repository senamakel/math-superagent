#!/usr/bin/env python3
"""Verify the Stroeker-de Weger 1999 (Math. Comp. 68, 1257-1281) Table 1
transformations that reduce each solved binomial equation C(n,k1)=C(m,k2) to
its stated elliptic model.

This is an independent algebraic check of the load-bearing anchor
`sdw-elliptic-logarithms-eight-pairs`: the eight reductions are exact
polynomial identities, so a remainder of zero (symbolic, exact rational
arithmetic) confirms the reduction step mechanically without reading the
paper's tables.

Setup: C(n,k1)=C(m,k2)  <=>  k2! * falling(n,k1)/k1! = falling(m,k2)
where falling(x,r) = x(x-1)...(x-r+1).  For each pair we substitute the
Table 1 variables (X,Y) or (U,V) into the model equation and reduce modulo
the binomial-equation polynomial.  Zero remainder = exact identity.

Also check the Mordell-Weil bases listed in Table 3 lie on their curve
(W23: (0,4),(3,4)).
"""

import sympy as sp

m, n = sp.symbols('m n', integer=True)

def falling(x, r):
    return sp.prod([x - i for i in range(r)])

def binom_poly(k1, k2, var):
    """k2! * C(var,k1) - falling(var,k2), zero exactly when C(var,k1)*k2!/k1! = (var)_k2.
    Use left variable n with degree k1, right variable m with degree k2."""
    # C(n,k1)=C(m,k2) <=> k2! (n)_{k1} / k1! = (m)_{k2}
    return sp.factorial(k2) * falling(n, k1) / sp.factorial(k1) - falling(m, k2)

def check(pair, xform, model_lhs, model_rhs, label):
    """xform: dict with 'X'/'U', 'Y'/'V' sympy exprs in (n,m).
    model: lhs == rhs as sympy exprs. Verify remainder of lhs-rhs mod P is 0."""
    k1, k2 = pair
    P = sp.expand(binom_poly(k1, k2, n))
    L = sp.expand(model_lhs - model_rhs)
    # substitute
    Lsub = sp.expand(L.subs(xform))
    # reduce modulo P as polynomial in n over Q(m)
    rem = sp.rem(sp.Poly(Lsub, n), sp.Poly(P, n))
    ok = rem.is_zero
    print(f"({k1},{k2}) [{label}]: remainder==0 -> {ok}")
    return ok

X, Y, U, V = sp.symbols('X Y U V')

results = []

# (k,l), transform dict, model equation lhs-rhs
W23 = Y*Y + Y - (X**3 - 9*X + 20)
results.append(check((2,3), {X: 3*m-3, Y: 9*n-5}, W23, 0, "W23 Y^2+Y=X^3-9X+20"))

Q24 = V*V - (3*U**4 + 6*U**3 - 3*U**2 - 6*U + 9)
results.append(check((2,4), {U: m-2, V: 6*n-3}, Q24, 0, "Q24 V^2=3U^4+6U^3-3U^2-6U+9"))

W26 = Y*Y + Y - (X**3 + X**2 - 58*X + 1294)
results.append(check((2,6), {X: sp.Rational(5,2)*m**2 - sp.Rational(25,2)*m + 8,
                             Y: 75*n - 38}, W26, 0, "W26 Y^2+Y=X^3+X^2-58X+1294"))

Q28 = V*V - (35*U**4 - 350*U**3 + 945*U**2 - 630*U + 11025)
results.append(check((2,8), {U: sp.Rational(1,2)*m**2 - sp.Rational(7,2)*m + 6,
                             V: 210*n - 105}, Q28, 0, "Q28 V^2=35U^4-350U^3+945U^2-630U+11025"))

W34 = Y*Y + Y - (X**3 - X)
results.append(check((3,4), {X: n-1, Y: sp.Rational(1,2)*m**2 - sp.Rational(3,2)*m},
                      W34, 0, "W34 Y^2+Y=X^3-X"))

C36 = 15*U**3 - 15*U - (V**3 - 4*V**2 + 3*V)
results.append(check((3,6), {U: n-1, V: sp.Rational(1,2)*m**2 - sp.Rational(5,2)*m + 3},
                      C36, 0, "C36 15U^3-15U=V^3-4V^2+3V"))

W46 = Y*Y + Y - (X**3 - 525*X + 10156)
results.append(check((4,6), {X: sp.Rational(15,2)*m**2 - sp.Rational(75,2)*m + 25,
                             Y: sp.Rational(225,2)*n**2 - sp.Rational(675,2)*n + 112},
                      W46, 0, "W46 Y^2+Y=X^3-525X+10156"))

Q48 = V*V - (105*U**4 + 210*U**3 - 945*U**2 - 1890*U + 11025)
results.append(check((4,8), {U: sp.Rational(1,2)*m**2 - sp.Rational(7,2)*m + 3,
                             V: 105*n**2 - 315*n + 105}, Q48, 0, "Q48 V^2=105U^4+210U^3-945U^2-1890U+11025"))

print()
print(f"all 8 transformation identities exact: {all(results)}")

# Also: MW bases of Table 3 lie on their curves
print()
print("MW-basis checks (points on curve):")
W23c = lambda x, y: y*y + y - (x**3 - 9*x + 20)
print("  W23 (0,4):", W23c(0, 4) == 0)
print("  W23 (3,4):", W23c(3, 4) == 0)
W26c = lambda x, y: y*y + y - (x**3 + x**2 - 58*x + 1294)
print("  W26 (-7,37):", W26c(-7, 37) == 0, " (8,37):", W26c(8, 37) == 0)
W34c = lambda x, y: y*y + y - (x**3 - x)
print("  W34 (0,0):", W34c(0, 0) == 0)
W46c = lambda x, y: y*y + y - (x**3 - 525*x + 10156)
print("  W46 (25,112):", W46c(25, 112) == 0, " (-20,112):", W46c(-20, 112) == 0, " (70,562):", W46c(70, 562) == 0)