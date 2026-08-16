#!/usr/bin/env python3
"""Verify the prime-order classes used in the Zsigmondy summary:
   for each d | 60, confirm 2^d-1 has a primitive prime divisor except d=6,
   by factoring 2^60-1 and computing ord_p(2) for each prime.
   Also confirm the sole exception d=6 (63 = 3^2 * 7, no order-6 prime).
"""
import sympy
from math import gcd

def ord_mod(a, m):
    if gcd(a, m) != 1:
        return None
    r, v = 0, 1
    while True:
        r += 1
        v = (v * a) % m
        if v == 1:
            return r

N = 2**60 - 1
fac = sympy.factorint(N)
print("2^60-1 =", dict(fac))

# distinct primes and their order of 2
orders = {}
for p in fac:
    orders[p] = ord_mod(2, p)
print("primes and ord_p(2):", orders)

# for each d dividing 60, which primes have order d
divs60 = [d for d in sympy.divisors(60)]
classmap = {d: [] for d in divs60}
for p, o in orders.items():
    classmap[o].append(p)
print("\norder classes among primes of 2^60-1:")
for d in divs60:
    if classmap[d]:
        print(f"  d={d}: {classmap[d]}")

# which d|60 have NO primitive prime divisor among primes of 2^60-1
print("\nd|60 with no prime of that order:", [d for d in divs60 if not classmap[d]])
# note: primitive prime divisor of 2^d-1 divides 2^60-1 iff d|60, so any class
# missing from the primes of N means 2^d-1 has no primitive prime divisor
print("expected only d=6 (and d=1 trivial), per Zsigmondy =>", [d for d in divs60 if not classmap[d] and d != 1])
