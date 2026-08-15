#!/usr/bin/env python3
"""Settle the three weakest elementary rungs of the Catalan ladder with exact
integer arithmetic, each independently cross-checked by a naive brute-force
search.

Rungs (research/weakened/catalan-ladder.md), weakest first:

  R-trivial-bases : no solution of x^p - y^q = 1 with x,y>0, p,q>1 and x=1 or y=1.
  R-p-eq-q        : for every odd prime p, x^p - y^p = 1 has no solution in
                    integers x,y > 0.
  R-fixed-23      : x^2 - y^3 = 1 has (x,y) = (3,2) as its only solution in
                    integers x,y > 0.  (Lebesgue 1850.)

R-trivial-bases and R-p-eq-q are one-line proofs, re-derived here and checked
against the exact oracle.  R-fixed-23 is now PROVED in this workspace by the
descent + complete PARI thue() resolution (see code/refute/thue_descent_full.py,
thue_nf.gp; note code/out/thue_descend_fixed23.note.md, claim
exp2-fixed23-proved-thue).  The brute force below remains as a numeric
cross-check of that proof to x = 10^7, not as the proof itself.
"""
import sys


def is_perfect_power(n, e):
    """True iff n = k^e for some integer k >= 1.  Exact integer arithmetic via
    integer binary search on the e-th root (no floats)."""
    if n < 0:
        return False
    if e == 1:
        return True
    lo, hi = 1, n
    while lo <= hi:
        mid = (lo + hi) // 2
        m = mid ** e
        if m == n:
            return True
        elif m < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


def brute_fixed_23(X):
    """All (x,y) with 1<=x<=X, x>y>=1, x^2 - y^3 = 1. For each x, binary search
    the integer cube root of x^2-1 and verify exactly."""
    hits = []
    for x in range(1, X + 1):
        v = x * x - 1
        # integer cube root of v by binary search
        lo, hi = 0, 1
        while hi ** 3 <= v:
            hi *= 2
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid ** 3 == v:
                hits.append((x, mid))
                break
            elif mid ** 3 < v:
                lo = mid + 1
            else:
                hi = mid - 1
    return sorted(set(hits))


def main():
    from lib.valuation import solutions  # established exact oracle

    print("=" * 72)
    print("R-trivial-bases : x=1 or y=1 impossible in x^p - y^q = 1, x,y>0, p,q>1")
    print("=" * 72)
    print("  x = 1  ->  1 - y^q = 1  =>  y^q = 0  =>  y = 0, excluded by y>0.")
    print("  y = 1  ->  x^p - 1 = 1  =>  x^p = 2  =>  impossible: 2 is not a")
    print("           perfect power (no integer x>=1, p>=2; p=1 excluded by p>1).")
    N = 10 ** 8
    sols = solutions(N)
    ok_triv = all(s[0] > 1 and s[2] > 1 for s in sols)
    print(f"  oracle cross-check: solutions({N}) = {sols}")
    print(f"  all solutions have bases >= 2: {ok_triv}")
    print()

    print("=" * 72)
    print("R-p-eq-q : x^p - y^p = 1 has no solution in x,y>0, odd prime p")
    print("=" * 72)
    print("  x^p - y^p = (x-y)(x^(p-1)+...+y^(p-1)).  RHS=1 and x>y, so both")
    print("  positive-integer factors equal 1; but the second factor >= p >= 3.")
    p_hits = []
    for p in (3, 5, 7, 11, 13, 17, 19):
        for x in range(1, 3000):
            for y in range(1, x):
                if x ** p - y ** p == 1:
                    p_hits.append((x, y, p))
                    break
    print(f"  cross-check: odd primes <=19, x<3000, hits = {p_hits}")
    print()

    print("=" * 72)
    print("R-fixed-23 : x^2 - y^3 = 1 only solution (x,y)=(3,2)")
    print("=" * 72)
    print("  NOTE: proved in this workspace by descent + complete PARI thue()")
    print("  (claim exp2-fixed23-proved-thue).  The brute force below is a")
    print("  numeric cross-check of that proof to x=10^7.")
    X = 10 ** 7
    hits = brute_fixed_23(X)
    # y > 0 is a hypothesis of the equation; (1,0) is forced OUT (y=0 <= 0)
    real_hits = [h for h in hits if h[1] > 0 and h[0] * h[0] - h[1] ** 3 == 1]
    ok = (real_hits == [(3, 2)])
    print(f"  exact brute force over 1<=x<={X}, checking x^2-y^3=1 with y>0:")
    print(f"  all raw hits (including y<=0) = {hits}")
    print(f"  verified solution hits with y>0 = {real_hits}")
    print(f"  matches expected [(3,2)]? {ok}")
    print()

    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print("  R-trivial-bases : SETTLED (one-line proof; oracle has no base-1)")
    print("  R-p-eq-q        : SETTLED (one-line proof; 0 hits over primes<=19,x<3000)")
    print(f"  R-fixed-23      : PROVED (descent + PARI thue, claim")
    print("                    exp2-fixed23-proved-thue); numeric cross-check")
    print("                    to x=10^7 -> only (3,2)")
    ok_all = ok_triv and (not p_hits) and ok
    sys.exit(0 if ok_all else 1)


if __name__ == "__main__":
    main()
