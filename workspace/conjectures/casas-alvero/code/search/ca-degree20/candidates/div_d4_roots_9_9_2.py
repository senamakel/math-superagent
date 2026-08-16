from sympy import symbols
x = symbols('x')
# CONSTRUCTION div-d4: PRESCRIBED ROOT MULTISET. roots: 1 mult 9, 2 mult 9,
# 3 mult 2. Multiplicity pattern 9-9-2 (two heavy roots + a light one).
f = (x - 1)**9 * (x - 2)**9 * (x - 3)**2
