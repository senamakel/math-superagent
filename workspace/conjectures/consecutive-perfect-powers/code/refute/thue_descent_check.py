#!/usr/bin/env python3
"""Attack the sub-claim in gap exp2-a-odd-descent:

  "r^q - 2^{mq-2} s^q = +-1, with q an odd prime, m >= 1, r,s >= 1, gcd(r,s)=1,
   has only the solution q=3, m=1, r=s=1."

Concretely, for each odd prime q and m >= 1, enumerate r,s and look for
signatures r^q - 2^{mq-2} s^q = +-1.  If any pair other than (q=3,m=1,r=s=1)
solves it, the descent lemma as stated is FALSE (a located gap in the sketch).

NOTE this is *not* the Catalan statement itself (that is true: x^2-y^q=1 has
only (3,2,3)).  The question is whether the intermediate Thue-type claim, as
the skeleton states it, is exactly right.

Exact integer arithmetic only.
"""
import sys
from math import gcd

def is_odd_prime(n):
    if n < 3 or n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def brute(q, m, R):
    """Return list of (r,s,sign) with 1<=r,s<=R, gcd(r,s)=1,
    r^q - 2^{mq-2} s^q == sign, sign in {+1,-1}."""
    coeff = 2 ** (m * q - 2)
    hits = []
    for r in range(1, R + 1):
        rq = r ** q
        for s in range(1, R + 1):
            if gcd(r, s) != 1:
                continue
            val = rq - coeff * (s ** q)
            if val == 1:
                hits.append((r, s, +1))
            elif val == -1:
                hits.append((r, s, -1))
    return hits

def main():
    # First: validate the known solution gives a hit.
    print("Known-solution calibration: q=3,m=1 -> r^3 - 2 s^3 = +-1, expect (1,1,-1)")
    print("  ", brute(3, 1, 5))

    # Sweep q, m.
    print("\nSweep over odd primes q<=13, m in 1..6, r,s<=200:")
    total_found = 0
    for q in [p for p in range(3, 14, 2) if is_odd_prime(p)]:
        for m in range(1, 7):
            R = 200
            h = brute(q, m, R)
            if h:
                for (r, s, sg) in h:
                    if (q, m, r, s) == (3, 1, 1, 1):
                        continue  # the known solution, not a counterexample
                    total_found += 1
                    print(f"  q={q} m={m}: r^q - 2^{{{m*q-2}}} s^q = {sg:+d} at (r,s)=({r},{s})  <-- CHECK")
                if all((q,m,r,s)==(3,1,1,1) for (r,s,_) in h):
                    print(f"  q={q} m={m}: only the known (r,s)=(1,1) within r,s<={R}")
            else:
                print(f"  q={q} m={m}: no solutions with r,s<={R}")
    print(f"\nCandidates other than the known (q=3,m=1,r=s=1): {total_found}")

if __name__ == "__main__":
    main()
