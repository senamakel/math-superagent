from sympy import symbols
x = symbols('x')
# CONSTRUCTION div-d5: f = (x-r)^m * g.  f = (x-2)^12 * (x^8 - x^4 - 1).
# Root 2 mult 12 covers 1..11; even-structured multi-term tail. Full support.
f = (x - 2)**12 * (x**8 - x**4 - 1)
