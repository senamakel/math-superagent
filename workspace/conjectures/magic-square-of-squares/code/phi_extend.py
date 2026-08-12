#!/usr/bin/env python3
"""Extended exact additive-chain search in Phi (optimized, M up to 400).

Phi = { 4mn(m^2-n^2)/(m^2+n^2)^2 : m > n >= 1 }  = { sin(4 arctan(n/m)) }.

No additive triple in Phi over Phi(150) pairs was found by phi_exact_search.py
(exact unbounded membership test, verified vs brute force).  This script:
  * builds Phi(M) as reduced integer pairs (num, den) — no Fraction overhead;
  * guesses no pair (m,n) satisfies it NONE of the pairs to avoid a known bar —
    no, simply: for every pair q1>q2 in Phi(M) with q1+q2 < 1, tests q1+q2 in
    Phi EXACTLY (unbounded representation) via the quartic criterion
        r = A/B in Phi  <=>  s^2 = B^2 - A^2 for integer s, s != 0,
                             (B+s)/(2B) and (B-s)/(2B) both rational squares;
  * reports the first additive triple/quadruple, if any, with its (m,n)
    preimages, and lifts it to a grid verified with isqrt;
  * falls back gracefully if a size is too slow (time budget per size).
"""
from math import gcd, isqrt
import sys
import time


def phi_pairs(M):
    """Reduced (num, den) pairs for all f(m,n), m>n>=1, m <= M."""
    out = set()
    for m in range(2, M + 1):
        m2 = m * m
        for n in range(1, m):
            num = 4 * m * n * (m2 - n * n)
            den = (m2 + n * n) ** 2
            g = gcd(num, den)
            out.add((num // g, den // g))
    return out


def in_phi_pair(A, B):
    """Exact: is reduced fraction A/B in Phi?  A,B > 0, gcd(A,B)=1."""
    d = B * B - A * A
    if d < 0:
        return False
    s = isqrt(d)
    if s * s != d:
        return False
    if s == 0:
        return False
    for ss in (s, -s):
        np_, dp_ = B + ss, 2 * B
        nm_, dm_ = B - ss, 2 * B
        if np_ <= 0 or dp_ <= 0 or nm_ <= 0 or dm_ <= 0:
            continue
        g1 = gcd(np_, dp_)
        a1, b1 = np_ // g1, dp_ // g1
        g2 = gcd(nm_, dm_)
        a2, b2 = nm_ // g2, dm_ // g2
        if (isqrt(a1) ** 2 == a1 and isqrt(b1) ** 2 == b1
                and isqrt(a2) ** 2 == a2 and isqrt(b2) ** 2 == b2):
            return True
    return False


def preimage(A, B, M):
    """Find (m,n) with m <= M and f(m,n) = A/B.  Slow scan, for reporting."""
    for m in range(2, M + 1):
        m2 = m * m
        for n in range(1, m):
            num = 4 * m * n * (m2 - n * n)
            den = (m2 + n * n) ** 2
            g = gcd(num, den)
            if num // g == A and den // g == B:
                yield (m, n)


def search(M, budget):
    t0 = time.time()
    pairs = sorted(phi_pairs(M))
    Phi = set(pairs)
    N = len(pairs)
    triples = []
    n_test = 0
    for i in range(N):
        A1, B1 = pairs[i]
        for j in range(i):
            A2, B2 = pairs[j]
            # sum = A1/B1 + A2/B2 with A1/B1 > A2/B2? pairs sorted by value
            # (sorting by tuple is by value since num,den reduced & positive:
            #  smaller tuple = smaller value for positive reduced fractions)
            num = A1 * B2 + A2 * B1
            den = B1 * B2
            if num >= den:            # sum >= 1 -> not in Phi
                continue
            g = gcd(num, den)
            A3, B3 = num // g, den // g
            if (A3, B3) in Phi:       # fast path: representation within M
                # still verify exactly (it is in Phi by construction)
                triples.append(((A1, B1), (A2, B2), (A3, B3)))
                continue
            n_test += 1
            if in_phi_pair(A3, B3):
                triples.append(((A1, B1), (A2, B2), (A3, B3)))
            if time.time() - t0 > budget and len(triples) == 0:
                print(f"[M={M}] budget {budget}s exhausted after "
                      f"{n_test} exact tests; no triple so far; "
                      f"|Phi|={N}")
                return None
    print(f"[M={M}] |Phi|={N}, pairs checked up to sum<1, exact "
          f"membership tests: {n_test}, triples: {len(triples)}, "
          f"{time.time()-t0:.0f}s")
    return triples, pairs


def main():
    sizes = sys.argv[1:] or ["200", "300"]
    for Ms in sizes:
        M = int(Ms)
        budget = float(sys.argv[1 + sizes.index(Ms) + 1]) if False else 600.0
        res = search(M, budget)
        if res is None:
            print(f"  M={M}: incomplete (budget); extending M further "
                  "not attempted\n")
            continue
        triples, pairs = res
        if triples:
            for (A1, B1), (A2, B2), (A3, B3) in triples[:3]:
                mns1 = list(preimage(A1, B1, M))
                mns2 = list(preimage(A2, B2, M))
                mns3 = list(preimage(A3, B3, M))
                print(f"  TRIPLE: {A1}/{B1} + {A2}/{B2} = {A3}/{B3}")
                print(f"    preimages: q1 in {mns1[:3]}, q2 in {mns2[:3]}, "
                      f"q3 in {mns3[:3]}")
                # lift: e = lcm of (m^2+n^2) over one preimage each
                from math import lcm
                e = 1
                for mns in (mns1[:1], mns2[:1], mns3[:1]):
                    mm, nn = mns[0]
                    e = lcm(e, mm * mm + nn * nn)
                c = e * e
                u = c * A1 // B1
                v = c * A2 // B2
                grid = [
                    [c + u, c - u - v, c + v],
                    [c - u + v, c, c + u - v],
                    [c - v, c + u + v, c - u],
                ]
                entries = [x for row in grid for x in row]
                sq = all(x > 0 and isqrt(x) ** 2 == x for x in entries)
                dist = len(set(entries)) == 9
                sums = [sum(r) for r in grid] + \
                       [[grid[0][j] + grid[1][j] + grid[2][j]
                         for j in range(3)]] + \
                       [[grid[0][0] + grid[1][1] + grid[2][2],
                         grid[0][2] + grid[1][1] + grid[2][0]]]
                sums = sums[0] + sums[1] + sums[2]
                magic = all(s == 3 * c for s in sums)
                print(f"    LIFT: e={e} u={u} v={v} grid={grid}")
                print(f"    squares={sq} distinct={dist} magic={magic}")
        else:
            print(f"  M={M}: NO additive triple — the necessary "
                  "rational-level condition fails for all pairs from "
                  f"m,n <= {M} (sum unbounded)\n")


if __name__ == "__main__":
    main()