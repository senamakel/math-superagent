#!/usr/bin/env python3
"""Clean gcd-Mersenne inclusion-exclusion check for order-60 set of PE622.

order-60 set among divisors of 2^60-1:
   {m>1 : m | 2^60-1} minus union_{d proper divisor of 60} A_d,
where A_d = {m>1 : m | 2^d-1}.

Every proper divisor of 60 divides one of {12,20,30}, so the union is just
A_12 u A_20 u A_30.  By gcd(2^a-1,2^b-1)=2^{gcd(a,b)}-1, the pairwise and
triple intersections of these three are A_{gcd(...)}.  So the union size is
   |A12|+|A20|+|A30| - |A4| - |A10| - |A6| + |A2|
and similarly for sums, where |A_d| = tau(2^d-1)-1 and sum = sigma(2^d-1)-1.
That gives C(60), S(60) purely from tau/sigma of 2^d-1 for small d.
"""
import sympy

def tausigma(d):
    """(tau(2^d-1)-1, sigma(2^d-1)-1)  = (|A_d|, sum A_d)"""
    N = 2**d - 1
    return (sympy.divisor_count(N) - 1, sympy.divisor_sigma(N, 1) - 1)

# singletons {12,20,30}; pair intersections gcd(12,20)=4, gcd(12,30)=10,
# gcd(20,30)=10... wait recompute: gcd(12,20)=4, gcd(12,30)=6, gcd(20,30)=10,
# triple gcd=2.
singles = [12, 20, 30]
pairs = [(4, 12, 20), (6, 12, 30), (10, 20, 30)]
triple = [2]

C = 0
S = 0
for d in singles:
    c, s = tausigma(d); C += c; S += s
for g, a, b in pairs:
    c, s = tausigma(g); C -= c; S -= s
c, s = tausigma(triple[0]); C += c; S += s

print("C(60) =", C)
print("S(60) =", S)
print("answer =", S + C)

# cross-check direct
N = 2**60 - 1
direct = {m for m in sympy.divisors(N)
          if m > 1 and sympy.n_order(2, m) == 60}
print("direct C(60) =", len(direct), "S(60) =", sum(direct),
      "match:", len(direct) == C and sum(direct) == S)
