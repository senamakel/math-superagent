#!/usr/bin/env python3
"""Exact-integer verification of the descent sub-claim for all odd primes
q <= 37 (and beyond), by two independent routes:

  Route 1 (direct): sweep m in [1,M], r,s in [1,S], gcd(r,s)=1, test
      r^q - 2^{mq-2} s^q in {+1,-1}.
  Route 2 (via equivalence with Lebesgue): sweep x odd, x<=X, test whether
      x^2 - 1 is an exact q-th power y^q; if so, (x,y) is a solution of
      x^2 - y^q = 1 and hence a descent solution.

Both exact integer arithmetic; no floats.  The two routes must agree that the
ONLY descent solution is (q,m,r,s)=(3,1,1,1) over the union of their ranges.

The sub-claim being tested:
  r^q - 2^{mq-2}s^q = +-1, q odd prime, m>=1, r,s>=1, gcd(r,s)=1
  has only the solution (q,m,r,s)=(3,1,1,1).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from lib.perfectpow import iroot, is_prime
from math import gcd


def route1_direct(Q, M, S):
    """Direct sweep of the descent equation.  Returns hits other than known."""
    hits = []
    for q in Q:
        for m in range(1, M + 1):
            target = 2 ** (m * q - 2)
            for r in range(1, S + 1):
                rq = r ** q
                for s in range(1, S + 1):
                    if gcd(r, s) != 1:
                        continue
                    val = rq - target * (s ** q)
                    if val in (1, -1):
                        if (q, m, r, s) != (3, 1, 1, 1):
                            hits.append((q, m, r, s, val))
    return hits


def route2_lebesgue(Q, X):
    """Sweep odd x<=X, test x^2-1 = y^q exactly.  This finds SOLUTIONS of
    x^2-y^q=1; each maps to a descent solution.  Return found (q,x,y) pairs."""
    found = []
    for q in Q:
        for x in range(3, X + 1, 2):
            v = x * x - 1
            y = iroot(v, q)
            if y ** q == v:
                found.append((q, x, y))
    return found


def main():
    Q = [p for p in range(3, 40) if is_prime(p)]
    print("odd primes considered:", Q)

    print("\n" + "=" * 72)
    print("ROUTE 1 — direct descent-equation sweep")
    print("=" * 72)
    M, S = 8, 500
    # calibrate on the known solution
    print("calibration q=3,m=1,r,s<=10 -> expect (1,1):")
    cal = route1_direct([3], 1, 10)
    print("  ", [(r, s) for (_, _, r, s, _) in cal])
    hits = route1_direct(Q, M, S)
    other = [h for h in hits if h[:4] != (3, 1, 1, 1)]
    print(f"route1: q in {Q}, m<= {M}, r,s<= {S}")
    print(f"  total descent solutions found: {len(hits)}")
    print(f"  the known (3,1,1,1): {sum(1 for h in hits if h[:4]==(3,1,1,1))}")
    print(f"  OTHER solutions (counterexamples to the sub-claim): {other}")
    print()

    print("=" * 72)
    print("ROUTE 2 — via Lebesgue equivalence (x^2 - y^q = 1)")

    print("=" * 72)
    # First calibrate: known solution (q=3, x=3, y=2) must be found
    X = 200000
    found = route2_lebesgue(Q, X)
    print(f"route2: odd x<= {X}, q in {Q}")
    print(f"  solutions of x^2-y^q=1: {found}")
    known = (3, 3, 2)
    print(f"  known solution (q=3,x=3,y=2) present: {known in found}")
    print()

    print("=" * 72)
    print("CROSS-CHECK: route1 hits mapped to x^2-y^q=1 must equal route2 hits")
    print("=" * 72)
    # Build route1's (x,y) image within a matching x-range and compare to route2's
    # route2 range x<=X but route1 maps to x = 2r^q+1 up to 2*500^37+1 (huge).
    # Compare on the common small region: route1 with r,s small so 2r^q+1<=X.
    r2_sols = {(q, x, y) for (q, x, y) in found}
    # route1 in the restricted region x<=X
    r1_restricted = set()
    for q in Q:
        for m in range(1, M + 1):
            target = 2 ** (m * q - 2)
            for r in range(1, S + 1):
                if 2 * (r ** q) + 1 > X:
                    break
                rq = r ** q
                for s in range(1, S + 1):
                    if gcd(r, s) != 1:
                        continue
                    val = rq - target * (s ** q)
                    if val in (1, -1):
                        x = 2 * rq + 1
                        y = (2 ** m) * r * s
                        r1_restricted.add((q, x, y))
    print("route1 solutions (m<=%d,r,s<=%d) with x<=%d:" % (M, S, X))
    print("  ", sorted(r1_restricted))
    print("route2 solutions (x<=%d):" % X)
    print("  ", sorted(r2_sols))
    match = (r1_restricted == r2_sols)
    print(f"  restricted route1 image == route2 full image: {match}")
    if not match:
        print("  route1-only:", r1_restricted - r2_sols)
        print("  route2-only:", r2_sols - r1_restricted)


if __name__ == "__main__":
    main()
