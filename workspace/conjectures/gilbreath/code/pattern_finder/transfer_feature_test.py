#!/usr/bin/env python3
"""What feature of the primes makes nu2(n) >= w(n)/2 hold?

Variants, all over n in [17, N] (N=2000, sieve enough primes):
  V0: real prime gaps (reproduce the transfer)            -> should hold
  V1: real prime BITS (mod-4 class) but ALL gaps = 2      (gap = 2 + 2*bit)
  V2: real prime BITS, random ORDER, real magnitudes      (shuffle bits)
  V3: random bits, real prime magnitudes                  (shuffle magnitudes)
  V4: real bits, all gaps = 2                              (same as V1, explicit)
  V5: real bits, gaps = 2+2*bit, but bits shifted by +1   (order matters?)
Report min nu2/w over n in [17,N], and first violation of nu2 >= w/2.
"""
import random
from lib.gilbreath import primes_up_to

N = 2000
P = primes_up_to(10 ** 6)
assert len(P) > N + 2
gaps = [P[i + 1] - P[i] for i in range(N + 1)]     # gaps g_1..g_{N+1}
bits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(N + 1)]  # halved parity
real_mags = [((P[i + 1] - P[i]) // 2) // 2 for i in range(N + 1)]


def evaluate(seq, label):
    """seq[0..N]: 2-then-odds row.  Returns min nu2/w over n in [17,N] and
    first violation n of nu2 >= w/2."""
    # incremental diagonal
    D = [seq[0]]
    hbits = [((seq[i + 1] - seq[i]) // 2) % 2 for i in range(len(seq) - 1)]
    pref = [0] * (len(hbits) + 1)
    for i, b in enumerate(hbits):
        pref[i + 1] = pref[i] + b
    min_ratio = 1.0; first_viol = None; worst = (0, 0)
    for n in range(1, N + 1):
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
            if n >= 17 and wv > 0:
                r = nu2v / float(wv)
                if r < min_ratio:
                    min_ratio = r; worst = (n, nu2v, wv)
                if nu2v < 0.5 * wv - 1e-12 and first_viol is None:
                    first_viol = n
    print("%-28s min nu2/w = %.4f at %s  first-violation=%s"
          % (label, min_ratio, worst, first_viol))
    return min_ratio, first_viol


def build_seq(gaps_list):
    seq = [2]
    for g in gaps_list:
        seq.append(seq[-1] + g)
    return seq


# V0: real
evaluate(build_seq(gaps[:N]), "V0 real primes")

# V1: real bits, minimal gaps (gap = 2+2*bit so halved parity = bit)
seq1 = [2, 3]
for b in bits[1:N]:
    seq1.append(seq1[-1] + 2 + 2 * b)
evaluate(seq1, "V1 real bits, gaps 2+2b")

# V2: real bits shuffled, real magnitudes
rng = random.Random(42)
bits_sh = bits[:]
rng.shuffle(bits_sh)
gaps2 = [2 * (2 * b + 2 * m) for b, m in zip(bits_sh, real_mags)]
evaluate(build_seq([1] + gaps2[1:]), "V2 shuffled bits, real mags")

# V3: random bits, real magnitudes (shuffle magnitudes instead)
mags_sh = real_mags[:]
rng.shuffle(mags_sh)
gaps3 = [2 * (2 * b + 2 * m) for b, m in zip(bits, mags_sh)]
evaluate(build_seq([1] + gaps3[1:]), "V3 real bits, shuffled mags")

# V5: real bits shifted by one position
bits5 = bits[1:] + bits[:1]
gaps5 = [2 * (2 * b + 2 * m) for b, m in zip(bits5, real_mags)]
evaluate(build_seq([1] + gaps5[1:]), "V5 bits shifted +1, real mags")

# V6: alternating bits 0,1,0,1 with minimal gaps (worst case from earlier)
seq6 = [2, 3]
for j in range(1, N):
    seq6.append(seq6[-1] + 2 + 2 * (j % 2))
evaluate(seq6, "V6 alternating bits, gaps 2+2b")
