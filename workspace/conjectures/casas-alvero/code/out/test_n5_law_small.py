"""Test the satisfier law at degree n=5 for small primes only.
bad primes of degree 5: {2,3,7,11,...}; good: 5,13,...
Run p in {2,3,5,7} only to keep it fast (max 7^5=16807).
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

print("degree n=5")
print(f"{'p':>4} {'bad?':>5} {'sat':>6} {'exp':>5} {'ce':>6} {'exp':>5} {'match':>6}")
for p, bad in [(2,True),(3,True),(5,False),(7,True)]:
    sat, ce = classify(5, p)
    exp_sat = p*p if bad else p
    exp_ce = p*(p-1) if bad else 0
    print(f"{p:>4} {str(bad):>5} {sat:>6} {exp_sat:>5} {ce:>6} {exp_ce:>5} {(sat==exp_sat and ce==exp_ce)!s:>6}")
