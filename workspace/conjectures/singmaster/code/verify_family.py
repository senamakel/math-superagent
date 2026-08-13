#!/usr/bin/env python3
"""Find equal binomial coefficients to expose the 6-fold family structure.

For n <= N and 2 <= k <= n/2 we bucket C(n,k) by value (exact integers).  Two
entries sharing a value are a distinct nontrivial occurrence pair — the kind
that, together with the trivial pair C(a,1)=C(a,a-1), makes N(a) >= 6 when two
such distinct pairs share a value.  We print every such equal pair (collision),
then the values that carry >= 2 nontrivial canonical reps (the N >= 6 family).

Each canonical rep (n,k), 2<=k<=n/2, stands for its mirror pair, so the printed
"canonical occurrences" are the distinct nontrivial entries, exactly as used in
code/out/witnesses.json.

Memory: buckets hold <= N*(N-1)/4 entries and every value that survives; a
value shared by two reps needs both, so storage is O(N^2) distinct values.  For
N = 1000 that is ~2.5e5 comb values, fine.
"""

import json
import sys
from math import comb

N_MAX = 1000
# Cap on stored value: a collision need only be considered where both binomials
# fall in the stored range; we cut off to keep bigints modest (matches how the
# known family's members are modest-sized with one rep at k=2 or k=3).
VALUE_CAP = 10**18


def equal_pairs(n_max, value_cap):
    """Return (collisions, high_multiplicities).

    collisions: list of (value, [(n,k) occurrences], [(n,k) mirrors])
        for every value with >=2 distinct canonical occurrences
    high: dict value -> {"N": int, "nontrivial": [[n,k],...]} for values whose
        canonical occurrence set has length >= 2 (--> N >= 6 with trivial pair).
    """
    buckets = {}
    for n in range(2, n_max + 1):
        for k in range(2, n // 2 + 1):
            v = comb(n, k)
            if v <= value_cap:
                buckets.setdefault(v, []).append((n, k))

    collisions = []
    high = {}
    for v, reps in sorted(buckets.items()):
        if len(reps) >= 2:
            collisions.append((v, sorted(reps)))
    for v, reps in sorted(buckets.items()):
        if len(reps) >= 2:
            # exact N: each canonical rep contributes 2 (mirror pair) unless
            # it is the central k=n/2 (own mirror, contributes 1); plus trivial
            # pair = 2.  None of our small reps is central, so N = 2 + 2*len.
            N = 2 + 2 * len(reps)
            high[v] = {"N": N, "nontrivial": [list(r) for r in sorted(reps)]}
    return collisions, high


if __name__ == "__main__":
    print(f"[verify_family] n in 2..{N_MAX}, 2<=k<=n/2, "
          f"value_cap={VALUE_CAP}, single process")
    collisions, high = equal_pairs(N_MAX, VALUE_CAP)

    print(f"\nDistinct values with >=2 canonical occurrences "
          f"(collisions): {len(collisions)}\n")
    for v, reps in collisions:
        print(f"  {v:>22}  {reps}")

    print(f"\nValues with N(a) >= 6 (>=2 nontrivial canonical reps, "
          f"4 <= N): {len(high)}\n")
    # Only show the ones that reach N >= 6 (i.e. len(reps) >= 2).
    for v in sorted(high):
        info = high[v]
        if info["N"] >= 6:
            print(f"  a={v}: N={info['N']}  nontrivial={info['nontrivial']}")

    with open("code/out/family_pairs.json", "w") as fh:
        json.dump({
            "n_max": N_MAX,
            "value_cap": VALUE_CAP,
            "convention": ("canonical reps (n,k), 2<=k<=n/2, each stands for "
                           "mirror pair; N counts both mirrors plus trivial "
                           "pair C(a,1)=C(a,a-1)"),
            "collisions": [[v, [list(r) for r in reps]] for v, reps in collisions],
            "high_multiplicity": {str(v): info for v, info in high.items()},
        }, fh, indent=1, sort_keys=True)
    print("\n[verify_family] wrote code/out/family_pairs.json")
