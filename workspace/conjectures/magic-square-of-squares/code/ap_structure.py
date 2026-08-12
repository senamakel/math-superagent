#!/usr/bin/env python3
"""Structural analysis of the AP-of-squares structure at the core of the
3x3 magic square of squares problem.

Definitions (from problem.md):
  A solution is a triple (e, u, v) with the grid all distinct positive
  squares.  The four lines through the centre e^2 are APs of squares with
  differences u, v, u+v, u-v.  Define
      S(e) = { d > 0 : e^2 - d and e^2 + d are both perfect squares }.
  Then EVERY element of S(e) gives a three-term AP of squares with middle
  e^2, and a solution exists iff there are u > v > 0 with
      u, v, u+v, u-v  all in S(e)
  (then all nine grid entries e^2 +/- u, e^2 +/- v, e^2 +/- (u+v),
  e^2 +/- (u-v) are positive squares and the grid is magic by the
  parametrisation).  Equivalence is checked mechanically below.

Closed form derived and verified here against enumeration:
  |S(e)| = ( prod_{p == 1 (mod 4), p^a || e} (2a+1) - 1 ) / 2.
  via the identity: every AP x^2, e^2, y^2 of squares satisfies
  x^2 + y^2 = 2e^2, and ((x+y)/2, (x-y)/2) -> Pythagorean triple, giving
  the complete parametrisation
      e = k(m^2+n^2),  d = 4 k^2 m n (m^2 - n^2)   (m > n >= 1, k >= 1).

The four-difference search (the conjecture in this form) is carried out by
the (m,n,k) inversion sieve: for every e <= N we build S(e) exactly from
all (m,n,k) with k(m^2+n^2) = e, then test u,v,u+v,u-v in S(e).
Cost ~ 1.5 N operations for the sieve plus the sparse |S(e)| >= 4 checks.
"""
from math import isqrt
from collections import defaultdict
import time


def S_by_xloop(e):
    """Enumerate S(e) by directly checking x^2 + y^2 = 2e^2.  O(e)."""
    out = set()
    c = e * e
    for x in range(1, isqrt(c - 1) + 1):
        y2 = 2 * c - x * x
        y = isqrt(y2)
        if y * y == y2:
            out.add(c - x * x)
    return out


def S_by_divisor_formula(e):
    """Enumerate S(e) from the divisor structure of e (independent route).
    For each divisor s of e with s = m^2 + n^2, m > n >= 1, and k = e/s,
    d = 4 k^2 m n (m^2 - n^2)."""
    out = set()
    for s in range(5, e + 1):
        if e % s:
            continue
        k = e // s
        # is s a sum of two squares with m > n >= 1?
        for m in range(2, isqrt(s) + 1):
            n2 = s - m * m
            if n2 >= 1 and n2 < m * m:
                n = isqrt(n2)
                if n * n == n2:
                    out.add(4 * k * k * m * n * (m * m - n * n))
    return out


def magic_grid_is_all_squares(e, u, v):
    """grid_from_params equivalent: entries are e^2 +/- (differences)."""
    c = e * e
    return {
        c + u, c - u - v, c + v,
        c - u + v, c, c + u - v,
        c - v, c + u + v, c - u,
    }


def check_equivalence_and_formula(N=200):
    """Verify (a) the parametrisation: S(e) enumerated by divisors equals
    the x-loop set; (b) the closed form for |S(e)|; (c) the grid-is-all-
    squares <-> four-difference equivalence on samples."""
    mism = 0
    for e in range(1, N + 1):
        s1 = S_by_xloop(e)
        s2 = S_by_divisor_formula(e)
        if s1 != s2:
            mism += 1
            print(f"MISMATCH S({e}): {s1} vs {s2}")
        # closed form
        n = e
        prod = 1
        p = 2
        while p * p <= n:
            if n % p == 0:
                a = 0
                while n % p == 0:
                    n //= p
                    a += 1
                if p % 4 == 1:
                    prod *= 2 * a + 1
            p += 1
        if n > 1 and n % 4 == 1:
            prod *= 3
        if prod % 2 == 0:
            print(f"odd-prod fail e={e}")
            mism += 1
            continue
        expect = (prod - 1) // 2
        if len(s1) != expect:
            mism += 1
            print(f"FORMULA FAIL e={e}: |S|={len(s1)} expect {expect}")
    # (c) equivalence on samples: for u,v in S(e), count of squares in the
    # grid must equal 5 + 2*[u-v in S] + 2*[u+v in S].
    import random
    rng = random.Random(12345)
    hits = 0
    for _ in range(2000):
        e = rng.randint(5, 400)
        s = S_by_xloop(e)
        if len(s) < 2:
            continue
        u, v = rng.sample(sorted(s), 2)
        grid = magic_grid_is_all_squares(e, u, v)
        n_sq = sum(1 for x in grid if x in s or x == e * e)
        pred = 5 + 2 * (1 if (u - v) in s else 0) + 2 * (1 if (u + v) in s else 0)
        if n_sq != pred:
            mism += 1
            print(f"EQUIV FAIL e={e} u={u} v={v}: squares {n_sq} pred {pred}")
        if (u - v) in s and (u + v) in s:
            hits += 1
    print(f"[check] S(e) x-loop == divisor-parametrisation for e<=200: "
          f"{'PASS' if mism == 0 else str(mism) + ' FAILS'}; "
          f"random samples with u,v,u-v,u+v in S: {hits}")
    return mism == 0


def four_difference_sieve(N):
    """Build S(e) for all e <= N by the (m,n,k) inversion, then find the
    first e with u,v,u+v,u-v in S(e)."""
    t = time.time()
    S = defaultdict(set)
    for m in range(2, isqrt(N) + 1):
        m2 = m * m
        for n in range(1, m):
            s0 = m2 + n * n
            if s0 > N:
                break
            base = 4 * m * n * (m * m - n * n)
            # k from 1 while k*s0 <= N: e = k*s0, d = k^2 * base
            kmax = N // s0
            for k in range(1, kmax + 1):
                S[k * s0].add(k * k * base)
    hits = []
    n_cand = 0
    for e in sorted(k for k in S):
        s = S[e]
        if len(s) < 4:
            continue
        n_cand += 1
        sl = sorted(s)
        found = False
        for i in range(len(sl)):
            a = sl[i]
            for b in sl[:i]:
                if (a + b) in s and (a - b) in s:
                    hits.append((e, a, b))
                    found = True
                    break
            if found:
                break
    print(f"[sieve] S(e) built for e <= {N} in {time.time() - t:.1f}s; "
          f"{n_cand} e's with |S(e)| >= 4 checked; four-difference hits: "
          f"{hits if hits else 'NONE'}")
    return hits


def main():
    check_equivalence_and_formula(200)

    # sequence |S(e)|, e = 1..64, via the closed form (independent of the
    # sieve), for the sequence tools.
    seq = []
    for e in range(1, 65):
        n = e
        prod = 1
        p = 2
        while p * p <= n:
            if n % p == 0:
                a = 0
                while n % p == 0:
                    n //= p
                    a += 1
                if p % 4 == 1:
                    prod *= 2 * a + 1
            p += 1
        if n > 1 and n % 4 == 1:
            prod *= 3
        seq.append((prod - 1) // 2)
    print("|S(e)| e=1..64:", ",".join(str(x) for x in seq))

    # first e with each |S| value 1..7
    for target in range(1, 8):
        got = None
        e = 1
        while True:
            n = e
            prod = 1
            p = 2
            while p * p <= n:
                if n % p == 0:
                    a = 0
                    while n % p == 0:
                        n //= p
                        a += 1
                    if p % 4 == 1:
                        prod *= 2 * a + 1
                p += 1
            if n > 1 and n % 4 == 1:
                prod *= 3
            if (prod - 1) // 2 == target:
                got = e
                break
            e += 1
        print(f"first e with |S(e)| = {target}: {got}")

    four_difference_sieve(10**6)
    four_difference_sieve(10**7)


if __name__ == "__main__":
    main()