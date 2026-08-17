from sympy import symbols
x = symbols('x')
# CONSTRUCTION div2 (b): PRESCRIBED ROOT MULTISET.
# roots {0 mult 16, 1 mult 2, 2 mult 2}: three distinct rational roots,
# non-trivial multiplicity pattern 16-2-2.
f = x**16*(x - 1)**2*(x - 2)**2
