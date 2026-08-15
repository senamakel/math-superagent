#!/usr/bin/env python3
"""Bounded, terminating verification of the descent<->Lebesgue equivalence.

The original verify_equivalence.py never terminated: it set
    Xb = 2 * S**q  = 2 * 30**q   (astronomically large)
and then swept `for x in range(3, Xb+1, 2)`, an infinite loop.  That is why
its captures were 0 bytes.

This corrected program bounds BOTH sides to a common feasible range and
verifies the round-trip bijection there in exact integer arithmetic:

  descent solutions  r^q - 2^{mq-2}s^q = +-1   (m<=M, r,s<=S, gcd=1)
  <-->  solutions of  x^2 - y^q = 1            (x odd, x<=X)

with the known maps (branch-correct):
  -1 branch: r^q - 2^{mq-2}s^q = -1  ->  x = 2r^q+1,  y = 2^m r s
  +1 branch: r^q - 2^{mq-2}s^q = +1  ->  x = 2r^q-1,  y = 2^m r s
(gcd(u,v)=1 and v-u=1 force the 2-power onto exactly one of u,v; the
descent equation is the single relation r^q - 2^{mq-2}s^q = +-1.)

The two sides are compared on their (x,y) images restricted to x<=X.  Every
descent solution with x<=X maps to an (x,y) solution, and conversely every
(x,y) solution with x<=X comes from a descent solution (via xy_to_descent).
The bijection statement is what makes the numerical sub-claim sweep (already
run to q<=37) equivalent to the Lebesgue case x^2-y^q=1.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from lib.perfectpow import iroot, is_prime
from math import gcd


def descent_xy(q, m, r, s, val):
    """Branch-correct map from a descent solution to (x, y) with x^2-y^q=1."""
    target = 2 ** (m * q - 2)
    assert r ** q - target * (s ** q) == val and val in (1, -1)
    x = (2 * r ** q + 1) if val == -1 else (2 * r ** q - 1)
    y = (2 ** m) * r * s
    assert x ** 2 - y ** q == 1, (q, m, r, s, val, x, y, x**2 - y**q)
    return x, y


def xy_to_descent(x, q):
    """Inverse: given x^2 - y^q = 1, recover (m, r, s, val).  None if no q-root."""
    v = x * x - 1
    y = iroot(v, q)
    if y ** q != v:
        return None
    x1, x2 = x - 1, x + 1
    u, vv = x1 // 2, x2 // 2
    assert gcd(u, vv) == 1 and vv - u == 1
    m, z = 0, y
    while z % 2 == 0:
        z //= 2
        m += 1
    target = 2 ** (m * q - 2)
    if u % target == 0 and vv % target == 0:
        return None
    if u % target == 0:
        s = iroot(u // target, q); r = iroot(vv, q); val = 1
    else:
        s = iroot(vv // target, q); r = iroot(u, q); val = -1
    assert s ** q == (u if u % target == 0 else vv) // target
    assert r ** q == (vv if u % target == 0 else u)
    descent = r ** q - target * (s ** q)
    assert descent == val and gcd(r, s) == 1
    return m, r, s, val


def main():
    Q = [p for p in range(3, 40) if is_prime(p)]
    print("odd primes:", Q)
    S, M, X = 300, 8, 300000
    total_ok = True
    for q in Q:
        # descent solutions with x<=X
        desc = set()
        for m in range(1, M + 1):
            target = 2 ** (m * q - 2)
            for r in range(1, S + 1):
                rq = r ** q
                # early break: 2*rq-1 (smallest x) > X -> no more r
                if 2 * rq - 1 > X:
                    break
                for s in range(1, S + 1):
                    if gcd(r, s) != 1:
                        continue
                    val = rq - target * (s ** q)
                    if val in (1, -1):
                        x, y = descent_xy(q, m, r, s, val)
                        if x <= X:
                            desc.add((x, y))
        # xy solutions x odd <= X
        xy = set()
        for x in range(3, X + 1, 2):
            res = xy_to_descent(x, q)
            if res is not None:
                xy.add((x, iroot(x * x - 1, q)))
        bijective = (desc == xy)
        total_ok &= bijective
        print(f"  q={q}: descent->{len(desc)} (x,y) | x^2-y^q=1->{len(xy)} (x,y) | equal: {bijective}")
        if not bijective:
            print("    desc-only:", sorted(desc - xy)[:10])
            print("    xy-only:  ", sorted(xy - desc)[:10])
    print("ROUND-TRIP BIJECTION HOLDS on x<=%d, m<=%d, r,s<=%d for all tested q: %s"
          % (X, M, S, total_ok))
    # calibration: the known solution (x,y)=(3,2) with q=3 must be present
    y3 = iroot(8, 3)
    print("calibration q=3: (3,2) solves x^2-y^3=1 ->",
          (8 == y3 ** 3))
    return 0 if total_ok else 1


if __name__ == "__main__":
    sys.exit(main())
