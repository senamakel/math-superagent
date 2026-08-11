#!/usr/bin/env python3
"""EXACT p(4,L) for extra integer-L values, with ncells — validation oracle.

Method (the same tetrahedron-subdivision arrangement solver that produced the
10 known values): speeds v_0..v_3 ~ iid Exp(1) are invariant to common
scaling, so the race outcome is a piecewise-constant function of the
normalized speed point, uniform on the 3-simplex (Dirichlet(1,1,1,1), density
(4-1)! = 6). Every candidate event time is const/(affine-linear) in the three
free coordinates (v0,v1,v2; v3 = 1 - sum):
    finish F_j = (L-40j)/v_j,   catch C_ab = 40(b-a)/(v_a-v_b),
so every equality of two candidate times — and every v_a = v_b equality — is
an affine PLANE. The arrangement of these planes cuts the tetrahedron into
open cells of constant chronological event order -> constant race outcome ->
constant parity (exact rational). We enumerate the cells (incremental convex
slicing, exact Fractions), evaluate the exact race parity at each cell's
interior centroid (exact_race.outcome_parity_exact) and sum the exact volumes
of even cells via facet triangulation. p(4,L) = 6 * (sum of even-cell
Euclidean volumes)  [simplex volume = 1/6].

The script FIRST re-derives the 10 known anchors (must reproduce
exact_p4_data.DATA exactly: 160,240,320,400,800,1000,1200,1400,1600,1800),
then computes the 12 requested extra L values and writes
code/out/exact_p4_extra.json as
    {"<L>": {"p": "<num>/<den>", "ncells": <int>}, ...}
incrementally after each value, so an interrupted run can resume (already
present L keys are skipped).

Usage:
    python3 exact_p4_extra.py [L1 L2 ...]   (default: the 12 extra L values)
Flag --skip-anchors skips the anchor re-derivation (for resume).

Complexity: 51 arrangement planes in 3D, cells_3d incremental convex slicing,
per-cell exact volume by vertex enumeration + facet triangulation — polynomial
in the description size, independent of L's magnitude. n=4 only.
"""
import sys, os, json
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from arrangement_pn import build_lines, compute_pn
from exact_p4_data import DATA as KNOWN

OUT = os.path.join('out', 'exact_p4_extra.json')
EXTRA_LS = [480, 560, 640, 900, 1100, 1300, 1500,
            2000, 2500, 3000, 4000, 5000]
SIM_VOL = F(1, 6)   # Euclidean volume of the 3-simplex (free coords)
DENSITY = 6         # (4-1)! Dirichlet density


def p4_exact(L):
    """Return (p, ncells) exact for n=4, integer L. p already carries the
    density factor: compute_pn returns DENSITY * even-cell measure and asserts
    the cell partition covers the whole simplex."""
    lines, _ = build_lines(4, L)
    p, ncells, cells = compute_pn(4, L, lines)
    return p, ncells


def main():
    skip_anchors = '--skip-anchors' in sys.argv
    args = [a for a in sys.argv[1:] if a != '--skip-anchors']
    targets = [int(x) for x in args] or list(EXTRA_LS)

    out = {}
    if os.path.exists(OUT):
        with open(OUT) as f:
            out = json.load(f)

    if not skip_anchors:
        print("=" * 78)
        print("A. Anchor re-derivation (known 10) — oracle sanity check")
        for L in sorted(KNOWN):
            p, ncells = p4_exact(L)
            ok = (str(p) == KNOWN[L])
            print(f"  L={L:5d}  p={p}  ({float(p):.12f})  cells={ncells:5d}"
                  f"  {'OK' if ok else 'MISMATCH expected ' + KNOWN[L]}")
            assert ok, f"anchor L={L}: got {p}, expected {KNOWN[L]}"
        print("  -> all 10 anchors reproduced exactly")
    else:
        print("A. Anchors skipped (--skip-anchors)")

    print("=" * 78)
    print("B. Requested extra L values")
    for L in targets:
        key = str(L)
        if key in out:
            print(f"  L={L:5d}  already in {OUT}: "
                  f"{out[key]['p']}  cells={out[key]['ncells']}")
            continue
        p, ncells = p4_exact(L)
        out[key] = {"p": f"{p.numerator}/{p.denominator}", "ncells": ncells}
        os.makedirs('out', exist_ok=True)
        with open(OUT, 'w') as f:
            json.dump(out, f, indent=2)
        print(f"  L={L:5d}  p={p}  ({float(p):.12f})  cells={ncells:5d}"
              f"  [json updated]")
    print("=" * 78)
    print(f"Final {len(out)} values in {OUT}:")
    for k in sorted(out, key=int):
        print(f"  L={k:5s}  p={out[k]['p']}  cells={out[k]['ncells']}")


if __name__ == '__main__':
    main()