from sympy import symbols
x = symbols('x')
# f = x^20 - 2x : root 0, only coeff of x^1 nonzero among 1..19
# f^(j) shares root 0 for all j in 2..19; j=1 binds -> expect 18
f = x**20 - 2*x
