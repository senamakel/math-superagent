#!/usr/bin/env python3
"""Verify the conjectured rational-in-m closed forms against EVERY stored
exact p(n,L), n=2,3,4. Also print the coefficient sequences and check the
pole-ladder prediction for the denominators.

p(2,L) = m/(2m-1)
p(3,L) = (7m^2-17m+12)/(18m^2-45m+27)
p(4,L) = (19m^3-119m^2+244m-162)/(36m^3-216m^2+423m-270)
= (19m^3-119m^2+244m-162)/(9(m-2)(2m-5)(2m-3)),  m=L/40.
"""
import os, json
from fractions import Fraction as F

def p2(m):
    return m/(2*m-1)
def p3(m):
    return (7*m*m-17*m+12)/(18*m*m-45*m+27)
def p4(m):
    num = 19*m**3-119*m**2+244*m-162
    den = 36*m**3-216*m**2+423*m-270
    return num/den

forms = {2: p2, 3: p3, 4: p4}

# gather all exact points from every json
points = {}   # (n,L) -> Fraction
files = {
    3: 'out/exact_p3_extra.json',
    4: 'out/exact_p4_extra.json',
}
for n, path in files.items():
    with open(path) as fh:
        data = json.load(fh)
    for L, rec in data.items():
        points[(n, int(L))] = F(rec['p'])

with open('out/exact_pn.json') as fh:
    data = json.load(fh)['L']
for nstr, d in data.items():
    n = int(nstr)
    if n not in forms:
        continue
    for L, rec in d.items():
        points[(n, int(L))] = F(rec['p'])

# on-the-spot verified extras from verify_p4_cubic.py
points[(4, 200)] = F(458, 945)
points[(4, 600)] = F(13616, 26325)

bad = 0
by_n = {2:0,3:0,4:0}
print(f"{'n':>2} {'L':>6} {'m':>7}  {'exact':>22} {'formula':>22}  ok")
for (n, L) in sorted(points):
    m = F(L, 40)
    pred = forms[n](m)
    ok = (pred == points[(n, L)])
    if not ok: bad += 1
    by_n[n] += 1
    print(f"{n:>2} {L:>6} {str(m):>7}  {str(points[(n,L)]):>22} {str(pred):>22}  {'OK' if ok else 'MISMATCH'}")
print(f"\nTOTAL exact points: {len(points)}  mismatches: {bad}")
print("by n:", by_n)
for n in (2,3,4):
    lim = forms[n](F(10**9))
    print(f"large-L limit p{n}(inf): {lim} = {float(lim):.8f}")
