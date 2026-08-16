"""Probe the FULL structure of Hasse-CA satisfiers at n=5, p=3 (bad prime),
where the count 15 breaks the naive p^2 law.  List every satisfier and
mark pure powers; look for an organizing description.
"""
from itertools import product
from lib.casas_alvero import is_ca_hasse, is_counterexample
from sympy import symbols, Poly, GF, factor

x = symbols("x")
n, p = 5, 3

sat = []
for cs in product(range(p), repeat=n):
    f = Poly(x**n + sum(a*x**j for j, a in enumerate(cs)), x, domain=GF(p))
    if is_ca_hasse(f, p):
        sat.append((cs, is_counterexample(f, p)))

print(f"n={n} p={p}: total satisfiers = {len(sat)}")
print("counterexamples:")
for cs, ce in sat:
    tag = "CE " if ce else "pure"
    print(f"  {tag} coeffs a0..a4: {cs}")
# sort by whether monic in x^3 terms etc
