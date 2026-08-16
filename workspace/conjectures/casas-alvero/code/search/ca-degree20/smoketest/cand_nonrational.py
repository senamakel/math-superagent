"""Smoke-test candidate (iii-c): degree 20, monic, but a non-rational
coefficient (I)."""
from sympy import symbols, I
x = symbols("x")
f = x**20 - I * x
