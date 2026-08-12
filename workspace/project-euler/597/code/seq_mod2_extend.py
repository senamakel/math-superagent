#!/usr/bin/env python3
"""Extend the reduced numerator/denominator parity check beyond the stored
range (m=4..40) to m=41..60, straight from the verified closed forms.
Purpose: the parity periods (p3_num odd iff m=1 mod 4, p3_den even iff m=2
mod 4, p4_num odd iff m odd, p4_den even iff m=2 mod 4) hold over all 37
stored terms; this extends the arithmetic to 20 more terms. It tests the
arithmetic of the closed form, NOT the race -- the closed form itself is
already the verified statement."""
from fractions import Fraction as F

def p3(m):
    m = F(m)
    return (7*m*m - 17*m + 12) / (18*m*m - 45*m + 27)

def p4(m):
    m = F(m)
    return (19*m**3 - 119*m**2 + 244*m - 162) / (36*m**3 - 216*m**2 + 423*m - 270)

rules = {
    "p3_num": lambda m: m % 4 == 1,
    "p3_den": lambda m: m % 4 != 2,
    "p4_num": lambda m: m % 2 == 1,
    "p4_den": lambda m: m % 4 != 2,
}

bad = 0
for m in range(41, 61):
    for name, fn in (("p3", p3), ("p4", p4)):
        x = fn(m)
        checks = {
            "p3_num": x.numerator % 2 == 1,
            "p3_den": x.denominator % 2 == 1,
            "p4_num": x.numerator % 2 == 1,
            "p4_den": x.denominator % 2 == 1,
        }
        for key, val in checks.items():
            ok = (val == rules[key](m))
            if not ok:
                bad += 1
                print(f"MISMATCH m={m} {key}: got odd={val}, rule says odd={rules[key](m)}")
print(f"extended parity check m=41..60: {20*4} checks, {bad} mismatches")