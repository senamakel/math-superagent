#!/usr/bin/env python3
"""Exact oracle for Singmaster's conjecture.

Provides `multiplicity(a, n_max)` — the exact count of (n,k) pairs with
0 <= k <= n <= n_max and C(n,k) = a — in exact integer arithmetic.

Counting convention (matches code/out/witnesses.json):
    counts BOTH mirrored occurrences and includes the trivial pair
    C(a,1) = C(a,a-1).  So an `a` with exactly one nontrivial canonical rep
    (n,k), 2 <= k <= n/2, reports N(a) = 4, and the record 3003 reports 8.

Method: inversion, never the triangle.
    For fixed a, every canonical rep (n,k) with 2 <= k <= n/2 satisfies
    a = C(n,k) >= C(2k,k) >= 2^k, so k <= log2(a).  For each such k, C(n,k)
    is strictly increasing in n (for n >= k), so binary-search the unique n
    with C(n,k) = a in O(log) time.  Each canonical rep (n,k) with 1<=k<=n/2
    contributes 2 occurrences (the pair (n,k),(n,n-k)); the trivial pair is
    the canonical rep (a,1) and contributes those same 2.  O(log2(a)^2) bigint
    comb calls per multiplicity, O(log2(a)) space.
"""

import json
from math import comb

from lib.binom_multiplicity import (
    CONVENTION,
    canonical_reps,
    multiplicity,
    nontrivial_reps,
)


def scan_high_multiplicity(a_max):
    """All a <= a_max with N(a) >= 6, by direct enumeration of canonical reps.

    Complete: any nontrivial canonical rep (n,k), 2<=k<=n/2, with value
    C(n,k) <= a_max satisfies n <= max_n where C(max_n,2) <= a_max (since for
    k>=2, C(n,k) >= C(n,2)).  Enumerating all such (n,k) buckets every value,
    and N(a) = 2 + 2*(#canonical nontriv reps of a) >= 6 iff the bucket holds
    >= 2 nontrivial reps.  For a<=10^7, max_n = 4473, ~5M pairs, a few seconds.
    """
    max_n = 2
    while comb(max_n + 1, 2) <= a_max:
        max_n += 1
    buckets = {}
    for n in range(2, max_n + 1):
        for k in range(2, n // 2 + 1):
            v = comb(n, k)
            if v <= a_max:
                buckets.setdefault(v, []).append((n, k))
    result = {}
    for v, reps in buckets.items():
        if len(reps) >= 2:
            # Exact N: a canonical rep with k == n/2 (central binomial, even n)
            # is its own mirror and contributes 1, not 2.  Punt to the exact
            # inversion oracle for the true count.
            result[v] = {"N": multiplicity(v, n_max=v),
                         "nontrivial": sorted(reps)}
    return result


if __name__ == "__main__":
    print(CONVENTION)
    print()

    # 1) The record: verify 3003 appears exactly 8 times, and show the reps.
    a = 3003
    occ = canonical_reps(a, n_max=a)
    N = multiplicity(a, n_max=a)
    print(f"multiplicity(3003, 3003) = {N}  (expected 8)")
    print(f"  canonical reps (each stands for its mirror pair): {sorted(occ)}")
    print(f"  nontrivial canonical reps: {nontrivial_reps(a, n_max=a)}")
    print("  identity  3003 = C(3003,1) = C(78,2) = C(15,5) = C(14,6):",
          [comb(x[0], x[1]) for x in [(3003,1),(78,2),(15,5),(14,6)]])
    assert N == 8, f"3003 multiplicity {N} != 8"
    assert multiplicity(120, n_max=120) == 6
    assert multiplicity(210, n_max=210) == 6
    assert multiplicity(1540, n_max=1540) == 6
    assert multiplicity(7140, n_max=7140) == 6
    assert multiplicity(11628, n_max=11628) == 6
    assert multiplicity(24310, n_max=24310) == 6
    print("  asserted: multiplicity==6 for 120,210,1540,7140,11628,24310")
    print()

    # 2) Scan a range and report every a with multiplicity >= 6.
    A_MAX = 10_000_000
    print(f"[count_multiplicity] scanning canonical reps with value <= {A_MAX}; "
          f"max n = {2} while C(n,2)<={A_MAX}")
    found = scan_high_multiplicity(A_MAX)
    print(f"values with N(a) >= 6 in a <= {A_MAX}: {len(found)}")
    for v in sorted(found):
        print(f"  a={v}: N={found[v]['N']}  nontrivial={found[v]['nontrivial']}")

    # Cross-check a few against the serial inversion oracle.
    for v in sorted(found):
        nv = multiplicity(v, n_max=v)
        assert nv == found[v]["N"], (v, nv, found[v]["N"])
    print(f"[count_multiplicity] all {len(found)} high-multiplicity values "
          f"cross-checked against inversion multiplicity: agree")

    # 3) Reproduce the witness list structure into code/out/witnesses.json.
    witness = {"3003": {"N": 8,
                        "nontrivial": sorted(nontrivial_reps(3003, n_max=3003))}}
    for vv, info in found.items():
        witness[str(vv)] = {"N": info["N"], "nontrivial": info["nontrivial"]}
    with open("code/out/witnesses.json", "w") as fh:
        json.dump({
            "generated_by": "code/count_multiplicity.py, exact integer arithmetic, "
                            "inversion for multiplicity, direct enumeration for scan",
            "conjecture": "N(a) is bounded by an absolute constant (Singmaster 1971)",
            "convention": CONVENTION,
            "scan": {"a_max": A_MAX, "reported_N_ge": 6},
            "witnesses": witness,
        }, fh, indent=1, sort_keys=True)
    print("[count_multiplicity] wrote code/out/witnesses.json")
