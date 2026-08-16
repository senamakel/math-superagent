#!/usr/bin/env python3
"""Control for scale-variance decomposition: is the g=0-dominant split
fold-generic or prime-specific?

Compare the per-scale variance share for:
  (a) the real prime h
  (b) a RANDOM balanced h (1-density ~0.585)  -- fold-generic
  (c) iid Bernoulli(0.5) h
The switch-density dead end says g=0 mean is the barrier.  If the g=0
VARIANCE share is large and equal for random h, the split is fold structure,
not arithmetic; if primes differ sharply from random, there is a primes-specific
signature.
"""
import random
import json
import numpy as np
from lib.primes import h_string


def trailing_ones(d):
    k = 0
    while d & 1:
        k += 1
        d >>= 1
    return k


def Sg_decomp_accum(n, h, meanSg2, totS2, count_str):
    from collections import defaultdict
    Sg = defaultdict(int)
    for d in range(2, n):
        g = trailing_ones(d)
        x = 0
        o = d
        base = n - 1 - d
        while True:
            x ^= h[base + o]
            if o == 0:
                break
            o = (o - 1) & d
        Sg[g] += (1 if x == 0 else -1)
    S = sum(Sg.values())
    totS2[0] += S * S / n
    for g in Sg:
        meanSg2[g] = meanSg2.get(g, 0) + Sg[g] * Sg[g] / n
    count_str[0] += 1


def run(h, name, N=6000, step=400):
    from collections import defaultdict
    meanSg2 = defaultdict(float)
    totS2 = defaultdict(float)
    cnt = defaultdict(int)
    for n in range(1000, N, step):
        Sg_decomp_accum(n, h, meanSg2, totS2, cnt)
    c = cnt[0]
    tot = totS2[0] / c
    totg = sum(meanSg2.values()) / c
    print(f"\n=== {name}: {c} windows, mean total S^2/n={tot:.4f}")
    g0 = (meanSg2[0] / c) if 0 in meanSg2 else 0
    g1 = (meanSg2[1] / c) if 1 in meanSg2 else 0
    print(f"   g=0 share={100*g0/totg:.1f}%  g=1 share={100*g1/totg:.1f}%  "
          f"g>=2 share={100*(totg-g0-g1)/totg:.1f}%")


def main():
    N = 6000
    hp = h_string(N + 1)
    run(hp, "PRIMES", N)

    random.seed(1)
    # balanced random h ~ 0.585 ones
    hb = [1 if random.random() < 0.585 else 0 for _ in range(N + 1)]
    run(hb, "RANDOM p=0.585", N)

    random.seed(2)
    hi = [1 if random.random() < 0.5 else 0 for _ in range(N + 1)]
    run(hi, "RANDOM p=0.5", N)


if __name__ == "__main__":
    main()
