#!/usr/bin/env python3
"""verify_base.py -- exact base-oracle verification for PE 597.

Reproduces four exact p(n,L) anchor values using the exact arrangement-cell
integration oracle cell_exact.p_exact, comparing against known exact rationals:

  p(3,160)  = 56/135
  p(4,400)  = 521/1020     (= 0.5107843137..., the given worked example)
  p(3,400)  = 542/1377
  p(4,1800) = 166802/317985

All arithmetic is exact rational (Fraction). Each (n,L) is evaluated once by
the arrangement enumerator and compared exactly. PASS/FAIL printed per case,
with cell counts.

Usage: python3 verify_base.py
"""
from fractions import Fraction as F
from cell_exact import p_exact

CASES = [
    (3, 160,  F(56, 135),      "p(3,160)"),
    (4, 400,  F(521, 1020),    "p(4,400)"),
    (3, 400,  F(542, 1377),    "p(3,400)"),
    (4, 1800, F(166802, 317985), "p(4,1800)"),
]


def main():
    all_ok = True
    for n, L, expected, label in CASES:
        p, even_vol, even_count, nleaves, dt = p_exact(n, L)
        ok = (p == expected)
        all_ok = all_ok and ok
        print(f"{label:14s} n={n} L={L:<5} cells={nleaves:<5} "
              f"even_cells={even_count:<5}  got={p}  expected={expected}")
        print(f"    float got={float(p):.12f}   ->  {'PASS' if ok else 'FAIL'}")
    print(f"\nOVERALL: {'ALL PASS' if all_ok else 'FAILURE'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
