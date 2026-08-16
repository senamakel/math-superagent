#!/usr/bin/env python3
"""Independent tail check for the third-pass threshold question.

GOAL.md's one unfinished computation: does the minimum weight ratio w/n at
which linear supply becomes typical tend to 0, or plateau near 1/8?

Two remarks this script checks:
(1) The exact-MEAN threshold theta_mean(n)=min{w: mean_n(w)>=0.40} is proved
    value-per-n by the scholar route (no sampling).  The on-disk capture
    threshold_limit_exact.txt extends it past 0.125: 0.0625@256, 0.0469@512,
    0.0342@1024, 0.0254@2048, 0.0188@4096.
(2) The pass-3 'plateau at 1/8' conclusion used the SAMPLED fraction column at
    n=64,128 (PART 2 of linear_supply_by_weight.txt: 0.125@64, 0.125@128).
    The fraction at n=256/512 (threshold_limit_exact.txt PART B) sits well
    below: ratio 0.05-0.075 has frac>=0.40 already ~0.53-0.75.

This script recomputes the exact-MEAN crossing a few values and brute-checks
the FRACTION hypothesis at modest n to see whether 0.125@64/128 was a small-n
artifact.
"""
from math import comb
from fractions import Fraction
from collections import Counter


def popcount_distribution(n):
    c = Counter()
    for d in range(2, n):
        c[d.bit_count()] += 1
    return c


def C(n, k):
    return comb(n, k)


def mean_exact(n, w, Np):
    """mean_n(w) = (1/n) sum_p N_p * P_{k_p}(w), k_p = 2^p, direct odd-count."""
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


def first_w(n, Np, thr=Fraction(2, 5)):
    for w in range(1, n):
        if mean_exact(n, w, Np) >= thr:
            return w
    return None


def sample_frac(n, w, trials=4000, seed=7):
    """Brute: sample random weight-w strings, fraction with nu2/n>=0.40."""
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


def main():
    print("=" * 78)
    print("sequence = weight-w binary strings over F2^n")
    print("oracle   = exact grouped odd-count for the mean; lib.supply_fold.s_sos for fraction")
    print("=" * 78)

    ns = [64, 128, 256, 512, 1024, 2048, 4096, 8192]
    print("exact-MEAN crossing theta_mean(n)=min{w/n: mean_n(w)>=0.40}:")
    rows = []
    for n in ns:
        Np = [(p, c) for p, c in sorted(popcount_distribution(n).items())]
        fw = first_w(n, Np)
        rows.append((n, fw))
        print(f"  n={n:>6}  first w={fw}  w/n={fw/n:.6f}" if fw else f"  n={n:>6} (none)")

    print("\nBRUTE FRACTION check at the claimed 0.125 plateau point and below:")
    tests = [(64, 8), (64, 6), (64, 4), (128, 16), (128, 10), (128, 8)]
    for n, w in tests:
        f = sample_frac(n, w)
        print(f"  n={n} w={w} (w/n={w/n:.3f}): frac(nu2/n>=0.40) = {f:.4f}")

    # log-log slope of the exact-mean theta
    import math
    tail = [r for r in rows if r[1] is not None and r[0] >= 256]
    xs = [math.log(n) for n, _ in tail]
    ys = [math.log(w / n) for n, w in tail]
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    print("\nlog(theta) vs log(n) tail slope (n>=256):", round(b, 4))
    print("  b < 0 -> theta -> 0; b == 0 -> plateau.")


if __name__ == "__main__":
    main()
