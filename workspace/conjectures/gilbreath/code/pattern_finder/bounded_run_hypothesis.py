#!/usr/bin/env python3
"""Bounded-run hypothesis for the transfer bound nu2(n) >= w(n)/2.

Minimal breaker found: pattern (0^9, 1^7) at length 16 — a long zero-run
followed by a long one-run.  Test:

Q1: Do the REAL prime bits have bounded runs?  Maximal run lengths of 0-bits
    and 1-bits among the first N gap-bits.

Q2: Does a bounded-run condition rescue the transfer for RANDOM patterns?
    Random {2,4} patterns with max 0-run <= R0 and max 1-run <= R1 (minimal
    gaps), measure min nu2/w over n in [17, N].  Try (R0,R1) in
    {(2,2),(3,3),(4,4),(5,5),(8,8)}.

Q3: How does the worst ratio decay as a function of the maximal run length
    for the canonical pattern (0^R, 1^R) and (0^R, 1^S)?

Q4: Check the actual prime pattern's runs against the transfer: restrict to
    the first n where max-run <= R; does nu2 >= w/2 hold up to that n?
"""
import random
from lib.gilbreath import primes_up_to


def transfer_stats(seq, N, lo=17):
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


def max_runs(bits):
    m0 = m1 = 0; cur = 1
    for i in range(1, len(bits)):
        if bits[i] == bits[i - 1]:
            cur += 1
        else:
            if bits[i - 1] == 0:
                m0 = max(m0, cur)
            else:
                m1 = max(m1, cur)
            cur = 1
    if bits[-1] == 0:
        m0 = max(m0, cur)
    else:
        m1 = max(m1, cur)
    return m0, m1


# ---------- Q1: real prime run lengths ----------
N = 3000
P = primes_up_to(10 ** 6)
bits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(N + 1)]
m0, m1 = max_runs(bits)
print("Q1: real prime gap-bits (first %d): max 0-run=%d, max 1-run=%d"
      % (N, m0, m1))
# runs over a much longer stretch
Pbig = primes_up_to(2 * 10 ** 7)
N2 = 100000
bits2 = [((Pbig[i + 1] - Pbig[i]) // 2) % 2 for i in range(N2)]
m0b, m1b = max_runs(bits2)
print("    first %d: max 0-run=%d, max 1-run=%d" % (N2, m0b, m1b))

# ---------- Q4: prime pattern prefix up to first occurrence of long runs ----------
print("\nQ4: prime pattern prefixes truncated when a run exceeds R:")
for R in [1, 2, 3, 4, 5, 6, 8]:
    # find the first n where some run in bits[1:n] exceeds R
    n_cut = N
    cur = 1
    for i in range(1, len(bits)):
        if bits[i] == bits[i - 1]:
            cur += 1
        else:
            cur = 1
        if cur > R:
            n_cut = i + 1  # bits index i (gap g_{i+2}); n = i+2
            break
    # truncate to n_cut-1 (exclude the offending bit)
    nn = min(n_cut - 1, N)
    if nn >= 17:
        gaps = [1] + [2 * (2 - b) for b in bits[1:nn]]
        seq = gaps_to_seq(gaps)
        mr, fh, vh = transfer_stats(seq, nn)
        print("  R=%d : cut at n=%d, min nu2/w=%.4f, viol=%d first=%s"
              % (R, nn, mr, vh, fh))
    else:
        print("  R=%d : cut at n=%d (too short)" % (R, nn))

# ---------- Q2: bounded-run random patterns ----------
print("\nQ2: random patterns with bounded runs, N=500, min nu2/w over 40 trials:")
for (R0, R1) in [(2, 2), (3, 3), (4, 4), (5, 5), (8, 8), (16, 16)]:
    worst = 1.0; nviol = 0
    for t in range(40):
        rng = random.Random(5000 + t * 31 + R0 * 7)
        # generate a random sequence with max runs: random walk with
        # regeneration — simplest: reject-sampling is too slow, instead
        # build runs of random length 1..R with alternating values
        pat = []
        v = rng.randrange(2)
        while len(pat) < N - 1:
            rlen = rng.randrange(1, R0 + 1 if v == 0 else R1 + 1)
            pat.extend([v] * rlen)
            v ^= 1
        pat = pat[:N - 1]
        gaps = [1] + [2 * (2 - b) for b in pat]
        seq = gaps_to_seq(gaps)
        mr, fh, vh = transfer_stats(seq, 500)
        worst = min(worst, mr)
        nviol += (1 if vh > 0 else 0)
    print("  (R0,R1)=(%2d,%2d): worst min nu2/w=%.4f over 40 trials, %d trials violated"
          % (R0, R1, worst, nviol))

# ---------- Q3: canonical (0^R, 1^S) decay ----------
print("\nQ3: canonical patterns (0^R, 1^R), n=2R+2:")
for R in [4, 5, 6, 7, 8, 9, 10, 12, 16, 24, 32]:
    pat = [0] * R + [1] * R
    gaps = [1] + [2 * (2 - b) for b in pat]
    seq = gaps_to_seq(gaps)
    mr, fh, vh = transfer_stats(seq, len(pat) + 2)
    print("  R=%2d : min nu2/w=%.4f viol=%d first=%s" % (R, mr, vh, fh))
