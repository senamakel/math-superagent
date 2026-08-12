#!/usr/bin/env python3
"""Independent verification of the conjectured exact closed form

    p(4, L) = (19 m^3 - 119 m^2 + 244 m - 162) / [9 (m-2)(2m-5)(2m-3)],
    m = L/40.

against EVERY exact rational p(4,L) the run has produced, from three sources:
  - code/out/exact_p4_extra.json  (12 original extras + 9 held-out from run 9)
  - code/out/exact_pn.json        (L = 160..1800 subset)
  - the two values computed on the spot: L=200 (m=5), L=600 (m=15)
Every point is exact-rational from the arrangement solver; none of the
hold-out points (L=200,600,2100,...,4800) was used in the original fit.
"""
import json, os
from fractions import Fraction as F

def cubic(m):
    """p4(m) conjecture, exact rational."""
    m = F(m)
    num = 19*m**3 - 119*m**2 + 244*m - 162
    den = 9*(m-2)*(2*m-5)*(2*m-3)
    return num/den

exact = {}
# source 1: extra json (22 entries now)
with open(os.path.join('out', 'exact_p4_extra.json')) as f:
    for L, rec in json.load(f).items():
        if L in exact: assert exact[L] == F(rec['p']), "conflict"
        exact[int(L)] = F(rec['p'])
# source 2: exact_pn.json n=4 entries
with open(os.path.join('out', 'exact_pn.json')) as f:
    data = json.load(f)['L']['4']
    for L, rec in data.items():
        if int(L) in exact: assert exact[int(L)] == F(rec['p']), "conflict"
        exact[int(L)] = F(rec['p'])
# source 3: on-the-spot values
exact[200] = F(458, 945)
exact[600] = F(13616, 26325)

Ls = sorted(exact)
bad = 0
print(f"Total exact p(4,L) points: {len(Ls)}")
print(f"{'L':>6} {'m':>8}  {'exact':>24} {'cubic':>24}  match")
for L in Ls:
    m = F(L, 40)
    pred = cubic(m)
    ok = (pred == exact[L])
    if not ok: bad += 1
    print(f"{L:>6} {str(m):>8}  {str(exact[L]):>24} {str(pred):>24}  {'OK' if ok else 'MISMATCH'}")

print(f"\nMismatches: {bad} / {len(Ls)}")
print(f"Large-L limit of cubic: {cubic(10**9)} = {float(cubic(10**9)):.6f}")