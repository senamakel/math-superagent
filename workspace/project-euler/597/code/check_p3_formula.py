#!/usr/bin/env python3
"""Test the conjectured exact closed form
   p(3, L) = (7 m^2 - 17 m + 12)/(18 m^2 - 45 m + 27),  m = L/40
against every exact data point available (12 original + 16 extras)."""
from fractions import Fraction as F
from exact_p3_data import DATA

EXTRA = {
    120: "4/9", 200: "17/42", 280: "118/297", 360: "71/180",
    440: "112/285", 520: "487/1242", 560: "382/975", 720: "658/1683",
    900: "4231/10836", 1100: "6451/16536", 2000: "5554/14259",
    2400: "896/2301", 3000: "6352/16317", 4000: "68312/175527",
    5000: "5959/15314",
}

def formula(L):
    m = F(L, 40)
    num = 7*m*m - 17*m + 12
    den = 18*m*m - 45*m + 27
    return num/den

all_pts = {}
for L, p in DATA.items():
    all_pts[L] = F(p)
for L, p in EXTRA.items():
    all_pts[L] = F(p)

bad = 0
for L in sorted(all_pts):
    exact = all_pts[L]
    pred = formula(L)
    ok = (pred == exact)
    if not ok: bad += 1
    print(f"L={L:5d}  exact={str(exact):>14s}  formula={str(pred):>14s}  match={ok}")

print(f"\nTOTAL points: {len(all_pts)}, mismatches: {bad}")
print("Limit m->inf of formula =", F(7,18), float(F(7,18)))
