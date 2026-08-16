"""Test the refined law:
  (T) ce = sat - p  [THEOREM: the p pure powers (x-a)^n always satisfy Hasse-CA]
  (C) sat is a multiple of p, i.e. sat = p*m for integer m.
  Good prime -> m = 1 (only pure powers).
  Bad prime  -> m = p  (law-holds case) except n=5,p=3 gives m=5=n.
Probe n=7,8,9 at small bad primes to find more exceptions to m=p.
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

# n=7 bad primes include 2,3,5,11,... (366 of them); n=8,9 at p=2
cases = [(7,2),(7,3),(8,2),(9,2),(9,3)]
for n, p in cases:
    if p**n > 80000:
        print(f"n={n} p={p}: SKIP (p^n={p**n} too big)"); continue
    sat, ce = classify(n, p)
    th = (ce == sat - p)
    div = (sat % p == 0)
    m = sat // p
    print(f"n={n} p={p}: sat={sat} ce={ce}  T(ce=sat-p)={th!s}  "
          f"sat%p==0: {div}  m=sat/p={m} (p={p})")
