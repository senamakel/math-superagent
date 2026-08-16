from sympy import symbols
x = symbols('x')
# two roots, one of multiplicity 10 at 0 (covers 1..9), simple roots elsewhere
f = x**10 * (x-1)*(x-2)*(x-3)*(x-4)*(x-5)*(x-6)*(x-7)*(x-8)*(x-9)*(x-10)
