#!/usr/bin/env python3
"""Is the g=0 variance bound fold-structural (independent of h)?

Count of g=0 depths in [2,n-1] = # d with v2(d+1)=0 = # odd d = ceil((n-2)/2).
For iid Bernoulli(p) h, S_0 = sum of ~n/2 independent ±1 => E[S_0^2] ~ n/2.
Test: for random h of various p, is mean S_0^2/n ~ 0.5 (structure) and does it
match the primes' 0.52?  If yes, the g=0 variance is PURE COUNT, no arithmetic.
"""
import random
import numpy as np


def trailing_ones(d):
    k = 0
    while d & 1:
        k += 1
        d >>= 1
    return k


def s0_var(h, N, step, start):
    tot0 = 0.0
    ncnt = 0
    for n in range(start, N, step):
        S0 = 0
        for d in range(2, n):
            if trailing_ones(d) == 0:
                x = 0
                o = d
                base = n - 1 - d
                while True:
                    x ^= h[base + o]
                    if o == 0:
                        break
                    o = (o - 1) & d
                S0 += (1 if x == 0 else -1)
        tot0 += S0 * S0 / n
        ncnt += 1
    return tot0 / ncnt, ncnt


def main():
    N = 6000
    step = 300
    start = 900
    print(f"n={start}..{N} step{step}: mean S_0^2/n for various inputs")
    for name, h in [("primes", None)]:
        pass
    from lib.primes import h_string
    hp = h_string(N + 1)
    m, c = s0_var(hp, N, step, start)
    print(f"  PRIMES:       mean S_0^2/n = {m:.4f}  ({c} windows)")

    for seed, p in [(1, 0.5), (2, 0.585), (3, 0.3)]:
        random.seed(seed)
        h = [1 if random.random() < p else 0 for _ in range(N + 1)]
        m, c = s0_var(h, N, step, start)
        print(f"  random p={p}:  mean S_0^2/n = {m:.4f}  ({c} windows)")


if __name__ == "__main__":
    main()
