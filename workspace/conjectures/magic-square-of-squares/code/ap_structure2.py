#!/usr/bin/env python3
"""Corrected structural analysis of the AP-of-squares core.

Correction vs ap_structure.py: the 'equivalence' sampler tested grid-entry
*values* against the *difference* set S(e) — wrong.  The true equivalence
(used everywhere below):

  grid entries c+-u, c+-v, c+- (u+v), c+- (u-v), c with c = e^2  (the
  parametrised magic square) are ALL perfect squares
      <=>  u, v, u+v, u-v all lie in S(e) = { d>0 : e^2-d, e^2+d squares }.

So the open conjecture is exactly: exists e with u>v>0, u,v,u+v,u-v in S(e).
Bremner's 7-square near-miss has centre e=425, S(425) = {97104, 138600,
150000, 173400, ...} (|S|=7) but needs differences 41496 and 180096 which
are NOT in S(425) — its middle row and one diagonal are integer APs whose
endpoints are the two non-squares.  So e=425 must be REJECTED by the
four-difference sieve; a sieve that accepted it would be buggy.

This file:
  [0] verification: sieve-built S(e) == x-loop S(e) for e <= 3000, and
      e=425 rejected by the four-difference test, and a sample of
      (e,u,v)-grids checked with isqrt to confirm the equivalence.
  [1] first e with the TRIPLE condition u, v, u+v in S(e) (six square
      entries with square centre: c, c+-u, c+-v, c+(u+v), needing c-(u+v)
      non-square) — the strongest near-miss structure short of the full
      four-difference condition; record all e <= 10^7 with it.
  [2] the four-difference sieve over e <= 10^7 (exact, complete).
  [3] sequences: |S(e)| for e = 1..80; record-holders of |S(e)|; first e
      with |S(e)| = k for k = 1..40.
"""
from math import isqrt
from collections import defaultdict
import time


def S_by_xloop(e):
    out = set()
    c = e * e
    for x in range(1, isqrt(c - 1) + 1):
        y2 = 2 * c - x * x
        y = isqrt(y2)
        if y * y == y2:
            out.add(c - x * x)
    return out


def build_S_sieve(N):
    """S(e) for all e <= N from the complete parametrisation
    e = k(m^2+n^2), d = 4 k^2 m n (m^2-n^2), BUT ONLY when e^2 > d
    (otherwise e^2-d < 0).  Returns dict e -> set(d)."""
    S = defaultdict(set)
    for m in range(2, isqrt(N) + 1):
        m2 = m * m
        for n in range(1, m):
            s0 = m2 + n * n
            if s0 > N:
                break
            for k in range(1, N // s0 + 1):
                e = k * s0
                d = 4 * k * k * m * n * (m2 - n * n)
                if d < e * e:          # keep only e^2 - d > 0
                    S[e].add(d)
    return S


def grid_from(e, u, v):
    c = e * e
    return {c + u, c - u - v, c + v,
            c - u + v, c, c + u - v,
            c - v, c + u + v, c - u}   # as a set; count squares by isqrt


def n_squares_isqrt(entries):
    return sum(1 for x in entries if x > 0 and isqrt(x) ** 2 == x)


def verify(N=3000):
    bad = 0
    S = build_S_sieve(N)
    for e in range(1, min(N, 1500) + 1):
        s1 = S_by_xloop(e)
        s2 = S.get(e, set())
        if s1 != s2:
            bad += 1
            if bad < 5:
                print(f"MISMATCH S({e}): {sorted(s1)} vs {sorted(s2)}")
    # e=425 must be rejected
    s4 = sorted(S.get(425, set()))
    ok425 = False
    sl = s4
    for i in range(len(sl)):
        a = sl[i]
        for b in sl[:i]:
            if (a + b) in S[425] and (a - b) in S[425]:
                ok425 = True
    # equivalence sample
    import random
    rng = random.Random(7)
    for _ in range(60):
        e = rng.randint(5, 2000)
        s = sorted(S.get(e, set()))
        if len(s) < 2:
            continue
        u, v = rng.sample(s, 2)
        entries = grid_from(e, u, v)
        nsq = n_squares_isqrt(entries)
        pred = 5 + 2 * (1 if (u - v) in S[e] else 0) + 2 * (1 if (u + v) in S[e] else 0)
        if nsq != pred:
            bad += 1
            if bad < 8:
                print(f"EQUIV e={e} u={u} v={v}: squares {nsq} pred {pred}")
    print(f"[0] sieve==xloop (e<=1500), e=425 rejected ({ok425} is "
          f"'four-difference' — expect False), equivalence sample: "
          f"{'PASS' if bad == 0 and not ok425 else str(bad) + ' FAILS'}")
    if ok425:
        print("    !! e=425 wrongly accepted — sieve is buggy")
    return bad == 0 and not ok425


def triple_condition_scan(N):
    """First e with u,v,u+v in S(e) (u != v): 6 distinct square entries
    with square centre, one failure c-(u+v) or c+(u-v) etc.
    Records all e <= N with |{d in S: ...}| >= 3 and a triple."""
    t = time.time()
    S = build_S_sieve(N)
    hits = []
    for e in sorted(k for k in S):
        s = S[e]
        if len(s) < 2:
            continue
        sl = sorted(s)
        found = False
        for i in range(len(sl)):
            a = sl[i]
            for b in sl[:i]:
                if (a + b) in s:
                    hits.append((e, a, b))
                    found = True
                    break
            if found:
                break
    print(f"[1] first e with u,v,u+v in S(e): "
          f"{hits[0] if hits else 'NONE'} for e <= {N} "
          f"(6-square with square centre); total such e: {len(hits)}")
    return hits, S


def four_difference_sieve(N):
    t = time.time()
    S = build_S_sieve(N)
    hits = []
    n_small = 0
    for e in sorted(k for k in S):
        s = S[e]
        if len(s) < 4:
            continue
        n_small += 1
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
    print(f"[2] four-difference sieve e <= {N}: {n_small} e's with "
          f"|S(e)|>=4 checked; hits: {hits if hits else 'NONE'}; "
          f"{time.time()-t:.1f}s")
    return hits


def sequences(NSEQLEN=40):
    """|S(e)| closed form (verified against x-loop in [0]): multiplicative
    (prod_{p=1 mod 4, p^a||e}(2a+1) - 1)/2."""
    def nS(e):
        n, prod = e, 1
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
        return (prod - 1) // 2
    seq = [nS(e) for e in range(1, 81)]
    print("[3] |S(e)| e=1..80:", ",".join(str(x) for x in seq))
    # records: e with |S(e)| strictly bigger than all previous
    rec = []
    best = -1
    for e in range(1, 200000):
        v = nS(e)
        if v > best:
            best = v
            rec.append((e, v))
    print("[3] record-holders of |S(e)| for e <= 200000:",
          [(e, v) for e, v in rec])
    # first e with |S(e)| = k
    first = {}
    e = 1
    k_target = 1
    while k_target <= 40:
        v = nS(e)
        if v == k_target and k_target not in first:
            first[k_target] = e
            if k_target in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 25, 30, 40):
                pass
            k_target += 1
        e += 1
        if e > 10 ** 7:
            break
    print("[3] first e with |S(e)| = k (k=1..40):",
          [first.get(k, None) for k in range(1, 41)])


def main():
    verify()
    triple_condition_scan(10 ** 7)
    four_difference_sieve(10 ** 7)
    sequences()


if __name__ == "__main__":
    main()