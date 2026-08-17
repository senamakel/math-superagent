from sympy import symbols
x = symbols('x')
# CONSTRUCTION div2 (c): f = (x-r)^m * g. f = x^15 * (x^5 - x - 1):
# root 0 mult 15 covers 1..14; irreducible deg-5 tail (distinct roots).
f = x**15*(x**5 - x - 1)
