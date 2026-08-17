#!/usr/bin/env python3
"""Bautin-trick ideal membership, full extension to degree 14, with a
second-route cross-check (G.contains) on every membership verdict.

Recurrence identical to mono_counts.py (which took 428 s wall to degree 14).
The only groebner bases built are 2- and 3-generator sets over the 5-variable
homogeneous grading ring, checking:
    L8  in <L4,L6>            -> expected False (3 generators needed)
    L10 in <L4,L6,L8>         -> expected True
    L12 in <L4,L6,L8>         -> expected True
    L14 in <L4,L6,L8>         -> the open question (Bautin trick survives?)
Each verdict is cross-checked by G.contains, an independent sympy path.
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
    print(f"degree {degree}: done ({time.time()-t0:.0f}s)", flush=True)


def in_ideal(target, gens, label):
    b = time.time()
    G = sp.groebner(gens, *params, order="lex")
    out = G.reduce(num(target))
    rem = out[-1]
    via_reduce = (sp.simplify(rem) == 0)
    via_contains = G.contains(num(target))
    ok = (via_reduce == via_contains)
    print(f"{label}: reduce->{via_reduce}  contains->{via_contains}  "
          f"agree={ok} ({time.time()-b:.1f}s)", flush=True)
    return ok and via_reduce


results = {}
results["L8 in <L4,L6>"] = in_ideal(
    obstruction[8], [obstruction[4], obstruction[6]], "L8 in <L4,L6>")
results["L10 in <L4,L6,L8>"] = in_ideal(
    obstruction[10], [obstruction[4], obstruction[6], obstruction[8]],
    "L10 in <L4,L6,L8>")
results["L12 in <L4,L6,L8>"] = in_ideal(
    obstruction[12], [obstruction[4], obstruction[6], obstruction[8]],
    "L12 in <L4,L6,L8>")
results["L14 in <L4,L6,L8>"] = in_ideal(
    obstruction[14], [obstruction[4], obstruction[6], obstruction[8]],
    "L14 in <L4,L6,L8>")

print("\nSUMMARY:", results)
print("total: %.0fs" % (time.time() - t0))