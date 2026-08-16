"""Smoke-test candidate (i): a genuine degree-20 candidate.

f = x^20 - x. Monic, degree 20, rational. Shares a root (0) with every
derivative f'', f''' , ..., f^(19) (their leading term is a scalar times
x^{18}, x^{17}, ... which vanishes at 0), but NOT with f' = 20x^19 - 1.
Expected: SCORE: 18.
"""

from sympy import symbols

x = symbols("x")
f = x**20 - x
