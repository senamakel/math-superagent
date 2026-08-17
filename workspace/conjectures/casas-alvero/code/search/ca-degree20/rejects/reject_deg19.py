"""Expected-reject candidate: degree 19, not 20.

f = x^19 - x. Must be INVALID: 'degree 19 != 20'.
"""
from sympy import symbols
x = symbols("x")
f = x**19 - x
