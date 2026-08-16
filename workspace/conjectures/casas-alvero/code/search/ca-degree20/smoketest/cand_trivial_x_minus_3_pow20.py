"""Smoke-test candidate (ii): the trivial family — the obvious exploit.

f = (x-3)^20. Shares a root with all 19 derivatives (the root 3 to
multiplicity 20): the polynomial the conjecture allows as the ONLY satisfiers
of the hypothesis. Must be rejected with INVALID naming '(x-a)^20'.
"""

from sympy import symbols

x = symbols("x")
f = (x - 3) ** 20
