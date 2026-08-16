from sympy import symbols
x = symbols('x')
# mult 9 at 0 covers 1..8; spread rest with distinct simple roots
f = x**9 * (x-1)*(x-2)*(x-3)*(x-4)*(x-5)*(x-6)*(x-7)*(x-8)*(x-9)*(x-10)*(x-11)
