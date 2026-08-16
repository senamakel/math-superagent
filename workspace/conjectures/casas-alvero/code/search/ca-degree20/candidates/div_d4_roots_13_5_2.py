from sympy import symbols
x = symbols('x')
# CONSTRUCTION div-d4: PRESCRIBED ROOT MULTISET. roots: 0 mult 13, 1 mult 5,
# -1 mult 2. Multiplicity pattern 13-5-2 (three recycled roots).
f = x**13 * (x - 1)**5 * (x + 1)**2
