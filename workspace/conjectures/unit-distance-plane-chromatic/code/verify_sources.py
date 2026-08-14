#!/usr/bin/env python3
"""
Scholar verification of the load-bearing sourced claims that are cheap to
check mechanically. Everything exact (rational / sqrt arithmetic via cmath-free
algebra). All output goes to code/out/verify_sources.captured.txt.

Checks:
  A. Eisenstein lattice: the six unit vectors of Z[omega] all have squared
     norm exactly 1; no other small Eisenstein integer does. Norm N(x+y omega)
     = x^2 - xy + y^2.
  B. Minkowski sum unit-distance condition |(a1-a2)+(b1-b2)|^2 = 1 is a
     tautology of the definition; verify the 9-point sum of two unit
     equilateral triangles is a unit-distance graph and count its edges.
  C. Chromatic number of that 9-vertex triangle-sum, computed exactly with a
     brute backtracking oracle. Directly probes the run's central open
     question: do Minkowski sums of small colourable graphs raise chi?
"""
from itertools import combinations

# --- exact complex a+b*sqrt(-3) arithmetic, but we only need squared norms ---
# Represent z = x + y*sqrt(-3), x,y rationals (Eisenstein integers have x,y
# integers/2).  Squared modulus |z|^2 = x^2 + 3y^2.

def eis_norm2(x, y):
    """|x + y*sqrt(-3)|^2 = x^2 + 3 y^2 for rational x,y (exact)."""
    return x * x + 3 * y * y

print("=== A. Eisenstein lattice unit vectors ===")
# Basis: omega = (-1+sqrt(-3))/2.  Write z = a + b*omega, a,b integers.
# z = a + b*(-1+sqrt(-3))/2 = (a - b/2) + (b/2)*sqrt(-3).
unit_vectors = []
for a in range(-3, 4):
    for b in range(-3, 4):
        x = a - b / 2          # real part, rational
        y = b / 2              # sqrt(-3) coefficient
        # use Fraction to keep it exact
        from fractions import Fraction
        xf = Fraction(2 * a - b, 2)
        yf = Fraction(b, 2)
        n2 = xf * xf + 3 * yf * yf
        if n2 == 1:
            unit_vectors.append((a, b))
print("Eisenstein integers with |z|^2 = 1 in [-3,3]^2:", len(unit_vectors))
print("  the vectors:", sorted(unit_vectors))
# expected six: units of Z[omega] = {+-1, +-omega, +-(1+omega)}
print("  [should be the 6 units; |z|^2=1 iff z is a unit vector]")

# also confirm N(a+b omega) = a^2 - ab + b^2 form
def eis_norm_ab(a, b):
    return a * a - a * b + b * b
ok = all(eis_norm_ab(a, b) == 1 for (a, b) in unit_vectors)
print("  all six satisfy a^2-ab+b^2=1:", ok)

print()
print("=== B. Minkowski sum of two unit equilateral triangles ===")
# Use exact coordinates in Q(sqrt3).  Triangle points via rotated vectors.
# Work with the Eisenstein lattice: triangle = {0, 1, (1+sqrt(-3))/2}.
# Represent as (real, imag*sqrt3) pairs of Fractions.
from fractions import Fraction as F
def T():
    return [(F(0), F(0)), (F(1), F(0)),
            (F(1, 2), F(1, 2))]  # (1+sqrt(-3))/2 = 1/2 + i sqrt3/2

def add(p, q):
    return (p[0] + q[0], p[1] + q[1])

def sqdist(p, q):
    dx = p[0] - q[0]
    dy = p[1] - q[1]
    return dx * dx + 3 * dy * dy   # |x + i sqrt3 y|^2 = x^2 + 3 y^2

A = T()
B = T()
S = sorted({add(p, q) for p in A for q in B})
print("|A+B| =", len(S), "(expected 9: no colliding sums)")
# unit-distance graph on S
n = len(S)
edges = []
for i, j in combinations(range(n), 2):
    if sqdist(S[i], S[j]) == 1:
        edges.append((i, j))
m = len(edges)
print("unit edges in triangle-sum:", m)
print("vertices:", n)
# edge density
print("avg degree =", 2 * m / n if n else 0)

print()
print("=== C. Chromatic number of the triangle-sum ===")
adj = [set() for _ in range(n)]
for i, j in edges:
    adj[i].add(j); adj[j].add(i)

def is_k_colorable(adj, k):
    colour = [-1] * n
    colour[0] = 0
    order = list(range(n))
    def ok(v, c):
        return all(colour[u] != c for u in adj[v])
    def bt(idx):
        if idx == n:
            return True
        v = order[idx]
        if v == 0:
            return bt(idx + 1)
        for c in range(k):
            if ok(v, c):
                colour[v] = c
                if bt(idx + 1):
                    return True
                colour[v] = -1
        return False
    if bt(1):
        return True
    return False

for k in (1, 2, 3, 4):
    print(f"  triangle-sum {k}-colourable:", is_k_colorable(adj, k))
