from sympy import symbols
x = symbols('x')
# multiplicity 15 at 0 -> covers 1..14
f = x**15 * (x-1)**5
