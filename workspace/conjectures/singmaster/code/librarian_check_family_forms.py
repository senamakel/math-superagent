#!/usr/bin/env python3
"""Verify that Brouwer/BBdW's family form and the run's family form are the same.

Brouwer (preprint, held at research/sources/brouwer-binomial-collisions-near.full.md):
    C(F_{2i+2} F_{2i+3}, F_{2i} F_{2i+3}) = C(F_{2i+2} F_{2i+3} - 1, F_{2i} F_{2i+3} + 1)

Run's form (research/summaries/singmaster-literature-exact.md, verify_fibonacci_identity.py):
    C(n+1, k+1) = C(n, k+2) with n = F_{2i+2} F_{2i+3} - 1, k = F_{2i} F_{2i+3} - 1

So the run's (n+1, k+1) = (F_{2i+2}F_{2i+3}, F_{2i}F_{2i+3}) and
run's (n, k+2) = (F_{2i+2}F_{2i+3}-1, F_{2i}F_{2i+3}+1) — claim: identical to
Brouwer's pair for the same i. Verify for i = 1..12.
"""
from math import comb

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

ok = True
for i in range(1, 13):
    F2i2 = fib(2*i + 2)
    F2i3 = fib(2*i + 3)
    F2i = fib(2*i)
    # Brouwer's form
    lhs = comb(F2i2 * F2i3, F2i * F2i3)
    rhs = comb(F2i2 * F2i3 - 1, F2i * F2i3 + 1)
    # Run's form
    n, k = F2i2 * F2i3 - 1, F2i * F2i3 - 1
    lhs2 = comb(n + 1, k + 1)
    rhs2 = comb(n, k + 2)
    same_pair = (n + 1 == F2i2 * F2i3 and k + 1 == F2i * F2i3
                 and n == F2i2 * F2i3 - 1 and k + 2 == F2i * F2i3 + 1)
    eq = (lhs == rhs == lhs2 == rhs2)
    ok = ok and eq and same_pair
    print(f"i={i}: C({F2i2*F2i3},{F2i*F2i3})={lhs}")
    print(f"      C({F2i2*F2i3-1},{F2i*F2i3+1})={rhs}  equal={eq} same_param={same_pair}")

print("ALL_IDENTICAL" if ok else "MISMATCH")