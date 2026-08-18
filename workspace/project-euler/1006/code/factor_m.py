#!/usr/bin/env python3
"""Factor M = 101001001, compute orders of 10 mod each factor."""
import sys
from sympy import factorint, n_order, Mod

M = 101001001
print(f"M = {M}")
print(f"Factorization: {factorint(M)}")

for p, e in factorint(M).items():
    pe = p**e
    ord_10 = n_order(10, pe)
    print(f"\nPrime power: {p}^{e} = {pe}")
    print(f"  ord(10) mod {pe} = {ord_10}")
    print(f"  phi({pe}) = {pe - p**(e-1)}")
    print(f"  ord divides phi: {(pe - p**(e-1)) % ord_10 == 0}")
    # Check the order modulo p (base prime)
    ord_p = n_order(10, p)
    print(f"  ord(10) mod {p} = {ord_p}")
    # For prime powers, either ord(pe) = ord(p) or ord(pe) = p * ord(p)
    if e > 1:
        print(f"  Ratio ord(pe)/ord(p) = {ord_10 // ord_p}")
        print(f"  Check ord(p) * p = {ord_p * p}")
