#!/usr/bin/env python3
"""Independent second engine for PE 597 (Torpids).

This is a from-scratch reimplementation of the race dynamics written without
reference to code/brute.py, to serve as a cross-check ground truth.

Model (per problem statement):
  Boats indexed 0..n-1; boat 0 is lowest-placed (downstream, pos 0), adjacent
  boats 40 m apart, finish line at L upstream.
  Boat j rows at constant speed v_j until it EITHER reaches pos L (FINISH) OR
  draws level with ("bumps") the nearest ROWING boat ahead -- the smallest
  k>j still rowing. On a bump the BUMPER stops (OUT, transparent to boats
  behind) and the bumped boat keeps rowing (and may itself be bumped again).
  Speeds v_j ~ Exp(1) iid.

Ordering: for i<j, i is placed HIGHER than j iff there is a bump chain
  i -> ... -> j (direct or transitive). Incomparable pairs keep start order
  (i below j). Parity = sign of the permutation from the starting ascending
  listing [0,1,...,n-1] to the new ascending listing.
"""

import random
from math import inf


def race_parity(n, L, speeds):
    """Return (parity, bump_edges) for the given speed vector.

    parity is 0 (even) or 1 (odd). bump_edges is a list of (bumper, bumped).
    """
    pos = [40.0 * j for j in range(n)]
    status = ['R'] * n          # R = ROWING, O = OUT, F = FINISHED
    edges = [[] for _ in range(n)]   # edges[a] = boats that a bumped

    def rowing():
        return [j for j in range(n) if status[j] == 'R']

    while rowing():
        best_t, best_kind, best_j, best_k = inf, None, None, None
        for j in rowing():
            ft = (L - pos[j]) / speeds[j]
            # nearest ROWING boat ahead
            k = None
            for kk in range(j + 1, n):
                if status[kk] == 'R':
                    k = kk
                    break
            # candidate events for this boat
            cands = [(ft, 'F', j, None)]
            if k is not None and speeds[j] > speeds[k]:
                ct = (pos[k] - pos[j]) / (speeds[j] - speeds[k])
                cands.append((ct, 'C', j, k))
            for (t, kind, jj, kk) in cands:
                if t is not None and t < best_t - 1e-15:
                    best_t, best_kind, best_j, best_k = t, kind, jj, kk
        # process earliest event (ties of prob 0; deterministic order)
        if best_kind == 'F':
            status[best_j] = 'F'
            pos[best_j] = L
        else:  # 'C' bump
            status[best_j] = 'O'
            pos[best_j] = pos[best_k]
            edges[best_j].append(best_k)

    # reachability: for i<j, chain i->...->j exists iff j reachable from i
    reach = [set() for _ in range(n)]
    for i in range(n):
        seen = {i}
        stack = [i]
        while stack:
            u = stack.pop()
            for w in edges[u]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        reach[i] = seen - {i}

    # build ascending order (lowest place first) with comparator
    def placed_lower(a, b):
        """True iff a comes before b in ascending-place listing."""
        if a < b:
            # a lower than b  <=>  no chain a->b
            return b not in reach[a]
        else:
            # a > b: a lower than b  <=>  b placed higher than a
            #   b higher than a  <=>  chain b->a
            return a in reach[b]

    order = [0]
    for a in range(1, n):
        idx = 0
        while idx < len(order):
            if placed_lower(a, order[idx]):
                break
            idx += 1
        order.insert(idx, a)

    # parity = inversion count of (indices) in this order mod 2
    pos_in_order = {boat: i for i, boat in enumerate(order)}
    inv = 0
    for i in range(n):
        for j in range(i + 1, n):
            if pos_in_order[i] > pos_in_order[j]:
                inv += 1
    return inv % 2, edges


def mc_estimate(n, L, N, seed=None):
    """MC estimate of p(n,L) using Exp(1) speeds, with binomial SE."""
    rng = random.Random(seed)
    even = 0
    for _ in range(N):
        speeds = [rng.expovariate(1.0) for _ in range(n)]
        par, _ = race_parity(n, L, speeds)
        even += 1 - par   # par==0 means even
    p = even / N
    se = (p * (1 - p) / N) ** 0.5
    return p, se, even


if __name__ == "__main__":
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "code"))
    import brute

    print("=== differential test: this engine vs brute.outcome_parity ===")
    rng = random.Random(2024)
    total = 0
    mism = 0
    for (n, L, trials) in [(2, 160, 20000), (2, 400, 20000), (3, 160, 40000),
                           (3, 400, 40000), (4, 400, 40000), (4, 1800, 40000),
                           (5, 1800, 40000), (6, 1800, 20000)]:
        m = 0
        for _ in range(trials):
            speeds = [rng.expovariate(1.0) for _ in range(n)]
            my_par, _ = race_parity(n, L, speeds)
            ref = brute.outcome_parity(n, L, speeds)
            m += (my_par != ref)
        total += trials
        mism += m
        print(f"n={n} L={L} trials={trials}: mismatches={m}")
    print(f"TOTAL mismatches / trials = {mism} / {total}")
    print()

    print("=== MC cross-checks (this engine, Exp(1) speeds) ===")
    anchors = [
        (2, 160, 200000, "n=2 exact MC"),
        (2, 400, 200000, "n=2 exact MC"),
        (3, 160, 200000, "exact 56/135 = 0.414815"),
        (3, 160, 50000, "exact 56/135 = 0.414815"),
        (4, 400, 50000, "given 0.5107843137"),
        (4, 400, 500000, "given 0.5107843137"),
    ]
    for (n, L, N, note) in anchors:
        p, se, even = mc_estimate(n, L, N, seed=12345)
        print(f"n={n} L={L} N={N}: p={p:.6f} SE={se:.6f} even={even}  [{note}]")

    # deliverable: p(13,1800)
    print()
    print("=== deliverable: p(13,1800) ===")
    p, se, even = mc_estimate(13, 1800, 1500000, seed=99)
    print(f"N=1500000: p={p:.6f} SE={se:.6f} even={even}")
