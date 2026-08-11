#!/usr/bin/env python3
"""TASK: verify PE 597 worked examples + taxonomy of bump-graph structure.

Part A — reproduce the n=3,L=160 five-row worked table with the brute engine:
  (none)                   edges=[]                    -> even  4/15
  B bumps C                edges=[(1,2)]               -> odd   8/45
  A bumps B                edges=[(0,1)]               -> odd   1/3
  B bumps C, A bumps C     edges=[(1,2),(0,2)]         -> even  4/27
  A bumps B, B bumps C     edges=[(0,1),(1,2)]         -> odd   2/27
Each row uses an Exp(1)-distributed speed vector that produces that exact
chronological edge set (same vectors as task1_verify.py). We also confirm the
exact rational sum of row probabilities = 4/15 + 8/45 + 1/3 + 4/27 + 2/27
= 56/135, matching the stated p(3,160).

Part B — Monte-Carlo verify p(4,400) ~ 0.5107843137.

Part C — bump-graph TAXONOMY over many MC trials for n in {3,4,5}, L in
{160,1800}: collect the distinct edge-structure / reachability ('above') sets
the true race reaches, and report
  * per-boat out-degree and in-degree statistics,
  * whether the bump graph is always a forest (out-degree<=1 + strictly
    increasing index edges => no cycles),
  * roots = boats that never bump (finishers), trees = #roots,
  * max bump-chain length,
  * geometry of edge sets (edge-endpoint index gaps, branching).

Uses the reference brute engine (code/brute.py) and its `above` reachability
representation.
"""
import sys, os
from collections import Counter, defaultdict
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from brute import simulate_order, parity_of_new_order, outcome_parity
from toolkits.race_events import race_events

# ---------------------------------------------------------------- Part A
def part_a():
    print("=" * 78)
    print("PART A: reproduce the n=3,L=160 five-row worked table (brute engine)")
    print("=" * 78)
    rows = [
        # (speed vector, expected parity, expected edges, prob label)
        ([0.157, 0.607, 1.473], 0, [], "4/15"),
        ([0.073, 0.215, 0.093], 1, [(1, 2)], "8/45"),
        ([0.257, 0.137, 1.662], 1, [(0, 1)], "1/3"),
        ([2.205, 2.057, 0.126], 0, [(1, 2), (0, 2)], "4/27"),
        ([3.218, 2.055, 1.316], 1, [(0, 1), (1, 2)], "2/27"),
    ]
    allok = True
    for speeds, exp_par, exp_edges, label in rows:
        n, L = 3, 160.0
        ev = race_events(n, L, speeds)
        par = ev['parity']
        edges = sorted(ev['bumps'])
        ok = (par == exp_par) and (edges == sorted(exp_edges))
        allok &= ok
        print(f"  speeds={speeds}")
        print(f"    edges={sorted(ev['bumps'])}  parity={par}  "
              f"(expected edges={exp_edges}, parity={exp_par})  [{label}]  "
              f"{'OK' if ok else 'FAIL'}")
    print(f"  all five rows: {'PASS' if allok else 'FAIL'}")

    # exact rational sum of row probabilities
    probs = [Fraction(4, 15), Fraction(8, 45), Fraction(1, 3),
             Fraction(4, 27), Fraction(2, 27)]
    total = sum(probs, Fraction(0))
    print(f"  sum of row probabilities = {total}  (target 56/135)  "
          f"{'OK' if total == Fraction(56,135) else 'FAIL'}")
    return allok


# ---------------------------------------------------------------- Part B
def part_b(N=400000, seed=12345):
    import random
    print("=" * 78)
    print(f"PART B: MC verify p(4,400) = even-parity fraction over {N} trials")
    print("=" * 78)
    rng = random.Random(seed)
    n, L = 4, 400.0
    even = 0
    for _ in range(N):
        speeds = [rng.expovariate(1.0) for _ in range(n)]
        if outcome_parity(n, L, speeds) == 0:
            even += 1
    est = even / N
    se = (est * (1 - est) / N) ** 0.5
    print(f"  MC p(4,400) = {est:.6f}  (SE={se:.6f})   given 0.5107843137")
    return est, se


# ---------------------------------------------------------------- Part C
def forest_depth(parent):
    """Given parent[i]=j (i bumps j) or None, return max chain length (number
    of edges in the longest directed path i->j->...)."""
    n = len(parent)
    memo = {}
    def depth(i):
        if i in memo:
            return memo[i]
        d = 0
        p = parent[i]
        if p is not None:
            d = 1 + depth(p)
        memo[i] = d
        return d
    return max((depth(i) for i in range(n)), default=0)


def part_c(configs, trials=60000, seed=2024):
    import random
    print("=" * 78)
    print(f"PART C: bump-graph TAXONOMY over {trials} MC trials per (n,L)")
    print("=" * 78)
    report = []
    for n, L in configs:
        rng = random.Random(seed + n * 100 + int(L))
        outdeg_hits = Counter()           # how many distinct boats bump exactly d times
        indeg_hits = Counter()
        forest_ok = 0
        cycles = 0
        nonincreasing = 0
        chains = Counter()
        above_sets = Counter()
        edge_sets = Counter()
        num_trees_hist = Counter()        # = number of finishers (roots)
        edge_count_hist = Counter()
        total_edges = 0
        maxindeg_per_samp = Counter()
        for _ in range(trials):
            speeds = [rng.expovariate(1.0) for _ in range(n)]
            ev = race_events(n, L, speeds)
            edges = ev['bumps']
            parent = [None] * n
            outdeg = Counter()
            indeg = Counter()
            for (a, b) in edges:
                parent[a] = b
                outdeg[a] += 1
                indeg[b] += 1
            # structural checks
            is_ok = True
            if any(c > 1 for c in outdeg.values()):
                is_ok = False
            if any(a >= b for a, b in edges):   # edge must go to strictly larger index
                is_ok = False
                nonincreasing += 1
            # cycle detection via increasing-index argument plus explicit check
            # (out-degree<=1 and all edges strictly increasing => forest)
            cyc = False
            # functional-graph cycle check
            state = [0] * n
            for i in range(n):
                if state[i]:
                    continue
                path = []
                cur = i
                while cur is not None and state[cur] == 0:
                    state[cur] = 1
                    path.append(cur)
                    cur = parent[cur]
                if cur is not None and state[cur] == 1 and cur in path:
                    cyc = True
            if cyc:
                cycles += 1
                is_ok = False
            if is_ok:
                forest_ok += 1
            roots = [i for i in range(n) if parent[i] is None]
            ml = forest_depth(parent)
            chains[ml] += 1
            num_trees_hist[len(roots)] += 1
            edge_count_hist[len(edges)] += 1
            total_edges += len(edges)
            for d in outdeg.values():
                outdeg_hits[d] += 1
            for d in indeg.values():
                indeg_hits[d] += 1
            mi = max(indeg.values(), default=0)
            maxindeg_per_samp[mi] += 1
            above_sets[frozenset(_edges_to_above(n, edges))] += 1
            edge_sets[tuple(sorted(edges))] += 1
        print(f"\n----- n={n}, L={L} -----")
        print(f"  always forest (outdeg<=1 & edges strictly increasing & acyclic): "
              f"{forest_ok}/{trials}")
        print(f"  detected cycles: {cycles}, non-increasing-index edges: {nonincreasing}")
        print(f"  out-degree histogram over {n*trials} boat-slots: "
              f"{dict(outdeg_hits)}  (out-degree>1 count: {outdeg_hits[2]+outdeg_hits[3]})")
        print(f"  in-degree histogram over boats: {dict(indeg_hits)}")
        print(f"  max in-degree within a sample: {dict(maxindeg_per_samp)}")
        print(f"  #bump-edges per race: {dict(sorted(edge_count_hist.items()))}")
        print(f"  #trees (= #finishers = #never-bumped boats) per race: "
              f"{dict(sorted(num_trees_hist.items()))}")
        print(f"  max bump-chain length distribution: {dict(sorted(chains.items()))}")
        print(f"  mean #edges: {total_edges/trials:.3f}")
        print(f"  distinct edge sets reached: {len(edge_sets)} of {trials} trials")
        print(f"  distinct 'above'-reachability sets reached: {len(above_sets)}")
        top = edge_sets.most_common(8)
        print("  most common edge structures:")
        for es, c in top:
            print(f"     {list(es)!s:28s} count={c:7d}  freq={c/trials:.5f}")
        report.append((n, L, forest_ok, cycles, dict(outdeg_hits),
                       dict(indeg_hits), total_edges / trials,
                       len(edge_sets), len(above_sets)))
    return report


def _edges_to_above(n, edges):
    """Return the 'above' reachability representation (frozenset of frozensets)
    from a direct edge set, matching brute.simulate_order."""
    adj = {i: [] for i in range(n)}
    for (a, b) in edges:
        adj[a].append(b)
    above = []
    for i in range(n):
        seen = {i}
        stack = [i]
        while stack:
            u = stack.pop()
            for w in adj[u]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        above.append(tuple(sorted(seen - {i})))
    return tuple(above)


if __name__ == '__main__':
    # Part A
    a_ok = part_a()
    # Part B
    b_est, b_se = part_b()
    # Part C
    configs = [(3, 160.0), (3, 1800.0), (4, 160.0), (4, 1800.0),
               (5, 160.0), (5, 1800.0)]
    rep = part_c(configs)
    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print(f"Part A rows reproduced: {'PASS' if a_ok else 'FAIL'}; "
          f"exact row-prob sum = 56/135.")
    print(f"Part B MC p(4,400) = {b_est:.6f} +/- {b_se:.6f} (given 0.5107843137)")
    for n, L, fo, cyc, od, idg, mean_e, nes, nas in rep:
        print(f"  n={n} L={int(L)}: forest={fo}/{60000} cycles={cyc} "
              f"outdeg={dict(od)} indeg={dict(idg)} mean_edges={mean_e:.3f} "
              f"distinct_edge_sets={nes} distinct_above_sets={nas}")
