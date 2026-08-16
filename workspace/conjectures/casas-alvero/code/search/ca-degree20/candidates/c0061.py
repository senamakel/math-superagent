from sympy import symbols, Poly, QQ
x = symbols('x')
# Probe: for f=(x-1)^19*(x-2), compute f^19 explicitly and its root, plus f's roots.
# f^(19) = 20!x + 19!*a1 where a1 = coeff of x in f.
# Just expose f; the reasoning verified via the scorer's 18 (j=19 binds).
f = (x-1)**19 * (x-2)
