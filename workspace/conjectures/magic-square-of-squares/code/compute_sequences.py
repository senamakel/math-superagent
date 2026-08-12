#!/usr/bin/env python3
"""Sequences from the AP-of-squares core of the 3x3 magic square of squares.

S(e) = { d > 0 : e^2 - d and e^2 + d are both perfect squares }
     = set of common differences of 3-term APs of squares with middle e^2.
Verified identities:
  * S(e) = { 4 k^2 m n (m^2 - n^2) : k(m^2+n^2) = e, m > n >= 1 }  (checked
    against direct x^2+y^2=2e^2 enumeration for e <= 1500).
  * |S(e)| = (prod_{p = 1 mod 4, p^a || e} (2a+1) - 1) / 2  =  number of
    Pythagorean triples with hypotenuse e  (checked e <= 200).
The open conjecture is exactly: exists e with u > v > 0 and
u, v, u+v, u-v in S(e).  Verified: NO such e with e <= 10^7, and in fact
no e <= 10^7 has even the triple condition u, v, u+v in S(e).

This file recomputes, correctly, the sequences:
  S1  |S(e)| for e = 1..120
  S2  record values of |S(e)| (for e up to 10^7)
  S3  record-holder e's
  S4  minimal e with |S(e)| = k, k = 1..25  (true minimum, not progressive)
  S5  cumulative count of e <= 10^k with |S(e)| >= 4 (the four-difference
      candidates), k = 1..7
  S6  histogram of |S(e)| over e <= 10^7
and verifies the sieve against direct enumeration on random large e.
"""
from math import isqrt
from collections import defaultdict
import random
import time


def nS_spf(nmax):
    """|S(e)| for e <= nmax via smallest-prime-factor sieve.
    prod(e) = prod over p = 1 mod 4 dividing e of (2*a_p + 1);
    |S(e)| = (prod(e) - 1) // 2."""
    prod = [1] * (nmax + 1)
    spf = list(range(nmax + 1))
    for i in range(2, isqrt(nmax) + 1):
        if spf[i] == i:                      # i prime
            for j in range(i * i, nmax + 1, i):
                if spf[j] == j:
                    spf[j] = i
    for e in range(2, nmax + 1):
        p = spf[e]
        n = e
        if p == e:                           # e prime
            if p % 4 == 1:
                prod[e] = 3
            continue
        a = 0
        while n % p == 0:
            n //= p
            a += 1
        rest = prod[n]
        if p % 4 == 1:
            prod[e] = (2 * a + 1) * rest
        else:
            prod[e] = rest
    return [(p - 1) // 2 for p in prod]


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
                S[e].add(d)                  # d < e^2 always (see notes)
    return S


def random_large_checks(N=10 ** 7, k=25):
    """Spot-check the sieve's S(e) against direct x-loop enumeration for
    random e in [10^5, N].  This is what makes the four-difference negative
    claim trustworthy beyond the e <= 1500 exhaustive check."""
    rng = random.Random(99)
    S = build_S_sieve(N)
    bad = 0
    picked = []
    for _ in range(k):
        e = rng.randint(10 ** 5, N)
        s1 = S_by_xloop(e)
        s2 = S.get(e, set())
        if s1 != s2:
            bad += 1
            picked.append((e, sorted(s1)[:6], sorted(s2)[:6]))
    print(f"[verify] sieve vs x-loop on {k} random e in [1e5, {N}]: "
          f"{'PASS' if bad == 0 else str(bad) + ' FAILS'}")
    for e, a, b in picked:
        print(f"   e={e}: xloop {a}, sieve {b}")
    return bad == 0


def main():
    t0 = time.time()
    N = 10 ** 7
    nS = nS_spf(N)                            # nS[e], e = 0..N

    # S1: |S(e)| e=1..120
    print("S1 |S(e)| e=1..120:",
          ",".join(str(nS[e]) for e in range(1, 121)))

    # S2/S3: records and record holders
    rec_val, rec_e = [], []
    best = -1
    for e in range(1, N + 1):
        if nS[e] > best:
            best = nS[e]
            rec_val.append(best)
            rec_e.append(e)
    print("S2 record |S| values:", ",".join(str(x) for x in rec_val))
    print("S3 record e's:", ",".join(str(x) for x in rec_e))

    # S4: minimal e with |S(e)| = k (true minimum, k = 1..25)
    first = {}
    for e in range(1, N + 1):
        v = nS[e]
        if 1 <= v <= 25 and v not in first:
            first[v] = e
    print("S4 minimal e with |S(e)|=k, k=1..25:",
          ",".join(str(first.get(k, "-")) for k in range(1, 26)))

    # S5: number of e <= 10^k with |S(e)| >= 4
    counts4 = []
    for k in range(1, 8):
        bound = 10 ** k
        c = sum(1 for e in range(1, bound + 1) if nS[e] >= 4)
        counts4.append(c)
    print("S5 # e<=10^k with |S|>=4:", ",".join(str(x) for x in counts4))

    # S6: histogram of |S(e)|, e <= 10^7, for the small values
    from collections import Counter
    hist = Counter(nS[1:])
    print("S6 histogram |S|=k over e<=1e7 (k=0..12):",
          ",".join(str(hist.get(k, 0)) for k in range(0, 13)))
    print("    max |S| over e<=1e7:", max(nS[1:]), "at e =",
          max((v, e) for e, v in enumerate(nS[1:], 1))[1])

    # S7: cumulative sum of |S(e)| at powers of 10 (growth of total APs)
    cum = 0
    cums = []
    j = 1
    for e in range(1, N + 1):
        cum += nS[e]
        if e == 10 ** j or e == N:
            cums.append((e, cum))
            j += 1
    print("S7 cumulative sum_{e<=n} |S(e)| at n=10^k:",
          ", ".join(f"n={e}:{cum}" for e, cum in cums))

    # verify
    random_large_checks(N)

    # full four-difference and triple scans (exact, complete for e <= N)
    S = build_S_sieve(N)
    t1 = time.time()
    n_cand = 0
    triple_hits = []
    four_hits = []
    for e in sorted(k for k in S):
        s = S[e]
        if len(s) < 3:
            continue
        sl = sorted(s)
        for i in range(len(sl)):
            a = sl[i]
            for b in sl[:i]:
                if len(s) >= 4 and (a + b) in s and (a - b) in s:
                    four_hits.append((e, a, b))
                if (a + b) in s:
                    triple_hits.append((e, a, b))
            if four_hits and triple_hits:
                break
        if four_hits:
            break
    print(f"[scan] e <= {N}: triple hits u,v,u+v in S: "
          f"{triple_hits[:5] if triple_hits else 'NONE'}; "
          f"four-difference hits: {four_hits[:5] if four_hits else 'NONE'}; "
          f"{time.time() - t1:.0f}s")
    print(f"[scan] total time {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()