from sympy import symbols
x = symbols('x')
# f = x^20 - 2x^2 : only coeff of x^2 nonzero among 1..19 -> binding j=2
f = x**20 - 2*x**2
