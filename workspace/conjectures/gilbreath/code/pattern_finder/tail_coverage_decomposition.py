#!/usr/bin/env python3
"""Structural decomposition of the transfer bound.

Hypothesis: for the primes, the maximal {0,2} suffix of the diagonal body
D[2:-1] is the WHOLE body (tail length L = n-3, i.e. K=2), so
nu2(n) = weight of the FULL Pascal convolution of the h-bits.

If weight(Pascal(h)) >= w/2 holds for ALL h (universally), then the transfer
nu2 >= w/2 for the primes reduces to the single claim "the prime diagonal
body is {0,2}-valued", which is a mod-4 statement about the triangle.

Tests:
Q1: for the primes, is K(n)=2 (tail = whole body) for all n <= 10000?
Q2: universality of weight(Pascal(h)) >= w/2 over ALL binary h of length m
    (exhaustive for m <= 20, random for larger).
Q3: for random patterns that FAIL the transfer, is the failure because the
    tail is short (K large)?  Compare min nu2/w with the FULL convolution
    weight ratio.
Q4: Pascal convolution weight vs input weight: exact identity?  For the
    Pascal matrix mod 2, weight(out) >= weight(in)/2 ?
"""
import random, time
from lib.gilbreath import primes_up_to


def pascal_weight_ratio(h):
    """out[t] = XOR_j binom(t,j) mod 2 * h[j]; returns weight(out)/weight(h)
    (exact rational as float)."""
    m = len(h)
    out = [0] * m
    for t in range(m):
        v = 0
        # binom(t,j) mod 2 = 1 iff j & ~t == 0  (Lucas)
        for j in range(t + 1):
            if (j & ~t) == 0:
                v ^= h[j]
        out[t] = v
    wo = sum(out)
    wi = sum(h)
    return (wo, wi, wo / float(wi) if wi else 1.0)


def diagonal_tail(seq, n):
    """Returns (K, nu2, w) for q_n: K = start index of maximal {0,2} suffix
    of body D[2:-1] (2-based), nu2 = #2s in it, w = switch weight."""
    D = [seq[0]]
    for i in range(1, n + 1):
        newD = [0] * (i + 1)
        newD[0] = seq[i]
        for k in range(1, i + 1):
            newD[k] = abs(newD[k - 1] - D[k - 1])
        D = newD
    body = D[2:-1]          # indices 2..n-2
    i = len(body)
    while i > 0 and body[i - 1] in (0, 2):
        i -= 1
    K = i + 2               # start index in D of the suffix
    cyc = body[i:]
    nu2 = cyc.count(2)
    return K, nu2, len(cyc)


# ---------- Q1: primes, is K=2 always? ----------
print("Q1: prime diagonal tail coverage K(n) for n <= 3000 (minimal gaps):")
N = 3000
P = primes_up_to(10 ** 6)
bits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(N + 1)]
seq = [2]
for b in bits[1:N]:
    seq.append(seq[-1] + 2 * (2 - b))
badK = []
Kvals = set()
for n in range(3, N):
    K, nu2, L = diagonal_tail(seq, n)
    Kvals.add(K)
    if K != 2:
        badK.append((n, K))
print("  K values seen: %s" % sorted(Kvals))
print("  n with K != 2 (first 10): %s (total %d)" % (badK[:10], len(badK)))

# ---------- Q2: universality of full Pascal weight ----------
print("\nQ2: weight(Pascal(h)) >= w/2 universally?  Exhaustive m<=18:")
worst = (1.0, None)
for m in range(2, 19):
    local_worst = 1.0; local_worst_h = None
    for h in range(2 ** m):
        bits_h = [(h >> j) & 1 for j in range(m)]
        wo, wi, r = pascal_weight_ratio(bits_h)
        if wi > 0 and r < local_worst:
            local_worst = r; local_worst_h = bits_h
    if local_worst < worst[0]:
        worst = (local_worst, (m, local_worst_h))
    print("  m=%2d: worst weight(out)/w = %.4f %s" % (m, local_worst,
          "VIOLATES w/2" if local_worst < 0.5 else ""))
print("  overall worst: m=%d pattern=%s ratio=%.4f" % (worst[1][0], worst[1][1], worst[0]))

# random large m
print("  random m=200: 20 trials worst ratio:")
wr = 1.0
for t in range(20):
    rng = random.Random(t)
    h = [1 if rng.random() < 0.6 else 0 for _ in range(200)]
    wo, wi, r = pascal_weight_ratio(h)
    wr = min(wr, r)
print("  worst = %.4f" % wr)

# ---------- Q3: failing random patterns — short tail? ----------
print("\nQ3: random Bernoulli(0.6) patterns (minimal gaps), N=300:")
print("  (trial, n, K, nu2, w, full-conv ratio)")
worst_full = 1.0
short_tail_count = 0
for t in range(40):
    rng = random.Random(500 + t)
    pat = [1 if rng.random() < 0.6 else 0 for _ in range(299)]
    seq2 = [2]
    for b in pat:
        seq2.append(seq2[-1] + 2 * (2 - b))
    # incremental diagonals, track min nu2/w
    D = [seq2[0]]
    pref = [0] * (len(pat) + 1)
    for i, b in enumerate(pat):
        pref[i + 1] = pref[i] + b
    mmin = 1.0; mmin_info = None
    for n in range(1, 300):
        newD = [0] * (n + 1)
        newD[0] = seq2[n]
        for k in range(1, n + 1):
            newD[k] = abs(newD[k - 1] - D[k - 1])
        D = newD
        if n >= 17:
            body = D[2:-1]
            i = len(body)
            while i > 0 and body[i - 1] in (0, 2):
                i -= 1
            cyc = body[i:]
            nu2v = cyc.count(2)
            wv = pref[n - 1] - pref[1]
            if wv > 0:
                r = nu2v / float(wv)
                if r < mmin:
                    mmin = r
                    mmin_info = (n, i + 2, nu2v, wv)
    # full convolution ratio for the whole pattern
    wo, wi, rfull = pascal_weight_ratio(pat[:299])
    worst_full = min(worst_full, rfull)
    if mmin_info is not None and mmin_info[1] > 2:
        short_tail_count += 1
    if t < 8:
        print("  trial %2d: min nu2/w=%.3f at %s ; full-conv ratio=%.3f"
              % (t, mmin, mmin_info, rfull))
print("  trials with K>2 at their worst point: %d/40" % short_tail_count)
print("  worst full-convolution ratio over 40 trials: %.4f" % worst_full)

# ---------- Q4: primes — nu2 vs full convolution weight ----------
print("\nQ4: primes: nu2(n) vs full Pascal-convolution weight of the h-window:")
for n in [50, 100, 200, 400, 800]:
    K, nu2, L = diagonal_tail(seq, n)
    hw = bits[1:n - 1]
    wo, wi, r = pascal_weight_ratio(hw)
    print("  n=%4d: K=%d L=%d nu2=%d full-conv-weight=%d w=%d nu2/full=%.3f"
          % (n, K, L, nu2, wo, wi, nu2 / float(wo) if wo else 0))
