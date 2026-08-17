from sympy import symbols
x = symbols('x')
# CONSTRUCTION div2 (c): f = (x-r)^m * g. f = (x+2)^14 * (x^6 - x - 1):
# root -2 mult 14 covers 1..13; irreducible multi-term deg-6 tail.
f = (x + 2)**14*(x**6 - x - 1)
