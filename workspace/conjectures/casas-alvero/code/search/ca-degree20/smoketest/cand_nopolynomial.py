"""Smoke-test candidate (iv): a module exposing NO polynomial in x.

Deliberately withholds any attribute sympy recognises as a polynomial in the
symbol x. The scorer must answer INVALID for the no-polynomial-reason.
"""

# a plain integer, a symbol-only expression, and a function: none is a
# polynomial in x.
version = 1
note = "no polynomial here"
greeting = lambda x: x + 1  # noqa: E731 - a function, not a polynomial
