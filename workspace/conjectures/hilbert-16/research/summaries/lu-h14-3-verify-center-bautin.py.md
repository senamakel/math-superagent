<!-- source: https://arxiv.org/src/2607.13785v2/anc/h14_3_reproducibility/certificates/verify_h14_center_bautin.py | converted from plain text -->

#!/usr/bin/env python3
"""Reproduce the focal calculations used in blueprint equations (B9)-(B10)."""

import sympy as sp

u, v = sp.symbols("u v")
A, C, D, E, F = sp.symbols("A C D E F")
a, B, m, d, w, eps = sp.symbols("a B m d w eps")

q1 = A * u**2 + C * u * v + D * v**2
q2 = E * u * v + F * v**2

def linear_part(poly):
    return sp.expand(-v * sp.diff(poly, u) + u * sp.diff(poly, v))

def quadratic_part(poly):
    return sp.expand(q1 * sp.diff(poly, u) + q2 * sp.diff(poly, v))

V = {2: (u**2 + v**2) / 2}
focal = {}

for degree in range(3, 7):
    coeffs = sp.symbols(f"c{degree}_0:{degree + 1}")
    candidate = sum(
        coeffs[j] * u ** (degree - j) * v**j
        for j in range(degree + 1)
    )
    unknowns = list(coeffs)
    target = 0
    if degree % 2 == 0:
        obstruction = sp.symbols(f"L{degree // 2 - 1}")
        unknowns.append(obstruction)
        target = obstruction * (u**2 + v**2) ** (degree // 2)

    equation = sp.Poly(
        linear_part(candidate) + quadratic_part(V[degree - 1]) - target,
        u,
        v,
    )
    equations = [
        equation.coeff_monomial(u ** (degree - j) * v**j)
        for j in range(degree + 1)
    ]
    if degree % 2 == 0:
        equations.append(coeffs[0])  # radial gauge

    solution = sp.solve(
        equations, unknowns, dict=True, simplify=False, rational=True
    )[0]
    V[degree] = sp.expand(candidate.subs(solution))
    if degree % 2 == 0:
        focal[degree] = sp.factor(solution[obstruction])

expected_L1 = (A * C + C * D + 2 * D * F - E * F) / 8
assert sp.simplify(focal[4] - expected_L1) == 0

omega_substitution = {
    A: B / w,
    C: a * (2 * B - 1) / w**2,
    D: (a**2 * (B - 1) + m - a * d) / w**3,
    E: 1 / w,
    F: (a + d) / w**2,
}

ell1 = (
    2 * B**2 * a
    + 2 * B * a * m
    - B * a
    - 2 * a**2 * d
    + a * m
    - 2 * a * d**2
    - a
    + 2 * m * d
    - d
)

L1_sub = sp.together(focal[4].subs(omega_substitution))
num1, den1 = sp.fraction(L1_sub)
num1 = sp.rem(
    sp.Poly(num1, w), sp.Poly(w**2 - (1 - a**2), w)
).as_expr()
assert sp.factor(num1 - ell1) == 0
assert sp.factor(den1 - 8 * w**5) == 0

L2_sub = sp.together(focal[6].subs(omega_substitution))
num2, den2 = sp.fraction(L2_sub)
num2 = sp.rem(
    sp.Poly(num2, w), sp.Poly(w**2 - (1 - a**2), w)
).as_expr()

# Both exact center components annihilate the second focal obstruction.
assert sp.factor(num2.subs({a: 0, d: 0})) == 0
assert sp.factor(num2.subs({m: -B, d: -a})) == 0

# Solve ell1=0 along the radial scaling through the order needed for U(0).
d2, d3 = sp.symbols("d2 d3")
d_series = -eps * a + eps**2 * d2 + eps**3 * d3
scaled_ell1 = sp.expand(
    ell1.subs({a: eps * a, B: eps * B, m: eps * m, d: d_series})
)
eq2 = sp.expand(scaled_ell1).coeff(eps, 2)
solution_d2 = sp.solve(eq2, d2)[0]
d_series = sp.expand(d_series.subs(d2, solution_d2))
scaled_ell1 = sp.expand(
    ell1.subs({a: eps * a, B: eps * B, m: eps * m, d: d_series})
)
eq3 = sp.expand(scaled_ell1).coeff(eps, 3)
solution_d3 = sp.solve(eq3, d3)[0]
d_series = sp.expand(d_series.subs(d3, solution_d3))

root_to_second_order = -a + solution_d2
unscaled_L2 = focal[6].subs(omega_substitution).subs(
    {d: root_to_second_order, w: sp.sqrt(1 - a**2)}
)
scaled_L2 = unscaled_L2.subs(
    {a: eps * a, B: eps * B, m: eps * m}, simultaneous=True
)
series_L2 = sp.series(scaled_L2, eps, 0, 4).removeO().expand()
assert sp.factor(series_L2.coeff(eps, 2) - a * (B + m) / 48) == 0

print("L1 =", sp.factor(focal[4]))
print("L2 universal numerator terms =", len(sp.Poly(sp.together(focal[6]).as_numer_denom()[0], A, C, D, E, F).terms()))
print("H14 L1 numerator check: OK")
print("L2 vanishes on both center components: OK")
print("L2|L1=0 =", sp.factor(series_L2.coeff(eps, 2)), "+ O(eps^3)")
print("U(0) = 1/48")
