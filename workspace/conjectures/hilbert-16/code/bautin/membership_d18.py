#!/usr/bin/env python3
"""Bautin-trick membership at degree 18 — the falsifier check for the
quadratic-complement conjecture.

Runs the focal-value (obstruction) recurrence through even degree 18 for the
5-parameter chart family Q1=A u^2+C u v+D v^2, Q2=E u v+F v^2, rotation
R(p)=-v p_u+u p_v, V2=(u^2+v^2)/2, gauge c_{k,0}=0, obstruction L_d at even
degree.  Computes the exact monomial count of L18 over (A,C,D,E,F), then tests
lex-Groebner membership of L18 in <L4,L6,L8> over QQ cross-checked by
G.contains, and re-verifies L10 in <L4,L6,L8> as a same-run sanity chain.

Exact sympy rational arithmetic, no floats.  This is the falsifier degree for
verify_quadratic_complement.py, which predicts a_18 = 2392.
"""
import sympy as sp
import time
import sys

max_degree = int(sys.argv[1]) if len(sys.argv) > 1 else 18

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


t0 = time.time()
V = {2: (u**2 + v**2) / 2}
obstruction = {}
for degree in range(3, max_degree + 1):
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

print(f"recurrence through degree {max_degree}: {time.time()-t0:.1f}s", flush=True)

# sanity guards against the held audit
print(f"sanity guard: 8*L4 == AC+CD+2DF-EF : "
      f"{sp.simplify(num(8*obstruction[4] - (A*C + C*D + 2*D*F - E*F))) == 0}",
      flush=True)

# monomial counts of even-degree obstructions (exact over A,C,D,E,F)
counts = {}
print(f"\nd  monomials  hdeg")
for d in range(4, max_degree + 1, 2):
    h = d - 2
    cnt = len(sp.Poly(num(obstruction[d]), *params).terms())
    counts[d] = cnt
    print(f"{d:<2d}  {cnt:9d}  {h:<3d}", flush=True)
print(f"monomial counts L_d (d=4..{max_degree} even): "
      f"{[counts[d] for d in range(4, max_degree+1, 2)]}", flush=True)

# membership chain (lex, exact over QQ)
if max_degree >= 18:
    r10 = in_ideal(obstruction[10], [obstruction[4], obstruction[6], obstruction[8]],
                   "L10 in <L4,L6,L8>")
    r18 = in_ideal(obstruction[18], [obstruction[4], obstruction[6], obstruction[8]],
                   "L18 in <L4,L6,L8>")
    print(f"monomial count L18: {counts[18]}", flush=True)
    print(f"SUMMARY: L10 in <L4,L6,L8> = {r10}; L18 in <L4,L6,L8> = {r18}", flush=True)
else:
    r10 = in_ideal(obstruction[10], [obstruction[4], obstruction[6], obstruction[8]],
                   "L10 in <L4,L6,L8>")
    print(f"monomial count L10: {counts[10]}", flush=True)
    print(f"SUMMARY (sanity run): L10 in <L4,L6,L8> = {r10}", flush=True)
print(f"total: {time.time()-t0:.0f}s", flush=True)
