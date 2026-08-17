from sympy import symbols
x = symbols('x')
# CONSTRUCTION div2 (c): f = (x-r)^m * g with g chosen so low derivatives
# share roots. f = (x-1)^15 * (x^5 - 2): root 1 mult 15 covers 1..14; tail
# x^5-2 irreducible deg 5 (distinct roots, none at 1).
f = (x - 1)**15*(x**5 - 2)
