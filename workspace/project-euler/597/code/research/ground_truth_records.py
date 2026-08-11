#!/usr/bin/env python3
"""Ground-truth experiment: is the bump-graph 'leader' set (= boats that never
bump = out-degree 0 roots) equal to the RIGHT-TO-LEFT record minima of speeds
in the infinite-line (large-L) limit? And how does a finite finish line L
break that (magnitudes matter)?

Also: characterize chain-pairs (i<j with visitor chain i->...->j) under the
record structure.

This grounds the research report's claim that the pure model = no-passing
platoon / right-to-left records of desired speeds, and that the finish line
breaks it (inverse-exponential finish times).
"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from code.brute import simulate_order  # noqa


def right_to_left_record_minima(speeds):
    """Indices j such that v_j = min_{k>=j} v_k (scanning from back/front to index 0)."""
    n = len(speeds)
    leaders = []
    cur_min = float('inf')
    for j in range(n - 1, -1, -1):
        if speeds[j] < cur_min:
            cur_min = speeds[j]
            leaders.append(j)
    return set(leaders)


def oracle_leaders(n, L, speeds):
    """Boats that never bump = out-degree 0 in the bump graph = roots."""
    edges = [[] for _ in range(n)]
    # re-implement the bump chronology minimally to record edges (transparent)
    state = [0] * n
    pos = [40.0 * j for j in range(n)]
    bump_edges = [[] for _ in range(n)]
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
                if best is None or c[0] < best[0] - 1e-15:
                    best = c
        t, kind, j, k = best
        if kind == 'F':
            state[j] = 1
        else:
            state[j] = 2
            bump_edges[j].append(k)
    leaders = [j for j in range(n) if len(bump_edges[j]) == 0]
    return set(leaders), bump_edges


def chain_pairs_from_edges(n, edges):
    """Set of (i,j), i<j, with a bump chain i->...->j."""
    seen = [set() for _ in range(n)]
    for i in range(n):
        st = [i]
        while st:
            u = st.pop()
            for w in edges[u]:
                if w not in seen[i]:
                    seen[i].add(w)
                    st.append(w)
    pairs = set()
    for i in range(n):
        for j in seen[i]:
            if i < j:
                pairs.add((i, j))
    return pairs


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    trials = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
    L = float(sys.argv[3]) if len(sys.argv) > 3 else 1e7   # large = ~infinite
    n = int(sys.argv[4]) if len(sys.argv) > 4 else 5
    rng = random.Random(seed)
    leader_mismatch = 0
    unlikely = 0
    for _ in range(trials):
        speeds = [rng.expovariate(1.0) for _ in range(n)]
        rec = right_to_left_record_minima(speeds)
        lead, edges = oracle_leaders(n, L, speeds)
        if rec != lead:
            leader_mismatch += 1
            if leader_mismatch <= 3:
                print(f"  leader mismatch: speeds={[round(s,3) for s in speeds]}")
                print(f"    records={sorted(rec)} leaders={sorted(lead)}")
        # check that chain-pair set, in this large-L regime, is determined by
        # the speed permutation (same speeds reordered shouldn't matter by
        # magnitude here, but different permutations should differ)
    print(f"n={n} L={L} trials={trials}")
    print(f"  leader==right-to-left-record-minima mismatches: "
          f"{leader_mismatch}/{trials}")

    # Now: how much does finite L break leaders==records? Compare a moderately
    # small L.
    rng2 = random.Random(12345)
    Lsmall = 1800.0
    m2 = 0
    for _ in range(trials):
        speeds = [rng2.expovariate(1.0) for _ in range(n)]
        rec = right_to_left_record_minima(speeds)
        lead, edges = oracle_leaders(n, Lsmall, speeds)
        if rec != lead:
            m2 += 1
    print(f"  (comparison) leaders==records mismatches at realistic L={Lsmall}: "
          f"{m2}/{trials}")


if __name__ == '__main__':
    main()
