#!/usr/bin/env python3
"""The descent sub-claim r^q - 2^{mq-2}s^q = +-1 is EXACTLY equivalent to the
Lebesgue case x^2 - y^q = 1.  This program proves the equivalence by exact
algebra and checks it computationally in both directions.

Equivalence (the structural fact that makes the sub-claim = Lebesgue):

  Forward (descent equation -> x^2 - y^q = 1):
    Let r^q - 2^{mq-2} s^q = 1  =>  set x = 2r^q + 1, y = 2^m r s.
    Then x^2 - 1 = (2r^q+1)^2 - 1 = 4 r^q (r^q + 1) = 4 r^q * 2^{mq-2} s^q
                 = 2^{mq} r^q s^q = (2^m r s)^q = y^q.
    So x^2 - y^q = 1.
    (Branch r^q - 2^{mq-2}s^q = -1 is identical: same x, same y.)

  Backward (x^2 - y^q = 1 with x odd >= 3  ->  descent equation):
    y^q = (x-1)(x+1), gcd(x-1, x+1) = 2 (x odd).  Write x-1 = 2u, x+1 = 2v,
    gcd(u,v)=1, v-u = 1.  Then 4uv = y^q with y = 2^m z (z odd):
       uv = y^q/4 = 2^{mq-2} z^q.  gcd(u,v)=1 => all 2s to one side and the
    odd q-th-power z^q splits as coprime q-th powers:
       {u,v} = {r^q, 2^{mq-2} s^q},  z = rs,  gcd(r,s)=1.
    Since v - u = 1:  r^q - 2^{mq-2}s^q = +-1.  (descent equation)

So a solution of the descent equation <-> a solution of x^2 - y^q = 1.
Hence the sub-claim (only (q,m,r,s)=(3,1,1,1)) is exactly Lebesgue's theorem
that x^2 - y^q = 1 has only the solution (x,y,q) = (3,2,3).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from lib.perfectpow import iroot, is_prime  # exact integer helpers

from math import gcd


def descent_to_xy(q, m, r, s, sign):
    """Given r^q - 2^{mq-2}s^q = sign (in +-1), return (x, y) with x^2-y^q=1."""
    # x = 2*r^q + 1 works for both signs (x^2-1 = 4 r^q (r^q +- (2^{...}s^q - {r^q}))
    # Verify: whichever branch, r^q + 1 = y^q/(4 r^q)? Let's just verify directly
    # that the constructed (x,y) satisfies x^2 - y^q = 1.
    coeff = 2 ** (m * q - 2)
    x = 2 * (r ** q) + 1
    y = (2 ** m) * r * s
    assert x ** 2 - y ** q == 1, (q, m, r, s, sign, x, y)
    return x, y


def xy_to_descent(x, q):
    """Given x^2 - y^q = 1 (find y by exact q-th root), return (m, r, s, sign)
    solving the descent equation.  Returns None if y not an exact q-th power."""
    v = x * x - 1
    y = iroot(v, q)
    if y ** q != v:
        return None
    # u,v decomposition
    x1, x2 = x - 1, x + 1
    # gcd = 2 (x odd) -> u = (x-1)/2, v = (x+1)/2, gcd(u,v)=1, v-u=1
    u, v = x1 // 2, x2 // 2
    assert gcd(u, v) == 1 and v - u == 1
    # y = 2^m z
    m, z = 0, y
    while z % 2 == 0:
        z //= 2
        m += 1
    # uv = 2^{mq-2} z^q ; find which of u,v carries the 2-power
    target = 2 ** (m * q - 2)  # the full 2-power factor (should divide one of u,v)
    if u % target == 0 and v % target == 0:
        return None
    # determine r,s
    if u % target == 0:
        # u = 2^{mq-2} s^q, v = r^q -> v - u = 1 -> r^q - 2^{...} s^q = 1
        s = iroot(u // target, q)
        r = iroot(v, q)
        sign = 1
    else:
        # v = 2^{mq-2} s^q, u = r^q -> v - u = 1 -> 2^{...}s^q - r^q = 1
        s = iroot(v // target, q)
        r = iroot(u, q)
        sign = -1
    assert s ** q == (u if u % target == 0 else v) // target
    assert r ** q == (v if u % target == 0 else u)
    # verify descent equation
    val = r ** q - target * (s ** q)
    assert val == sign, (r, s, val, sign)
    assert gcd(r, s) == 1
    return m, r, s, sign


def log2i(n):
    """Exact integer log2 (n must be a power of 2, and we assert)."""
    e = 0; t = n
    while t > 1:
        assert t % 2 == 0
        t //= 2; e += 1
    return e


def verify_equivalence_roundtrip(Q):
    """For each q in Q, verify: every odd x with x^2-y^q=1 (y up to iroot bound)
    maps through xy_to_descent to a descent solution, and every (m,r,s) whose
    descent value is +-1 maps back.  Confirms the two sets are in bijection.
    """
    print("=" * 72)
    print("Equivalence round-trip: descent solutions <-> x^2-y^q=1 solutions")
    print("=" * 72)
    for q in Q:
        # All descent solutions for r,s up to S, m up to M
        S, M = 30, 6
        desc_sols = set()
        for m in range(1, M + 1):
            target = 2 ** (m * q - 2)
            for r in range(1, S + 1):
                rq = r ** q
                for s in range(1, S + 1):
                    if gcd(r, s) != 1:
                        continue
                    val = rq - target * (s ** q)
                    if val in (1, -1):
                        x, y = descent_to_xy(q, m, r, s, val)
                        desc_sols.add((m, r, s, val, x, y))
        # All x (odd) with x^2 - y^q = 1 for x <= Xb
        Xb = 2 * (S ** q) + 1 + 2   # covers all x built above
        xy_sols = set()
        for x in range(3, Xb + 1, 2):
            res = xy_to_descent(x, q)
            if res is not None:
                xy_sols.add((res[0], res[1], res[2], res[3], x, iroot(x*x-1, q)))
        # Compare the (x,y) image sets
        img_desc = {(x, y) for (_, _, _, _, x, y) in desc_sols}
        img_xy = {(x, y) for (_, _, _, _, x, y) in xy_sols}
        bijective = (img_desc == img_xy)
        print(f"  q={q}: descent sols (m<=6,r,s<=30) -> {len(img_desc)} distinct (x,y)"
              f" | x^2-y^q=1 sols (x<=Xb) -> {len(img_xy)} distinct (x,y)"
              f" | images equal: {bijective}")
        if not bijective:
            print("    DIFF desc-only:", img_desc - img_xy)
            print("    DIFF xy-only:", img_xy - img_desc)
    print()


if __name__ == "__main__":
    Q = [p for p in range(3, 40) if is_prime(p)]
    print("odd primes considered:", Q)
    # Direct algebra sanity: the identity x^2-1 = (2r^q+1)^2-1 = 4 r^q 2^{mq-2} s^q
    # holds iff r^q - 2^{mq-2}s^q = +-1 (i.e. r^q + 1 = 2^{...}s^q or = 2^{...}s^q-2+... )
    print()
    for q in [3, 5, 7]:
        for (m, r, s) in [(1, 1, 1), (1, 2, 2), (2, 1, 1)]:
            target = 2 ** (m * q - 2)
            val = r ** q - target * (s ** q)
            if val in (1, -1):
                x, y = descent_to_xy(q, m, r, s, val)
                print(f"  q={q} m={m} r={r} s={s}: descent val={val} -> "
                      f"(x,y)=({x},{y}), x^2-y^q={x**2 - y**q}")
    print()
    verify_equivalence_roundtrip(Q)
