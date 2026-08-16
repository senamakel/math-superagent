#!/usr/bin/env python3
"""Positive control for the per-scale drift measurement.

Does mean S_0/n (g=0 adjacent switch scale) DETECT a real switch-density drift
in h?  Construct strings with a strong mod-4 switch bias and see if the fold's
per-scale drift picks it up.

h is the switch indicator of a 2-valued residue string r (values e.g. 1/3).
Switch density = P(r changes).  A bias between 1->3 and 3->1 rates makes the
switch process asymmetric.  We build r with:
  * 3->1 transition with probability p31
  * 1->3 transition with probability p13
and measure mean S_0/n.
If it's ~0 even with a strong switch bias, then the fold's g=0 drift is
decoupled from switch density structurally (a real finding for goal 5).  If it
tracks the bias, the measurement is sensitive and the earlier prime S_0~0
really means "no switch-density drift in the primes' fold".
"""
import random
import numpy as np


def trailing_ones(d):
    k = 0
    while d & 1:
        k += 1
        d >>= 1
    return k


def residue_string(n, p13, p31, seed):
    # r[0]=1; transition 1->3 with p13, 3->1 with p31
    rnd = random.Random(seed)
    r = [1]
    for _ in range(n - 1):
        if r[-1] == 1:
            r.append(3 if rnd.random() < p13 else 1)
        else:
            r.append(1 if rnd.random() < p31 else 3)
    h = [1 if r[j + 1] != r[j] else 0 for j in range(n - 1)]
    return h, r


def mean_S0(h, N, step):
    from collections import defaultdict
    acc = 0.0
    ncnt = 0
    tot = 0.0
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
        acc += Sg[0] / n
        ncnt += 1
    return acc / ncnt, tot / ncnt, ncnt


def main():
    # balanced switch (p13=p31=0.5): symmetric, should have S0~0
    for name, p13, p31 in [("balanced .5/.5", 0.5, 0.5),
                           ("weak bias .6/.4", 0.6, 0.4),
                           ("strong bias .8/.2", 0.8, 0.2),
                           ("extreme .9/.1", 0.9, 0.1)]:
        h, r = residue_string(9001, p13, p31, 42)
        m0, mall, ncnt = mean_S0(h, 9000, 400)
        ones = sum(h) / len(h)
        print(f"{name:22s} 1-density={ones:.3f}  mean S_0/n={m0:+.5f}  "
              f"mean S/n={mall:+.5f}  ({ncnt} windows)")


if __name__ == "__main__":
    main()
