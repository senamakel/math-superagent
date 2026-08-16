from sympy import symbols
x = symbols('x')
# CONSTRUCTION div-d5: f = (x-r)^m * g.  f = (x-1)^14 * (x-2)^6.  Two heavy
# recycled roots: 1 mult 14, 2 mult 6. Pure multiplicity structure, no cross
# sharing between the two roots (the recycled-roots locus).
f = (x - 1)**14 * (x - 2)**6
