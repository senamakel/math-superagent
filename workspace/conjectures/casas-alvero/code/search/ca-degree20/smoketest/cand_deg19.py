"""Smoke-test candidate (iii-a): degree 19, not 20. Full definition here so the
scorer's degree check is exercised on its own module."""
from sympy import symbols
x = symbols("x")
f = x**19 - x
