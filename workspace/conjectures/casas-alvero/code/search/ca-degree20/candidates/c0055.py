from sympy import symbols
x = symbols('x')
# mult 8 at 0 + mult 8 spread + 4 distinct
f = x**8 * (x-21)**8 * (x-1)*(x-2)*(x-3)*(x-4)
