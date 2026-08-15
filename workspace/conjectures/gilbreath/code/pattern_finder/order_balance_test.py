#!/usr/bin/env python3
"""What distinguishes the real prime bit pattern from random majority ones?

Observations so far:
  - real primes: min nu2/w = 0.5 exactly (N=2000), survives 1% flips
  - random majority patterns: fail (0.12 at p=0.5 conditioned)
  - bounded-run random: fail even at runs <= 4
  - canonical (0^R,1^R): fails for R >= 8 (ratio 1/(2R-2) ~ 0.125 at R=8)

So neither majority nor bounded runs characterise it.  Test new candidates:

Q1: Alternation/balance.  Real prime bits: what is the distribution of the
    *alternating count* (number of bit changes) up to n, and is it
    "maximally alternating"?  Check: does nu2 >= w/2 hold for patterns built
    by random permutation of a fixed count of 1s (i.e. only the SET of switch
    positions matters, not the order)?

Q2: Test "prime pattern with magnitudes stripped but ORDER kept" vs "same
    bits, random order".  If order matters, random permutation of the prime
    bits breaks it.

Q3: Threshold n for the real prime pattern: min nu2/w per n over a longer
    range (n up to 10000, incremental diagonal on minimal gaps from prime
    bits): does the 0.5 bound persist, and where are the tightest points?
    Also: is the tight point always at nu2 = w/2 exactly (equality)?

Q4: The canonical (0^R,1^S): when does it first violate, as function of R,S?
    Map the boundary: does the violating region correlate with S - R?
    (0^R then 1^S: the 1s come after the 0s; the diagonal accumulates zeros
    during the 0-run, then the 1-run's XOR expansion...)
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
    tight = []          # n where nu2 == w/2 exactly (equality points)
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
                if abs(nu2v - 0.5 * wv) < 1e-9:
                    tight.append(n)
                if nu2v < 0.5 * wv - 1e-12:
                    viol += 1
                    if first is None:
                        first = n
    return min_ratio, first, viol, tight


def gaps_to_seq(gaps):
    s = [2]
    for g in gaps:
        s.append(s[-1] + g)
    return s


N = 2000
P = primes_up_to(10 ** 6)
bits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(N + 1)]

# ---------- Q1/Q2: order matters? ----------
print("Q2: order of prime bits — same multiset, random permutation (minimal gaps, N=2000):")
real_mr, real_fh, real_vh, real_tight = transfer_stats([2] + [3] + [3 + sum(2*(2-b) for b in bits[1:i+1]) for i in range(1, N)], N)
print("  real prime bits in order: min nu2/w=%.4f, viol=%d first=%s" % (real_mr, real_vh, real_fh))
worst_perm = 1.0
for t in range(8):
    rng = random.Random(31 + t)
    pat = bits[1:N].copy()
    rng.shuffle(pat)
    seq = gaps_to_seq([1] + [2 * (2 - b) for b in pat])
    mr, fh, vh, tight = transfer_stats(seq, N)
    worst_perm = min(worst_perm, mr)
print("  worst over 8 random permutations: min nu2/w=%.4f" % worst_perm)

# ---------- Q3: prime pattern longer range ----------
print("\nQ3: real prime bits, minimal gaps, N=5000 (minimal gaps from prime bits):")
P2 = primes_up_to(5 * 10 ** 6)
bits5k = [((P2[i + 1] - P2[i]) // 2) % 2 for i in range(5000 + 1)]
seq5k = gaps_to_seq([1] + [2 * (2 - b) for b in bits5k[1:5000]])
mr, fh, vh, tight = transfer_stats(seq5k, 5000)
print("  N=5000 real bits: min nu2/w=%.4f, viol=%d first=%s" % (mr, vh, fh))
print("  equality points nu2==w/2 (first 10):", tight[:10], "... total", len(tight))

# ---------- Q4: canonical (0^R,1^S) map ----------
print("\nQ4: canonical (0^R, 1^S) violation map (min ratio / first violation n):")
print("     R\\S  |  4      6      8      10     12     16     20")
for R in [4, 6, 8, 10, 12, 16]:
    row = []
    for S in [4, 6, 8, 10, 12, 16, 20]:
        pat = [0] * R + [1] * S
        seq = gaps_to_seq([1] + [2 * (2 - b) for b in pat])
        mr, fh, vh, tight = transfer_stats(seq, len(pat) + 2)
        row.append("%.2f/%s" % (mr, fh if fh else "-"))
    print("  %2d      | %s" % (R, "  ".join(row)))
