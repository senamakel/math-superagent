#!/usr/bin/env python3
"""Independent check scripts referenced by the research report.

NOTE: These are single-purpose helpers kept for provenance. The authoritative
race oracle is code/brute.py (verified). They re-verify the two structural
claims that the report relies on:
 (A) the parity identity: parity = #(pairs i<j with a bump chain i->...->j) mod 2;
 (B) that in the pure (very large L) race the bump-cluster leaders equal the
     right-to-left record minima of the speeds.
Run:  python3 -m research.check_torpids_claims  [n] [L] [trials] [seed]
"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from code.brute import simulate_order, parity_of_new_order  # noqa


def chain_pair_count_from_above(above):
    """#(pairs i<j with j in above[i])."""
    n = len(above)
    c = 0
    for i in range(n):
        c += sum(1 for j in above[i] if j > i)
    return c


def rtl_record_minima(speeds):
    n = len(speeds)
    leaders, m = [], float('inf')
    for j in range(n - 1, -1, -1):
        if speeds[j] < m:
            m = speeds[j]
            leaders.append(j)
    return set(leaders)


def race_leaders(n, L, speeds):
    """Boats that never bump (out-degree 0). Uses the brute engine's edges."""
    edges = [[] for _ in range(n)]
    state = [0] * n
    pos = [40.0 * j for j in range(n)]
    while True:
        rowing = [j for j in range(n) if state[j] == 0]
        if not rowing:
            break
        best = None
        for j in rowing:
            ft = (L - pos[j]) / speeds[j]
            k = None
            for kk in range(j + 1, n):
                if state[kk] == 0:
                    k = kk
                    break
            cands = [(ft, 'F', j, None)]
            if k is not None and speeds[j] > speeds[k]:
                cands.append(((pos[k] - pos[j]) / (speeds[j] - speeds[k]), 'C', j, k))
            for c in cands:
                if c[0] == float('inf'):
                    continue
                if best is None or c[0] < best[0] - 1e-15:
                    best = c
        _t, kind, j, k = best
        if kind == 'F':
            state[j] = 1
            pos[j] = L
        else:
            state[j] = 2
            edges[j].append(k)
    return {j for j in range(n) if not edges[j]}, edges


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    L = float(sys.argv[2]) if len(sys.argv) > 2 else 1e7   # large => ~pure race
    trials = int(sys.argv[3]) if len(sys.argv) > 3 else 20000
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    rng = random.Random(seed)

    # (A) parity identity vs oracle
    par_bad = 0
    for _ in range(trials):
        speeds = [rng.expovariate(1.0) for _ in range(n)]
        above = simulate_order(n, 400.0 if L > 400 else L, speeds)
        par, _ = parity_of_new_order(n, above)
        cc = chain_pair_count_from_above(above) % 2
        if par != cc:
            par_bad += 1
    print(f"(A) parity == (#chain-pairs mod 2): mismatches {par_bad}/{trials}")

    # (B) leaders == right-to-left record minima (pure race)
    lead_bad = 0
    for _ in range(trials):
        speeds = [rng.expovariate(1.0) for _ in range(n)]
        leaders, _ = race_leaders(n, L, speeds)
        rec = rtl_record_minima(speeds)
        if leaders != rec:
            lead_bad += 1
    print(f"(B) race leaders == r-to-l record minima (pure L={L}): "
          f"mismatches {lead_bad}/{trials}")


if __name__ == '__main__':
    main()
