#!/usr/bin/env python3
"""Exact (rational) race dynamics for PE 597. Speeds may be exact Rationals,
giving exact event times and comparisons; parity classes then partition the
speed simplex exactly for a given parametrized family. Used both for the
oracle (sampled rational speeds) and for exact cell integration.

API mirrors brute.py but on Fractions.
"""
from fractions import Fraction as F
from brute import parity_of_new_order

def simulate_order_exact(n, L, speeds):
    """speeds: list of Fraction (or convertible). L: int/Fraction.
    Returns `above` sets like brute.simulate_order, but every comparison and
    position update is exact."""
    L = F(L)
    state = [0]*n
    pos = [F(40)*j for j in range(n)]
    edges = [[] for _ in range(n)]
    while True:
        rowing = [j for j in range(n) if state[j] == 0]
        if not rowing:
            break
        best = None
        for j in rowing:
            vj = F(speeds[j])
            ft = (L - pos[j]) / vj
            k = None
            for kk in range(j+1, n):
                if state[kk] == 0:
                    k = kk; break
            cands = [(ft,'F',j,None)]
            if k is not None:
                vk = F(speeds[k])
                if vj > vk:
                    cands.append(((pos[k]-pos[j])/(vj-vk),'C',j,k))
            for c in cands:
                if best is None or c[0] < best[0]:
                    best = c
        t, kind, j, k = best
        if kind == 'F':
            state[j] = 1; pos[j] = L
        else:
            state[j] = 2
            pos[j] = pos[k]
            edges[j].append(k)
    above = [set() for _ in range(n)]
    for i in range(n):
        seen = {i}
        stack = [i]
        while stack:
            u = stack.pop()
            for w in edges[u]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        above[i] = seen - {i}
    return above

def outcome_parity_exact(n, L, speeds):
    above = simulate_order_exact(n, L, speeds)
    par, _ = parity_of_new_order(n, above)
    return par