"""Test the satisfier law at degree n=5:
  sat(n,p) = p   if p good for n (CA_{n,p} holds)
           = p^2 if p bad
  ce(n,p)  = 0   good
           = p(p-1) bad

n=5 bad primes (Castryck 2012 Thm 4, Hasse): {2,3,7,11,131,193,599,3541,8009}
n=5 good small primes: 5,13,17,19,23,...
Check bad: p=2,3,7 (small), and good: p=5,13.
"""
from itertools import product
from lib.casas_alvero import is_ca_hasse, is_counterexample
from sympy import symbols, Poly, GF

x = symbols("x")

def mono_polys(n, p):
    for cs in product(range(p), repeat=n):
        yield Poly(x**n + sum(a*x**j for j, a in enumerate(cs)), x, domain=GF(p))

def classify(n, p):
    sat = ce = 0
    for f in mono_polys(n, p):
        if is_ca_hasse(f, p):
            sat += 1
            if is_counterexample(f, p):
                ce += 1
    return sat, ce

print("degree n=5 ; p^5 total polys")
print(f"{'p':>4} {'bad?':>5} {'sat':>6} {'expect':>9} {'ce':>6} {'expect':>9} {'match':>6}")
for p, bad in [(2,True),(3,True),(5,False),(7,True),(11,True),(13,False),(17,False)]:
    sat, ce = classify(5, p)
    exp_sat = p*p if bad else p
    exp_ce = p*(p-1) if bad else 0
    match = (sat==exp_sat and ce==exp_ce)
    print(f"{p:>4} {str(bad):>5} {sat:>6} {exp_sat:>9} {ce:>6} {exp_ce:>9} {match!s:>6}")
