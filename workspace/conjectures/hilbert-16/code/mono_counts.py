#!/usr/bin/env python3
"""Compute the Bautin focal-value obstructions L_d (even d) for the chart
family Q1 = A u^2 + C u v + D v^2, Q2 = E u v + F v^2 with rotation linear
part, and report each L_d's monomial count and homogeneous degree exactly.

This reproduces the held audit (L4 has 4 monomials, L6 has 30) and extends
the monomial-count sequence to degrees 8, 10, 12, 14 -- the numbers lyap_extend
computed but crashed before printing. No Groebner reductions here (that is
what made the full run time out); just the exact linear blocks.
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


t0 = time.time()
V = {2: (u**2 + v**2) / 2}
obstruction = {}
for degree in range(3, 15):
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
    print(f"degree {degree}: done ({time.time()-t0:.0f}s)", flush=True)

print("\nReconciled against held audit:", flush=True)
print("  L4 == (AC+CD+2DF-EF)/8 ?",
      sp.factor(8 * obstruction[4] - (A*C + C*D + 2*D*F - E*F)) == 0, flush=True)

print("\nd  monomials  hdeg", flush=True)
counts = []
for d in (4, 6, 8, 10, 12, 14):
    e = sp.expand(sp.together(obstruction[d]))
    num, den = sp.fraction(e)
    if den != 1:
        print(f"{d}  NOT a polynomial (denominator present)", flush=True)
        counts.append(None)
        continue
    p = sp.Poly(num, *params)
    monoms = p.terms()
    degs = [sum(m) for m, _ in monoms]
    hdeg = degs[0] if all(x == degs[0] for x in degs) else None
    counts.append(len(monoms))
    # the leading (largest) coefficient, as a sign/dimension sanity check
    print(f"{d}  {len(monoms):9d}  {str(hdeg):5s}", flush=True)

print("\nmonomial-count sequence L_d for d=4,6,8,10,12,14:",
      counts, flush=True)
print("total wall time: %.0fs" % (time.time() - t0), flush=True)
