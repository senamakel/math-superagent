<!-- source: https://arxiv.org/src/2607.13785v2/anc/h14_3_reproducibility/certificates/verify_bautin_recurrence.py | converted from plain text -->

#!/usr/bin/env python3
"""Exact audit for blueprint equations (B9b1)--(B9c)."""

import sympy as sp

u, v = sp.symbols("u v")
A, C, D, E, F = sp.symbols("A C D E F")
Q1 = A * u**2 + C * u * v + D * v**2
Q2 = E * u * v + F * v**2

def rotation(poly):
    return sp.expand(-v * sp.diff(poly, u) + u * sp.diff(poly, v))

V = {2: (u**2 + v**2) / 2}
obstruction = {}
for degree in range(3, 7):
    coeffs = sp.symbols(f"c{degree}_0:{degree + 1}")
    correction = sum(
        coeffs[j] * u ** (degree - j) * v**j
        for j in range(degree + 1)
    )
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
    equations = [
        polynomial.coeff_monomial(u ** (degree - j) * v**j)
        for j in range(degree + 1)
    ]
    if degree % 2 == 0:
        equations.append(coeffs[0])

    solution = sp.solve(equations, unknowns, dict=True, simplify=False)[0]
    V[degree] = sp.expand(correction.subs(solution))
    if radial is not None:
        obstruction[degree] = sp.factor(solution[radial])

assert sp.factor(
    8 * obstruction[4] - (A * C + C * D + 2 * D * F - E * F)
) == 0

G6 = sp.Poly(
    sp.expand(Q1 * sp.diff(V[5], u) + Q2 * sp.diff(V[5], v)), u, v
)
g6 = [G6.coeff_monomial(u ** (6 - j) * v**j) for j in range(7)]
weighted_g6 = 5 * g6[0] + g6[2] + g6[4] + 5 * g6[6]
assert sp.factor(obstruction[6] - weighted_g6 / 16) == 0

P = (
    76 * A**3 * C + 24 * A**3 * F + 142 * A**2 * C * D
    + 29 * A**2 * C * E + 192 * A**2 * D * F - 96 * A**2 * E * F
    + 23 * A * C**3 + 109 * A * C**2 * F + 76 * A * C * D**2
    + 42 * A * C * D * E + 3 * A * C * E**2 + 144 * A * C * F**2
    + 132 * A * D**2 * F - 28 * A * D * E * F - 37 * A * E**2 * F
    - 24 * A * F**3 + 23 * C**3 * D + 159 * C**2 * D * F
    - 27 * C**2 * E * F + 10 * C * D**3 + 13 * C * D**2 * E
    + 3 * C * D * E**2 + 350 * C * D * F**2 - 101 * C * E * F**2
    + 20 * D**3 * F + 16 * D**2 * E * F - 27 * D * E**2 * F
    + 248 * D * F**3 + E**3 * F - 124 * E * F**3
)
assert sp.factor(-12 * weighted_g6 - P) == 0
assert sp.factor(192 * obstruction[6] + P) == 0
assert len(sp.Poly(P, A, C, D, E, F).terms()) == 30

print("B9b/B9c recurrence audit: exact; degree-six monomials: 30")
