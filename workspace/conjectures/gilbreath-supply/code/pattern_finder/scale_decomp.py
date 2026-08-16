#!/usr/bin/env python3
"""Per-dyadic-scale decomposition of S(n).

S(n) = sum_{d=2}^{n-1} (-1)^{T(n,d)}, and each depth d has a scale
g(d) = trailing-ones(d) = v2(d+1). Group:

    S_g(n) = sum_{d in [2,n-1], trailing_ones(d)=g} eps_d(n),  eps=(-1)^T.

The martingale note claims the g=0 (adjacent-residue) scale carries a
non-trivial fraction of the mass (its drift is switch density).  We measure
the per-scale mass distribution and its growth for the prime string, to see
whether the higher scales (which are NOT switch density) are already still.

Uses the direct submask-XOR oracle (fold). Exact.
"""
import numpy as np
from lib.primes import h_string
from lib.direct_fold import nu2_xor_zeta  # reuse verification only
from lib.supply_fold import s_sos


def trailing_ones(d):
    # number of trailing 1-bits of d == v2(d+1)
    k = 0
    while d & 1:
        k += 1
        d >>= 1
    return k


def T_fold(n, h):
    """Return T(n,d) for d in [2,n-1] via s_sos's S=sum(-1)^T? Not directly.
    Use per-depth direct: XOR over submasks."""
    # direct submask XOR per depth (oracle)
    out = {}
    for d in range(2, n):
        x = 0
        o = d
        base = n - 1 - d
        while True:
            x ^= h[base + o]
            if o == 0:
                break
            o = (o - 1) & d
        out[d] = x
    return out


def main():
    N = 4001
    h = h_string(N + 1)
    # per-scale mass at a selection of n
    for n in [64, 128, 256, 512, 1024, 2000, 3000]:
        T = T_fold(n, h)
        from collections import defaultdict
        Sg = defaultdict(int)
        counts = defaultdict(int)
        for d in range(2, n):
            g = trailing_ones(d)
            Sg[g] += (1 if T[d] == 0 else -1)
            counts[g] += 1
        gmax = max(Sg)
        total = sum(abs(v) for v in Sg.values())
        print(f"n={n}: total|Sg|={total}")
        for g in sorted(Sg):
            print(f"   g={g}: S_g={Sg[g]:+5d}  count={counts[g]:4d}  |S_g|/n={abs(Sg[g])/n:.4f}")


if __name__ == "__main__":
    main()
