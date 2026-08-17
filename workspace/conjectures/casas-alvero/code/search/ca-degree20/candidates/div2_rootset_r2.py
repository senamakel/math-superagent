from sympy import symbols
x = symbols('x')
# CONSTRUCTION div2 (b): PRESCRIBED ROOT MULTISET.
# roots {1 mult 15, 2 mult 3, 3 mult 2}: pattern 15-3-2, three distinct roots.
f = (x - 1)**15*(x - 2)**3*(x - 3)**2
