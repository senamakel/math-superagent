from sympy import symbols
x = symbols('x')
# sparse: zeros at x^2..x^9 and x^11..x^19, nonzero at x^1 and x^10
# shares root 0 for 17 derivatives; check j=1,10
f = x**20 - x**10 - x
