#!/usr/bin/env python3
"""Exact verification of the A052905 identification for the Bautin
monomial-count complement sequences.

Data (exact, held captures):
  5-param chart family:  counts a_d (d=4..16) = 4,30,97,236,485,890,1505
     (code/out/mono_counts.captured.txt, focal_denoms.captured.txt,
      .d16 run)   dim(h) = C(h+4,4), h = d-2
  6-param general focus: counts a_d (d=4..12) = 6,56,220,628,1481
     (code/out/bautin_focal_values.captured.txt, focal6_L10_L12.captured.txt)
     dim(h) = C(h+5,5), h = d-2

Claim to verify: c(h) := dim - 2*a  equals  A052905(h/2) = (j^2+7j+2)/2,
j = h/2, for every computed even h >= 4 in each family, and the 6-param
c_6(h) = c_5(h) + h exactly.

Everything exact integer/rational arithmetic; no floats.
"""
from math import comb
from fractions import Fraction

A052905 = lambda j: (j*j + 7*j + 2) // 2   # OEIS A052905, a(n)=(n^2+7n+2)/2

print("# A052905 identification check — exact")
print("# 5-param: c5(h) = C(h+4,4) - 2*a_{h+2};  6-param: c6(h) = C(h+5,5) - 2*a_{h+2}")
print()

a5 = {4: 4, 6: 30, 8: 97, 10: 236, 12: 485, 14: 890, 16: 1505}
a6 = {4: 6, 6: 56, 8: 220, 10: 628, 12: 1481}

print("5-param family:")
all5 = True
for d, a in sorted(a5.items()):
    h = d - 2
    dim = comb(h + 4, 4)
    c = dim - 2 * a
    j = h // 2
    pred = A052905(j)
    frac = Fraction(h*h + 14*h + 8, 8)
    ok = (c == pred == frac)
    all5 &= ok
    print(f"  d={d:2d} h={h:2d} a={a:5d} dim={dim:5d} c={c:4d}  "
          f"A052905({j})={pred:4d}  formula={frac}  match={ok}")
print("  ALL 5-PARAM MATCH:", all5)
print()

print("6-param family:")
all6 = True
for d, a in sorted(a6.items()):
    h = d - 2
    dim = comb(h + 5, 5)
    c = dim - 2 * a
    pred = Fraction(h*h + 22*h + 8, 8)
    j = h // 2
    ok = (c == pred and c == A052905(j) + h)   # c6(h) = c5(h) + h
    all6 &= ok
    print(f"  d={d:2d} h={h:2d} a={a:5d} dim={dim:5d} c={c:4d}  "
          f"(h^2+22h+8)/8={pred}  A052905({j})+h={A052905(j)+h}  match={ok}")
print("  ALL 6-PARAM MATCH:", all6)
print()
print("cross-family: c6(h) - c5(h) == h on shared h:")
for h in (4, 6, 8, 10):
    c5 = comb(h+4, 4) - 2*a5[h+2]
    c6 = comb(h+5, 5) - 2*a6[h+2]
    print(f"  h={h:2d}: c6-c5 = {c6-c5}  (h = {h})  match={c6-c5 == h}")
print()

print("# Falsifiers (uncomputed when this note was written):")
print("#  5-param: a_18 = (C(20,4) - A052905(8))/2 =", (comb(20,4) - A052905(8)) // 2)
print("#  6-param: a_14 = (C(17,5) - (A052905(6)+12))/2 =",
      (comb(17, 5) - (A052905(6) + 12)) // 2)
print("#  (C(17,5) =", comb(17,5), ", c6(12) =", A052905(6)+12, ")")
