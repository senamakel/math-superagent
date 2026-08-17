<!-- source: https://arxiv.org/src/2607.13785v2/anc/h14_3_reproducibility/certificates/verify_h14_center_basis.py | converted from plain text -->

#!/usr/bin/env python3
"""Symbolic regression checks for the H14^3 center-generator bridge."""

import sympy as sp

def check_zero(name, expression):
    value = sp.factor(sp.expand(expression))
    if value != 0:
        raise AssertionError(f"{name}: {value}")

B, mu2, mu4, mu5, d = sp.symbols("B mu2 mu4 mu5 d")
a = mu4 + B * mu5
c = (1 - 2 * B) * mu5

alpha = c - d
beta = a + d
gamma = d * (B + mu2)

tau = mu4 + (1 - B) * mu5
ell = d - (1 - 2 * B) * mu5
sigma = d * (B + mu2)

check_zero("tau=a+c", tau - (a + c))
check_zero("ell=-alpha", ell + alpha)
check_zero("sigma=gamma", sigma - gamma)
check_zero("beta=tau+ell", beta - (tau + ell))

x, y = sp.symbols("x y")
P = -y - d * x + B * (x**2 - y**2)
Q = (1 + y) * (x + d * y)

L = 1 + y
F = (
    B * (B - 1) * x**2
    - B * d * x * y
    - B**2 * y**2
    - d * (2 * B - 1) * x
    + (d**2 - 2 * B) * y
    + d**2
    - 1
)

X_L = P * sp.diff(L, x) + Q * sp.diff(L, y)
X_F = P * sp.diff(F, x) + Q * sp.diff(F, y)
div_X = sp.diff(P, x) + sp.diff(Q, y)

check_zero("X(L) cofactor", X_L - (x + d * y) * L)
check_zero("X(F) cofactor", X_F - (2 * B * x + d * y) * F)
check_zero(
    "inverse-integrating-factor cofactor",
    div_X - ((x + d * y) + (2 * B * x + d * y)),
)

print("center-generator bridge: OK")
print("second center component Darboux identities: OK")
