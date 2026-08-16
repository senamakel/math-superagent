#!/usr/bin/env python3
"""Hand-check (not the final answer) of the currently-attacked weakened rung
R-ord51-2: orderOf (2 : ZMod 51) = 8, and the related worked-example facts.

The refuter cannot run this itself; this is recorded for tool_builder to run.
The values here are what a faithful TPTP encoding would be checked against.
"""
from math import gcd


def ord_mod(a, m):
    if gcd(a, m) != 1:
        return None
    r, val = 0, 1
    while True:
        r += 1
        val = (val * a) % m
        if val == 1:
            return r


print("ord_51(2) =", ord_mod(2, 51))          # expect 8
print("ord_3(2) =", ord_mod(2, 3), " ord_17(2) =", ord_mod(2, 17))

# R-sum8 worked example: divisors of 255 with ord_m(2)=8
bads = []
for m in (1, 3, 5, 15, 17, 51, 85, 255):
    o = ord_mod(2, m) if m > 1 else 0
    print("m=%3d ord=%s" % (m, o))
print("sum of m in {17,51,85,255} =", 17 + 51 + 85 + 255, " -> +count =", 17+51+85+255+4)
