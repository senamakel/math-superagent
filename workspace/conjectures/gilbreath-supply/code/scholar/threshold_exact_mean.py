#!/usr/bin/env python3
"""Exact mean of nu2/n over ALL weight-w strings under the fold, and the
threshold ratio.

Scholar verification of the third-pass question (GOAL.md): does the minimum
weight ratio w/n at which linear supply becomes typical tend to 0 or plateau
near 1/8?

The MEAN half of the 'typical' test (mean nu2/n >= 0.40) can be computed
EXACTLY over the whole weight-w layer, with no sampling.  By symmetry, for a
fixed depth d the fold cell T(n,d) is the XOR of the k = 2^popcount(d)
positions in row M_d, and over all weight-w strings

    P_d(w) := P( over weight-w strings, XOR of those k positions is odd )
            = ( C(n,w) - c_w ) / ( 2 C(n,w) ),
            c_w = [z^w] (1-z)^k (1+z)^{n-k}   (coefficient of z^w).

Proof of the parity identity: count weight-w strings with an odd number of
ones in M_d by r = number of ones in M_d, sum_{r odd} C(k,r)C(n-k,w-r).
The alternating total sum_r (-1)^r C(k,r)C(n-k,w-r) = c_w, and
(sum over r with (E-odd)/2 formula):
  #{odd} = ( C(n,w) - c_w ) / 2.
So P_d(w) = #{odd}/C(n,w).  The sweep over weight w and depth d follows.

The mean of nu2/n over the weight-w layer is
    mean_n(w) = (1/(n-2)) * sum_{d=2}^{n-1} P_d(w).

We report, for each n, the minimum weight ratio w/n at which mean_n(w) >= 0.40
AND (the exact) fraction of weight-w strings with nu2/n >= 0.40 is >= 0.5.
The fraction requires the full distribution, which we compute exactly only for
small n (exhaustive) -- for the mean we can go large.  We report mean-threshold
ratio and whether it tends to 0 or plateaus.

Everything exact integer / Fraction arithmetic.
"""

from math import comb
from fractions import Fraction
import sys


def parity_prob_coeff(n, w, k):
    """P_d(w): probability, over weight-w strings, that the XOR of a fixed set
    of k positions is odd.  = ( C(n,w) - c_w ) / ( 2 C(n,w) ),
    c_w = [z^w] (1-z)^k (1+z)^{n-k}."""
    # coefficient of z^w in (1-z)^k (1+z)^{n-k}
    # = sum_j (-1)^j C(k, j) C(n-k, w-j)
    c = 0
    lo = max(0, w - (n - k))
    hi = min(k, w)
    for j in range(lo, hi + 1):
        c += (-1) ** j * comb(k, j) * comb(n - k, w - j)
    C = comb(n, w)
    return Fraction(C - c, 2 * C)


def mean_over_weight(n, w, oracle_popcounts):
    """Exact mean of nu2/n over ALL weight-w strings of length n.
    nu2 = sum_{d=2}^{n-1} [T(n,d)==1];  mean(nu2/n) = (1/n) sum_d P_d(w).
    Uses the canonical d-range [2, n-1] (rows are the depths d)."""
    total = Fraction(0)
    for d in range(2, n):
        k = 1 << bin(d).count("1")          # 2^popcount(d)
        total += parity_prob_coeff(n, w, k)
    return total / n


def popcount_distribution(n):
    """Number of d in [2, n-1] with each popcount.  d in [2,n-1]."""
    from collections import Counter
    c = Counter()
    for d in range(2, n):
        c[bin(d).count("1")] += 1
    return c


def main():
    print("=" * 78)
    print("EXACT mean of nu2/n over all weight-w strings (no sampling)")
    print("formula: P_d(w) = (C(n,w) - [z^w](1-z)^{2^pc}(1+z)^{n-2^pc}) / (2 C(n,w))")
    print("=" * 78)

    # First: validate P_d formula against exhaustive enumeration for small n.
    # brute: sum over all weight-w strings, count nu2 via direct fold.
    # We cross-check mean_n(w) for a few (n,w).
    from lib.supply_fold import s_sos

    def brute_mean(n, w):
        """Exact mean of nu2/n over all weight-w strings, from literal fold."""
        tot = 0
        cnt = 0
        # iterate over subsets of [0,n-1] of weight w
        positions = list(range(n))
        from itertools import combinations
        for ones in combinations(positions, w):
            h = [0] * n
            for j in ones:
                h[j] = 1
            S, c1 = s_sos(n, h)
            # c1 = number of T=1 = nu2
            tot += c1
            cnt += 1
        return Fraction(tot, cnt) / n

    print("\nCross-check mean vs brute (small n, exhaustive):")
    for n, w in [(6, 1), (6, 2), (8, 1), (8, 3), (10, 2), (12, 3)]:
        m = mean_over_weight(n, w, None)
        b = brute_mean(n, w)
        status = "OK" if m == b else "MISMATCH"
        print(f"  n={n} w={w}: formula={float(m):.4f} brute={float(b):.4f} {status}")

    print("\n" + "=" * 78)
    print("EXACT mean-threshold: min w/n where mean nu2/n >= 0.40")
    print("(the mean half of 'typical'; fraction half needs distribution)")
    print("=" * 78)
    print(f"{'n':>6} {'first w':>8} {'w/n':>8}")
    for n in [8, 10, 12, 14, 16, 32, 64, 128, 256, 512, 1024]:
        # find min w with mean >= 0.40
        first = None
        for w in range(1, n):
            m = mean_over_weight(n, w, None)
            if m >= Fraction(4, 10):
                first = w
                break
        if first is not None:
            print(f"{n:>6} {first:>8} {first/n:>8.3f}")
        else:
            print(f"{n:>6} {'(none)':>8}")

    print("\n" + "=" * 78)
    print("Mean nu2/n at selected weight ratios, showing the trend")
    print("=" * 78)
    print(f"{'n':>6} {'w/n=0.05':>10} {'0.10':>10} {'0.125':>10} {'0.15':>10} {'0.20':>10} {'0.25':>10} {'0.30':>10}")
    for n in [32, 64, 128, 256, 512, 1024]:
        row = []
        for ratio in [0.05, 0.10, 0.125, 0.15, 0.20, 0.25, 0.30]:
            w = int(round(ratio * n))
            w = max(1, min(w, n - 1))
            m = mean_over_weight(n, w, None)
            row.append(f"{float(m):.3f}")
        print(f"{n:>6} " + " ".join(f"{x:>10}" for x in row))


if __name__ == "__main__":
    main()
