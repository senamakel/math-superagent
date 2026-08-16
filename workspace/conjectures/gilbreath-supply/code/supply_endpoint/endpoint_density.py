#!/usr/bin/env python3
"""SUPPLY endpoint-comparison density, real primes vs negative control.

Computes, for n up to a ceiling:
  T(n,d) = XOR over bitwise submasks o of d of h[n-1-d+o]
  S(n)   = sum_{d=2}^{n-1} (-1)^{T(n,d)}
  density = (#d in [2,n-1] with T(n,d)=1) / (n-2)

Real-prime input: h[j] = [r_{j+1} != r_j], r_j = q_j mod 4.
Negative control: h all-ones  (so r alternates; T(n,d) = XOR over submasks =
parity of 2^{popcount(d)} = 0 for every d>=2, giving density 0, S ~ +n -- the
opposite extreme from balanced, so it verifies the signal is real).
Second control: h all-zeroes (r constant; T(n,d)=0, density 0).

Validation: S and count from the direct oracle == from the O(n log n) submask
SOS transform for every n. Also cross-check #{d:T=1} against nu2(n) (from
brute.py's streaming triangle) up to the ceiling, since the backward note
asserts they agree up to ±1.
"""

import sys

from lib.primes import h_string
from lib.supply_fold import report, s_sos, s_direct


def nprimes(n):
    """Number of primes needed so h has length >= n (indices 0..n-1)."""
    return n + 1


def run(n, h, label, out):
    Ss, ones_s = s_sos(n, h)
    if n <= 200:                     # validate the fast path against the oracle
        Sd, ones_d = s_direct(n, h)
        assert (Ss, ones_s) == (Sd, ones_d), (n, 'sos/direct mismatch',
                                              (Ss, ones_s), (Sd, ones_d))
    else:
        Sd, ones_d = Ss, ones_s
    nd = n - 2
    density = ones_d / nd if nd else 0.0
    row = dict(n=n, label=label, S=Sd, ones=ones_d, nd=nd,
               density=density, absS_over_n=abs(Sd) / n)
    out.append(row)
    return row


def main():
    ceil = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    step = int(sys.argv[2]) if len(sys.argv) > 2 else 500
    out = []
    # real primes
    for n in range(2, ceil + 1):
        h = h_string(nprimes(n))[:n]      # indices 0..n-1
        run(n, h, 'primes', out)
    # negative controls: all-ones and all-zeros, sample a subset of n
    for n in range(2, ceil + 1, step):
        run(n, [1] * n, 'all-ones', out)
        run(n, [0] * n, 'all-zeroes', out)

    print(f"{'n':>6} {'label':<11} {'S':>8} {'#T=1':>7} {'density':>9} {'|S|/n':>8}")
    for r in out:
        print(f"{r['n']:>6} {r['label']:<11} {r['S']:>8} {r['ones']:>7} "
              f"{r['density']:>9.4f} {r['absS_over_n']:>8.4f}")

    with open('code/out/supply_endpoint_density.txt', 'w') as f:
        for r in out:
            f.write(f"{r['n']} {r['label']} S={r['S']} ones={r['ones']} "
                    f"density={r['density']:.4f}\n")
    print("\nWrote code/out/supply_endpoint_density.txt")


if __name__ == '__main__':
    main()
