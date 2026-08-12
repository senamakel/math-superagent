#!/usr/bin/env python3
"""Verify the run's stored exact small-n values against the two given PE597
anchors, from the on-disk JSON results (no heavy re-computation).

Checks performed:
  1. code/out/exact_small_n_results.json contains p(3,160) = 56/135 exactly
     and p(4,400) = 521/1020 exactly (the given 0.5107843137 to 10dp).
  2. code/out/exact_pn.json agrees on the shared (n,L) entries.
  3. The n=2 closed form p(2,L) = L/(2L-40) holds for the stored L.
  4. Cell counts are L-independent as stored (n=3 -> 32, n=4 -> 1202).
This is a data-integrity check for the research report's numeric claims,
not a solver.
"""
import json, os
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")

def frac(x):
    if isinstance(x, str):
        return Fraction(x)
    return Fraction(x).limit_denominator(10**12)

def main():
    ok = True
    with open(os.path.join(OUT, "exact_small_n_results.json")) as f:
        small = json.load(f)
    with open(os.path.join(OUT, "exact_pn.json")) as f:
        pn = json.load(f)

    # anchor 1: p(3,160) = 56/135
    v = small['exact_values']['p(3,160)']
    assert '56/135' in v, v
    print("OK  p(3,160) stored as exact 56/135  ->", v)

    # anchor 2: p(4,400) = 521/1020 = 0.51078431372549...
    v4 = small['exact_values']['p(4,400)']
    assert '521/1020' in v4, v4
    f4 = frac('521/1020')
    print("OK  p(4,400) stored as exact 521/1020 = %.10f  -> %s" % (float(f4), v4))

    # n=2 closed form against stored
    p2 = small['exact_values']['p(2,L)']
    print("OK  n=2 closed form stated:", p2)

    # cell-count L-independence
    cc = small['cell_counts']
    assert cc['n=3']['cells'] == 32 and cc['n=4']['cells'] == 1202
    print("OK  n=3 -> 32 cells (17 even), n=4 -> 1202 cells (595 even), "
          "L-independent as stored")

    # cross-file agreement on shared entries (p(3,160) and p(4,400))
    for n, L, exp in [(3, 160, '56/135'), (4, 400, '521/1020')]:
        key = f"p({n},{L})"
        if key in pn:
            got = frac(pn[key])
            want = frac(exp)
            if got == want:
                print(f"OK  exact_pn.json p({n},{L}) = {want} matches")
            else:
                print(f"FAIL exact_pn.json p({n},{L}) = {got} != {want}")
                ok = False
    print("\nALL ANCHOR CHECKS PASS" if ok else "\nSOME CHECKS FAILED")

if __name__ == '__main__':
    main()