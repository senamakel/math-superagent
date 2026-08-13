#!/usr/bin/env python3
"""Verify the internal claims of the three new proposed approaches:

1. pascal-descent: (a) the worked-example identity C(13,6)=C(14,5)+C(13,4)
   claimed in the approach file; (b) the growth claim that binomial
   coefficients grow exponentially in the row index for FIXED column
   (mechanism's engine); (c) the power-law relation y ~ x^(k1/k2) for the
   (78,2)/(15,5) witness pair.
2. legendre-digit-sum: omega(a) (number of distinct prime divisors) for all
   seven high-multiplicity witnesses — the number of simultaneous p-adic
   constraints in the proposed adelic system.
3. chabauty-coleman-uniform: genus vs rank data points for the small pairs
   from the library (rank 2 at (2,3),(2,4) asserted in deweger-genus3-curve),
   and the structure of Coleman's bound #X(Q) <= #X(F_p) + 2g - 2 (Hasse gives
   #X(F_p) <= p+1+2g sqrt(p), so the bound grows with g and p).

Exact integer arithmetic only; no triangle construction.
"""
import math
from functools import reduce

def C(n, k):
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    return reduce(lambda acc, i: acc * (n - i) // (i + 1), range(k), 1)

def distinct_prime_divisors(n):
    ps = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            ps.add(d)
            n //= d
        d += 1
    if n > 1:
        ps.add(n)
    return ps

print("=== 1. pascal-descent worked example arithmetic ===")
print("C(13,6)      =", C(13,6), "(claimed equal to C(14,5)+C(13,4))")
print("C(14,5)      =", C(14,5))
print("C(13,4)      =", C(13,4))
print("C(14,5)+C(13,4) =", C(14,5)+C(13,4))
print("identity claimed holds:", C(13,6) == C(14,5)+C(13,4))
print()
print("C(15,5)-C(13,5) =", C(15,5)-C(13,5), "(claimed equal to C(14,5)+C(13,4))")
print()
# correct Pascal expansions
print("Correct expansion candidates:")
print("C(13,6) vs C(14,4)+C(13,4):", C(13,6), C(14,4)+C(13,4))
print("C(13,6) vs C(14,5)+C(13,5):", C(13,6), C(14,5)+C(13,5))
print("C(15,5)-C(13,5) = C(13,6):", C(15,5)-C(13,5) == C(13,6))
print()

print("=== 1b. growth of C(n,k) for FIXED small k (polynomial, not exponential) ===")
for k in [2, 3, 5]:
    vals = [C(n, k) for n in (100, 200, 400, 800)]
    ratios = [vals[i+1]/vals[i] for i in range(len(vals)-1)]
    print(f"k={k}: values at n=100,200,400,800 = {vals}" )
    print(f"    doubling ratios {['%.3f' % r for r in ratios]}  (4^k-growth would be 16.0 for degree-k polynomial)")
print("Exponential in row index happens only when k grows with n (e.g., central):")
print("C(2k,k) for k=10,20,40:", C(20,10), C(40,20), C(80,40))
print("ratio per doubling ~4^k:", C(40,20)/C(20,10), C(80,40)/C(40,20))
print()

print("=== 1c. power-law relation for the (78,2)/(15,5) witness pair ===")
x, k1, y, k2 = 15, 5, 78, 2
pred = (math.factorial(k2)/math.factorial(k1))**(1/k2) * x**(k1/k2)
print(f"k1={k1},k2={k2}, x={x}: C={C(x,k1)}, y={y}: C={C(y,k2)}")
print(f"leading-term prediction y ~ {pred:.1f}  (not 'rows close' unless k1/k2 ~ 1)")
print()

print("=== 2. legendre-digit-sum: number of primes dividing each witness ===")
witnesses = [3003, 120, 210, 1540, 7140, 11628, 24310]
for a in witnesses:
    ps = sorted(distinct_prime_divisors(a))
    print(f"a={a}: N(a)>= {6 if a!=3003 else 8}, omega(a)={len(ps)}, primes={ps}")
print()

print("=== 3. chabauty-coleman: genus vs rank data points ===")
# genus from the run's closed form g = ((k1-1)(k2-1)+1-gcd(k1,k2))/2
def genus(k1, k2):
    return ((k1-1)*(k2-1) + 1 - math.gcd(k1, k2)) // 2
pairs = [(2,3),(2,4),(3,4),(2,5),(2,6),(2,8),(3,6),(4,6),(4,8)]
print("(2,3),(2,4) rank 2 asserted in library (deweger-genus3-curve); r<g fails there.")
for (a,b) in pairs:
    print(f"({a},{b}): genus g={genus(a,b)}")
print()
print("Coleman's bound is #X(Q) <= #X(F_p)+2g-2 with p>2g; Hasse: #X(F_p) <= p+1+2g*sqrt(p).")
print("So the bound is O(g*sqrt(p)) with p>2g: it GROWS with the family, it is not a constant.")