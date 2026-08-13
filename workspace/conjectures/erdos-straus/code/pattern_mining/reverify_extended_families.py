#!/usr/bin/env python3
"""Independently re-verify every sub-progression family found by the extended
search (parsed from the FOUND lines carrying full x,y,z expressions), as a
symbolic identity 4/n = 1/x+1/y+1/z with n=a*k+b, plus exact numeric check
at sampled k, plus per-modulus residue coverage accounting."""
import re
from sympy import Symbol, simplify
from fractions import Fraction

k = Symbol('k')
txt = open('code/out/extended_subprogression.full.txt').read()

# Each FOUND block spans 3-4 lines: FOUND a= b=  x=... \n y=... \n z=... [shape]
fams = []
i = 0
lines = txt.splitlines()
while i < len(lines):
    m = re.match(r'FOUND a=(\d+) b=(\d+)\s+x=(.+)$', lines[i])
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        x = m.group(3)
        yline = lines[i+1]
        zline = lines[i+2]
        ym = re.match(r'\s*y=(.+)$', yline)
        zm = re.match(r'\s*z=(.+?)\s+\[', zline)
        if ym and zm:
            fams.append((a, b, x, ym.group(1), zm.group(1)))
        i += 3
    else:
        i += 1

print(f"parsed {len(fams)} families with full x,y,z expressions")

bad_ident = []
bad_numeric = []
bad_pos = []
from collections import defaultdict
per = defaultdict(set)
checked = 0
for (a, b, xs, ys, zs) in fams:
    x, y, z = simplify(xs), simplify(ys), simplify(zs)
    diff = simplify(4 / (a*k + b) - (1/x + 1/y + 1/z))
    if diff != 0:
        bad_ident.append((a, b))
    # numeric exact check at a handful of k AND positivity
    ok_num = True
    for kk in range(4):
        try:
            xx, yy, zz, nn = [int(simplify(e.subs(k, kk))) for e in (x, y, z)], a*kk+b
        except Exception:
            ok_num = False; break
        xx, yy, zz = [int(simplify(e.subs(k, kk))) for e in (x, y, z)]
        if min(xx,yy,zz) <= 0 or Fraction(1,xx)+Fraction(1,yy)+Fraction(1,zz) != Fraction(4, nn):
            ok_num = False; break
    if not ok_num:
        bad_numeric.append((a, b))
    per[a//840].add((b-1)//840)
    checked += 1

print(f"checked {checked} families")
print(f"symbolic identity failures: {len(bad_ident)}  {bad_ident[:5]}")
print(f"numeric/positivity failures: {len(bad_numeric)}  {bad_numeric[:5]}")

# Per-modulus coverage
print("\nper-modulus covered residues (K mod M):")
for M in sorted(per):
    print(f"  M={M:3}: {sorted(per[M])}  ({len(per[M])}/{M})")
