#!/usr/bin/env python3
"""Quick focused check: exact-MEAN threshold at 64/128/256 and BRUTE FRACTION
at the plateau point, small enough to run fast."""
from math import comb
from fractions import Fraction
from collections import Counter


def popcount_distribution(n):
    c = Counter()
    for d in range(2, n):
        c[d.bit_count()] += 1
    return c


def mean_exact(n, w, Np):
    total = C(n, w)
    s = Fraction(0)
    for p, cnt in Np:
        k = 1 << p
        lo = max(0, w - (n - k))
        hi = min(k, w)
        odd = 0
        for r in range(lo, hi + 1):
            if r & 1:
                odd += C(k, r) * C(n - k, w - r)
        s += cnt * Fraction(odd, total)
    return s / n


def C(n, k):
    return comb(n, k)


def first_w(n, Np, thr=Fraction(2, 5)):
    for w in range(1, n):
        if mean_exact(n, w, Np) >= thr:
            return w
    return None


def sample_frac(n, w, trials=5000, seed=11):
    import random
    from lib.supply_fold import s_sos
    rng = random.Random(seed)
    frac = 0
    for _ in range(trials):
        ones = rng.sample(range(n), w)
        h = [0] * n
        for j in ones:
            h[j] = 1
        _, c1 = s_sos(n, h)
        if c1 / n >= 0.40:
            frac += 1
    return frac / trials


for n in [64, 128, 256]:
    Np = [(p, c) for p, c in sorted(popcount_distribution(n).items())]
    fw = first_w(n, Np)
    print(f"n={n} exact-mean threshold first w={fw} w/n={fw/n:.4f}")

print("fraction brute at past-plateau points:")
for n, w in [(64, 8), (128, 16), (128, 10), (128, 6), (64, 4), (64, 3)]:
    f = sample_frac(n, w)
    print(f"  n={n} w={w} w/n={w/n:.3f} frac={f:.4f}")
