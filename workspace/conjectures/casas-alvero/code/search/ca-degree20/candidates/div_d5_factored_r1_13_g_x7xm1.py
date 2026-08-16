from sympy import symbols
x = symbols('x')
# CONSTRUCTION div-d5: f = (x-r)^m * g.  f = (x-1)^13 * (x^7 - x - 1).
# Root 1 mult 13 covers 1..12; multi-term irreducible degree-7 tail. Full
# 20-term support (heavy root not at zero -> no sparse collapse).
f = (x - 1)**13 * (x**7 - x - 1)
