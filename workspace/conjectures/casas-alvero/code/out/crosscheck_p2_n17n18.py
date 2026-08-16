"""Independent cross-check: the n=17 and n=18 p=2 multiplier values, using the
CANONICAL sympy oracle lib.casas_alvero.is_ca_hasse directly (the slow route),
not my bit-parallel checker.  This is rule-11 / rule-9 verification: a second,
different route to the same value.

n=17: 2^17=131072, n=18: 2^18=262144 monic polys over F2, exact counting.
"""
from itertools import product
from lib.casas_alvero import is_ca_hasse, is_pure_power
from sympy import symbols, Poly, GF

x = symbols("x")


def counts(n, p=2):
    sat = ce = 0
    for cs in product(range(p), repeat=n):
        f = Poly(x**n + sum(a * x**j for j, a in enumerate(cs)), x, domain=GF(p))
        if is_ca_hasse(f, p):
            sat += 1
            if not is_pure_power(f, p):
                ce += 1
    return sat, ce


for n in (17, 18):
    sat, ce = counts(n)
    print(f"n={n}: sat={sat} m=sat/2={sat//2} ce={ce}")
