from sympy import symbols
x = symbols('x')
# CONSTRUCTION div-d5: f = (x-r)^m * g with g a genuine (multi-root) tail.
# f = x^12 * (x-1)^5 * (x-2)^3 : root 0 mult 12, then g = (x-1)^5 (x-2)^3.
# Multiplicity pattern 12-5-3, three recycled roots.
f = x**12 * (x - 1)**5 * (x - 2)**3
