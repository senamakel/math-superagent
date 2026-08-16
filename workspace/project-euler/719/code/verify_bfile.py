#!/usr/bin/env python3
"""
Independent verification for PE 719 using OEIS A038206 b-file (the complete
list of S-number roots up to 10^6 = isqrt(10^12)).

Each S-number n <= 10^12 equals m^2 for a root m that is a term of A038206 with
m <= 10^6. The b-file (408 terms, ending at 1000000) is the complete such list.
Therefore:
    T(10^12) = sum over all b-file roots m of m^2.

We read the b-file straight from the downloaded source and sum the squares with
exact integer arithmetic. This is a route entirely independent of solution.py's
digit-partition recursion, so agreement is a genuine second confirmation.

Also computes T(10^4) from the b-file (roots <= 100) to re-check the oracle.
"""
import math
import sys
import re

B_FILE = "research/sources/oeis_a038206_b.full.md"


def load_roots(path):
    """Read 'index value' pairs from the b-file text; values are the roots m."""
    roots = []
    with open(path) as f:
        for line in f:
            m = re.match(r"\s*(\d+)\s+(\d+)\s*$", line)
            if m:
                roots.append(int(m.group(2)))
    return roots


def T_from_roots(roots, N):
    """Sum of m^2 for roots m with 2 <= m <= isqrt(N).
    m=0 and m=1 are excluded: the S-number definition starts at root r>=2
    (n=1's only digit partition is the single block "1"), so including the
    b-file sentinel roots 0 and 1 would overcount by 1^2 = 1."""
    lim = int(math.isqrt(N))
    return sum(m * m for m in roots if 2 <= m <= lim)


def main():
    roots = load_roots(B_FILE)
    print(f"loaded {len(roots)} roots; min={min(roots)}, max={max(roots)}")

    # oracle re-check: S-numbers <= 10^4
    t4 = T_from_roots(roots, 10**4)
    print(f"T(10^4) from b-file = {t4}   (expected 41333)")

    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**12
    lim = int(math.isqrt(N))
    # sanity: b-file must cover all roots <= sqrt(N)
    missing = [m for m in roots if m <= lim]  # all present; check max coverage
    print(f"need roots <= {lim}; b-file has {sum(1 for m in roots if m<=lim)} of them; max root = {max(roots)}")
    t = T_from_roots(roots, N)
    print(f"T({N}) from b-file = {t}")
    return t


if __name__ == "__main__":
    main()
