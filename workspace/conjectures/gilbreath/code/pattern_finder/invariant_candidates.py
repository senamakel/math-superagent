#!/usr/bin/env python3
"""Candidate invariants of the real prime bit pattern that force the transfer.

The canonical breaker (0^R,1^S) violates when the 0-run precedes a long 1-run
and the diagonal's maximal {0,2} suffix fails to accumulate enough 2s.  Real
prime bits survive with min ratio exactly 0.5 to N=5000.

Test these candidate properties against (a) the real prime bits, (b) random
patterns that ALSO have the property, to see which property is sufficient:

P1: every prefix has w(n) >= (n-2)/2  (majority) — KNOWN insufficient (Q3 of
    earlier run: conditioned random still fail)
P2: every prefix with a 0-run of length >= a has, at its end, w at least
    (n-2)/2 + margin (the majority margin grows after long zero-runs)
P3: bounded *imbalance*: |#0 - #1| over every prefix <= C  (balance)
P4: no long (0-run then 1-run) pairs: for every i<j with a long 0-run ending
    at i and 1-run starting after i, some condition on the local window
P5: autocorrelation / two-point bias: the pattern is "almost alternating"
    with slow drift — measure the correlation between bit[i] and bit[i+k]
P6: the pattern is the mod-2 of a "sawtooth" (prime gaps grow slowly): test
    whether small-window histograms of 0/1 runs look like a memoryless
    process with p~0.6 (Bernoulli) — compute the empirical run-length
    distribution of the real bits and compare to Bernoulli(0.6)

Also, a sharper combinatorial question:  FOR WHICH (R,S) does (0^R,1^S) with
a *tail of alternating bits appended* still violate?  I.e. does appending
balanced bits after the (0^R,1^S) breaker rescue it?  This tests whether the
violation is a *local* prefix effect or global.
"""
import random, math
from lib.gilbreath import primes_up_to
from collections import Counter


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


N = 3000
P = primes_up_to(10 ** 6)
bits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(N + 1)]
prime_bits = bits[1:]          # gaps g_2..g_{N+1}

# ---------- P3: balance ----------
print("P3: prefix imbalance |#1 - #0| of prime bits (first %d):" % N)
bal = 0; maxbal = 0
for i, b in enumerate(prime_bits):
    bal += 1 if b else -1
    maxbal = max(maxbal, abs(bal))
print("  final balance=%d, max |balance|=%d" % (bal, maxbal))
# For comparison: a random walk of length N has max |bal| ~ sqrt(N) ~ 55
print("  (random-walk reference: ~sqrt(%d) = %.0f)" % (N, math.sqrt(N)))

# ---------- P5: autocorrelation ----------
print("\nP5: autocorrelation of prime bits (first %d):" % N)
for k in [1, 2, 3, 4, 5, 8, 16, 32]:
    s = sum(1 for i in range(len(prime_bits) - k)
            if prime_bits[i] == prime_bits[i + k])
    frac = s / (len(prime_bits) - k)
    print("  corr(k=%2d): %.4f  (0.5 = uncorrelated)" % (k, frac))

# ---------- P6: run-length distribution ----------
print("\nP6: prime-bit run-length distribution (first %d):" % N)
runs = []
cur = 1
for i in range(1, len(prime_bits)):
    if prime_bits[i] == prime_bits[i - 1]:
        cur += 1
    else:
        runs.append((prime_bits[i - 1], cur))
        cur = 1
runs.append((prime_bits[-1], cur))
r0 = [r for v, r in runs if v == 0]
r1 = [r for v, r in runs if v == 1]
print("  0-runs: n=%d mean=%.2f max=%d" % (len(r0), sum(r0)/len(r0), max(r0)))
print("  1-runs: n=%d mean=%.2f max=%d" % (len(r1), sum(r1)/len(r1), max(r1)))
# Bernoulli(p) run length distribution: P(L=l) = p^{l-1}(1-p); mean = 1/(1-p)
p1 = sum(prime_bits) / len(prime_bits)
print("  density of 1s: %.4f ; Bernoulli run mean would be 0-run %.2f, 1-run %.2f"
      % (p1, 1/p1, 1/(1-p1)))

# ---------- P2: majority margin after long 0-runs ----------
print("\nP2: majority margin (2w-(n-2)) at the end of each 0-run (prime bits):")
# for 0-runs of length >= 4, what is the margin at the run's end?
pref_w = [0] * (len(prime_bits) + 1)
for i, b in enumerate(prime_bits):
    pref_w[i + 1] = pref_w[i] + b
margin_at_zerorun_end = []
i = 0
while i < len(prime_bits):
    if prime_bits[i] == 0:
        j = i
        while j < len(prime_bits) and prime_bits[j] == 0:
            j += 1
        L = j - i
        if L >= 4:
            n = j + 1           # gap index -> n = j+2-1 = j+1?? careful
            # w(n) = pref_w[n-1] (hbits[2..n-1] = prime_bits[1..n-2]...)
            # prime_bits[k] = bit of gap g_{k+2}; w(n) sums bits for gaps
            # g_3..g_n = prime_bits[1..n-2]?? Let's just compute directly.
            wsum = sum(prime_bits[1:n - 1])
            margin = 2 * wsum - (n - 2)
            margin_at_zerorun_end.append((j + 1, L, margin))
        i = j
    else:
        i += 1
print("  (position n, 0-run length, margin 2w-(n-2)) for 0-runs >= 4:")
for rec in margin_at_zerorun_end[:12]:
    print("   ", rec)

# ---------- Appending balanced tail to the canonical breaker ----------
print("\nQ4b: does appending alternating bits after (0^R,1^S) rescue the transfer?")
for (R, S) in [(8, 8), (8, 10), (10, 10), (12, 12), (16, 16)]:
    for tail in ["alt01", "alt10", "zeros", "ones"]:
        pat = [0] * R + [1] * S
        L = len(pat)
        if tail == "alt01":
            pat += [i % 2 for i in range(200)]
        elif tail == "alt10":
            pat += [1 - i % 2 for i in range(200)]
        elif tail == "zeros":
            pat += [0] * 200
        else:
            pat += [1] * 200
        seq = gaps_to_seq([1] + [2 * (2 - b) for b in pat])
        mr, fh, vh = transfer_stats(seq, len(pat) + 2)
        print("  (R=%2d,S=%2d)+%s: min nu2/w=%.4f viol=%d first=%s"
              % (R, S, tail, mr, vh, fh))
