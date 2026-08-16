"""Gather the Hasse-CA counterexample count over F_p for degrees n=3..6,
across small primes, to characterize when the p(p-1) law holds.
"""
from itertools import product
from lib.casas_alvero import is_ca_hasse, is_counterexample
from sympy import symbols, Poly, GF

x = symbols("x")

def classify(n, p):
    sat = ce = 0
    for cs in product(range(p), repeat=n):
        f = Poly(x**n + sum(a*x**j for j, a in enumerate(cs)), x, domain=GF(p))
        if is_ca_hasse(f, p):
            sat += 1
            if is_counterexample(f, p):
                ce += 1
    return sat, ce

# published bad-prime sets
BAD = {3:{2}, 4:{3,5,7}, 5:{2,3,7,11,131,193,599,3541,8009},
       6:{2,5,7,11,13,19,23,29,37,47,61,67,73,97,257,811,983,1069,1087,
          1187,1487,1499,1901,2287,3209,3877,3881,4019,4943,5471,6983,8699,
          9337,15131,15823,20771,21379,23993,150203,266587,547061,685177,
          885061,1030951,7783207,17250187,40362599,9348983563,70016757407,
          2610767527031,225833117528659,7390044713023799,51313000813080529}}

for n in (3,4,5,6):
    print(f"=== degree n={n} ===")
    primes = [2,3,5,7,11] if n <= 4 else [2,3,5,7,11,13]
    for p in primes:
        if p**n > 50000:  # keep bounded
            continue
        sat, ce = classify(n, p)
        bad = p in BAD[n]
        exp_ce = p*(p-1) if bad else 0
        law = (ce == exp_ce)
        print(f"  p={p:2d} bad={str(bad):5s} sat={sat:5d} ce={ce:5d} p(p-1)={p*(p-1):4d} law-holds={law!s:5s}")
    print()
