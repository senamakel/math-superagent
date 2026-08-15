"""Verify the hand-derived A2 hexagonal 7-colouring margin before anything
rests on it. Numbers must come from a program, not memory."""
from sympy import sqrt, Rational, simplify, N

sqrt3 = sqrt(3)
sqrt7 = sqrt(7)
sqrt21 = sqrt(21)

# A2 triangular lattice, nearest-neighbour centre spacing = sqrt3 * L
# (adjacent regular hexagons of side L have centre distance 2 * apothem
#  = 2 * (sqrt3/2 * L) = sqrt3 * L).
# The 7-colouring = reduction mod the ideal (2-omega) of Z[omega], norm 7,
# so the minimal same-colour centre vector has norm 7 in the lattice where
# nearest neighbours have norm 1. Hence same-colour centre distance
#  = sqrt7 * sqrt3 * L = sqrt21 * L.
same_colour_centre = sqrt7 * sqrt3  # times L

# Properness: two same-colour hexagons (circumradius L) must be > 1 apart at
# their closest points => centre distance - 2L > 1  =>  (sqrt21 - 2)L > 1.
# Within-cell: hexagon diameter 2L < 1 => L < 1/2.
window_lo = 1 / (sqrt21 - 2)
window_hi = Rational(1, 2)

print("same-colour centre distance factor =", same_colour_centre,
      "=", N(same_colour_centre))
print("valid L window:", N(window_lo), "< L <", N(window_hi))
print("window nonempty:", simplify(window_lo < window_hi))

# Min same-colour separation at the extremal L -> 1/2:
sep_at_half = (sqrt21 - 2) * Rational(1, 2)
print("min same-colour separation at L=1/2:", N(sep_at_half))

# Thickening form: radius rho = L (circumradius), need sqrt21*L > 1 + 2L,
# same inequality.
print("thickening condition identical:",
      simplify(sqrt21 - 2 > Rational(0)))
