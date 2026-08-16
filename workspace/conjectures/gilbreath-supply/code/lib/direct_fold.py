#!/usr/bin/env python3
"""Direct submask-XOR route to nu2(n) = wt(Phi_n h) for the SUPPLY fold:

    T(n,d) = XOR over bitwise submasks s of d of h[n-1-s],   d in [2, n-1],
    nu2(n) = #{ d in [2, n-1] : T(n,d) = 1 }.

Two implementations, both exact, both different code paths from
lib.supply_fold.s_sos (the +-1 submask-PRODUCT zeta):

  nu2_literal_direct -- literal per-submask expansion (the from-scratch
                        oracle; the loop is the definition itself);
  nu2_xor_zeta       -- subset-XOR zeta transform in the 0/1 algebra
                        (numpy, uint8), the closed form of the SAME direct
                        submask-XOR: with b_s = h[n-1-s], g[x] ^= g[x ^ bit]
                        over all bits computes g[d] = XOR_{s subseteq d} b_s
                        for every d in O(n log n) instead of literal
                        expansion.  Algebraically different from s_sos
                        (XOR of bits vs product of +-1).

Verified equal to s_sos / s_direct on n = 2..200, and full-prefix equal to
s_sos to N=40000 by code/verif/fair_variance_independent_verify.py (values
also saved to code/out/nu2_primes_xor_40000.txt).  Exact; display only.

Complexity: literal per-n O(sum_{d<n} 2^popcount(d)) = O(n^{log_2 3})
(oracle); XOR-zeta per-n O(n log n).   Memory O(n) (XOR-zeta allocates one
power-of-two array per call).
"""

import numpy as np


def nu2_literal_direct(n, h):
    """nu2(n) by literal expansion of the direct submask-XOR decomposition.

    For each d in [2, n-1], XOR h[n-1-d+o] over all bitwise submasks o of d
    (enumerated by the standard (o-1)&d descent, which visits exactly the
    submasks), count the T=1 cells.  h is a 0/1 list of length >= n.
    Exact.  Oracle cost O(n^{log_2 3}) per n.
    """
    ones = 0
    for d in range(2, n):
        x = 0
        o = d
        base = n - 1 - d
        while True:
            x ^= h[base + o]
            if o == 0:
                break
            o = (o - 1) & d
        ones += x
    return ones


def nu2_xor_zeta(n, harr):
    """nu2(n) by the subset-XOR zeta of the direct submask-XOR decomposition.

    b_s = h[n-1-s] for s = 0..n-1, padded with 0s to the next power of two;
    g[d] = XOR_{s subseteq d} b_s via g[x] ^= g[x ^ bit] over all bits
    (vectorised with numpy on disjoint half-views), and
    nu2(n) = sum_{d=2}^{n-1} g[d].

    harr: numpy uint8 array of the h bits, length >= n.  Exact integer
    arithmetic (XOR has no carries).  O(n log n) time, O(2^ceil(log2 n)) space.
    """
    size = 1 << (n - 1).bit_length()
    g = np.zeros(size, dtype=np.uint8)
    g[:n] = harr[n - 1::-1]
    stride = 1
    while stride < size:
        v = g.reshape(-1, stride * 2)
        v[:, stride:] ^= v[:, :stride]
        stride <<= 1
    return int(g[2:n].sum())