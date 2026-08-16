from sympy import symbols
x = symbols('x')
# even-symmetric with many zero coeffs; nonzero at x^2,x^4 => binds j=2,4
f = x**20 + x**4 + x**2
