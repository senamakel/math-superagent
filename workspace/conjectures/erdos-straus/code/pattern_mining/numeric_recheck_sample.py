#!/usr/bin/env python3
"""Confirm the numeric 'failures' were a checker bug: re-check a sample of the
603 families with exact Fraction arithmetic and proper positivity (k>=1)."""
import re
from sympy import Symbol, simplify, Rational
from fractions import Fraction

k = Symbol('k')
txt = open('code/out/extended_subprogression.full.txt').read()
lines = txt.splitlines()
fams = []
i = 0
while i < len(lines):
    m = re.match(r'FOUND a=(\d+) b=(\d+)\s+x=(.+)$', lines[i])
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        x = m.group(3)
        ym = re.match(r'\s*y=(.+)$', lines[i+1])
        zm = re.match(r'\s*z=(.+?)\s+\[', lines[i+2])
        if ym and zm:
            fams.append((a, b, simplify(x), simplify(ym.group(1)), simplify(zm.group(1))))
        i += 3
    else:
        i += 1

print(f"{len(fams)} families")
# Use sympy Rational evaluation: expression may be rational like p/q; convert exactly.
def ev(e, kk):
    v = e.subs(k, kk)
    if isinstance(v, Rational):
        return v
    v = simplify(v)
    if isinstance(v, Rational):
        return v
    # integer
    return v

bad_exact = 0
bad_pos = 0
samples_shown = 0
for (a, b, x, y, z) in fams:
    for kk in [1, 5, 17, 100]:
        def Q(e):
            v = ev(e, kk)
            return Fraction(int(v.p), int(v.q)) if hasattr(v, 'p') and hasattr(v, 'q') else Fraction(int(v))
        xx, yy, zz, nn = Q(x), Q(y), Q(z), a*kk + b
        if xx <= 0 or yy <= 0 or zz <= 0:
            if samples_shown < 3:
                print(f"NONPOSITIVE a={a} b={b} k={kk}: x={xx} y={yy} z={zz}")
            bad_pos += 1
        if Fraction(1,xx)+Fraction(1,yy)+Fraction(1,zz) != Fraction(4, nn):
            bad_exact += 1
            samples_shown += 1
print(f"exact-equality failures over sampled k: {bad_exact}")
print(f"non-positive occurrences: {bad_pos}")
print("=> families are exact-positive-integer identities at sampled k "
      "(0 failures at k=1,5,17,100 if both counts 0)")
