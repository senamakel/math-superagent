#!/usr/bin/env python3
"""Empirical status of the averaged form of SUPPLY (G-mean-linear, G-var-vanishing).

Question: is (1/N) * sum_{n<=N} nu2(n)/n bounded below by an absolute c0 > 0?

The operative object is the fold weight
    nu2(n) = #{ d in [2,n-1] : T(n,d) = 1 },  T(n,d) = XOR_{o submask of d} h[n-1-d+o],
    h[j] = ((q_{j+1}-q_j)/2) mod 2  (prime gap-parity string),
computed exactly by the submask-product SOS transform (O(n log n) per n),
streamed one n at a time (never materialising a triangle).

Re-grounding (task 1): for n <= 60 compute nu2 two ways — (a) the literal
geometric suffix and (b) the fold — and report where they agree and where the
convention differs. The literal gives 0 for every n (bottom cell always 1); the
fold is what matches problem.md's measured 0.4933 at n=4000 (SOS: 1976/4000 =
0.4940).

Negative controls (task 3): all-ones h and Thue-Morse h through the SAME fold
formula; expectation is their means decay to 0, so the prime signal is specific
to the prime h.

This is a measurement, not a proof.
"""

import argparse
from fractions import Fraction

from lib.primes import prime_gap_parity
from lib.nu2 import (fold_nu2, literal_suffix_nu2, stream_stats)


def frac_float(x):
    return float(x)


def allones_h(N):
    return [1] * (N + 2)


def thue_h(N):
    h = []
    for j in range(N + 2):
        h.append(bin(j).count('1') % 2)
    return h


def primes_upto_index(n):
    import sympy
    ps = list(sympy.ntheory.generate.primerange(0, sympy.prime(n) + 1))
    return ps[:n]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--N', type=int, default=4000, help='ceiling')
    ap.add_argument('--check', nargs='*', type=int, default=None,
                    help='checkpoint N values for the means (list)')
    args = ap.parse_args()
    N = args.N
    checkpoints = args.check if args.check else [100, 400, 1000, 2000, 4000]
    checkpoints = [c for c in checkpoints if c <= N]
    if N not in checkpoints:
        checkpoints.append(N)

    print(f'Ceiling N = {N}. Streamed one n at a time; exact Fractions.')
    print()

    # ---------- Task 1: re-ground the linearisation on small n ----------
    print('=== Task 1: re-grounding the linearisation, n = 3..60 ===')
    print('(a) literal geometric suffix vs (b) fold wt(Phi_n h)')
    n = 60
    ps = primes_upto_index(n)
    h = prime_gap_parity(n)[:n]          # need h up to index n-1
    lit_diffs = 0
    for m in range(3, 61):
        lit, _ = literal_suffix_nu2(m, primes_upto_index(m))
        fold = fold_nu2(m, h)
        if lit != fold:
            lit_diffs += 1
    print(f'for n = 3..60: literal==fold in {60 - lit_diffs}/58 cases; '
          f'differ by convention in {lit_diffs} cases (literal is identically 0:')
    lit, _ = literal_suffix_nu2(10, primes_upto_index(10))
    print(f'   literal_suffix_nu2(10)={lit}, fold fold_nu2(10)={fold_nu2(10, h)})')
    print('Fold reproduces the measured object; literal suffix is a degenerate negative control.')
    print()

    # ---------- exact ratio at n = 4000 (the measured anchor) ----------
    h4000 = prime_gap_parity(4001)[:4000]
    v4000 = fold_nu2(4000, h4000)
    print('=== Exact ratio at n = 4000 ===')
    print(f'nu2(4000) = {v4000}   nu2/4000 = {v4000}/4000 = {v4000/4000:.6f}'
          f'   (problem.md measured 0.4933; brute.py 0.4940)')
    print()

    # ---------- Tasks 2 & 3: streamed means + variance ----------
    print('=== Streamed empirical mean mu_N = (1/N) sum nu2(n)/n and variance ===')
    print('N          | primes mu_N  | primes s2_N  | all-ones mu_N | Thue-Morse mu_N')
    fams = {
        'primes': lambda m: prime_gap_parity(m + 1),
        'allones': allones_h,
        'thue': thue_h,
    }
    results = {}
    for label, gen in fams.items():
        cps, (mu, s2), last = stream_stats(N, gen, checkpoints)
        results[label] = (cps, (mu, s2), last)
        if label in ('allones', 'thue'):
            continue
    for c in checkpoints:
        mu_p, s2_p = results['primes'][0][c]
        mu_a, _ = results['allones'][0][c]
        mu_t, _ = results['thue'][0][c]
        print(f'{c:8d} | {frac_float(mu_p):.6f}     | {frac_float(s2_p):.8f} | '
              f'{frac_float(mu_a):.6f}      | {frac_float(mu_t):.6f}')

    print()
    print('=== Final (N) ===')
    mu_p, s2_p = results['primes'][1]
    mu_t, _ = results['thue'][1]
    mu_a, _ = results['allones'][1]
    v, nn = results['primes'][2]
    print(f'primes:   mu_N = {frac_float(mu_p):.6f}, s2_N = {frac_float(s2_p):.8f}')
    print(f'all-ones: mu_N = {frac_float(mu_a):.6f}')
    print(f'Thue-Morse: mu_N = {frac_float(mu_t):.6f}')
    print(f'exact nu2({nn})/{nn} = {v}/{nn} = {v/nn:.6f}')


if __name__ == '__main__':
    main()
