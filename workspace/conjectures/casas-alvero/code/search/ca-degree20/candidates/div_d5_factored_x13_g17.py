from sympy import symbols
x = symbols('x')
# CONSTRUCTION div-d5: f = (x-r)^m * g.  f = x^13 * (x-1)^7.  Two recycled
# roots (0 mult 13, 1 mult 7), pure multiplicity, the classic near-CA shape.
f = x**13 * (x - 1)**7
