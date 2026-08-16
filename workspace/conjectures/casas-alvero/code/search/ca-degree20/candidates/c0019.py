from sympy import symbols
x = symbols('x')
# root 0 mult 2 (covers j=1) + zeros at x^3..x^19, one shared attempt
f = x**2 * (x**18 - 2)
