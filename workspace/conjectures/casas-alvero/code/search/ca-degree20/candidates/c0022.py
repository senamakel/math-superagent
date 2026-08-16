from sympy import symbols
x = symbols('x')
# all even exponents (even function) - f'(0)=0 so j=1 shares root 0 if f(0)=0
# f = x^20 + x^18 + x^16 + ... but need f(0)=0 and f^(j)(0)=0 for as many j
# f with constant term 0 and all coeffs of x^j = 0 except few
f = x**20 + 2*x**18 + 3*x**16 + 4*x**14 + 5*x**12 + 6*x**10 + 7*x**8 + 8*x**6 + 9*x**4 + 10*x**2
