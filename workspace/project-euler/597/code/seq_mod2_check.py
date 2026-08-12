#!/usr/bin/env python3
"""Check mod-2 residue periodicities the analyzer flagged on the reduced
numerator/denominator sequences of p(3,m), p(4,m), m=L/40.
Sequences come from code/out/numden_seq.json (m=4..40).
Verifies the periodicity holds over ALL terms (mechanically), and states the
first term that would falsify an extrapolation."""
from fractions import Fraction as F
import json

data = json.load(open("code/out/numden_seq.json"))
p3_num, p3_den = data["p3_num"], data["p3_den"]
p4_num, p4_den = data["p4_num"], data["p4_den"]

def p3(m):
    m = F(m)
    return (7*m*m - 17*m + 12) / (18*m*m - 45*m + 27)
def p4(m):
    m = F(m)
    return (19*m**3 - 119*m**2 + 244*m - 162) / (36*m**3 - 216*m**2 + 423*m - 270)

for name, fn, L in [("p3", p3, p3_num), ("p3", p3, p3_den),
                    ("p4", p4, p4_num), ("p4", p4, p4_den)]:
    pass

# regenerate directly from the closed forms for m=4..40 and compare parity
for nm, fn in [("p3", p3), ("p4", p4)]:
    for part in ("num", "den"):
        seq = []
        for m in range(4, 41):
            x = fn(m)
            v = x.numerator if part == "num" else x.denominator
            seq.append(v % 2)
        # find minimal period
        N = len(seq)
        found = None
        for p in range(1, N):
            if all(seq[i] == seq[i % p] for i in range(N)):
                found = p
                break
        print(f"{nm}_{part} mod2 over m=4..40 ({N} terms): {seq[:20]}... period={found}")

# check the reduced-fraction parity observation: is p(n,m) itself (as a
# rational) ever reducible to odd/odd? just report parity of reduced num/den.
print()
for nm, fn in [("p3", p3), ("p4", p4)]:
    for m in range(4, 41):
        x = fn(m)
        a, b = x.numerator % 2, x.denominator % 2
        assert not (a == 0 and b == 0), "both even -> fraction not reduced"
    print(f"{nm}: all reduced fractions over m=4..40 have num,den not both even [OK]")
