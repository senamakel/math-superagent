from sympy import symbols
x = symbols('x')
# multiplicity 18 at 0 covers 1..17; spread rest
f = x**18 * (x-1)*(x-2)
