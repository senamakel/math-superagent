#!/usr/bin/env python3
"""Naive but obviously-correct Monte Carlo simulator for PE 597 (Torpids).

Boats j=1..n (j=1 lowest/downstream at pos 0, gap 40, finish at L).
Speeds v_j ~ Exp(1) iid. Each sample run: generate speeds, run the
deterministic chronological dynamics, read off the final permutation parity.

Dynamics per race_spec.md: a boat rows at constant speed until it either
reaches the finish line L (FINISHED) or catches the nearest ROWING boat ahead
(bump; the bumping boat stops = OUT and becomes transparent). A bumped boat
continues. Race ends when no boat is ROWING.
"""
import random, sys
from math import isinf

def simulate(n, L, speeds):
    # states: 0=ROWING, 1=FINISHED(sits at L), 2=OUT(stopped, transparent)
    state = [0]*n
    pos = [40.0*(j) for j in range(n)]      # pos[j] for boat j (0-indexed)
    # record direct bumps: bumped_by[j] = index of boat that directly bumped j (-1 none)
    bumped_by = [-1]*n
    while True:
        rowing = [j for j in range(n) if state[j] == 0]
        if not rowing:
            break
        best_t = None; best_kind = None; best_j = None; best_k = None
        for j in rowing:
            vj = speeds[j]
            ft = (L - pos[j]) / vj
            # nearest rowing boat ahead (larger index still rowing)
            k = None
            for kk in range(j+1, n):
                if state[kk] == 0:
                    k = kk; break
            if k is not None:
                vk = speeds[k]
                if vj > vk:
                    ct = (pos[k] - pos[j]) / (vj - vk)
                else:
                    ct = float('inf')
            else:
                ct = float('inf')
            # event: finish of j, or j catches k
            for (t, kind, jj, kk) in ((ft,'F',j,None),(ct,'C',j,k)):
                if kind=='C' and kk is None: continue
                if t < best_t if best_t is not None else True:
                    best_t = t; best_kind = kind; best_j = jj; best_k = kk
        if best_kind == 'F':
            state[best_j] = 1; pos[best_j] = L
        else:
            # bump: j catches k at best_t
            state[best_j] = 2
            pos[best_j] = pos[best_k] + (speeds[best_k]) * 0  # stopped at level point
            # bumping boat j stops exactly where it caught k:
            pos[best_j] = pos[best_k]  # they are level at catch
            bumped_by[best_k] = best_j
    return state, bumped_by

def final_perm(n, bumped_by):
    # chains: i above j (i<j) iff path i->...->j via bumped_by edges
    # outs[j] = bump target of j (j is bumper)
    out_of = [-1]*n
    for j in range(n):
        for k in range(n):
            if bumped_by[k] == j:
                out_of[j] = k
    # path adjacency via out_of (each boat bumps at most one)
    # above[j] = set of boats i that are above j
    above = [set() for _ in range(n)]
    for i in range(n):
        cur = out_of[i]
        while cur != -1:
            above[i].add(cur)
            cur = out_of[cur]
    # place: rank 1 = highest. place[j] = 1 + #{ i : i above j } (i>j or i<j)
    place = [0]*n
    for j in range(n):
        place[j] = 1
        for i in range(n):
            if i == j: continue
            if i < j:
                if i in above[j]:
                    place[j] += 1   # i above j -> j lower
            else:
                if j not in above[i]:
                    place[j] += 1   # i is not above j -> i stays below j? 
        # place: among boats, count how many are above j (higher place than j)
    # redo cleanly: higher place number = lower rank (placed lower).
    # boat a is above boat b  <->  a ranks higher than b.
    # rank_higher: define above_relation directly
    return above

def parity_by_relation(n, above):
    # above[i] = set of j such that i is placed above j
    # Build total order: boat a placed higher than b iff a above b, or (incomparable and a>b? no)
    # Incomparable pairs keep STARTING relative order: original i lower than j -> i stays lower.
    # So final ranking: sort by (a above b) then starting order for incomparable.
    # We need the permutation parity of new order vs starting order.
    # Represent new order as a permutation list of boats (0..n-1) from highest place to lowest.
    # comparison for total order:
    def cmp(a, b):  # returns True if a should be placed higher than b
        if a in above and b in above.get(a,set()):
            return True
        if b in above.get(a,set()) if a in above else False:
            return True
        if a in above and a in above.get(b,set()):
            return False
        # check both directions
        if a in above and b in above.get(a, set()):
            return True
        if a in above and a in above.get(b, set()):
            return False
        # explicit
        aa = above.get(a, set()); bb = above.get(b, set())
        if b in aa: return True
        if a in bb: return False
        # incomparable: keep starting order (a lower index stays lower = placed lower)
        return a > b   # smaller index lower => higher index placed higher
    # build order via insertion
    order = [0]
    for a in range(1, n):
        inserted = False
        for idx in range(len(order)):
            if cmp(a, order[idx]):
                order.insert(idx, a); inserted=True; break
        if not inserted:
            order.append(a)
    # order = highest place first. Starting order highest place first = n-1,n-2,...,0
    start_hi = list(range(n-1, -1, -1))
    # permutation: maps start position (in order start_hi) to new
    # parity = sign of permutation mapping start_hi->order
    # sign of permutation p on positions
    pos_in_new = {boat:i for i,boat in enumerate(order)}
    # build the list new_perm where new_perm[rank_in_start] = rank_in_new
    new_perm = [pos_in_new[boat] for boat in start_hi]
    # count inversions
    inv = 0
    for i in range(n):
        for j in range(i+1,n):
            if new_perm[i] > new_perm[j]:
                inv += 1
    return inv % 2, order

def outcome_parity(n, L, speeds):
    state, bumped_by = simulate(n, L, speeds)
    above = {}
    for i in range(n):
        above[i]=set()
    # chains via bumped_by
    out_of = [-1]*n
    for k in range(n):
        if bumped_by[k] != -1:
            out_of[bumped_by[k]] = k
    for i in range(n):
        cur = out_of[i]
        while cur != -1:
            above[i].add(cur)
            cur = out_of[cur]
    inv, order = parity_by_relation(n, above)
    return inv, order

def run(N, n, L, seed=None):
    rng = random.Random(seed)
    even = 0
    for _ in range(N):
        speeds = [rng.expovariate(1.0) for _ in range(n)]
        inv, order = outcome_parity(n, L, speeds)
        if inv == 0:
            even += 1
    return even/N

if __name__ == '__main__':
    n = int(sys.argv[1]); L = float(sys.argv[2]); N = int(sys.argv[3]); seed=int(sys.argv[4]) if len(sys.argv)>4 else 1
    print(run(N, n, L, seed))
