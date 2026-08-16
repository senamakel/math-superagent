from sympy import symbols
x = symbols('x')
# 3 roots with multiplicities 7,7,6 -> covers 1..6 (mult-7 roots) 
f = (x-1)**7 * (x-2)**7 * (x-3)**6
