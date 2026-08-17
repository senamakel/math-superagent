#!/usr/bin/env python3
"""Extend the Lu-paper Bautin focal-value computation beyond the held audit.

The audit (blueprint eqs (B9b1)-(B9c)) computes the even-degree obstructions
L_4, L_6 (focal values) of the chart family

    Q1 = A u^2 + C u v + D v^2 ,   Q2 = E u v + F v^2 ,   linear part = rotation,

and asserts they are the polynomials with 4 and 30 monomials.  This program
continues the same exact recurrence to degrees 8, 10, 12 and reports:

  * obstruction[d] for each even d, checked to be a genuine polynomial in
    (A,C,D,E,F), with monomial count and (homogeneous) degree;
  * ideal membership L_10, L_12 in <L_4, L_6, L_8> (exact Groebner reduction
    over Q) — the Bautin-trick statement: the third focal value generates the
    rest of the focal-value ideal;
  * non-membership of L_8 in <L_4, L_6>, L_6 in <L_4> (independence of the
    first three generators).

Everything exact (sympy, QQ rationals).  Bounded degree 12 -> polynomial time.
"""
import sympy as sp
import time

u, v = sp.symbols("u v")
A, C, D, E, F = sp.symbols("A C D E F")
params = [A, C, D, E, F]
Q1 = A * u**2 + C * u * v + D * v**2
Q2 = E * u * v + F * v**2


def rotation(poly):
    return sp.expand(-v * sp.diff(poly, u) + u * sp.diff(poly, v))


def poly_terms(poly_expr):
    """(monomial_count, homogeneous_degree, is_polynomial) of an expression
    in the five parameters, exact."""
    e = sp.expand(sp.together(poly_expr))
    num, den = sp.fraction(e)
    if den != 1:
        return None
    p = sp.Poly(num, *params)
    degs = [sum(m) for _, m in p.terms()]
    hdeg = degs[0] if all(d == degs[0] for d in degs) else None
    return len(p.terms()), hdeg


t0 = time.time()
V = {2: (u**2 + v**2) / 2}
obstruction = {}
V_detail = {}
for degree in range(3, 13):
    coeffs = sp.symbols(f"c{degree}_0:{degree + 1}")
    correction = sum(coeffs[j] * u ** (degree - j) * v**j
                     for j in range(degree + 1))
    unknowns = list(coeffs)
    equation = sp.expand(
        rotation(correction)
        + Q1 * sp.diff(V[degree - 1], u)
        + Q2 * sp.diff(V[degree - 1], v)
    )
    radial = None
    if degree % 2 == 0:
        radial = sp.symbols(f"L{degree}")
        unknowns.append(radial)
        equation -= radial * (u**2 + v**2) ** (degree // 2)
    polynomial = sp.Poly(equation, u, v)
    equations = [polynomial.coeff_monomial(u ** (degree - j) * v**j)
                 for j in range(degree + 1)]
    if degree % 2 == 0:
        equations.append(coeffs[0])
    solution = sp.solve(equations, unknowns, dict=True, simplify=False)[0]
    V[degree] = sp.expand(correction.subs(solution))
    if radial is not None:
        obstruction[degree] = sp.factor(solution[radial])

print(f"recurrence through degree 12: {time.time() - t0:.1f}s")

print("\nd  monomials  hdeg  is_polynomial")
for d in (4, 6, 8, 10, 12):
    info = poly_terms(obstruction[d])
    if info is None:
        print(f"{d}  NOT a polynomial (rational with denominator)")
    else:
        print(f"{d}  {info[0]:9d}  {str(info[1]):5s}  yes")

# ---- ideal membership, exact Groebner reduction over QQ ----
b = time.time()
G368 = sp.groebner([obstruction[4], obstruction[6], obstruction[8]],
                   *params, order="lex")
rem10, _ = G368.reduce(sp.expand(sp.together(obstruction[10])))
rem12, _ = G368.reduce(sp.expand(sp.together(obstruction[12])))
print(f"groebner reduction: {time.time() - b:.1f}s")
print("L10 in <L4,L6,L8>: remainder == 0 ?", sp.simplify(rem10) == 0)
print("L12 in <L4,L6,L8>: remainder == 0 ?", sp.simplify(rem12) == 0)

b = time.time()
G46 = sp.groebner([obstruction[4], obstruction[6]], *params, order="lex")
rem8, _ = G46.reduce(sp.expand(sp.together(obstruction[8])))
print("L8 in <L4,L6>:     remainder == 0 ?", sp.simplify(rem8) == 0)
G4 = sp.groebner([obstruction[4]], *params, order="lex")
rem6, _ = G4.reduce(sp.expand(sp.together(obstruction[6])))
print("L6 in <L4>:        remainder == 0 ?", sp.simplify(rem6) == 0)
print(f"independence checks: {time.time() - b:.1f}s")

print("\nmonomial-count sequence L_d (d = 4,6,8,10,12):",
      [poly_terms(obstruction[d])[0] for d in (4, 6, 8, 10, 12)])