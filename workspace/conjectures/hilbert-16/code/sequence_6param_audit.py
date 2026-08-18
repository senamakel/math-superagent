#!/usr/bin/env python3
"""Exact audit of the 6-parameter general-quadratic-focus focal-value data.

Family (linear centre part):
    u' = -v + a1 u^2 + a2 u v + a3 v^2
    v' =  u + b1 u^2 + b2 u v + b3 v^2
rot(p) = -v p_u + u p_v, V2 = (u^2+v^2)/2, gauge c_{d,0}=0,
L_d = even-degree radial obstruction (d-th focal value), homogeneous of
degree h = d-2 in the six parameters (a1,a2,a3,b1,b2,b3).

Data provenance (all exact, held captures):
  L4=6, L6=56, L8=220 monomials  -- code/out/bautin_focal_values.captured.txt
      (printed inline as "monomials: 6 / 56 / 220"), and re-asserted as a
      guard by the exact run in code/out/focal6_L10_L12.captured.txt.
  L10=628, L12=1481             -- code/out/focal_6coeff_L10.txt / L12.txt
      (exact ilcm-cleared dumps; recounted here from the raw term lists).
  Denominators: L10=1105920, L12=22295347200 (same dumps).

This program recounts the dumps itself, re-derives the denominators and L1
norms, checks homogeneity, assembles the count and complement sequences, and
tests the quadratic complement conjecture c(h) = (h^2 + 22 h + 8)/8.
Everything exact integer/rational arithmetic; no floats.
"""
import re
from math import comb
from fractions import Fraction

PARAM_MONOMIALS_6V = [comb(h + 5, 5) for h in (2, 4, 6, 8, 10, 12)]


def load_dump(path):
    txt = open(path).read()
    denom = int(re.search(r"DENOM_L\d+ = (\d+)", txt).group(1))
    rows = re.findall(r"\((-?\d+), \(([\d, ]+)\)\)", txt)
    terms = [(int(c), tuple(int(x) for x in m.split(","))) for c, m in rows]
    return denom, terms


def main():
    print("# 6-parameter general-quadratic-focus focal values: exact audit")
    print("# family: u'=-v+a1u^2+a2uv+a3v^2, v'=u+b1u^2+b2uv+b3v^2, rot, gauge c_{d,0}=0")
    print()

    # --- recount the machine dumps directly ---
    d10, t10 = load_dump("code/out/focal_6coeff_L10.txt")
    d12, t12 = load_dump("code/out/focal_6coeff_L12.txt")
    print("dump recount: L10 terms =", len(t10), " denom =", d10,
          " L1 =", sum(abs(c) for c, _ in t10))
    print("dump recount: L12 terms =", len(t12), " denom =", d12,
          " L1 =", sum(abs(c) for c, _ in t12))
    hd10 = set(sum(m) for _, m in t10)
    hd12 = set(sum(m) for _, m in t12)
    print("homogeneity: L10 hdeg =", hd10, "(expect {8}); L12 hdeg =", hd12,
          "(expect {10})")
    assert len(t10) == 628 and d10 == 1105920
    assert len(t12) == 1481 and d12 == 22295347200
    assert hd10 == {8} and hd12 == {10}
    print("guards on the dumps: PASS (counts 628/1481, denoms 1105920/22295347200)")
    print()

    # --- assembled exact sequences ---
    counts = {4: 6, 6: 56, 8: 220, 10: 628, 12: 1481}   # L_d monomial counts
    denoms = {4: 8, 6: 192, 8: 18432, 10: 1105920, 12: 22295347200}
    hvals = [2, 4, 6, 8, 10]
    a = [counts[d] for d in (4, 6, 8, 10, 12)]
    dims = [comb(h + 5, 5) for h in hvals]
    c = [dim - 2 * x for dim, x in zip(dims, a)]
    print("counts a_d (d=4..12):      ", a)
    print("ambient dim C(h+5,5), h=d-2:", dims)
    print("complements c = dim - 2a:   ", c)
    print("first diffs of c:           ", [c[i+1]-c[i] for i in range(len(c)-1)])
    print("second diffs of c:          ", [c[i+2]-2*c[i+1]+c[i] for i in range(len(c)-2)])
    print()

    # --- quadratic complement conjecture on h >= 4 ---
    print("## conjecture: c(h) = (h^2 + 22h + 8)/8 for even h >= 4")
    for h, cc, aa in zip(hvals, c, a):
        f = Fraction(h*h + 22*h + 8, 8)
        print(f"  h={h:2d}  c={cc:3d}  formula={f}  PASS={cc == f}   "
              f"(then a = {Fraction(dims[hvals.index(h)] - f, 2)})")
    f2 = Fraction(2*2 + 22*2 + 8, 8)
    print(f"  h= 2  c={c[0]:3d}  formula={f2}  exceptional (like the 5-param family)")
    print()

    # --- cross-family comparison with the 5-param chart family ---
    print("## cross-family comparison (5-param chart family vs 6-param general focus)")
    c5 = {2: 7, 4: 10, 6: 16, 8: 23, 10: 31, 12: 40, 14: 50}
    print("  denominators ilcm: 5-param [8,192,18432,1105920,22295347200]")
    print("                     6-param", [denoms[d] for d in (4, 6, 8, 10, 12)])
    print("  (same at every computed d; both recurrences invert the same rot map)")
    print("  complement c(h):   5-param (h^2+14h+8)/8,  6-param (h^2+22h+8)/8")
    print("  linear coeff 14 -> 22 when going 5 -> 6 parameters (2 data points only)")
    print()

    # --- predicted falsifier ---
    h12 = 12
    f12 = Fraction(h12*h12 + 22*h12 + 8, 8)
    a14 = Fraction(comb(17, 5) - f12, 2)
    print("## first falsifier: h=12 (d=14)")
    print(f"  predicted c(12) = {f12}; predicted a_14 = (C(17,5)-c)/2 = {a14}")
    print("  integer?", a14.denominator == 1)


if __name__ == "__main__":
    main()
