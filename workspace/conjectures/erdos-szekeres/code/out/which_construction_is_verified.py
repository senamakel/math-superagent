#!/usr/bin/env python3
"""Which ES-construction module in code/lib is actually correct?

Steering item 2: only one construction module may be the "verified" one.
Docstrings make claims that have historically been wrong (the resolution doc
shows an old es_construct.es_set_radial failing n=6).  Test EVERY construction
function with the exact oracle, so the quarantine is based on measurement, not
on the file's self-description.

Oracle: lib.es_geom (exact integer/rational determinants, verified earlier).
Property wanted (GOAL criterion 3): 2^{n-2} points, in general position, with
NO convex n-gon, i.e. largest_convex_subset == n-1 (for n=4,5,6).

Runs on the box: this is a 16- or 32-point largest-convex-subset enumeration
per n, exact arithmetic, single process — seconds.
"""
from fractions import Fraction
from lib.es_geom import (in_general_position, largest_convex_subset,
                         has_convex_k_subset)

import lib.es_construct
import lib.es_construction
import lib.es_lower
import lib.esz


def check(name, es_set, n):
    S = es_set(n)
    N = len(S)
    gp = in_general_position(S)
    if n <= 6:
        k, wit = largest_convex_subset(S)
        ok = (N == 2 ** (n - 2) and gp and k == n - 1)
        return (N, gp, k, ok)
    else:
        has7 = has_convex_k_subset(S, 7)[0]
        ok = (N == 2 ** (n - 2) and gp and not has7)
        return (N, gp, 7 if has7 else 0, ok)


modules = [
    ("es_construct.es_set",      lib.es_construct.es_set),
    ("es_construction.es_lower_set", lib.es_construction.es_lower_set),
    ("es_lower.es_lower_set",    lib.es_lower.es_lower_set),
    ("esz.es_set",               lib.esz.es_set),
]

print("module                          n | |S|  gp   maxConvex  ok")
print("-" * 62)
for name, fn in modules:
    row = []
    for n in (4, 5, 6):
        try:
            N, gp, k, ok = check(name, fn, n)
            row.append(f"n={n}: |S|={N} gp={gp} maxC={k} {'OK' if ok else 'FAIL'}")
        except Exception as e:
            row.append(f"n={n}: ERROR {type(e).__name__}: {e}")
    print(f"{name:32s}")
    for r in row:
        print(f"    {r}")
