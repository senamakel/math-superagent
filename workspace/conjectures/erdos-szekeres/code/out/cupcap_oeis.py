#!/usr/bin/env python3
"""Verify f(k,k) = C(2k-4,k-2)+1 equals the OEIS A323230 form C(2(n-1),n-1)+1
with the right shift, and confirm the DP recurrence F(k,l)=F(k,l-1)+F(k-1,l).
"""
from math import comb

# The cups/caps DP: F(k,l) = C(k+l-4, k-2) is the number of points in the
# extremal set (the threshold for a k-cup or l-cap is F+1).
def F(k, l):
    return comb(k + l - 4, k - 2)

print("Cross-check f(k,k)=C(2k-4,k-2)+1 vs the DP sum identity:")
for k in range(2, 10):
    direct = comb(2*k - 4, k - 2) + 1
    # A323230 with n=k-1: C(2(k-1-1),k-1-1)... let's just state both
    oeis_n = k - 1
    oeis = comb(2*(oeis_n - 1), oeis_n - 1) + 1
    print(f"  k={k}: C(2k-4,k-2)+1 = {direct}, "
          f"OEIS a({oeis_n})=C(2({oeis_n}-1),{oeis_n}-1)+1 = {oeis}, "
          f"match={direct==oeis==2*comb(2*k-5,k-3)+1 if False else direct==oeis}")
    # also f(k-1,k-1) relation
print()
print("Cups/caps DP recurrence F(k,l)=F(k,l-1)+F(k-1,l) (Pascal):")
for k in range(3, 7):
    for l in range(3, 7):
        lhs = F(k, l); rhs = F(k, l-1) + F(k-1, l)
        assert lhs == comb(k+l-4, k-2)
        print(f"  F({k},{l})={lhs} == F({k},{l-1})+F({k-1},{l})={rhs} "
              f"{'OK' if lhs==rhs else 'BAD'}")
