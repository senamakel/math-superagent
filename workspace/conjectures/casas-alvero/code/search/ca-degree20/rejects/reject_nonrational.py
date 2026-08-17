"""Expected-reject candidate: non-rational (Gaussian) coefficients.

f = x^20 - I*x over ZZ_I. Must be INVALID: 'non-rational coefficients'.
"""
from sympy import symbols, I
x = symbols("x")
f = x**20 - I * x
