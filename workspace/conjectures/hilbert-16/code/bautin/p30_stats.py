#!/usr/bin/env python3
"""Coefficient statistics of P30 (the degree-6 Bautin obstruction numerator).

P30_TERMS = [(coeff, (degA,degC,degD,degE,degF))] with 30 terms.
Report: total coefficient sum, |coeff| L1 norm, number of positive/negative
coeffs, sign pattern as a sequence, whether coefficients are all integers
(with what gcd), and the distribution of (degA..degF) — all exact."""
import math

P30_TERMS = [(-124, (0, 0, 0, 1, 3)),(1, (0, 0, 0, 3, 1)),(248, (0, 0, 1, 0, 3)),(-27, (0, 0, 1, 2, 1)),(16, (0, 0, 2, 1, 1)),(20, (0, 0, 3, 0, 1)),(-101, (0, 1, 0, 1, 2)),(350, (0, 1, 1, 0, 2)),(3, (0, 1, 1, 2, 0)),(13, (0, 1, 2, 1, 0)),(10, (0, 1, 3, 0, 0)),(-27, (0, 2, 0, 1, 1)),(159, (0, 2, 1, 0, 1)),(23, (0, 3, 1, 0, 0)),(-24, (1, 0, 0, 0, 3)),(-37, (1, 0, 0, 2, 1)),(-28, (1, 0, 1, 1, 1)),(132, (1, 0, 2, 0, 1)),(144, (1, 1, 0, 0, 2)),(3, (1, 1, 0, 2, 0)),(42, (1, 1, 1, 1, 0)),(76, (1, 1, 2, 0, 0)),(109, (1, 2, 0, 0, 1)),(23, (1, 3, 0, 0, 0)),(-96, (2, 0, 0, 1, 1)),(192, (2, 0, 1, 0, 1)),(29, (2, 1, 0, 1, 0)),(142, (2, 1, 1, 0, 0)),(24, (3, 0, 0, 0, 1)),(76, (3, 1, 0, 0, 0))]

print("n terms:", len(P30_TERMS))
coeffs = [c for c, _ in P30_TERMS]
print("sum coeffs:", sum(coeffs))
print("L1 norm:", sum(abs(c) for c in coeffs))
pos = sum(1 for c in coeffs if c > 0)
neg = sum(1 for c in coeffs if c < 0)
print(f"positive {pos}, negative {neg}")
g = 0
for c in coeffs:
    g = math.gcd(g, abs(c))
print("gcd of coefficients:", g)
print("sign pattern (ordered as P30_TERMS):", "".join("+" if c > 0 else "-" for c, _ in P30_TERMS))

# degree distributions per variable
print("\ndegree distributions per variable (A,C,D,E,F):")
names = "ACDEF"
for j in range(5):
    ds = [t[j] for _, t in P30_TERMS]
    from collections import Counter
    cnt = Counter(ds)
    print(f"  {names[j]}: " + ", ".join(f"deg{i}:{cnt[i]}" for i in sorted(cnt)))

# total degree of each monomial must be 4 (degree-6 numerator? no — check)
print("\ntotal degrees of the 30 monomials:", sorted({sum(t) for _, t in P30_TERMS}))