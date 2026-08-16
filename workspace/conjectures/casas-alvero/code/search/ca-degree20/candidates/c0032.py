from sympy import symbols
x = symbols('x')
# mult 16 at 0 -> covers 1..15
f = x**16 * (x-1)**4
