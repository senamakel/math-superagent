#!/usr/bin/env python3
"""Per-dyadic-scale VARIANCE decomposition of S(n) for the prime string.

The key question for goal priority 5 (is SUPPLY equivalent to switch density?):
does the g=0 scale (adjacent mod-4 switch pairs = switch density) dominate
E[S(n)^2], or do the higher scales (which are variance/correlation statements,
NOT the open switch-density mean) carry the mass?

We compute, for each n, S(n) grouped by scale g(d)=trailing_ones(d):
    S_g(n) = sum_{d in [2,n-1], g(d)=g} (-1)^{T(n,d)}
and accumulate mean S_g^2 / n across a wide window, plus cross-correlations.

If sum_g E[S_g^2]/n ~ 1 with g=0 contributing a large fixed fraction, the
switch-density barrier dominates the variance.  If the higher scales dominate,
a variance bound not touching switch density may suffice.
"""
import json
import numpy as np


def trailing_ones(d):
    k = 0
    while d & 1:
        k += 1
        d >>= 1
    return k


def Sg_decomp(n, T):
    """T: dict d->T(n,d) for d in [2,n-1].  Return dict g -> (S_g, count)."""
    from collections import defaultdict
    Sg = defaultdict(int)
    cnt = defaultdict(int)
    for d in range(2, n):
        g = trailing_ones(d)
        Sg[g] += (1 if T[d] == 0 else -1)
        cnt[g] += 1
    return Sg, cnt


def T_fold(n, h):
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
    from lib.primes import h_string
    N = 9000
    h = h_string(N + 1)
    # accumulate E[S_g^2]/n and cross
    meanSg2 = {}      # g -> sum S_g^2/n
    count_n = 0
    # total E[S^2]/n accumulator
    totS2 = 0.0
    for n in range(2000, N, 500):
        T = T_fold(n, h)
        Sg, cnt = Sg_decomp(n, T)
        Sg[0] = Sg.get(0, 0)  # ensure
        S = sum(Sg.values())
        totS2 += S * S / n
        for g in Sg:
            meanSg2[g] = meanSg2.get(g, 0) + Sg[g] * Sg[g] / n
        count_n += 1
    print(f"windows n=2000..{N-500} step500: {count_n} windows")
    print(f"mean total S^2/n over windows = {totS2/count_n:.4f}")
    totg = sum(meanSg2.values())
    print(f"sum_g mean S_g^2/n = {totg/count_n:.4f}")
    print(f"S_g variance share (mean S_g^2/n / total):")
    for g in sorted(meanSg2):
        share = meanSg2[g] / totg if totg else 0
        print(f"   g={g:2d}: mean S_g^2/n = {meanSg2[g]/count_n:8.4f}  share={share*100:5.1f}%")


if __name__ == "__main__":
    main()
