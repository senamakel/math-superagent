#!/usr/bin/env python3
"""(A) Print the record-denominator sequence  t_k = P_{2k-1} (odd-index Pell),
where the k-th record value of f is 1 - 1/t_k^2, achieved at (P_k,P_{k-1}).
(B) Also print the record-value numerators  N_k = P_{2k-1}^2 - 1
and the exact sequence of record f-values as decimals (for growth).
"""
from math import gcd

def pell(k):
    if k <= 1: return 1
    p0, p1 = 1, 2
    for _ in range(2, k):
        p0, p1 = p1, 2*p1 + p0
    return p1

t = [pell(2*k-1) for k in range(1, 21)]
print("t_k = P_{2k-1} (record denominators):")
print(",".join(map(str, t)))
N = [x*x - 1 for x in t]
print("N_k = t_k^2 - 1 (record numerators of 1-1/t^2):")
print(",".join(map(str, N)))
# record f values 1 - 1/t^2 as decimals (first few for growth shape)
print("\nrecord f = 1 - 1/t^2:")
from decimal import Decimal, getcontext
getcontext().prec = 30
for x in t[:10]:
    v = Decimal(1) - Decimal(1)/(Decimal(x)*Decimal(x))
    print(f"  t={x}: {v}")
# growth ratios of t
print("\ngrowth ratio t_{k+1}/t_k:")
for i in range(1, len(t)):
    print(f"  {t[i]}/{t[i-1]} = {t[i]/t[i-1]:.6f}")
