#!/usr/bin/env python3
"""
Clean-room verification of the Lu H14^3 finite computational core.

WHAT RAN:      python code/bautin/verify_lu_core.py
WHICH DEFS:    (A) Bautin-recurrence audit: chart family (u,v), quadratic part
                 Q1 = A u^2 + C u v + D v^2,  Q2 = E u v + F v^2,
                 rotation R(p) = -v d/du p + u d/dv p, V2 = (u^2+v^2)/2,
                 homological recurrence at degree k:
                   R(c_k) + Q1 V_{k-1,u} + Q2 V_{k-1,v} = L_k (u^2+v^2)^{k/2}
                 (even k has the radial obstruction L_k; gauge c_{k,0}=0).
               (B) H14^3 field and Darboux data:
                 P = -y - d x + B(x^2 - y^2),  Q = (1+y)(x + d y),
                 L = 1 + y, F = B(B-1)x^2 - B d x y - B^2 y^2
                                 - d(2B-1)x + (d^2-2B)y + d^2 - 1,
                 X = P d/dx + Q d/dy  (Lie derivative).
WHICH IDENTITIES: (A) 8 L4 == AC+CD+2DF-EF  and  192 L6 + P30 == 0
                     where P30 is the 30-monomial polynomial below
                     (equivalently 12 weighted_g6 + P30 == 0);
                 (B) X(L) == (x + d y) L,  X(F) == (2B x + d y) F,
                     div(X) == (x+dy) + (2Bx+dy)  (inverse-integrating-factor
                     cofactor identity).

Everything uses exact sympy rational/symbolic arithmetic; no floats, no
importing of the paper's own scripts (definitions are restated from the
paper's text as read in research/sources/lu-h14-3-hemicycle-html.full.md).
All assertions must PASS.
"""
import sympy as sp

# ---------------- (A) Bautin-recurrence audit, clean room ----------------
u, v = sp.symbols("u v")
A, C, D, E, F = sp.symbols("A C D E F")
Q1 = A * u**2 + C * u * v + D * v**2
Q2 = E * u * v + F * v**2


def rotation(poly):
    """R(p) = -v p_u + u p_v (the rotation / linear-part Lie derivative)."""
    return sp.expand(-v * sp.diff(poly, u) + u * sp.diff(poly, v))


V = {2: (u**2 + v**2) / 2}
obstruction = {}
for degree in range(3, 7):
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
        equations.append(coeffs[0])          # gauge c_{k,0}=0
    sol = sp.solve(equations, unknowns, dict=True, simplify=False)[0]
    V[degree] = sp.expand(correction.subs(sol))
    if radial is not None:
        obstruction[degree] = sp.factor(sol[radial])

#

# degree-4 identity: 8*L4 == AC+CD+2DF-EF
assert sp.factor(8 * obstruction[4] - (A * C + C * D + 2 * D * F - E * F)) == 0
print("(A) 8*L4 == AC+CD+2DF-EF : PASS")

# degree-6: reconstruct weighted_g6 from V5, then compare with the paper's
# 30-monomial P30 (coefficients read from the held certificate's spelling).
G6 = sp.Poly(sp.expand(Q1 * sp.diff(V[5], u) + Q2 * sp.diff(V[5], v)), u, v)
g6 = [G6.coeff_monomial(u ** (6 - j) * v**j) for j in range(7)]
weighted_g6 = 5 * g6[0] + g6[2] + g6[4] + 5 * g6[6]

# P30, the 30-monomial polynomial as spelled out in the certificate
# (76 A^3 C + 24 A^3 F + 142 A^2 C D + ...), coefficients from the held
# verify_bautin_recurrence.py transcription in
# research/summaries/verify_bautin_recurrence.md.
P30 = (
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
assert sp.factor(12 * weighted_g6 + P30) == 0
print("(A) 192*L6 == -P30 (equivalently 12*weighted_g6 + P30 == 0) : PASS")
assert sp.factor(192 * obstruction[6] + P30) == 0
print("(A) 192*L6 + P30 == 0 directly on the obstruction : PASS")
assert len(sp.Poly(P30, A, C, D, E, F).terms()) == 30
print("(A) P30 has exactly 30 monomials : PASS")

# ---------------- (B) Darboux identities, clean room ----------------
x, y, B, mu2, mu4, mu5, d = sp.symbols("x y B mu2 mu4 mu5 d")
P = -y - d * x + B * (x**2 - y**2)
Q = (1 + y) * (x + d * y)
Lf = 1 + y
Ff = (B * (B - 1) * x**2 - B * d * x * y - B**2 * y**2
      - d * (2 * B - 1) * x + (d**2 - 2 * B) * y + d**2 - 1)


def lie(phi):
    """X(phi) = P phi_x + Q phi_y for the field X = P dx + Q dy."""
    return sp.expand(P * sp.diff(phi, x) + Q * sp.diff(phi, y))


assert sp.factor(lie(Lf) - (x + d * y) * Lf) == 0
print("(B) X(L) == (x+d*y)*L : PASS")
assert sp.factor(lie(Ff) - (2 * B * x + d * y) * Ff) == 0
print("(B) X(F) == (2B*x + d*y)*F : PASS")
divX = sp.expand(sp.diff(P, x) + sp.diff(Q, y))
assert sp.factor(divX - ((x + d * y) + (2 * B * x + d * y))) == 0
print("(B) div X == (x+dy)+(2Bx+dy)  (inverse-integrating-factor cofactor) : PASS")

print("\nALL CLEAN-ROOM CHECKS PASS")