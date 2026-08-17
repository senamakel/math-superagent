#!/usr/bin/env python3
"""Bautin-trick membership at degree 16 — the falsifier check.

Tests whether L16 (16th focal-value obstruction) lies in <L4,L6,L8> over QQ,
lex Groebner.  If TRUE, the 3-generator generation claim survives to d=16;
if FALSE, it dies here.  Cross-checked by G.contains on every verdict.
Exact sympy, no floats.  Recurrence to degree 16 (~30 min wall).
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
for degree in range(3, 17):
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
    print(f"degree {degree}: done ({time.time()-t0:.0f}s cumulative)", flush=True)


def in_ideal(target, gens, label):
    b = time.time()
    G = sp.groebner(gens, *params, order="lex")
    out = G.reduce(num(target))
    rem = out[-1]
    via_reduce = (sp.simplify(rem) == 0)
    via_contains = G.contains(num(target))
    print(f"{label}: reduce->{via_reduce}  contains->{via_contains}  "
          f"agree={via_reduce == via_contains} ({time.time()-b:.1f}s)",
          flush=True)
    return via_reduce and via_contains


r16 = in_ideal(obstruction[16], [obstruction[4], obstruction[6], obstruction[8]],
               "L16 in <L4,L6,L8>")
# re-state the earlier degrees in the same run for a same-run sanity chain
r10 = in_ideal(obstruction[10], [obstruction[4], obstruction[6], obstruction[8]],
               "L10 in <L4,L6,L8>")
print(f"monomial count L16: {len(sp.Poly(num(obstruction[16]), *params).terms())}",
      flush=True)
print(f"SUMMARY: L10 in <L4,L6,L8> = {r10}; L16 in <L4,L6,L8> = {r16}", flush=True)
print(f"total: {time.time()-t0:.0f}s", flush=True)
