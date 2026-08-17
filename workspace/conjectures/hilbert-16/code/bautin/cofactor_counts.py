#!/usr/bin/env python3
"""Cofactor certificates for Bautin-trick ideal memberships, degree 14.

For each L_d in <L4,L6,L8> (d=10,12,14), verified by exact Groebner reduction,
emit the identity L_d = q1*L4 + q2*L6 + q3*L8 (q_i rational polys in A,C,D,E,F)
by reading the quotients the reduction returns, re-checking the identity by
direct expansion, and counting the total monomials across q1,q2,q3 — this last
count is the integer sequence of interest (size of the cofactor certificate).

The G.reduce return of sympy is (quotients, remainder): out[0] is the list of
quotients [q1,q2,q3], out[1] is the remainder.  (The earlier
cofactor_certificate.py read out[:-1] as the quotients, a bug: that picks up
the whole quotient-list as one element.)
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


def num(poly_expr):
    e = sp.expand(sp.together(poly_expr))
    n, _ = sp.fraction(e)
    return n


t0 = time.time()
V = {2: (u**2 + v**2) / 2}
obstruction = {}
for degree in range(3, 15):
    coeffs = sp.symbols(f"c{degree}_0:{degree + 1}")
    correction = sum(coeffs[j] * u ** (degree - j) * v**j
                     for j in range(degree + 1))
    unknowns = list(coeffs)
    equation = sp.expand(
        rotation(correction) + Q1 * sp.diff(V[degree - 1], u)
        + Q2 * sp.diff(V[degree - 1], v))
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
    sol = sp.solve(equations, unknowns, dict=True, simplify=False)[0]
    V[degree] = sp.expand(correction.subs(sol))
    if radial is not None:
        obstruction[degree] = sp.factor(sol[radial])
print(f"recurrence through degree 14: {time.time()-t0:.1f}s", flush=True)

# non-membership L8 in <L4,L6>
G46 = sp.groebner([obstruction[4], obstruction[6]], *params, order="lex")
rem8 = G46.reduce(num(obstruction[8]))[1]
print("L8 in <L4,L6> non-membership: remainder nonzero?",
      sp.simplify(rem8) != 0, flush=True)

G = sp.groebner([obstruction[4], obstruction[6], obstruction[8]],
                *params, order="lex")
for d in (10, 12, 14):
    quots, rem = G.reduce(num(obstruction[d]))
    identity = sp.expand(
        num(obstruction[d])
        - (quots[0] * num(obstruction[4])
           + quots[1] * num(obstruction[6])
           + quots[2] * num(obstruction[8])))
    per = [len(sp.Poly(q, *params).terms()) for q in quots]
    print(f"L{d}: remainder==0 -> {sp.simplify(rem) == 0}; "
          f"identity == 0 -> {identity == 0}; "
          f"cofactor monomial counts q1,q2,q3 = {per}, "
          f"total = {sum(per)}", flush=True)
print(f"total: {time.time()-t0:.0f}s", flush=True)
