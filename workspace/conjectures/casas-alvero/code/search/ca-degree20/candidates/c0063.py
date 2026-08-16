from sympy import symbols
x = symbols('x')
# sparse, nonzero at x^5 only among 1..19
f = x**20 - 3*x**5
