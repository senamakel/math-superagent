#!/usr/bin/env python3
"""Verify Goetgheluck's ratio-2 binomial families, attested via Luca-Szalay 2004
and the MaRDI portal citation (Math. Comp. 67 (1998) 1727-1733).

Family 1 (explicit, from the search summary): C(2r, r) = 2 * C(2r-1, r-1).
Plus a general ratio-2 checker that solves C(n,k) = 2*C(a,b) by exact binomial
computation for a small range, to confirm the attested families are real.
"""
from math import comb

print("Family 1: C(2r, r) == 2*C(2r-1, r-1)  (Goetgheluck, ratio 2)")
ok = True
for r in range(1, 31):
    lhs = comb(2 * r, r)
    rhs = 2 * comb(2 * r - 1, r - 1)
    if lhs != rhs:
        ok = False
        print(f"  FAIL r={r}: C({2*r},{r})={lhs} vs 2*C({2*r-1},{r-1})={rhs}")
print("  all r=1..30 match:", ok)

# Brute-check the ratio-2 relationship in general: find all (n,k,a,b) with
# C(n,k) = 2*C(a,b) for small bounds, to confirm these are the families.
print("\nBrute scan for C(n,k) == 2*C(a,b) with 2<=k<=n//2, 2<=b<=a//2, n,a<=120:")
found = set()
for n in range(4, 121):
    for k in range(2, n // 2 + 1):
        c = comb(n, k)
        # find a,b with 2*C(a,b) == c
        for a in range(k, 121):
            for b in range(2, a // 2 + 1):
                if 2 * comb(a, b) == c:
                    found.add((n, k, a, b))
for (n, k, a, b) in sorted(found):
    print(f"  C({n},{k}) = {comb(n,k)} = 2*C({a},{b})")
print("total:", len(found))
