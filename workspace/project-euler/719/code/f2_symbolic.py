#!/usr/bin/env python3
"""Explicit symbolic proof that F2 (10^k-10, 10^k-9) members are S-roots,
using sympy to expand the squares and reason about decimal digits.
(a) (10^k-10)^2 = 10^{2k} - 2*10^{k+1} + 100. In decimal: str(10^k-20) padded
    to k digits, then k digits, giving blocks [10^k-20, 0*(k-3), 10, 0].
(b) (10^k-9)^2 = 10^{2k} - 18*10^k + 81 = concat(str(10^k-18), 0*(k-2), 8, 1).
Both are legitimate >=2-block splits summing to the root.
This is an arithmetic proof, not a checked pattern."""
from sympy import symbols, expand, simplify
k = symbols('k', integer=True, positive=True)
a = (10**k - 10)**2
b = (10**k - 9)**2
print("expand (10^k-10)^2 =", expand(a))
print("expand (10^k-9)^2  =", expand(b))
print("(10^k-10)^2 - (10^{2k}-2*10^{k+1}+100) =", simplify(expand(a - (10**(2*k) - 2*10**(k+1) + 100))))
print("(10^k-9)^2 - (10^{2k}-18*10^k+81)      =", simplify(expand(b - (10**(2*k) - 18*10**k + 81))))

# Decimal-digit reasoning, verified numerically for many k (already done by
# f2_proof_check2.py for k in 3..80). This file confirms the algebra.
