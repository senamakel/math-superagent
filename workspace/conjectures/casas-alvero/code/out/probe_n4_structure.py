"""Verify the Law of over-F_p satisfier counts against the corner cases and
probe the STRUCTURE of the extra satisfiers at a bad prime.

Law (conjecture):
  For degree n polynomial over F_p satisfying the Hasse-CA hypothesis,
    sat(n,p) = p      if p is GOOD for degree n (CA_{n,p} holds)
             = p^2    if p is BAD  for degree n (CA_{n,p} fails)
    ce(n,p)  = 0            good prime
             = p(p-1)       bad prime
  Identified at n=3 (good: p=3,5,7,11,13; bad: p=2) and n=4 (good: 2,11,13; bad: 3,5,7).

Check: n=4 p=2 should give sat=2, ce=0 (p=2 good for n=4 in Hasse formulation).
Also list the actual counterexample-coefficient structure for n=4 bad primes.
"""
from itertools import product
from lib.casas_alvero import is_ca_hasse, is_counterexample
from sympy import symbols, Poly, GF

x = symbols("x")

def mono_polys(n, p):
    for cs in product(range(p), repeat=n):
        yield Poly(x**n + sum(a*x**j for j, a in enumerate(cs)), x, domain=GF(p))

def classify(n, p):
    sat, ce, pure = [], [], []
    for f in mono_polys(n, p):
        if is_ca_hasse(f, p):
            sat.append(f.as_expr())
            if is_counterexample(f, p):
                ce.append(f.as_expr())
            else:
                pure.append(f.as_expr())
    return sat, ce, pure

# Corner: n=4, p=2 (good for n=4 in Hasse)
for (n, p) in [(4, 2)]:
    sat, ce, pure = classify(n, p)
    print(f"n={n} p={p}: satisfiers={len(sat)} (expect {p}) ce={len(ce)} pure={len(pure)} (expect {p})")

# Structure of extra satisfiers at bad primes: n=4 p=3,5,7
for p in (3, 5, 7):
    sat, ce, pure = classify(4, p)
    print(f"\nn=4 p={p}: sat={len(sat)} ce={len(ce)} pure={len(pure)}")
    print("  pure powers:", [str(s) for s in pure])
    print("  first 8 counterexamples:", [str(s) for s in ce[:8]])
