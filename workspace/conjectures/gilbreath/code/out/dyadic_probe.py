#!/usr/bin/env python3
"""Probe the dyadic collapse: for h periodic of period 2^k, examine the fold
output sequence y_c (the subset-zeta transform of the reflected window u of h)
and how many 1s it has up to m.  Identifies the structural pattern to prove."""
import sys

def submasks(c):
    """all i with (i & c) == i"""
    out = []
    i = c
    while True:
        out.append(i)
        if i == 0:
            break
        i = (i - 1) & c
    return out

def y_seq(h, m):
    """h abstract input indexed 0..m-1 (columns 2..n-1).  Returns outputs
    y_c for c=1..m  (matching fold_weight_h: c=k-1 in 1..m)."""
    N = m - 1
    res = []
    for c in range(1, m + 1):
        s = 0
        for i in submasks(c):
            pos = N - c + i
            s ^= h[pos]
        res.append(s)
    return res

def periodic_h(period_marker, m):
    """h[j] = 1 if bit at j of a period is 1.  period given as binary string,
    word[0] applies to j=0."""
    L = len(period_marker)
    return [int(period_marker[j % L]) for j in range(m)]

def nu2(period_marker, m):
    return sum(y_seq(periodic_h(period_marker, m), m))

for period_marker in ["0","1","01","10","0011","0110","00001111"]:
    print(period_marker, "->", [nu2(period_marker, m) for m in [20,40,80,200,400,800]])

print()
# examine the actual y sequence for period 2 (01) at m=32
for period_marker in ["01","10","0011","00001111"]:
    m = 40
    y = y_seq(periodic_h(period_marker, m), m)
    print(period_marker, "y_c (c=1..40):", y)
    print("  positions of 1:", [i+1 for i,v in enumerate(y) if v])
