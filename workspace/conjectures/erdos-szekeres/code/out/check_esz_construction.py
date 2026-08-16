#!/usr/bin/env python3
"""Check ES lower-bound constructions with the EXACT es_geom oracle.

Property to verify: a set of 2^{n-2} points in general position with NO
convex n-gon (largest convex subset == n-1).
Also dump cup/cap spectra and block sizes where relevant.
"""
from lib.es_geom import (
    in_general_position, has_convex_k_subset, largest_convex_subset,
    longest_cap, longest_cup,
)
from lib.es_construction import es_lower_set, cups_caps_block, largest_block_capcup

def check(name, S, n):
    N = len(S)
    gp = in_general_position(S)
    if N <= 24:
        k, wit = largest_convex_subset(S)
        status = "PASS" if k == n - 1 else "FAIL"
        has = has_convex_k_subset(S, n)
        print(f"[{name}] n={n}: |S|={N} general={gp} largestConvex={k} "
              f"(want {n-1}) hasConvex{n}-gon={has[0]}  -> {status}")
    else:
        has = has_convex_k_subset(S, n)
        print(f"[{name}] n={n}: |S|={N} general={gp} "
              f"hasConvex{n}-gon={has[0]} (want False) -> "
              f"{'PASS' if not has[0] else 'FAIL'}")

if __name__ == "__main__":
    for n in (4, 5, 6, 7):
        S = es_lower_set(n)
        check("es_lower_set", S, n)
    print()
    print("block cap/cup verification (should be <= bounds):")
    for n in (5, 6, 7):
        print(f" n={n}: {largest_block_capcup(n)}")
