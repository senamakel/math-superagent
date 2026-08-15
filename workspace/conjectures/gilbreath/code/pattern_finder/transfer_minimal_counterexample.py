#!/usr/bin/env python3
"""Characterize the transfer bound nu2(n) >= w(n)/2 exactly.

Q1: EXACT minimal counterexample search over {2,4}-gap patterns.
    Find the smallest pattern length L and smallest n where a {2,4} pattern
    violates nu2 >= w/2 (nu2 = #2s in maximal {0,2} suffix of diagonal body
    D[2:-1]; w = # of 1-bits among gaps g_3..g_n).  Also track the min ratio
    over ALL patterns of each length, to see whether violations are rare at
    small n and how the worst ratio decays with length.

Q2: Prime-pattern robustness.  Take the REAL prime bit pattern (first N bits
    from the primes), flip a fraction f at random positions, minimal {2,4}
    gaps, and measure min nu2/w over n in [17,N].  How many flips does it
    take to break the transfer?

Q3: Conditioning test.  Random {2,4} patterns with P(bit=1)=p conditioned on
    switch-majority e(n)=2w(n)-(n-2) >= 0 for all n; does the transfer hold
    for p in {0.5, 0.6}?  (All-odds = p=1 passes the conditioning and fails,
    so we expect "no" — this nails whether majority is the right ingredient.)
"""
import random
from itertools import product
from lib.gilbreath import primes_up_to


def transfer_stats(seq, N, lo=17):
    """Returns (min nu2/w over n in [lo,N-1] with w>0, first violation n of
    nu2>=w/2, violation count)."""
    D = [seq[0]]
    hbits = [((seq[i + 1] - seq[i]) // 2) % 2 for i in range(len(seq) - 1)]
    pref = [0] * (len(hbits) + 1)
    for i, b in enumerate(hbits):
        pref[i + 1] = pref[i] + b
    min_ratio = 1.0
    viol = 0; first = None
    for n in range(1, N):
        newD = [0] * (n + 1)
        newD[0] = seq[n]
        for k in range(1, n + 1):
            newD[k] = abs(newD[k - 1] - D[k - 1])
        D = newD
        if n >= lo:
            body = D[2:-1]
            i = len(body)
            while i > 0 and body[i - 1] in (0, 2):
                i -= 1
            cyc = body[i:]
            nu2v = cyc.count(2)
            wv = pref[n] - pref[2]
            if wv > 0:
                r = nu2v / float(wv)
                if r < min_ratio:
                    min_ratio = r
                if nu2v < 0.5 * wv - 1e-12:
                    viol += 1
                    if first is None:
                        first = n
    return min_ratio, first, viol


def gaps_to_seq(gaps):
    s = [2]
    for g in gaps:
        s.append(s[-1] + g)
    return s


# ---------- Q1: exhaustive, length by length ----------
print("Q1: exhaustive {2,4}-gap patterns, find first nu2 < w/2 violation")
found = None
for L in range(4, 20):          # L bits -> seq length L+2 (gaps g_2..g_{L+1})
    worst = (1.0, None)
    viols = 0
    for pat in product([0, 1], repeat=L):
        gaps = [1] + [2 * (2 - b) for b in pat]
        seq = gaps_to_seq(gaps)
        mr, fh, vh = transfer_stats(seq, L + 2)
        if mr < worst[0]:
            worst = (mr, pat)
        if vh > 0:
            viols += 1
            if found is None:
                found = (L, pat, fh, mr)
    print("  L=%2d : patterns=%8d violators=%6d worst_min_ratio=%.4f%s"
          % (L, 2 ** L, viols, worst[0],
             "  FIRST: pat=%s at n=%d ratio=%.4f" % (found[1], found[2], found[3])
             if found is not None and L == found[0] else ""))
    if found is not None and viols > 0:
        break
print("  minimal violation found: pattern length %d, bits %s, first at n=%d, ratio %.4f"
      % (found if found else "NONE within L<20"))

# ---------- Q2: robustness of the prime pattern ----------
print("\nQ2: flip fraction of real prime bits (minimal gaps), min nu2/w over n in [17,N=1500]")
N = 1500
P = primes_up_to(10 ** 6)
bits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(N + 1)]
for f in [0.0, 0.01, 0.03, 0.05, 0.1, 0.2, 0.3]:
    worst_over_trials = 1.0
    for t in range(12):
        rng = random.Random(1000 + t)
        pat = bits[1:N].copy()
        nflip = int(f * len(pat))
        for idx in rng.sample(range(len(pat)), nflip):
            pat[idx] ^= 1
        gaps = [1] + [2 * (2 - b) for b in pat]
        seq = gaps_to_seq(gaps)
        mr, fh, vh = transfer_stats(seq, N)
        worst_over_trials = min(worst_over_trials, mr)
    print("  flip=%.2f : worst min nu2/w over 12 trials = %.4f" % (f, worst_over_trials))

# ---------- Q3: conditioning on majority ----------
print("\nQ3: random patterns conditioned on switch-majority e(n)>=0 everywhere (N=400):")
for p in [0.5, 0.6]:
    worst = 1.0
    accepted = 0
    rng = random.Random(777 + int(100 * p))
    while accepted < 20:
        pat = [1 if rng.random() < p else 0 for _ in range(400 - 1)]
        # e(n) = 2w(n)-(n-2) >= 0 for all n in [2, 400]
        w = 0; ok = True
        for i, b in enumerate(pat):
            n = i + 2
            w += b
            if 2 * w - (n - 2) < 0:
                ok = False
                break
        if not ok:
            continue
        gaps = [1] + [2 * (2 - b) for b in pat]
        seq = gaps_to_seq(gaps)
        mr, fh, vh = transfer_stats(seq, 400)
        worst = min(worst, mr)
        accepted += 1
    print("  p=%.1f : 20 accepted majority-patterns, worst min nu2/w = %.4f" % (p, worst))
