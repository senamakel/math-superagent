from sympy import symbols
x = symbols('x')
# mult 12 at 0 covers 1..11; target higher with another mult 8 at different root
f = x**12 * (x-2)**8
