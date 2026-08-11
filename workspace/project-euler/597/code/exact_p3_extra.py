#!/usr/bin/env python3
"""EXACT p(3,L) for the extra integer-L list (validation oracle, n=3 only).

Method (same machinery as arrangement_pn.py): speeds v0,v1,v2 ~ iid Exp(1),
invariant to common scaling, so the race outcome is a piecewise-constant
function of the normalized speed point, uniform on the 2-simplex
(Dirichlet(1,1,1), density (3-1)! = 2). Every candidate event time is
const/linear  (finish F_j = (L-40j)/v_j, catch C_ab = 40(b-a)/(v_a-v_b)), so
every pairwise equality of candidate times, and every v_a = v_b equality, is
an affine LINE in the two free coordinates (v0, v1; v2 = 1-v0-v1). The
arrangement of these lines cuts the triangle into open cells of constant
chronological event order -> constant race outcome -> constant parity. We
enumerate the cells exactly (recursive polygon clipping), evaluate the exact
race parity at each cell centroid (exact_rational, via
exact_race.outcome_parity_exact), and sum the exact cell areas of even cells.
p(3,L) = 2 * (sum of even-cell Euclidean areas)  [simplex volume = 1/2].

This script FIRST re-derives the 12 known anchors (must reproduce
exact_p3_data.DATA exactly), THEN computes the 16 requested extra L values and
writes code/out/exact_p3_extra.json as
    {"<L>": {"p": "<num>/<den>", "ncells": <int>}, ...}

Complexity: 18 arrangement lines in 2D -> at most O(m^2) cells per L, exact
rational clipping; polynomial in the description size, independent of L's
magnitude. Bounded to n=3 only (the 2D enumerator).
"""
import sys, os, json
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from arrangement_pn import build_lines, compute_pn, poly_area
from exact_p3_data import DATA as KNOWN

EXTRA_LS = [120, 200, 280, 360, 440, 520, 560, 720, 900,
            1100, 1400, 2000, 2400, 3000, 4000, 5000]

SIM_VOL = F(1, 2)          # Euclidean area of the 2-simplex
DENSITY = 2                # (3-1)! Dirichlet density


def p3_exact(L):
    """Return (p, ncells) exact for n=3, integer L."""
    lines, _ = build_lines(3, L)
    p, ncells, cells = compute_pn(3, L, lines)
    # sanity: the arrangement must partition the whole simplex
    tot = sum(poly_area(c) for c in cells)
    assert tot == SIM_VOL, (L, tot)
    return p, ncells


def main():
    out = {}
    print("=" * 78)
    print("A. Anchor re-derivation (known 12) — oracle sanity check")
    for L in sorted(KNOWN):
        p, ncells = p3_exact(L)
        ok = (str(p) == KNOWN[L])
        print(f"  L={L:5d}  p={p}  ({float(p):.12f})  cells={ncells:4d}"
              f"  {'OK' if ok else 'MISMATCH expected ' + KNOWN[L]}")
        assert ok, f"anchor L={L}: got {p}, expected {KNOWN[L]}"
    print("  -> all 12 anchors reproduced exactly")
    print("=" * 78)
    print("B. Requested extra L values")
    for L in EXTRA_LS:
        p, ncells = p3_exact(L)
        out[str(L)] = {"p": f"{p.numerator}/{p.denominator}", "ncells": ncells}
        print(f"  L={L:5d}  p={p}  ({float(p):.12f})  cells={ncells:4d}")
    outpath = os.path.join('out', 'exact_p3_extra.json')
    os.makedirs('out', exist_ok=True)
    with open(outpath, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"  -> wrote {outpath}")
    print("=" * 78)
    # duplicate note: 1400 is already in the known list (444/1139)
    L = 1400
    print(f"Note: L=1400 appears in BOTH lists; result above is "
          f"{out[str(L)]['p']} = KNOWN[1400]={KNOWN[1400]} — "
          f"{'consistent' if out[str(L)]['p'] == KNOWN[1400] else 'INCONSISTENT'}")


if __name__ == '__main__':
    main()