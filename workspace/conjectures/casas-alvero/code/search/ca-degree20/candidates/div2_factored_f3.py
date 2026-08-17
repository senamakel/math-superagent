from sympy import symbols
x = symbols('x')
# CONSTRUCTION div2 (c): f = (x-r)^m * g. f = (x-1)^16 * (x^4 - 3x^2 + 1):
# root 1 mult 16 covers 1..15; g has roots at +/-sqrt((3±sqrt5)/2) (distinct,
# non-rational -> multi-term tail that does not collapse to a monomial).
f = (x - 1)**16*(x**4 - 3*x**2 + 1)
