#!/usr/bin/env python3
"""generate_p30.py — emit the 30 monomials of the degree-6 Bautin-obstruction
polynomial P30 as an exact Lean `def`s under code/lean/Lib/Generated/, using a
deterministic monomial order so the generated file is stable.

The coefficients are computed from the SAME recurrence used in
code/bautin/verify_lu_core.py (rotation operator, V2..V5, weighted_g6), and
P30 is defined as -12*weighted_g6. This is the untrusted *data* layer: the
Lean file is generated, and the checker (outside Generated/) is written by
hand and is what carries the theorem.

Monomial order (deterministic): lexicographic on (deg_A, deg_C, deg_D, deg_E,
deg_F). The Lean def names the monomials m_i : Fin 5 -> Fin 5 with m_i j =
exponent of variable j, and coeffs : Fin 30 -> ℤ.
"""

import sympy as sp

A, C, D, E, F = sp.symbols("A C D E F")

u, v = sp.symbols("u v")
Q1 = A * u**2 + C * u * v + D * v**2
Q2 = E * u * v + F * v**2


def rotation(poly):
    return sp.expand(-v * sp.diff(poly, u) + u * sp.diff(poly, v))


V = {2: (u**2 + v**2) / 2}
for degree in range(3, 6):  # V3, V4, V5; P30 only needs weighted_g6 (degree 6)
    cs = sp.symbols(f"c{degree}_0:{degree + 1}")
    correction = sum(cs[j] * u ** (degree - j) * v**j for j in range(degree + 1))
    unknowns = list(cs)
    equation = sp.expand(
        rotation(correction) + Q1 * sp.diff(V[degree - 1], u) + Q2 * sp.diff(V[degree - 1], v)
    )
    radial = None
    if degree % 2 == 0:
        radial = sp.symbols(f"L{degree}")
        unknowns.append(radial)
        equation -= radial * (u**2 + v**2) ** (degree // 2)
    polynomial = sp.Poly(equation, u, v)
    eqs = [polynomial.coeff_monomial(u ** (degree - j) * v**j) for j in range(degree + 1)]
    if degree % 2 == 0:
        eqs.append(cs[0])
    sol = sp.solve(eqs, unknowns, dict=True)[0]
    V[degree] = sp.expand(correction.subs(sol))

G6 = sp.Poly(sp.expand(Q1 * sp.diff(V[5], u) + Q2 * sp.diff(V[5], v)), u, v)
g6 = [G6.coeff_monomial(u ** (6 - j) * v**j) for j in range(7)]
weighted_g6 = sp.expand(5 * g6[0] + g6[2] + g6[4] + 5 * g6[6])
P30_expr = sp.expand(-12 * weighted_g6)

# coefficient dict {monomial: coefficient}
coeff_dict = P30_expr.as_coefficients_dict()
monomials = sorted(
    coeff_dict.keys(),
    key=lambda m: (m.as_dict().get(A, 0), m.as_dict().get(C, 0),
                   m.as_dict().get(D, 0), m.as_dict().get(E, 0),
                   m.as_dict().get(F, 0)),
)
assert len(monomials) == 30, f"expected 30 monomials, got {len(monomials)}"

# sanity: recompute P30 from the emitted data and compare
data_rebuilt = sum(coeff_dict[m] * m for m in monomials)
assert sp.expand(data_rebuilt - P30_expr) == 0

lines = []
lines.append("/- Generated data: the 30 monomials and integer coefficients of the")
lines.append("degree-6 Bautin-obstruction polynomial P30 = -12*weighted_g6.")
lines.append("UNTRUSTED: produced by code/bautin/generate_p30.py (sympy, exact),")
lines.append("same recurrence as code/bautin/verify_lu_core.py. No theorems here.")
lines.append("The checker in BautinRecurrence.lean (written by hand) is what")
lines.append("verifies the identity 192*L6 + P30 = 0. -/")
lines.append("")
lines.append("import Mathlib.Algebra.MvPolynomial.Basic")
lines.append("import Mathlib.Data.Int.Basic")
lines.append("")
lines.append("noncomputable section")
lines.append("")
lines.append("namespace LuH14.Generated")
lines.append("")
lines.append("/-- The five variables A,C,D,E,F of the Bautin recurrence. -/")
lines.append("abbrev Var := Fin 5")
lines.append("")
lines.append("/-- The 30 monomials m_i : Var -> Var of P30 (exponent vectors), in")
lines.append("the deterministic lexicographic order used by the generator. -/")
lines.append("def ms : Fin 30 -> Var -> Var :=")
lines.append("  ![")
for i, m in enumerate(monomials):
    d = m.as_dict()
    exps = [d.get(A, 0), d.get(C, 0), d.get(D, 0), d.get(E, 0), d.get(F, 0)]
    line = f"    ![{exps[0]}, {exps[1]}, {exps[2]}, {exps[3]}, {exps[4]}]"
    line += "," if i < 29 else ""
    lines.append(line)
lines.append("  ]")
lines.append("")
lines.append("/-- The 30 integer coefficients of P30, matching `ms` term by term. -/")
lines.append("def coeffs : Fin 30 -> ℤ :=")
lines.append("  ![")
for i, m in enumerate(monomials):
    coeff = int(coeff_dict[m])
    line = f"    {coeff}"
    line += "," if i < 29 else ""
    lines.append(line)
lines.append("  ]")
lines.append("")
lines.append("end LuH14.Generated")
lines.append("")
lines.append("end")
lines.append("")

out = "\n".join(lines)
print(out)