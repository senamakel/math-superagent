"""Expected-reject candidate: the trivial family (x-a)^20.

f = (x-4)^20. Must be INVALID: 'f is (x-a)^20 (the trivial family...)'.
This is the exploit — a pure power reaches score 19; the scorer rejects it.
"""
from sympy import symbols
x = symbols("x")
f = (x - 4) ** 20
