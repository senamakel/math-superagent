from sympy import symbols
x = symbols('x')
# CONSTRUCTION div2 (b): PRESCRIBED ROOT MULTISET.
# roots {0 mult 8, 1 mult 7, -1 mult 5}: pattern 8-7-5, three distinct roots,
# balanced multiplicities (forces cross-sharing among high derivatives).
f = x**8*(x - 1)**7*(x + 1)**5
