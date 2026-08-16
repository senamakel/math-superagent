"""Compute the multiplier m = sat/p (sat = # monic degree-n polys over F_p
satisfying Hasse-CA) as a sequence in n, for fixed p=2 and p=3, over a range
large enough for the sequence tools.

Note: m=1 at good primes (only pure powers).  At bad primes m>1.  We record
sat (and m) for n=3..N at p=2 and p=3.  Enumerate p^n monic polys.
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

for p in (2, 3):
    N = 16 if p == 2 else 9   # 2^n cheap to n=16 (65536); 3^n to n=9 (19683)
    sat_seq = []
    for n in range(3, N+1):
        if p**n > 100000:
            print(f"p={p} n={n}: SKIP p^n={p**n}"); break
        sat = sat_count(n, p)
        m = sat // p
        sat_seq.append(sat)
        print(f"p={p} n={n:2d}: sat={sat:6d} m={m}", flush=True)
    print(f"p={p} sat sequence: {sat_seq}\n")
