"""Expected-reject candidate: monic-degree-20 shape but leading coeff 2.

f = 2x^20 - x. Must be INVALID: 'not monic (leading coefficient 2)'.
Submitted through the live scorer to exercise the rejection path.
"""
from sympy import symbols
x = symbols("x")
f = 2 * x**20 - x
