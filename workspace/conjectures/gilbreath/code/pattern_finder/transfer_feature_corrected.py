#!/usr/bin/env python3
"""Corrected feature test for the transfer bound nu2(n) >= w(n)/2.

A gap g has halved parity b = (g//2)%2.  Minimal gaps realizing parity b:
  b=1 -> 2,  b=0 -> 4   (gap = 2*(2-b)).

Q1 (universality): does nu2 >= w/2 hold for EVERY {2,4}-gapped 2-then-odds
sequence?  Exhaustive over all 2^(N-2) bit patterns for N-2 <= 16, then
random long patterns.  This is the combinatorial core: the prime bit pattern
is one input, so a proof for all patterns would make the prime case trivial;
a single failing pattern refutes universality.

Q2 (feature): with REAL prime bits (order fixed) and various magnitude
schemes, does nu2 >= w/2 survive to N=2000?
  V1 real bits, minimal gaps (gap=2*(2-b))
  V2 real bits, gaps = 2*(2-b) + 4*m (m random 0..3)   [same bits, larger gaps]
  V3 real bits + random +1 shift, minimal gaps
  V4 random bits (fair), minimal gaps
  V5 real bits, all gaps = 2  (constant parity-1 gaps; w = n-3 then)
  V6 alternating bits, minimal gaps (the known breaker)
Exact integers.  Bounded oracle: N <= 2000, patterns exhaustive only to
length 16.
"""
import random
from itertools import product
from lib.gilbreath import primes_up_to

# ---------- core evaluator ----------
def transfer_stats(seq, N, lo=17):
    """seq[0..N-1] 2-then-odds.  Returns (min nu2/w over n in [lo,N-1] with
    w>0, first violation of nu2>=w/2, first violation of nu2>=w, count of
    violations of nu2>=w/2)."""
    D = [seq[0]]
    hbits = [((seq[i + 1] - seq[i]) // 2) % 2 for i in range(len(seq) - 1)]
    pref = [0] * (len(hbits) + 1)
    for i, b in enumerate(hbits):
        pref[i + 1] = pref[i] + b
    min_ratio = 1.0
    viol_half = 0; viol_one = 0
    first_half = None; first_one = None
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
            wv = pref[n] - pref[2]
            if n >= lo and wv > 0:
                r = nu2v / float(wv)
                if r < min_ratio:
                    min_ratio = r
                if nu2v < 0.5 * wv - 1e-12:
                    viol_half += 1
                    if first_half is None:
                        first_half = n
                if nu2v < wv:
                    viol_one += 1
                    if first_one is None:
                        first_one = n
    return min_ratio, first_half, viol_half, first_one, viol_one


def gaps_to_seq(gaps):
    s = [2]
    for g in gaps:
        s.append(s[-1] + g)
    return s


# ---------- Q1: exhaustive over {2,4} bit patterns ----------
print("Q1 exhaustive over {2,4}-gap patterns (gap = 2*(2-b)):")
worst = (1.0, None)
first_fail = None
NQ = 17   # sequence length: bits for gaps g_2..g_{NQ-1}: NQ-2 bits
for pat in product([0, 1], repeat=NQ - 2):
    gaps = [1] + [2 * (2 - b) for b in pat]
    seq = gaps_to_seq(gaps)
    mr, fh, vh, fo, vo = transfer_stats(seq, NQ)
    if mr < worst[0]:
        worst = (mr, pat)
    if fh is not None and first_fail is None:
        first_fail = (pat, fh)
print("  all %d patterns of length %d: min nu2/w = %.4f (pattern %s)"
      % (2 ** (NQ - 2), NQ, worst[0], worst[1]))
print("  first pattern violating nu2>=w/2: %s at n=%s" % (first_fail if first_fail else "NONE", first_fail[1] if first_fail else "-"))

# random long patterns over {2,4} gaps
print("random long {2,4} patterns (N=400):")
rng = random.Random(7)
wmin = 1.0
for t in range(50):
    pat = [rng.randrange(2) for _ in range(400 - 2)]
    gaps = [1] + [2 * (2 - b) for b in pat]
    seq = gaps_to_seq(gaps)
    mr, fh, vh, fo, vo = transfer_stats(seq, 400)
    wmin = min(wmin, mr)
print("  min nu2/w over 50 random patterns: %.4f" % wmin)

# ---------- Q2: real prime bits with magnitude variations ----------
N = 2000
P = primes_up_to(10 ** 6)
assert len(P) > N + 2
gaps_real = [P[i + 1] - P[i] for i in range(N + 1)]
bits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(N + 1)]

print("\nQ2 feature test over real prime bits (N=%d):" % N)

# V0 real primes
seq0 = P[:N]
mr, fh, vh, fo, vo = transfer_stats(seq0, N)
print("  V0 real primes           : min nu2/w=%.4f viol(>=w/2)=%d first=%s viol(>=w)=%d first=%s"
      % (mr, vh, fh, vo, fo))

# V1 real bits, minimal gaps
gaps1 = [1] + [2 * (2 - b) for b in bits[1:N]]
mr, fh, vh, fo, vo = transfer_stats(gaps_to_seq(gaps1), N)
print("  V1 real bits, min gaps   : min nu2/w=%.4f viol(>=w/2)=%d first=%s viol(>=w)=%d first=%s"
      % (mr, vh, fh, vo, fo))

# V2 real bits, gaps 2*(2-b) + 4*m (larger, parity preserved)
gaps2 = [1] + [2 * (2 - b) + 4 * (i % 5) for i, b in enumerate(bits[1:N])]
mr, fh, vh, fo, vo = transfer_stats(gaps_to_seq(gaps2), N)
print("  V2 real bits, gaps +4m   : min nu2/w=%.4f viol(>=w/2)=%d first=%s viol(>=w)=%d first=%s"
      % (mr, vh, fh, vo, fo))

# V3 real bits shifted +1, minimal gaps
bits3 = bits[1:] + bits[:1]
gaps3 = [1] + [2 * (2 - b) for b in bits3[1:N]]
mr, fh, vh, fo, vo = transfer_stats(gaps_to_seq(gaps3), N)
print("  V3 real bits shift+1     : min nu2/w=%.4f viol(>=w/2)=%d first=%s viol(>=w)=%d first=%s"
      % (mr, vh, fh, vo, fo))

# V4 random fair bits, minimal gaps
rng = random.Random(99)
worst4 = 1.0
for t in range(30):
    pat = [rng.randrange(2) for _ in range(N - 1)]
    gaps4 = [1] + [2 * (2 - b) for b in pat]
    mr, fh, vh, fo, vo = transfer_stats(gaps_to_seq(gaps4), N)
    worst4 = min(worst4, mr)
print("  V4 random bits, min gaps : worst min nu2/w over 30 = %.4f" % worst4)

# V5 all gaps 2 (constant parity-1), w = n-3
gaps5 = [1] + [2] * (N - 1)
mr, fh, vh, fo, vo = transfer_stats(gaps_to_seq(gaps5), N)
print("  V5 all gaps=2            : min nu2/w=%.4f viol(>=w/2)=%d first=%s" % (mr, vh, fh))

# V6 alternating bits, minimal gaps (known breaker)
gaps6 = [1] + [2 * (2 - (i % 2)) for i in range(N - 1)]
mr, fh, vh, fo, vo = transfer_stats(gaps_to_seq(gaps6), N)
print("  V6 alternating bits      : min nu2/w=%.4f viol(>=w/2)=%d first=%s" % (mr, vh, fh))
