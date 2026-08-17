#!/usr/bin/env python3
"""Cofactor certificates for the Bautin-trick ideal memberships.

For each membership L_d in <L4,L6,L8> (d = 10,12,14), verified to hold by
exact Groebner reduction over QQ, emit the identity

    L_d  =  q1*L4 + q2*L6 + q3*L8        (q_i rational polynomials)

by taking the quotients that the reduction returns and re-checking the
identity by direct expansion.  The identity check is the certificate a
Lean formalisation can consume (cofactor proof of ideal membership).

Also emits the non-membership verdict for L8 in <L4,L6> (no identity
exists; the reduction remainder is nonzero).

Exact, no floats.  Bounded degree 14.
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

# ---- non-membership L8 in <L4,L6> ----
G46 = sp.groebner([obstruction[4], obstruction[6]], *params, order="lex")
out8 = G46.reduce(num(obstruction[8]))
rem8 = out8[-1]
print("L8 in <L4,L6> non-membership: remainder nonzero?",
      sp.simplify(rem8) != 0, flush=True)

# ---- memberships with cofactor certificates ----
G = sp.groebner([obstruction[4], obstruction[6], obstruction[8]],
                *params, order="lex")
for d in (10, 12, 14):
    out = G.reduce(num(obstruction[d]))
    quots, rem = out[:-1], out[-1]
    identity = sp.expand(
        num(obstruction[d])
        - (quots[0] * num(obstruction[4])
           + quots[1] * num(obstruction[6])
           + quots[2] * num(obstruction[8])))
    total_terms = sum(len(sp.Poly(q, *params).terms()) for q in quots)
    print(f"L{d}: remainder==0 -> {sp.simplify(rem) == 0}; "
          f"identity L{d}==q1*L4+q2*L6+q3*L8 -> {identity == 0}; "
          f"cofactor total monomial terms: {total_terms}", flush=True)

print(f"total: {time.time()-t0:.0f}s", flush=True)