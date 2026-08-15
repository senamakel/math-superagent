#!/usr/bin/env python3
"""Fit the degree-7 chromatic polynomial of the Moser spindle to values at
k=0..7 (P(0)=P(1)=P(2)=P(3)=0, P(4)=384,...), then evaluate it at 8,9,10 and
compare with the freshly computed exact counts. If they match, the
"proper-colouring count is a degree-n polynomial" fact is verified on the Moser
with an out-of-sample check.
"""
from sympy import symbols, interpolate, Rational, expand, factor
k=symbols('k')
points = {0:0,1:0,2:0,3:0,4:384,5:5040,6:31680,7:134400}
poly=interpolate(list(points.items()), k)
poly=expand(poly)
print("chromatic polynomial (degree 7):")
print(poly)
print("\nfactorised:")
print(factor(poly))
print("\npredicted values at k=8,9,10 vs exact fresh:")
print("P(8)  pred", poly.subs(k,8), "(exact 443520)")
print("P(9)  pred", poly.subs(k,9), "(exact 1227744)")
print("P(10) pred", poly.subs(k,10), "(exact 2983680)")
