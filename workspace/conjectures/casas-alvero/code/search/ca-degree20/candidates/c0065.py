from sympy import symbols
x = symbols('x')
# mult 15 at 0 covers 1..14, plus (x-3)^5 covers another set of low j for root3
f = x**15 * (x-3)**5
