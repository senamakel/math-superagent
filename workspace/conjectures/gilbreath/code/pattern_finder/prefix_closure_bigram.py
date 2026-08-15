#!/usr/bin/env python3
"""Final structural probes on the transfer bound nu2 >= w/2.

Q3 (fixed): prefix-closure.  In random failing patterns, where is the
EARLIEST violation n?  If always at small n, the violation is a short-prefix
effect; the canonical breaker (0^R,1^S) violates at n=R+S+2 which grows with
R,S, suggesting NOT prefix-closed.  Measure the empirical distribution.

Q4: bigram structure of prime switch-bits vs Bernoulli(p=0.59): conditional
probability that bit[i+1]=1 given bit[i]=b; and joint distribution of
(0-run length, following 1-run length) — does the prime pattern avoid
"long 0-run immediately followed by long 1-run" (the breaker shape) while
Bernoulli does not?

Q5: does the transfer fail *monotonically* as patterns approach the breaker
shape?  Interpolate between the real prime prefix (length 2000, which holds)
and the breaker (0^9,1^7): bitwise-flip a growing fraction of a FAILING
random pattern toward the prime pattern — the first violations should
disappear exactly when the pattern becomes prime-like.  This tells whether
the *set of holding patterns* is a smooth region or a knife-edge.
"""
import random, time
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


def earliest_violation(pat, N):
    seq = gaps_to_seq([1] + [2 * (2 - b) for b in pat[:N - 1]])
    mr, fh, vh = transfer_stats(seq, N)
    return fh, mr


# ---------- Q3: earliest violation ----------
print("Q3: earliest violation n in random p=0.6 patterns (N=600, 150 trials):")
buckets = {}
for t in range(150):
    rng = random.Random(1000 + t)
    pat = [1 if rng.random() < 0.6 else 0 for _ in range(599)]
    fh, mr = earliest_violation(pat, 600)
    if fh is not None:
        b = fh // 25 * 25
        buckets[b] = buckets.get(b, 0) + 1
tot = sum(buckets.values())
for b in sorted(buckets):
    print("  n in [%3d,%3d): %3d  (%.1f%%)" % (b, b + 25, buckets[b], 100.0 * buckets[b] / tot))
print("  total violating trials: %d/150" % tot)
# canonical breaker earliest violation
for (R, S) in [(8, 8), (12, 12), (16, 16)]:
    pat = [0] * R + [1] * S
    fh, mr = earliest_violation(pat, R + S + 2)
    print("  canonical (0^%d,1^%d): first violation at n=%d (pattern length %d)"
          % (R, S, fh, R + S))

# ---------- Q4: bigram structure ----------
print("\nQ4: bigram structure, prime bits vs Bernoulli(0.59):")
N = 100000
P = primes_up_to(2 * 10 ** 7)
bits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(N)]
def bigram(bits):
    n11 = n10 = n01 = n00 = 0
    for i in range(len(bits) - 1):
        if bits[i]:
            if bits[i + 1]:
                n11 += 1
            else:
                n10 += 1
        else:
            if bits[i + 1]:
                n01 += 1
            else:
                n00 += 1
    return n11, n10, n01, n00
n11, n10, n01, n00 = bigram(bits)
print("  prime:  P(1|1)=%.4f P(0|1)=%.4f P(1|0)=%.4f P(0|0)=%.4f  (n=%d)"
      % (n11 / (n11 + n10), n10 / (n11 + n10), n01 / (n00 + n01), n00 / (n00 + n01), N))
rng = random.Random(5)
bern = [1 if rng.random() < 0.59 else 0 for _ in range(N)]
n11, n10, n01, n00 = bigram(bern)
print("  Bernoulli(0.59): P(1|1)=%.4f P(0|1)=%.4f P(1|0)=%.4f P(0|0)=%.4f"
      % (n11 / (n11 + n10), n10 / (n11 + n10), n01 / (n00 + n01), n00 / (n00 + n01)))

# joint (0-run length, following 1-run length): the breaker shape
def run_pairs(bits):
    pairs = []
    i = 0
    while i < len(bits):
        if bits[i] == 0:
            j = i
            while j < len(bits) and bits[j] == 0:
                j += 1
            r0 = j - i
            k = j
            while k < len(bits) and bits[k] == 1:
                k += 1
            r1 = k - j
            pairs.append((r0, r1))
            i = k
        else:
            i += 1
    return pairs
pp = run_pairs(bits)
bp = run_pairs(bern)
print("\n  (0-run, following 1-run) pairs with 0-run>=6:")
print("  prime:      ", sorted([p for p in pp if p[0] >= 6])[:12])
print("  Bernoulli:  ", sorted([p for p in bp if p[0] >= 6])[:12])
print("  max (0run,1run) prime:", max(pp), "Bernoulli:", max(bp))

# ---------- Q5: interpolation ----------
print("\nQ5: interpolate a FAILING random pattern toward the prime prefix:")
N = 2000
P2 = primes_up_to(10 ** 6)
pbits = [((P2[i + 1] - P2[i]) // 2) % 2 for i in range(N)]
rng = random.Random(4242)
base = [1 if rng.random() < 0.6 else 0 for _ in range(N - 1)]
fh, mr = earliest_violation(base, N)
print("  random base: first violation at n=%d, min ratio=%.4f" % (fh, mr))
for f in [0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 1.0]:
    pat = base.copy()
    nflip = int(f * len(pat))
    idxs = rng.sample(range(len(pat)), nflip)
    for i in idxs:
        pat[i] = pbits[i + 1]
    fh2, mr2 = earliest_violation(pat, N)
    print("  flip %.1f toward prime: first violation=%s min ratio=%.4f"
          % (f, fh2, mr2))
