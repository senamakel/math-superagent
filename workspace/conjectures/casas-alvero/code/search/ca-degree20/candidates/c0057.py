from sympy import symbols
x = symbols('x')
# k=20 would need x^20 term; use sparse with nonzero at x^3 and x^17
# root0 shared by all j except 3 and 17
f = x**20 - x**17 - x**3
