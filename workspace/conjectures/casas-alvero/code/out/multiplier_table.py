"""For a FIXED degree n, tabulate the multiplier m = sat/p over several bad
primes, to characterize when m == p (law) vs the exceptions.

n=7 is bad for many small primes {2,3,5,11,13,...}.  Enumerate n=7 at
p=2,3,5 (5^7=78125 feasible, 11^7 infeasible).  Also n=8 p=3, n=9 p=5, n=10 p=2
(as far as feasible).
"""
from itertools import product
from lib.casas_alvero import is_ca_hasse
from sympy import symbols, Poly, GF

x = symbols("x")

def sat_count(n, p):
    s = 0
    for cs in product(range(p), repeat=n):
        f = Poly(x**n + sum(a*x**j for j, a in enumerate(cs)), x, domain=GF(p))
        if is_ca_hasse(f, p):
            s += 1
    return s

cases = [(7,2),(7,3),(7,5),(8,3),(9,5),(10,2),(8,5)]
for n, p in cases:
    if p**n > 200000:
        print(f"n={n} p={p}: SKIP p^n={p**n}"); continue
    sat = sat_count(n, p)
    print(f"n={n:2d} p={p:2d}: sat={sat}  m=sat/p={sat//p}  (m==p? {sat//p==p})", flush=True)
