#!/usr/bin/env python3
"""Cheap Bautin-trick ideal-membership tests over QQ (exact), small sets."""
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
    sol = sp.solve(equations, unknowns, dict=True, simplify=False)[0]
    V[degree] = sp.expand(correction.subs(sol))
    if radial is not None:
        obstruction[degree] = sp.factor(sol[radial])
print(f"recurrence through degree 12: {time.time() - t0:.1f}s", flush=True)


def in_ideal(target, gens, label):
    b = time.time()
    G = sp.groebner(gens, *params, order="lex")
    out = G.reduce(num(target))
    rem = out[-1]  # remainder is the last element (quotients first)
    res = (sp.simplify(rem) == 0)
    print(f"{label}: remainder==0 ? {res} ({time.time()-b:.1f}s)", flush=True)
    return res


in_ideal(obstruction[8], [obstruction[4], obstruction[6]], "L8 in <L4,L6>")
in_ideal(obstruction[10], [obstruction[4], obstruction[6], obstruction[8]],
         "L10 in <L4,L6,L8>")
in_ideal(obstruction[12], [obstruction[4], obstruction[6], obstruction[8]],
         "L12 in <L4,L6,L8>")
in_ideal(obstruction[14], [obstruction[4], obstruction[6], obstruction[8]],
         "L14 in <L4,L6,L8>")
