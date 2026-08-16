#!/usr/bin/env python3
"""Demo + verification for code/lib/es_geom.py (exact-arithmetic oracle).

Runs every verification target in the tool request and writes the transcript
to code/out/es_oracle_verify.txt.
"""
import sys
import os
from itertools import combinations
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from lib.es_geom import (orient, general_position, in_convex_position,
                         largest_convex_subset, has_convex_k_gon,
                         convex_hull, cups_caps)
from lib.es_construction import build_es

OUT = os.path.join(os.path.dirname(__file__), "..", "out", "es_oracle_verify.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

lines = []


def log(s=""):
    print(s)
    lines.append(s)


def check(name, got, expected):
    ok = (got == expected)
    log(f"[{'PASS' if ok else 'FAIL'}] {name}: got {got}, expected {expected}")
    return ok


all_ok = True


def main():
    global all_ok
    log("=" * 70)
    log("Exact-arithmetic Erdős–Szekeres oracle — verification transcript")
    log("=" * 70)

    # ---- orient / general position sanity ------------------------------
    log("\n--- orient: exact sign of orientation determinant ---")
    A = (Fraction(0), Fraction(0))
    B = (Fraction(1), Fraction(0))
    C = (Fraction(0), Fraction(1))
    D = (Fraction(1), Fraction(1))
    E = (Fraction(2), Fraction(0))
    all_ok &= check("orient(A,B,C) ccw", orient(A, B, C), 1)
    all_ok &= check("orient(A,C,B) cw", orient(A, C, B), -1)
    all_ok &= check("orient(A,B,E) collinear", orient(A, B, E), 0)

    # ---- 4-point set with one point inside a triangle ------------------
    log("\n--- ES(4) > 4 witness: one point inside a triangle ---")
    tri_pts = [(Fraction(0), Fraction(0)),
               (Fraction(4), Fraction(0)),
               (Fraction(0), Fraction(4)),
               (Fraction(1), Fraction(1))]   # (1,1) strictly inside
    all_ok &= check("general_position(4-pt)", general_position(tri_pts), True)
    lc = largest_convex_subset(tri_pts)
    all_ok &= check("largest_convex_subset == 3", lc, 3)

    # ---- convex pentagon ------------------------------------------------
    log("\n--- convex pentagon: largest convex subset 5 ---")
    pent = [(Fraction(0), Fraction(0)),
            (Fraction(2), Fraction(0)),
            (Fraction(3), Fraction(1)),
            (Fraction(1), Fraction(3)),
            (Fraction(-1), Fraction(2))]
    all_ok &= check("in_convex_position(pentagon)", in_convex_position(pent), True)
    all_ok &= check("largest_convex_subset(pentagon)", largest_convex_subset(pent), 5)

    # ---- ES(4)=5 upper bound: every 5-subset of a 5x5 grid (general pos) ----
    log("\n--- ES(4) = 5 upper check: all 5-subsets of 5x5 grid ---")
    grid = [(Fraction(x), Fraction(y)) for x in range(5) for y in range(5)]
    n_five, n_gp, n_convex4, n_bad = 0, 0, 0, 0
    for sub in combinations(grid, 5):
        n_five += 1
        if not general_position(sub):
            continue
        n_gp += 1
        if has_convex_k_gon(sub, 4):
            n_convex4 += 1
        else:
            n_bad += 1
            if n_bad <= 3:
                log(f"  !! 5-set with NO convex 4-gon (general pos): {sub}")
    log(f"  5-subsets total={n_five}, general-position={n_gp}, with convex 4-gon={n_convex4}, bad={n_bad}")
    all_ok &= check("every general-position 5-subset has convex 4-gon", n_bad, 0)
    all_ok &= check("found >=1 general-position 5-subset", n_gp > 0, True)

    # ---- ES construction: largest convex subset at n=4,5,6 --------------
    log("\n--- ES construction (2^{n-2} points, no convex n-gon) ---")
    for n in (4, 5, 6):
        s = build_es(n)
        gp = general_position(s)
        lc = largest_convex_subset(s)
        exp_size = 1 << (n - 2)
        all_ok &= check(f"ES n={n}: |S| == 2^{n-2}", len(s), exp_size)
        all_ok &= check(f"ES n={n}: general position", gp, True)
        all_ok &= check(f"ES n={n}: no convex {n}-gon (largest <= {n-1})",
                        lc <= n - 1, True)
        log(f"  ES n={n}: exact largest convex subset = {lc}")
        all_ok &= check(f"ES n={n}: has_convex_{n}_gon is False", has_convex_k_gon(s, n), False)
        log(f"  S = {s}")

    # ---- cups / caps on the ES construction -------------------------------
    log("\n--- cup/cap spectra (exact slopes) ---")
    for n in (4, 5, 6):
        s = build_es(n)
        sp = cups_caps(s)
        log(f"  n={n}: longest cup={sp['cup']}, longest cap={sp['cap']} "
            f"(points sorted by x: {len(sp['sorted'])})")

    # ---- summary ----------------------------------------------------------
    log("\n" + "=" * 70)
    log("RESULT: " + ("ALL CHECKS PASSED" if all_ok else "SOME CHECKS FAILED"))
    log("=" * 70)

    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"\n[transcript written to {OUT}]")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
