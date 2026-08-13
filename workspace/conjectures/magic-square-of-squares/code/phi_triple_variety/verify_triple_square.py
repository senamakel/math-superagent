#!/usr/bin/env python3
"""Verify: for REDUCED 0<A<B with gcd(A,B)=1,
    A/B in Phi  <=>  (B-A), B, (B+A) are all perfect squares.
(This collapses the two_side/1±q test because with gcd(A,B)=1 both
 (B-A)/B and (B+A)/B are already reduced, so 'rational square' means each
 numerator and the denominator are perfect squares, and the common
 denominator B must itself be square.)
Check exhaustively: all members of Phi(m<=N) pass; no reduced non-member
A/B (B<=N, 0<A<B) passes.  Also cross-check vs in_phi on every reduced
fraction B<=N.
"""
import sys
from math import gcd, isqrt
from lib.phi import phi_pairs, in_phi


def triple_square(A, B):
    """Exact: reduced 0<A<B, gcd=1, is A/B in Phi via B±A,B squares."""
    if A <= 0 or A >= B:
        return False
    r, c, d = isqrt(B - A), isqrt(B), isqrt(B + A)
    return r * r == B - A and c * c == B and d * d == B + A


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    Phi = phi_pairs(N)
    bad_members = sum(1 for q in Phi if not triple_square(*q))
    # check every reduced fraction A/B, B<=N
    mp_bad = 0   # members failing triple_square
    non_pass = 0 # non-members passing triple_square
    for B in range(2, N + 1):
        for A in range(1, B):
            if gcd(A, B) != 1:
                continue
            got = triple_square(A, B)
            want = in_phi(A, B)
            if got != want:
                non_pass += 1
                if non_pass < 8:
                    print("  mismatch:", (A, B), "triple_square=", got,
                          "in_phi=", want)
    # also check members (they are in Phi by construction): in_phi true, so
    # triple_square must also be true
    for q in Phi:
        if not triple_square(*q):
            mp_bad += 1
            if mp_bad < 8:
                print("  member fails triple_square:", q)
    print(f"N={N}: |Phi|={len(Phi)}; members failing triple_square: {mp_bad}; "
          f"reduced-fraction mismatches vs in_phi (B<={N}): {non_pass}")
    print("=> triple_square EXACTLY equivalent to in_phi"
          if mp_bad == 0 and non_pass == 0
          else "=> NOT equivalent (see mismatches)")


if __name__ == "__main__":
    main()
