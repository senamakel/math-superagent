"""Count, over F_p, monic degree-n polynomials satisfying the Hasse-CA
hypothesis and the number of counterexamples, for n=3 and n=4.

Computed exact: every monic degree-n polynomial over F_p is enumerated
(p^n of them) and classified with lib.casas_alvero.is_ca_hasse /
is_counterexample.  Feasible because p^n is small here.

The capture badprimes_sn.captured.txt reported for n=4:
  p=3: 81 polys, 9 satisfiers, 6 counterexamples
  p=5: 625, 25, 20
  p=7: 2401, 49, 42
i.e. satisfiers = p^2, counterexamples = p^2 - p.
We extend to p=11,13 (and re-verify 3,5,7), and tabulate n=3 for contrast.
"""
from itertools import product
from lib.casas_alvero import is_ca_hasse, is_counterexample
from sympy import symbols, Poly, GF

x = symbols("x")

def mono_polys(n, p):
    # coefficients a_0..a_{n-1}; f = x^n + a_{n-1} x^{n-1} + ... + a_0
    for cs in product(range(p), repeat=n):
        expr = x ** n + sum(a * x ** j for j, a in enumerate(cs))
        yield Poly(expr, x, domain=GF(p))

def counts(n, p):
    sat = 0
    ce = 0
    for f in mono_polys(n, p):
        if is_ca_hasse(f, p):
            sat += 1
            if is_counterexample(f, p):
                ce += 1
    return sat, ce

for n in (3, 4):
    print(f"=== degree n={n} ===")
    for p in (3, 5, 7, 11, 13):
        sat, ce = counts(n, p)
        print(f"  p={p:2d}: polys={p**n:5d} satisfiers={sat:5d} (=p^{n-1}? {sat==p**(n-1)}) "
              f"=p^2? {sat==p*p}  counterexamples={ce:5d} (=-sat+p? {sat-ce==p}) "
              f"(-sat+p^1? {sat-ce==p})  pure-powers={sat-ce}")
    print()
