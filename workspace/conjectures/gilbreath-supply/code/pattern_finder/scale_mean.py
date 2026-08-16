#!/usr/bin/env python3
"""Per-scale MEAN (drift) of S_g(n) for primes vs random h.

E[S_g(n)] is the drift at scale g.  g=0 = adjacent mod-4 switch pairs.
Question for goal priority 5: does E[S_0(n)] for the primes carry the
switch-density mean signal, or is S_0 pure variance noise (mean 0)?

We average S_g(n)/n over many windows and compare primes vs random balanced h.
If primes' E[S_0/n] is consistently nonzero while random is ~0, there is a
prime-specific drift at the switch scale.  If both are ~0 (variance-dominated),
the fold's g=0 weight is noise, NOT the switch-density mean — a structural fact.
"""
import random
import numpy as np
from lib.primes import h_string


def trailing_ones(d):
    k = 0
    while d & 1:
        k += 1
        d >>= 1
    return k


def run(h, name, N=9000, step=400):
    from collections import defaultdict
    acc = defaultdict(float)   # g -> sum S_g/n
    cnt = defaultdict(int)
    tot = 0.0
    ncnt = 0
    for n in range(500, N, step):
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
        tot += S / n
        ncnt += 1
        for g in Sg:
            acc[g] += Sg[g] / n
            cnt[g] += 1
    print(f"\n=== {name} ({ncnt} windows)")
    print(f"   mean S/n (all scales) = {tot/ncnt:+.4f}")
    for g in sorted(acc):
        print(f"   g={g:2d}: mean S_g/n = {acc[g]/ncnt:+.5f}")


def main():
    N0 = 9000
    run(h_string(N0 + 1), "PRIMES")
    random.seed(7)
    hb = [1 if random.random() < 0.585 else 0 for _ in range(N0 + 1)]
    run(hb, "RANDOM p=0.585")


if __name__ == "__main__":
    main()
