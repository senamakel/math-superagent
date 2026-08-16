from sympy import symbols
x = symbols('x')
# CONSTRUCTION div-d1: TRINOMIAL (three powers in the support, degree 20).
# x^20 - 3x^3 - 2x^2 : two "exposed" monomial positions in the low range.
f = x**20 - 3*x**3 - 2*x**2
