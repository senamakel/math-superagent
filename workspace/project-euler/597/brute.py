#!/usr/bin/env python3
"""Naive but obviously-correct engine for PE 597 (Torpids).

Boats j=0..n-1 (0 = lowest/downstream at pos 0, gap 40, finish at L).
Speeds v_j ~ Exp(1) iid. Boat rows at constant speed until it either reaches
the finish (FINISHED) or catches the nearest ROWING boat ahead (bump; the
bumper stops and becomes OUT/transparent). A bumped boat continues. A chain
i->j (bump chain, low to high) means i finishes placed above j.

Parity: new order sorted high-to-low; compare with starting order high-to-low
to get the permutation, sign = (-1)^(inversions).

This module exposes pure functions so solution.py and monte_carlo can reuse
them; everything is exact/deterministic given the speeds (floats, but the
event logic uses comparisons).
"""
import math

# ---- deterministic dynamics (given speeds) --------------------------------
def simulate_order(n, L, speeds):
    """Return `above`: above[i] = set of boats j that i is placed above
    (j reachable from i by bump chains, j>i always)."""
    state = [0]*n            # 0 ROWING, 1 FINISHED, 2 OUT
    pos = [40.0*j for j in range(n)]
    bumped_by = [-1]*n       # bumped_by[k] = direct bumper of k (or -1)
    TIE = 0
    while True:
        rowing = [j for j in range(n) if state[j] == 0]
        if not rowing:
            break
        best = None  # (t, 'F', j) or (t,'C',j,k)
        for j in rowing:
            vj = speeds[j]
            ft = (L - pos[j]) / vj
            k = None
            for kk in range(j+1, n):
                if state[kk] == 0:
                    k = kk; break
            if k is None:
                cands = [(ft,'F',j,None)]
            else:
                vk = speeds[k]
                ct = (pos[k]-pos[j])/(vj-vk) if vj > vk else float('inf')
                cands = [(ft,'F',j,None),(ct,'C',j,k)]
            for c in cands:
                if c[0] == float('inf'): continue
                if best is None or c[0] < best[0] - 1e-15:
                    best = c
        t, kind, j, k = best
        if kind == 'F':
            state[j] = 1; pos[j] = L
        else:
            state[j] = 2
            pos[j] = pos[k]   # level at catch
            bumped_by[k] = j
    # build chains
    out_of = [-1]*n
    for k in range(n):
        if bumped_by[k] != -1:
            out_of[bumped_by[k]] = k
    above = [set() for _ in range(n)]
    for i in range(n):
        cur = out_of[i]
        while cur != -1:
            above[i].add(cur)
            cur = out_of[cur]
    return above

def parity_of_new_order(n, above):
    """above[i] = set of boats placed below i by bump chains. Return
    (parity, new_order_high_to_low)."""
    # new order high-to-low: comparator placed_higher(a,b) = b in above[a]
    order = [0]
    for a in range(1, n):
        idx = 0
        while idx < len(order):
            b = order[idx]
            # is a placed higher than b? -> b in above[a]
            if b in above[a]:
                break
            idx += 1
        order.insert(idx, a)
    start_hi = list(range(n-1, -1, -1))
    pos_in_new = {boat:i for i,boat in enumerate(order)}
    new_perm = [pos_in_new[boat] for boat in start_hi]
    inv = 0
    for i in range(n):
        for j in range(i+1, n):
            if new_perm[i] > new_perm[j]:
                inv += 1
    return inv % 2, order

def outcome_parity(n, L, speeds):
    above = simulate_order(n, L, speeds)
    par, _ = parity_of_new_order(n, above)
    return par
