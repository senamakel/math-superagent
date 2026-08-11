#!/usr/bin/env python3
"""Naive but obviously-correct engine for PE 597 (Torpids).

Boats j=0..n-1 (0 = lowest/downstream at pos 0, gap 40, finish at L).
Speeds v_j ~ Exp(1) iid. Boat rows at constant speed until it either reaches
the finish (FINISHED) or catches the nearest ROWING boat ahead (bump; the
bumper stops and becomes OUT/transparent). A bumped boat continues.

New ordering (ascending place, lowest first): the table in the statement lists
the new order lowest-placed first, matching the starting order [A,B,C] with A
lowest. For i<j, i is placed HIGHER than j iff there is a bump chain i->...->j
(direct or transitive). Incomparable pairs keep starting relative order.

Parity = sign of the permutation mapping the starting ascending listing
[0,1,...,n-1] to the new ascending listing.
"""
import math

def simulate_order(n, L, speeds):
    """Return above: above[i] = set of boats placed below i via bump chains."""
    state = [0]*n            # 0 ROWING, 1 FINISHED, 2 OUT
    pos = [40.0*j for j in range(n)]
    bumped_by = [-1]*n
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
            bumped_by[k] = j
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
    """Return (parity, new_ascending) where new_ascending lists boats lowest
    place first. above[i] = boats placed below i."""
    # ascending comparator: a before b iff a placed lower than b:
    #   b above a  OR (incomparable and a<b)
    def lower(a, b):      # is a placed lower than b?
        if a in above and b in above[a]:   # b above a -> a lower
            return True
        if b in above and a in above[b]:   # a above b -> b lower, a not
            return False
        # incomparable -> keep start order a<b => a lower
        return a < b
    order = [0]
    for a in range(1, n):
        idx = 0
        while idx < len(order):
            b = order[idx]
            if lower(a, b):
                break
            idx += 1
        order.insert(idx, a)
    # start ascending = [0,1,...,n-1]
    pos_in_new = {boat:i for i,boat in enumerate(order)}
    new_perm = [pos_in_new[boat] for boat in range(n)]
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
