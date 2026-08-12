#!/usr/bin/env python3
"""Reconfirm the two exact closed forms in memory:

    p(3,L) = (7m^2 - 17m + 12)/(18m^2 - 45m + 27)
    p(4,L) = (19m^3 - 119m^2 + 244m - 162)/(36m^3 - 216m^2 + 423m - 270)

with m = L/40, by exact rational evaluation.

Prints exact rationals at:
  - L = 1800  (m = 45)  -- the PE597 target finish distance,
  - L = 160   (m = 4)   -- n=3 statement example,
  - L = 400   (m = 10)  -- n=4 statement example,
and the large-L limits.

Cross-checks against every stored exact arrangement-solver value in
out/exact_p3_extra.json and out/exact_p4_extra.json (0 mismatches expected),
including the two statement anchors 56/135 and 521/1020.

Pure exact integer/rational arithmetic (fractions.Fraction); no sampling.
"""
import json
from fractions import Fraction as F

def p3(m):
    m = F(m)
    return (7*m**2 - 17*m + 12) / (18*m**2 - 45*m + 27)

def p4(m):
    m = F(m)
    num = 19*m**3 - 119*m**2 + 244*m - 162
    den = 36*m**3 - 216*m**2 + 423*m - 270
    return num / den

def p2(m):
    m = F(m)
    return m / (2*m - 1)

def check_stored():
    """All stored exact points vs the closed forms; returns (npts, nmis)."""
    nmis = 0
    npts = 0
    with open('out/exact_p3_extra.json') as fh:
        for L, rec in json.load(fh).items():
            exact = F(rec['p'])
            pred = p3(F(int(L), 40))
            npts += 1
            if pred != exact:
                nmis += 1
                print(f"  MISMATCH n=3 L={L}: exact {exact} vs {pred}")
    with open('out/exact_p4_extra.json') as fh:
        for L, rec in json.load(fh).items():
            exact = F(rec['p'])
            pred = p4(F(int(L), 40))
            npts += 1
            if pred != exact:
                nmis += 1
                print(f"  MISMATCH n=4 L={L}: exact {exact} vs {pred}")
    return npts, nmis

if __name__ == "__main__":
    print("=== Closed-form reconfirmation, m = L/40, exact rationals ===")
    print()
    for n, fn in ((2, p2), (3, p3), (4, p4)):
        for L in (160, 400, 1800):
            m = F(L, 40)
            val = fn(m)
            print(f"  n={n} L={L:5d} m={m!s:>4}:  {val}  =  {float(val):.12f}")
        print()

    p3_sym = F(7, 18)
    p4_sym = F(19, 36)
    print(f"  large-L limit p(3,inf) = {p3_sym} = {float(p3_sym):.10f}")
    print(f"  large-L limit p(4,inf) = {p4_sym} = {float(p4_sym):.10f}")
    print(f"  large-L limit p(2,inf) = 1/2")
    print()

    # anchors
    a3 = p3(F(160, 40))
    a4 = p4(F(400, 40))
    assert a3 == F(56, 135), a3
    assert a4 == F(521, 1020), a4
    print(f"  anchors: p(3,160) = {a3}  (statement 56/135 OK)")
    print(f"           p(4,400) = {a4} = {float(a4):.10f}  (statement 0.5107843137 OK)")
    print()
    npts, nmis = check_stored()
    print(f"  stored exact points checked: {npts}, mismatches: {nmis}")
    import os
    with open('out/closed_form_reconfirmation.txt', 'w') as fh:
        fh.write("Closed-form reconfirmation (exact rationals), m = L/40\n")
        fh.write("p(3,L) = (7m^2-17m+12)/(18m^2-45m+27)\n")
        fh.write("p(4,L) = (19m^3-119m^2+244m-162)/(36m^3-216m^2+423m-270)\n")
        fh.write("\n")
        for n, fn in ((2, p2), (3, p3), (4, p4)):
            for L in (160, 400, 1800):
                val = fn(F(L, 40))
                fh.write(f"n={n} L={L} m={F(L,40)}: {val} = {float(val):.12f}\n")
        fh.write("\n")
        fh.write(f"large-L limit p(3,inf) = {p3_sym} = {float(p3_sym):.10f}\n")
        fh.write(f"large-L limit p(4,inf) = {p4_sym} = {float(p4_sym):.10f}\n")
        fh.write("\n")
        fh.write(f"anchors: p(3,160)={a3}, p(4,400)={a4}={float(a4):.10f}\n")
        fh.write(f"stored exact points rechecked: {npts}, mismatches: {nmis}\n")
    print()
    print(f"wrote out/closed_form_reconfirmation.txt")