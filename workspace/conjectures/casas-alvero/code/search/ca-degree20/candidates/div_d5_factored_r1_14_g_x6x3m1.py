from sympy import symbols
x = symbols('x')
# CONSTRUCTION div-d5: f = (x-r)^m * g with a GENUINELY MULTI-TERM g and the
# heavy root shifted OFF zero (so the support does NOT collapse to a sparse
# monomial family).  f = (x-1)^14 * (x^6 - x^3 - 1).  Root 1 mult 14 covers
# derivatives 1..13; g is an irreducible-degree-6 tail. Full 20-term support.
f = (x - 1)**14 * (x**6 - x**3 - 1)
