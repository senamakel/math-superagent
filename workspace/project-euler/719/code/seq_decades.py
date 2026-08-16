#!/usr/bin/env python3
"""Decade-increment sequences from the A038206 b-file (complete to 10^9).
D_k = #{roots in (10^{k-1}, 10^k]}, k=1..9
I_k = sum of m^2 over roots in (10^{k-1}, 10^k], k=1..9
"""
import re, json

B_FILE = "research/sources/oeis_a038206_b.full.md"
roots = []
with open(B_FILE) as f:
    for line in f:
        m = re.match(r"\s*(\d+)\s+(\d+)\s*$", line)
        if m:
            roots.append(int(m.group(2)))

bounds = [10**k for k in range(0, 10)]
D, I = [], []
for k in range(1, 10):
    lo, hi = bounds[k-1], bounds[k]
    D.append(sum(1 for r in roots if lo < r <= hi))
    I.append(sum(r*r for r in roots if lo < r <= hi))
print("D_k (roots in decade k):", D)
print("I_k (sum m^2 in decade k):", I)
print("checks: sum(D) == 3191, 4+sum(D[1:]) == 3191:", 4 + sum(D[1:]) == 3191)
print("T(10^1)..T(10^9) from cumsum of I:", [sum(I[:k]) + 182 - 182 for k in range(1, 10)])