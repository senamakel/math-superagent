"""Smoke-test candidate (iii-b): degree 20 but not monic (leading coeff 2)."""
from sympy import symbols
x = symbols("x")
f = 2 * x**20 - x
