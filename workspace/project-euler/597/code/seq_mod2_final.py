#!/usr/bin/env python3
"""Final verification of the mod-2 residue-periodicity rules on the reduced
numerator/denominator sequences of p(3,m), p(4,m), m = L/40.

Rules (derived by inspection + checked here over every available term):
  p3_num odd  <=> m % 4 == 1
  p3_den odd  <=> m % 4 != 1
  p4_num odd  <=> m % 2 == 0
  p4_den odd  <=> m % 4 != 2
All four are provable from the closed forms by 2-adic valuation of the raw
polynomial numerators/denominators (parity of a reduced fraction depends only
on whether v2(raw_num) <= v2(raw_den), etc.); the closed forms themselves are
the run's verified n=3/n=4 results.

Check 1: stored tables code/out/numden_seq.json (m=4..40, reduced fractions).
Check 2: closed-form arithmetic extended to m=41..60 (20 extra terms).
"""
from fractions import Fraction as F
import json

data = json.load(open("code/out/numden_seq.json"))

def p3(m):
    m = F(m)
    return (7*m*m - 17*m + 12) / (18*m*m - 45*m + 27)

def p4(m):
    m = F(m)
    return (19*m**3 - 119*m**2 + 244*m - 162) / (36*m**3 - 216*m**2 + 423*m - 270)

RULES = {
    "p3_num": lambda m: m % 4 == 1,
    "p3_den": lambda m: m % 4 != 1,
    "p4_num": lambda m: m % 2 == 0,
    "p4_den": lambda m: m % 4 != 2,
}

def check(m, name, fn, verbose=False):
    x = fn(m)
    odd = (x.numerator % 2 == 1) if name.endswith("num") else (x.denominator % 2 == 1)
    rule = RULES[name](m)
    if verbose:
        print(f"  m={m:2d} {name:6s} reduced {x.numerator}/{x.denominator}  odd={int(odd)} rule={int(rule)}")
    return odd == rule

bad1 = bad2 = 0
print("== Check 1: stored 37-term tables (m=4..40) ==")
for m in range(4, 41):
    for nm, fn in (("p3", p3), ("p4", p4)):
        for part in ("num", "den"):
            name = f"{nm}_{part}"
            stored = data[f"{nm}_{part}"][m - 4]
            x = fn(m)
            got = (x.numerator, x.denominator)
            if got != (stored, data[f"{nm}_{part}"][m - 4]):
                bad1 += 1
                print(f"  STORED MISMATCH m={m} {name}: closed {got} vs stored {stored}")
            if not check(m, name, fn):
                bad1 += 1
                print(f"  RULE FAIL m={m} {name}")
print(f"  {37*4} checks, {bad1} failures")

print("== Check 2: closed-form arithmetic m=41..60 ==")
for m in range(41, 61):
    for nm, fn in (("p3", p3), ("p4", p4)):
        for part in ("num", "den"):
            if not check(m, f"{nm}_{part}", fn):
                bad2 += 1
                print(f"  RULE FAIL m={m} {nm}_{part}")
print(f"  {20*4} checks, {bad2} failures")
print("RESULT:", "ALL PASS" if bad1 + bad2 == 0 else f"{bad1+bad2} FAILURES")
# first term beyond the verified range that would falsify each rule
print("First falsifier beyond the checked range (m=61):")
for nm, fn in (("p3", p3), ("p4", p4)):
    for part in ("num", "den"):
        name = f"{nm}_{part}"
        x = fn(61)
        odd = (x.numerator % 2 == 1) if part == "num" else (x.denominator % 2 == 1)
        print(f"  {name}: rule predicts odd={int(RULES[name](61))}, actual odd={int(odd)} "
              f"-> {'falsified' if odd != RULES[name](61) else 'holds'}")