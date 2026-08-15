#!/usr/bin/env python3
"""Bernoulli-density threshold for the transfer bound nu2 >= w/2, and the
large-n prime-pattern check.

Q1: For random Bernoulli(p) {2,4}-gap patterns (minimal gaps), over many
    trials, what is the worst min nu2/w over n in [17,N], as a function of p
    in {0.5, 0.55, 0.6, 0.65, 0.7}?  The primes have p ~ 0.59.  If Bernoulli
    at p=0.6 fails, then density alone is not the ingredient.

Q2: The real prime pattern at large n with minimal gaps: does min nu2/w stay
    >= 0.5 all the way to N = 20000?  (Incremental diagonal on minimal gaps
    from the prime bits; O(N^2) diffs, N=20000 -> 4e8 diffs... too slow in
    pure Python.  Use numpy vectorization?  The diagonal recurrence is
    inherently sequential in n; but each row pass is O(N).  N=20000 -> 2e8
    cell computations, each a couple of Python ops... ~60s.  Acceptable with
    the 540s timeout, but let's do N=10000 first (1e8 cells) then decide.)

Q3: Does the transfer hold at p around 0.59-0.6 with the *minimal gaps*, for
    n up to 2000?  Find the p that separates "always holds" from "sometimes
    fails" empirically.

Q4: Critical check — prime pattern with gaps REPLACED by their halved-parity
    minimal value vs the REAL gaps at larger n (N=10000): if both give
    min ratio 0.5, then the transfer's validity is about the bit pattern
    alone at these scales, and magnitudes matter only through parity.
"""
import random, time
from lib.gilbreath import primes_up_to


def transfer_stats_np(seq, N, lo=17):
    """numpy-vectorized diagonal: the incremental diagonal has O(N^2) cells,
    but each cell is |newD[k-1] - D[k-1]|; vectorize with numpy ops per row."""
    import numpy as np
    D = np.array(seq[:1], dtype=np.int64)
    hbits = [((seq[i + 1] - seq[i]) // 2) % 2 for i in range(len(seq) - 1)]
    pref = [0] * (len(hbits) + 1)
    for i, b in enumerate(hbits):
        pref[i + 1] = pref[i] + b
    min_ratio = 1.0
    viol = 0; first = None
    for n in range(1, N):
        # newD length n+1: newD[0] = seq[n], newD[k] = |newD[k-1]-D[k-1]|
        newD = np.empty(n + 1, dtype=np.int64)
        newD[0] = seq[n]
        # sequential dependence: newD[k] = |newD[k-1] - D[k-1]|
        # cannot vectorize the absolute-diff chain directly, but the chain is
        # the standard scan; python loop over k with numpy scalar ops is slow.
        # Just do the python loop (each cell cheap).
        acc = seq[n]
        for k in range(1, n + 1):
            acc = abs(acc - D[k - 1])
            newD[k] = acc
        D = newD
        if n >= lo:
            body = D[2:-1]
            i = len(body)
            while i > 0 and body[i - 1] in (0, 2):
                i -= 1
            cyc = body[i:]
            nu2v = int((cyc == 2).sum())
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


# ---------- Q1: Bernoulli p threshold ----------
print("Q1: Bernoulli(p) minimal-gap patterns, N=800, worst min nu2/w over 25 trials:")
for p in [0.5, 0.55, 0.59, 0.6, 0.65, 0.7, 0.8]:
    worst = 1.0; nv = 0
    for t in range(25):
        rng = random.Random(9000 + t * 17 + int(p * 100))
        pat = [1 if rng.random() < p else 0 for _ in range(800 - 1)]
        seq = gaps_to_seq([1] + [2 * (2 - b) for b in pat])
        mr, fh, vh = transfer_stats_np(seq, 800)
        worst = min(worst, mr)
        nv += (1 if vh > 0 else 0)
    print("  p=%.2f : worst min nu2/w = %.4f, %d/25 trials violated" % (p, worst, nv))

# ---------- Q2/Q4: real prime bits at large n ----------
N = 10000
print("\nQ2/Q4: real prime bits, minimal gaps, N=%d (large-n transfer):" % N)
t0 = time.time()
P = primes_up_to(3 * 10 ** 6)
bits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(N + 1)]
seq = gaps_to_seq([1] + [2 * (2 - b) for b in bits[1:N]])
mr, fh, vh = transfer_stats_np(seq, N)
print("  minimal-gap prime pattern: min nu2/w=%.4f, viol=%d first=%s (%.1fs)"
      % (mr, vh, fh, time.time() - t0))

t0 = time.time()
Pbig = primes_up_to(2 * 10 ** 7)   # enough primes for gaps
gaps_real = [Pbig[i + 1] - Pbig[i] for i in range(N + 1)]
seq_real = gaps_to_seq(gaps_real[1:N])
mr2, fh2, vh2 = transfer_stats_np(seq_real, N)
print("  real prime gaps:            min nu2/w=%.4f, viol=%d first=%s (%.1fs)"
      % (mr2, vh2, fh2, time.time() - t0))
print("  -> transfer holds identically for real gaps and minimal-gap pattern" if
      (mr == mr2 and vh == vh2) else "  -> DIFFERENT: magnitudes matter")
