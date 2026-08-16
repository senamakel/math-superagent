from sympy import symbols
x = symbols('x')
# derivative-19 targeted: choose a_1 so f^(19) root = a root of f.
# f=(x-1)^19(x-2): set so f^(19) root is 1 -> this would be near CA, but mult>=18
# forces pure power per Laterveer-Ounaies; try mult 18, roots 1 (x18), plus
# simple roots chosen so f^(18), f^(19) share roots. 
f = (x-1)**18 * (x**2 - 3*x + 2)
