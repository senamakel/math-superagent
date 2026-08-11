#!/usr/bin/env python3
"""Corrected race engine for PE 597 (reference: brute.py).

Fixes the multi-bump overwrite bug: instead of remembering a single
bumped_by[k], it records EVERY bump edge j->k and computes `above` by graph
reachability (a boat m is below i iff there is a bump chain i -> ... -> m).

API same as brute.simulate_order / parity_of_new_order.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brute import parity_of_new_order

def simulate_order(n, L, speeds):
    state = [0]*n            # 0 ROWING, 1 FINISHED, 2 OUT
    pos = [40.0*j for j in range(n)]
    edges = [[] for _ in range(n)]          # bump edges: edges[j].append(k)
    while True:
        rowing = [j for j in range(n) if state[j] == 0]
        if not rowing:
            break
        best = None
        for j in rowing:
            vj = speeds[j]
            ft = (L - pos[j]) / vj
            k = None
            for kk in range(j+1, n):
                if state[kk] == 0:
                    k = kk; break
            cands = [(ft,'F',j,None)]
            if k is not None:
                vk = speeds[k]
                if vj > vk:
                    cands.append(((pos[k]-pos[j])/(vj-vk),'C',j,k))
            for c in cands:
                if c[0] == float('inf'): continue
                if best is None or c[0] < best[0] - 1e-15:
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
        seen = set([i])
        stack = [i]
        while stack:
            u = stack.pop()
            for w in edges[u]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        above[i] = seen - {i}
    return above

def outcome_parity(n, L, speeds):
    above = simulate_order(n, L, speeds)
    par, _ = parity_of_new_order(n, above)
    return par
