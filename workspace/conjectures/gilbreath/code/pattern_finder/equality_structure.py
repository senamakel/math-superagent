#!/usr/bin/env python3
"""Structure of the equality point n=43 (nu2 = w/2 exactly) and the
prefix-closed combinatorial question.

Q1: At n=43 with real prime bits (minimal gaps), print the full diagonal
    delta(q_43), the {0,2} suffix, and compare nu2 vs w.  Also find ALL n
    where nu2 == w/2 exactly over N=2000, and all where nu2 < w (strict).

Q2: The {0,2} suffix of the diagonal is the "absorbed" tail.  Its length L(n)
    and 2-count nu2(n).  Is there a *deterministic* relation between the
    suffix length and w(n)?  Plot (print) L(n) vs w(n) at sample n.

Q3: Prefix-closed test: if a pattern fails at some n (nu2 < w/2), does some
    PREFIX of it also fail at a smaller n?  I.e. is the violating set
    upward-closed under extension?  Test on random patterns: for each
    violating pattern at length N, find the earliest violation.  If the
    earliest violation is always at a small prefix, the property is
    prefix-closed, which would make it checkable locally.

Q4: The MOD-2 structure: halve the diagonal values (all even after index 1)
    and write the diagonal recurrence in {0,1}.  The {0,2} suffix of D
    corresponds to a suffix of the halved diagonal where values are {0,1}.
    The transfer nu2 >= w/2 says: in the maximal {0,1} suffix of the halved
    diagonal, the number of 1s is at least half the number of 1s in the
    mod-4-switch bits.  Is there a direct combinatorial map from switch-bits
    to diagonal-1s?
"""
import time
from lib.gilbreath import primes_up_to


def diagonal_and_cycle(seq, n):
    """delta(q_n) and (tau, nu2) of its {0,2} suffix (body D[2:-1])."""
    D = [seq[0]]
    for i in range(1, n + 1):
        newD = [0] * (i + 1)
        newD[0] = seq[i]
        for k in range(1, i + 1):
            newD[k] = abs(newD[k - 1] - D[k - 1])
        D = newD
    body = D[2:-1]
    i = len(body)
    while i > 0 and body[i - 1] in (0, 2):
        i -= 1
    cyc = body[i:]
    tau = i + 2          # start index in D
    nu2 = cyc.count(2)
    return D, tau, nu2, len(cyc)


N = 2000
P = primes_up_to(10 ** 6)
bits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(N + 1)]
gaps = [1] + [2 * (2 - b) for b in bits[1:N]]
seq = [2]
for g in gaps:
    seq.append(seq[-1] + g)

# ---------- Q1: equality points ----------
print("Q1: n with nu2 == w/2 exactly (N=2000, prime bits, minimal gaps):")
pref_w = [0] * (N + 1)
for i, b in enumerate(bits[1:N]):
    pref_w[i + 1] = pref_w[i] + b
# w(n) = pref_w[n-1]  (bits g_3..g_n => bits[1..n-2]... careful with indexing)
# bits[k] (0-based over gaps g_{k+2}); w(n) sums bits for gaps g_3..g_n
# = bits[1..n-2] if bits[0]=g_2.  Let's recompute directly per n.
D = [seq[0]]
equal_ns = []
less_than_w = []
tight_min = None
for n in range(1, N):
    newD = [0] * (n + 1)
    newD[0] = seq[n]
    for k in range(1, n + 1):
        newD[k] = abs(newD[k - 1] - D[k - 1])
    D = newD
    if n >= 2:
        body = D[2:-1]
        i = len(body)
        while i > 0 and body[i - 1] in (0, 2):
            i -= 1
        cyc = body[i:]
        nu2v = cyc.count(2)
        wv = sum(bits[1:n - 1])   # gaps g_3..g_n: bit of gap g_{j+2} = bits[j], j=1..n-2
        if wv > 0:
            if nu2v == 0.5 * wv:
                equal_ns.append(n)
            if nu2v < wv:
                less_than_w.append(n)
            if nu2v < 0.5 * wv:
                tight_min = n
                break
print("  equality points:", equal_ns[:20], "total", len(equal_ns))
print("  n with nu2 < w (strict):", len(less_than_w), "first few:", less_than_w[:10])
print("  first n with nu2 < w/2:", tight_min)

# the n=43 case in detail
D43, tau43, nu243, L43 = diagonal_and_cycle(seq, 43)
w43 = sum(bits[1:42])
print("\n  n=43: tau=%d, suffix length=%d, nu2=%d, w=%d, nu2==w/2? %s"
      % (tau43, L43, nu243, w43, nu243 == w43 // 2 and w43 % 2 == 0))
print("  D43 =", D43)
print("  body D[2:-1] =", D43[2:-1])
print("  suffix (max {0,2}) =", D43[tau43:-1])

# ---------- Q2: suffix length vs w ----------
print("\nQ2: suffix length L(n) vs w(n) at samples:")
samp = [50, 100, 200, 400, 800, 1600]
D = [seq[0]]
for n in range(1, N):
    newD = [0] * (n + 1)
    newD[0] = seq[n]
    for k in range(1, n + 1):
        newD[k] = abs(newD[k - 1] - D[k - 1])
    D = newD
    if n in samp:
        body = D[2:-1]
        i = len(body)
        while i > 0 and body[i - 1] in (0, 2):
            i -= 1
        cyc = body[i:]
        nu2v = cyc.count(2)
        wv = sum(bits[1:n - 1])
        print("  n=%5d: L=%4d nu2=%4d w=%4d nu2/w=%.3f" % (n, len(cyc), nu2v, wv, nu2v / wv))

# ---------- Q3: prefix-closure of violations ----------
print("\nQ3: prefix-closure — earliest violation position in violating patterns:")
rng = random.Random(1234)
early_counts = {}
for t in range(200):
    pat = [1 if rng.random() < 0.6 else 0 for _ in range(600 - 1)]
    seq2 = [2]
    for g in [1] + [2 * (2 - b) for b in pat]:
        seq2.append(seq2[-1] + g)
    D = [seq2[0]]
    first_v = None
    pref2 = [0] * (len(pat) + 1)
    for i, b in enumerate(pat):
        pref2[i + 1] = pref2[i] + b
    for n in range(1, 600):
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
            wv = pref2[n - 1] - pref2[1]
            if wv > 0 and nu2v < 0.5 * wv - 1e-12:
                first_v = n
                break
    if first_v is not None:
        bucket = first_v // 25 * 25
        early_counts[bucket] = early_counts.get(bucket, 0) + 1
print("  distribution of earliest violation n (buckets of 25), 200 random p=0.6 patterns:")
for b in sorted(early_counts):
    print("    n in [%3d,%3d): %d" % (b, b + 25, early_counts[b]))
