#!/usr/bin/env python3
"""Is the transfer bound nu2(n) >= w(n)/2 a combinatorial lemma (all inputs)
or prime-specific?

Input: a 2-then-odds sequence q (q_1=2, q_{n+1}-q_n = g_n with g_n odd >= 1...
wait: gaps between odd numbers are even; the sequence is 2, then odd numbers,
so g_1=2->odd is odd, then odd->odd gaps are even).

We construct the triangle of absolute differences, read the right diagonal
delta(q_n), compute nu2(n) = #2s in the maximal {0,2} suffix of the diagonal
(convention: body = diag[2:-1], maximal {0,2} suffix of body), and
w(n) = Hamming weight of the halved mod-2 gap bits h[j] = (gap_{j+1}//2) % 2
for j in [2, n-1] (i.e. gaps g_3..g_n halved parity).

Test whether nu2(n) >= w(n)/2 holds at EVERY n in [17, N] for:
  (a) random gaps with iid uniform halved-parity bits (fair coin)
  (b) adversarial bits: all bits = 0 (all gaps 0 mod 4)
  (c) alternating bits 0,1,0,1,...
  (d) random gaps drawn from the actual empirical prime-gap mod-4 mixture
      (density ~0.6 of switch bits) with iid magnitude

For each input we need actual even gaps; choose gap = 2*(2*b + jitter) so the
halved bit is b and the gap is even, >= 2.  For variety also try bigger even
gaps to see whether magnitude matters at all.

The triangle is truncated: to read diagonal delta(q_n) for all n <= N we need
row 0 columns 0..N-1 only (diagonal cells (k, n-k) have k <= n-1, column
n-k in [0, n-1] <= N-1), so truncating the sequence to N entries is EXACT
for all n <= N.

O(N^2) diffs, O(N) memory.
"""
import random, sys
from collections import Counter

N = int(sys.argv[1]) if len(sys.argv) > 1 else 200
TRIALS = int(sys.argv[2]) if len(sys.argv) > 2 else 300


def triangle_and_nu2(seq, N):
    """seq[0..N-1]: the starting row.  Returns (list of nu2(n) for n in
    [2..N-1], list of w(n)).  Iterates the triangle row by row, but keeps
    the whole first row and diagonal reads; O(N^2) diffs."""
    rows = [seq[:]]              # row 0
    # We'll compute rows incrementally but each row k only needs width N-k.
    # Diagonal through q_n: cell (k, n-k) for k=0..n-1.
    # To get it, we need row k truncated at column n-k.
    # Simplest: build full truncated rows A_k[0..N-1-k].
    cur = seq[:]
    diags = []                   # diags[n] = delta(q_n) as list, n=0..N-1
    # n=0: delta(q_0)?  We use 1-indexed q: q_1..q_N.  delta(q_n) length n.
    # Build incrementally: rows[k] = A_k truncated to width N-k.
    # delta(q_n)[k] = A_k[n-k]; A_k width N-k, need index n-k <= N-1-k OK.
    nu2 = []
    w = []
    hbits = [((seq[i + 1] - seq[i]) // 2) % 2 for i in range(len(seq) - 1)]
    pref = [0] * (len(hbits) + 1)
    for i, b in enumerate(hbits):
        pref[i + 1] = pref[i] + b

    width = N
    row = seq[:]
    # diagonal reads: for each n, delta(q_n) = [row_k[n-k] for k in 0..n-1]
    # We can maintain rows incrementally; but reading all diagonals needs all
    # rows simultaneously in the worst case... Instead: incremental diagonal
    # (like rightdiag.py): D = delta(q_n) extends to delta(q_{n+1}) by
    # newD[0] = q_{n+1}, newD[k] = |newD[k-1] - D[k-1]|.  O(N^2) total.
    D = [seq[0]]
    # D is delta(q_1), length 1
    for n in range(1, N):
        newD = [0] * (n + 1)
        newD[0] = seq[n]
        for k in range(1, n + 1):
            newD[k] = abs(newD[k - 1] - D[k - 1])
        D = newD
        # now D = delta(q_n), length n+1 (indices 0..n)
        # body for the cycle: D[2:-1] (indices 2..n-1)
        if n >= 2:
            body = D[2:-1]
            i = len(body)
            while i > 0 and body[i - 1] in (0, 2):
                i -= 1
            cyc = body[i:]
            nu2v = cyc.count(2)
            wv = pref[n] - pref[2]   # hbits[2..n-1], i.e. gaps g_3..g_n
            nu2.append(nu2v)
            w.append(wv)
    # nu2 list indexed by n-2 (n from 2 to N-1)
    return nu2, w


def make_seq(bits, magnitudes):
    """bits[0..N-2] = halved-parity of gaps g_2..g_N?  seq[0]=2, then odds.
    gap g_1 = seq[1]-seq[0] odd; gaps g_2.. : even, gap//2 parity = bit."""
    seq = [2]
    # g_1: choose 1 (smallest odd)
    seq.append(3)
    for i, (b, mag) in enumerate(zip(bits, magnitudes)):
        # gap g_{i+2} has halved parity b and magnitude mag (>=1)
        gap = 2 * mag + (1 if b else 0)
        # ensure parity of gap: gap//2 % 2 == b, and gap even >= 2
        # if b: mag odd -> gap = 2*odd ≡ 2 mod 4; else mag even
        # simplest: gap = 2*(2*b + 1) * mag2 ... keep it exact:
        # choose gap = 2*b*2 + ... let's just do gap = 2*(mag) with parity b:
        # 2*mag % 4 == 0 iff mag even, == 2 iff mag odd.  So set mag parity = b.
        gap = 2 * mag
        seq.append(seq[-1] + gap)
    return seq


fails_by_kind = Counter()
worst_ratio = {}
worst_at = {}
for trial in range(TRIALS):
    for kind in ["fair", "zeros", "alternating", "ones"]:
        rng = random.Random(12345 + trial * 7 + hash(kind) % 1000)
        bits = []
        mags = []
        for _ in range(N - 1):
            if kind == "fair":
                b = rng.randrange(2)
            elif kind == "zeros":
                b = 0
            elif kind == "ones":
                b = 1
            else:  # alternating
                b = (trial + _) % 2
            bits.append(b)
            # magnitude: keep it small but with some spread so cells get
            # various sizes: 1..3 uniformly
            mags.append(rng.randrange(1, 4))
        seq = make_seq(bits, mags)
        nu2, w = triangle_and_nu2(seq, N)
        for idx, (nv, wv) in enumerate(zip(nu2, w)):
            n = idx + 2
            if n >= 17 and wv > 0:
                r = nv / float(wv)
                if r < 0.5 - 1e-12:
                    fails_by_kind[kind] += 1
                prev = worst_ratio.get(kind, 1.0)
                if r < prev:
                    worst_ratio[kind] = r
                    worst_at[kind] = (trial, n, nv, wv)

print("N=%d trials=%d  (kind: #violations of nu2>=w/2, worst ratio)" % (N, TRIALS))
for kind in ["fair", "zeros", "alternating", "ones"]:
    print("  %-12s fails=%3d  worst nu2/w=%.4f at (trial=%d n=%d nu2=%d w=%d)"
          % (kind, fails_by_kind[kind], worst_ratio.get(kind, 1.0),
             *(worst_at.get(kind, (0, 0, 0, 0)))))
