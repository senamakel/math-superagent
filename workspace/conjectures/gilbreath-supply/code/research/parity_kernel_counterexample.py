#!/usr/bin/env python3
"""Check the parity-shadow counterexample: are the kernel vectors spread?

even-alt = indicator of even indices. If S' (reflected even positions) occupies
~half of every popcount layer of the m-cube, then it is a 'spread' set.

Also verify nu2(even-alt) = 0 (it is in the kernel) directly, and nu2 of a
generic random subset ~ (n-2)/2 by the fair binomial law.
"""
from collections import defaultdict
from lib.supply_fold import s_sos


def popcount(v):
    return bin(v).count('1')


def layer_density(m, S):
    """For each popcount p in 0..m, fraction of layer-p elements in S."""
    per_p = defaultdict(lambda: [0, 0])
    for j in range(1 << m):
        p = popcount(j)
        per_p[p][1] += 1
        if j in S:
            per_p[p][0] += 1
    out = {}
    for p in range(m + 1):
        have, tot = per_p[p]
        out[p] = (have, tot, (have / tot) if tot else None)
    return out


m = 4
n = 1 << m
# even-alt as set of indices where h[j]=1: even indices 0,2,...
even_alt = {j for j in range(n) if j % 2 == 0}
print("even-alt layer occupancy (m=4):")
for p, (have, tot, frac) in layer_density(m, even_alt).items():
    print(f"  pc={p}: {have}/{tot} = {frac:.2f}")

# nu2 of even-alt via fold
h = [1 if j in even_alt else 0 for j in range(n)]
_, ones = s_sos(n, h)
print("nu2(even-alt) at n=16 =", ones, "(in kernel -> should be 0)")

# generic random subset (spread) parity shadow
import random
random.seed(1)
for dens in (0.3, 0.5, 0.7):
    S = {j for j in range(n) if random.random() < dens}
    hh = [1 if j in S else 0 for j in range(n)]
    _, o = s_sos(n, hh)
    print(f"random density {dens}: nu2 = {o} (out of n-2={n-2})")
