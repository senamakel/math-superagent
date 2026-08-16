from sympy import symbols
x = symbols('x')
# mult 18 + two simple roots -> covers 1..17, likely binding 18,19
f = (x-1)**18 * (x-2)*(x-3)
