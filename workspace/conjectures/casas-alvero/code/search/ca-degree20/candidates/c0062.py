from sympy import symbols
x = symbols('x')
# MIXED: root 0 mult 10 + root 5 mult 10 -> covers 1..9 only (mult-10 roots cover j=1..9)
f = x**10 * (x-5)**10
