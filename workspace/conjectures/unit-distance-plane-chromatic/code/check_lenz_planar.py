"""Check the planar restriction of the Lenz construction exactly.

Lenz configuration (as reported in Erdos 1946, formalised for d >= 4 by
Swanepoel 2008): p = d/2 circles of radius 1/sqrt(2) centred at the origin in
pairwise orthogonal 2-planes; any two points on *different* circles are at
unit distance.

In the PLANE (d = 2, p = 1) there is only one circle, so only the chord
geometry matters. This script checks, in exact arithmetic:

1. On the circle of radius 1/sqrt(2), two points at central angle theta are at
   unit distance iff theta = 90 degrees.
2. Hence from any point on the circle exactly two other points (at +-90 deg)
   can be at unit distance: degree <= 2, chi <= 3 for any single-circle set.
3. The 'different circles' all-pairs-at-unit-distance trick cannot exist in the
   plane: two unit circles in the plane intersect in at most two points, so
   cross-circle unit pairs are at most O(1) per pair of points.

Uses sympy exact arithmetic; no floats anywhere.
"""
import sympy as sp

r = 1 / sp.sqrt(2)          # exact radius
theta = sp.Symbol("theta", real=True)

# chord length between two points on the circle at central angle theta
chord2 = (2 * r * sp.sin(theta / 2)) ** 2   # squared length
# chord = 1  <=>  chord2 = 1
sols = sp.solve(sp.Eq(sp.simplify(chord2), 1), theta)
print("solutions of chord^2 = 1 on circle radius 1/sqrt(2):")
for s in sols:
    print("  theta =", s, " degrees =", sp.deg(s))

# Neighbour count: from angle 0, which angles phi have chord length 1?
phi = sp.Symbol("phi", real=True)
chord2_phi = sp.simplify((2 * r * sp.sin(phi / 2)) ** 2)
eq = sp.Eq(chord2_phi, 1)
# reduce to cos form and find phi in [0, 2pi)
cos_phi = sp.solve(sp.Eq(sp.simplify(chord2_phi), 1)
                   .rewrite(sp.cos), sp.cos(phi))
print("\ncos(phi) values giving unit chord from angle 0:", cos_phi)
print("=> phi in {pi/2, 3pi/2} modulo 2pi: exactly two distinct points.")

# Two circles of radius 1/sqrt(2) in the plane: intersection of unit-distance
# constraints. A point on circle 2 at unit distance from a fixed point p of
# circle 1 lies on the unit circle around p; circles intersect in <= 2 points,
# so each p has <= 2 neighbours on the other circle -> cross degree <= 2.
print("\nCross-circle (two concentric circles) degree check:")
# circles radius r and s, centre 0. |z - r e^{ia}| = 1 with |z| = s:
#   s^2 + r^2 - 2rs cos(a-b) = 1  (law of cosines, exact)
s = sp.Symbol("s", positive=True)
a, b = sp.Symbol("a", real=True), sp.Symbol("b", real=True)
cross_eq = sp.Eq(sp.simplify(s ** 2 + r ** 2 - 2 * s * r * sp.cos(a - b)), 1)
print("cross-circle condition:", cross_eq)
print("solutions for cos(a-b):",
      sp.solve(cross_eq, sp.cos(a - b)))
# for s = r = 1/sqrt(2): cos(a-b) = (1 - 1/2 - 1/2)/(-1) = 0 -> 90deg again;
# generically at most 2 solutions in [0,2pi). So cross degree <= 2.