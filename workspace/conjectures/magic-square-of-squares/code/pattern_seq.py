#!/usr/bin/env python3
"""Recompute the exact integer sequences that matter for pattern analysis.

The open conjecture: exists e with u>v>0 and u, v, u+v, u-v all in
S(e) = { d>0 : e^2-d and e^2+d are perfect squares }, with the closed form
(verified in ap_structure2.py against direct x-loop enumeration for
e <= 1500):

    |S(e)| = ( prod_{p = 1 mod 4, p^a || e} (2a+1) - 1 ) / 2.

Sequences emitted (all exact, via the multiplicative formula / sieve):
  S1  |S(e)| for e = 1..N
  S2  record values of |S(e)| over e <= N (strictly increasing)
  S3  record-holder indices e
  S4  first e with |S(e)| = k for k = 1..K (true minimum, not progressive)
  S5  # { e <= 10^k : |S(e)| >= 4 } for k = 1..8
  S6  histogram of |S(e)| over e <= 10^7
  S7  max |S(e)| over e <= 10^7 and its location
"""
from math import isqrt
from collections import Counter
import sys


def nS_spf(nmax):
    """|S(e)| for e=0..nmax via smallest-prime-factor sieve."""
    prod = [1] * (nmax + 1)
    spf = list(range(nmax + 1))
    for i in range(2, isqrt(nmax) + 1):
        if spf[i] == i:
            for j in range(i * i, nmax + 1, i):
                if spf[j] == j:
                    spf[j] = i
    for e in range(2, nmax + 1):
        p = spf[e]
        n = e
        if p == e:
            if p % 4 == 1:
                prod[e] = 3
            continue
        a = 0
        while n % p == 0:
            n //= p
            a += 1
        if p % 4 == 1:
            prod[e] = (2 * a + 1) * prod[n]
        else:
            prod[e] = prod[n]
    return [(p - 1) // 2 for p in prod]


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 7
    nS = nS_spf(N)

    out = []
    out.append("S1 |S(e)| e=1..120: " + ",".join(str(nS[e]) for e in range(1, 121)))

    rec_val, rec_e = [], []
    best = -1
    for e in range(1, N + 1):
        if nS[e] > best:
            best = nS[e]
            rec_val.append(best)
            rec_e.append(e)
    out.append("S2 record |S| values over e<=1e7: " + ",".join(str(x) for x in rec_val))
    out.append("S3 record-holder e's: " + ",".join(str(x) for x in rec_e))

    first = {}
    for e in range(1, N + 1):
        v = nS[e]
        if 1 <= v <= 40 and v not in first:
            first[v] = e
    out.append("S4 first e with |S(e)|=k, k=1..40: "
               + ",".join(str(first.get(k, "-")) for k in range(1, 41)))

    counts4 = []
    for k in range(1, 9):
        bound = min(10 ** k, N)
        counts4.append(sum(1 for e in range(1, bound + 1) if nS[e] >= 4))
    out.append("S5 # e<=10^k with |S|>=4: " + ",".join(str(x) for x in counts4))

    hist = Counter(nS[1:])
    out.append("S6 histogram over e<=1e7 (k=0..15): "
               + ",".join(str(hist.get(k, 0)) for k in range(0, 16)))
    mx = max((v, e) for e, v in enumerate(nS[1:], 1))
    out.append("S7 max |S| over e<=1e7: " + str(mx[0]) + " at e=" + str(mx[1]))

    # S8: the record gaps: how far apart record holders are; and the
    # "jump" sequence rec_val[i] - rec_val[i-1]
    out.append("S8 record increments: " + ",".join(
        str(rec_val[i] - (rec_val[i - 1] if i else 0))
        for i in range(len(rec_val))))

    # S9: for the record-holder e's: e mod 4, and whether e is prime
    out.append("S9 record e parity/mod4: " + ",".join(
        str(e % 4) for e in rec_e))
    print("\n".join(out))

    # S10: the four-difference candidate count: # e <= 10^k with |S(e)|>=4
    # already in S5; also the e's itself with |S(e)| >= 10 (supercharge)
    big = [(e, nS[e]) for e in range(1, N + 1) if nS[e] >= 12]
    print("S10 first 20 e with |S|>=12:", big[:20], "| total:", len(big))


if __name__ == "__main__":
    main()