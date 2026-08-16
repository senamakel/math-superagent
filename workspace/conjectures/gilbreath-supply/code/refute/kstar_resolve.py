#!/usr/bin/env python3
"""Resolve the K*(n) definitional dispute in the run's own data.

Three conflicting tables exist on disk:
  - witness-hunt-imported.txt            : K* = 1,1,2,2,3,4,4,5,5,6,6,...
  - witness-crosscheck (min K const)     : n=7->3, n=9->4  (floor at odd n)
  - orderk_correlation brute (single)    : n=8->5 (above ceil)

Their difference is single-C_K (S^2 const on every individual C_K fiber) vs
cumulative and the two conventions "min K with no pair" vs "largest K with a
pair". I recompute everything cleanly from the oracle, under the definition
stated in the run's own claim G-kstar-budget:

    K*(n) := min{ K >= 1 : S^2 is constant on every C_K-fiber of F_2^n }
           = min{ K : no pair h,h' with C_K(h)=C_K(h') but S^2(h)!=S^2(h') }.

Both cumulative (C_1..C_K same) and single-C_K coincide since C_K determines
C_{K-1} by marginalisation, but I report BOTH the 'first no-pair' value and the
'largest K with a pair' value to pin what each prior table meant.

Also verify by hand the find_counterexample witness at n=8, K=4:
    h  = 01110111   S^2 = 16
    h' = 10111011   S^2 = 4
same 5-gram histogram (C_4), different S^2.
"""

import sys, itertools
sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos


def c_k_single(h, K):
    """(K+1)-gram histogram as a canonical sorted tuple."""
    n = len(h)
    counts = {}
    for start in range(n - K):
        w = 0
        for t in range(K + 1):
            w = (w << 1) | h[start + t]
        counts[w] = counts.get(w, 0) + 1
    return tuple(sorted(counts.items()))


def s_squared(n, h):
    S, _ = s_sos(n, h)
    return S * S


def kstar_values(n):
    """Return (first_no_pair, largestK_with_pair, {K: has_separating_pair})."""
    strings = list(itertools.product([0, 1], repeat=n))
    s2 = {s: s_squared(n, s) for s in strings}
    sep = {}
    first_nopair = None
    for K in range(1, n):
        fibers = {}
        for s in strings:
            key = c_k_single(s, K)
            fibers.setdefault(key, []).append(s)
        has = any(len({s2[s] for s in grp}) > 1 for grp in fibers.values())
        sep[K] = has
        if not has and first_nopair is None:
            first_nopair = K
    largest_pair = max((k for k, v in sep.items() if v), default=None)
    return first_nopair, largest_pair, sep


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    out = []
    out.append("K* resolution: min K with no C_K-separating pair (claim def)")
    out.append("vs largest K with a C_K-separating pair vs ceil(n/2).")
    out.append("oracle: lib.supply_fold.s_sos (canonical floored); n=3..%d" % nmax)
    out.append("")
    out.append("%4s %18s %20s %8s   %s" % ("n", "min-no-pair", "largest-pair",
                                           "ceil", "has-separating-pair-at-K"))
    out.append("-"*78)
    for n in range(3, nmax + 1):
        first, largest, sep = kstar_values(n)
        ce = (n + 1) // 2
        seplist = ",".join(str(k) for k in range(1, n) if sep.get(k)) or "-"
        out.append("%4d %18s %20s %8d   %s" % (n, first, largest, ce, seplist))
    out.append("")
    out.append("If min-no-pair == ceil(n/2) for all n>=6, the closed-form claim")
    out.append("G-kstar-budget / R-budget-n32 HOLDS under that definition.")
    print("\n".join(out))


if __name__ == "__main__":
    main()
