#!/usr/bin/env python3
"""Compute M's factorisation and ord_M(10)."""
from sympy import isprime, factorint, n_order, divisors, totient

M = 101001001
print(f"M = {M}")
print(f"isprime(M) = {isprime(M)}")
if not isprime(M):
    print(f"factorint(M) = {factorint(M)}")
else:
    # order of 10 mod M
    L = n_order(10, M)
    print(f"ord_M(10) = {L}")
    print(f"(M-1)/L = {(M-1)//L}")
    print(f"M-1 = {M-1}")
    print(f"factorint(M-1) = {factorint(M-1)}")
    # 10^k mod M cycle
    print(f"10^L mod M = {pow(10, L, M)}")
    # check the mod-100 cross-check
    # Psi(k) mod 100 == 1 + floor(k/phi^2)
    # phi = (1+sqrt5)/2, phi^2 = (3+sqrt5)/2
    # 1/phi^2 = (3-sqrt5)/2
    from sympy import sqrt, floor
    phi = (1 + sqrt(5)) / 2
    inv_phi2 = 1 / phi**2
    print(f"1/phi^2 = {float(inv_phi2)}")
    for k in [10**18]:
        val = 1 + int(floor(k * inv_phi2))
        print(f"Psi(10^18) mod 100 should be {val % 100}")
