#!/usr/bin/env python3
"""Verify the Goetgheluck ratio-2 binomial families (attested via Luca-Szalay
2004 and the MaRDI portal: Math. Comp. 67 (1998) 1727-1733) and the infinite
six-fold Singmaster/Lind family that all claimed bounds must survive.

Run:  timeout 540 python3 verify_goetgheluck_ratio2.py 2>&1 | tee verify_goetgheluck_ratio2.captured.txt; echo EXIT=$?
"""
from math import comb

print("== Goetgheluck Family 1: C(2r, r) = 2*C(2r-1, r-1) (r=1..40) ==")
ok = True
for r in range(1, 41):
    if comb(2 * r, r) != 2 * comb(2 * r - 1, r - 1):
        ok = False
        print(f"  FAIL r={r}")
print("  all match:", ok)

print("\n== Goetgheluck ratio-2 scan over bounded range (n,a<=150) ==")
found = set()
for n in range(4, 151):
    for k in range(2, n // 2 + 1):
        c = comb(n, k)
        for a in range(k, 151):
            for b in range(2, a // 2 + 1):
                if 2 * comb(a, b) == c:
                    found.add((n, k, a, b))
for (n, k, a, b) in sorted(found):
    print(f"  C({n},{k}) = {comb(n,k)} = 2*C({a},{b})")
print("  total ratio-2 pairs found:", len(found))

print("\n== Singmaster/Lind infinite six-fold family (the B>=6 witness) ==")
# n = F_{2j+2}F_{2j+3}-1, k = F_{2j}F_{2j+3}-1 give C(n+1,k+1)=C(n,k+2)
F = [0, 1]
for _ in range(60):
    F.append(F[-1] + F[-2])
for j in range(1, 7):
    n = F[2 * j + 2] * F[2 * j + 3] - 1
    k = F[2 * j] * F[2 * j + 3] - 1
    lhs = comb(n + 1, k + 1)
    rhs = comb(n, k + 2)
    print(f"  j={j}: C({n+1},{k+1})={lhs} == C({n},{k+2})={rhs} : {lhs==rhs}")
