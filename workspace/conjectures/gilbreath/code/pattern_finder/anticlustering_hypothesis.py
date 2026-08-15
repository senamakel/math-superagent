#!/usr/bin/env python3
"""Decisive hypothesis: does NEGATIVE BIGRAM AUTOCORRELATION (switch
anti-clustering, as in the primes) rescue the transfer nu2 >= w/2?

Q1: Generate 2-state Markov patterns with P(1|1)=a, P(1|0)=b.  The primes
    have a=0.552, b=0.602 (stationary density ~ b/(1-a+b) = 0.602/(1.05) =
    0.573... hmm compute exactly).  Test (a,b) grid:
      (0.55, 0.60)  [prime-like]
      (0.50, 0.60)
      (0.45, 0.60)
      (0.40, 0.60)
      (0.59, 0.59)  [Bernoulli-like, control]
      (0.60, 0.50)  [positive autocorrelation, switches cluster]
    Does the transfer hold for the anti-clustered ones?

Q2: Same, but with the *stationary density forced to ~0.59*: adjust b so the
    stationary density matches the primes.  P(1) = b/(1-a+b).  For a=0.55:
    want P(1)=0.59 => 0.59(1-0.55+b)=b => 0.59*0.45 + 0.59b = b => 0.2655 =
    0.41b => b=0.6476.  Test (a,b) = (0.55,0.648), (0.50,0.742)...  wait
    that's P(1|0) quite high.  Check which (a,b) with the prime density 0.59
    hold.

Q3: Exact verification of the prime bigram on a longer stretch and the
    transfer on the *Markov chain with the prime's exact empirical
    transition matrix*.
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


def markov_pattern(a, b, L, rng):
    """P(1|1)=a, P(1|0)=b.  Start from the stationary distribution."""
    stat1 = b / (1 - a + b) if (1 - a + b) > 0 else 0.5
    pat = [1 if rng.random() < stat1 else 0]
    for _ in range(L - 1):
        if pat[-1]:
            pat.append(1 if rng.random() < a else 0)
        else:
            pat.append(1 if rng.random() < b else 0)
    return pat


print("Q1: Markov (a=P(1|1), b=P(1|0)), N=800, 30 trials each, worst min nu2/w:")
configs = [
    ("prime-like (0.55, 0.60)", 0.55, 0.60),
    ("anti-cluster (0.50, 0.60)", 0.50, 0.60),
    ("anti-cluster (0.45, 0.60)", 0.45, 0.60),
    ("anti-cluster (0.40, 0.60)", 0.40, 0.60),
    ("Bernoulli control (0.59, 0.59)", 0.59, 0.59),
    ("cluster (0.60, 0.50)", 0.60, 0.50),
    ("strong cluster (0.75, 0.25)", 0.75, 0.25),
]
for name, a, b in configs:
    worst = 1.0; nv = 0
    for t in range(30):
        rng = random.Random(20000 + t * 13 + int(a * 100))
        pat = markov_pattern(a, b, 800 - 1, rng)
        seq = gaps_to_seq([1] + [2 * (2 - bb) for bb in pat])
        mr, fh, vh = transfer_stats(seq, 800)
        worst = min(worst, mr)
        nv += (1 if vh > 0 else 0)
    print("  %-28s: worst min nu2/w=%.4f, %d/30 trials violated"
          % (name, worst, nv))

print("\nQ2: Markov with stationary density ~0.59 (prime density):")
for name, a, b in [
    ("(0.55, 0.648)", 0.55, 0.648),
    ("(0.50, 0.742)", 0.50, 0.742),
    ("(0.45, 0.863)", 0.45, 0.863),
    ("(0.60, 0.561)", 0.60, 0.561),
]:
    stat = b / (1 - a + b)
    worst = 1.0; nv = 0
    for t in range(30):
        rng = random.Random(30000 + t * 17 + int(a * 100))
        pat = markov_pattern(a, b, 800 - 1, rng)
        seq = gaps_to_seq([1] + [2 * (2 - bb) for bb in pat])
        mr, fh, vh = transfer_stats(seq, 800)
        worst = min(worst, mr)
        nv += (1 if vh > 0 else 0)
    print("  %-14s (stat=%.3f): worst min nu2/w=%.4f, %d/30 violated"
          % (name, stat, worst, nv))

print("\nQ3: prime's empirical transition matrix, N=2000, 20 trials:")
N = 2000
P = primes_up_to(10 ** 6)
bits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(N + 1)]
n11 = n10 = n01 = n00 = 0
for i in range(len(bits) - 1):
    if bits[i]:
        n11 += bits[i + 1]; n10 += 1 - bits[i + 1]
    else:
        n01 += bits[i + 1]; n00 += 1 - bits[i + 1]
a_emp = n11 / (n11 + n10); b_emp = n01 / (n00 + n01)
print("  empirical a=%.4f b=%.4f" % (a_emp, b_emp))
worst = 1.0; nv = 0
for t in range(20):
    rng = random.Random(40000 + t)
    pat = markov_pattern(a_emp, b_emp, N - 1, rng)
    seq = gaps_to_seq([1] + [2 * (2 - bb) for bb in pat])
    mr, fh, vh = transfer_stats(seq, N)
    worst = min(worst, mr)
    nv += (1 if vh > 0 else 0)
print("  Markov with prime transitions: worst min nu2/w=%.4f, %d/20 violated"
      % (worst, nv))
