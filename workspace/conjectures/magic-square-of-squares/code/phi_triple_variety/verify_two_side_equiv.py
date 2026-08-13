#!/usr/bin/env python3
"""Verify the claimed equivalence:
    q in Phi  <=>  0<q<1 AND both 1-q, 1+q are rational squares.
This is the prefilter used by the fast search.  If TRUE (exactly equivalent),
then 0 prefilter survivors over a search range already proves no triple there,
and the authoritative in_phi call is pure confirmation.
Check by exhaustive agreement on all q = f(m,n) with m,n <= N, plus the
negatives (fractions that are NOT in Phi must not pass the two-sided test).
"""
import sys
from math import gcd, isqrt
from lib.phi import phi_pairs, in_phi, rational_square


def two_side(q_nd):
    A, B = q_nd
    if A <= 0 or A >= B:
        return False
    g1 = gcd(B - A, B)
    g2 = gcd(B + A, B)
    return (rational_square((B - A) // g1, B // g1)
            and rational_square((B + A) // g2, B // g2))


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    Phi = phi_pairs(N)
    bad = 0
    # (1) all members must pass two-side
    for q in Phi:
        if not two_side(q):
            bad += 1
            print("  MEMBER FAILS two_side:", q)
    # (2) non-members (reduced fractions A/B with B<=N, 0<A<B, not in Phi) must FAIL two_side
    non_ok = 0
    for B in range(2, N + 1):
        for A in range(1, B):
            if gcd(A, B) != 1:
                continue
            q = (A, B)
            if q in Phi:
                continue
            if two_side(q):
                non_ok += 1
                if non_ok < 8:
                    print("  NON-MEMBER PASSES two_side:", q)
    print(f"Phi({N}) size {len(Phi)}; members failing two_side: {bad}; "
          f"non-members passing two_side: {non_ok}")
    print("=> two_side EXACTLY equivalent to membership"
          if bad == 0 and non_ok == 0
          else "=> two_side is NOT equivalent (see above)")


if __name__ == "__main__":
    main()
