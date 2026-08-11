#!/usr/bin/env python3
"""Empirical structural study of PE597 (Torpids) — three questions.

Q1: correlate race parity with three candidate scalar-priority treaps
    (a) w_i = v_i/(L-40i)
    (b) f_i = finish time = (L-40i)/v_i
    (c) raw speed v_i
    For each, build min-priority Cartesian tree over index ranges (root=global
    min, recurse on left/right subranges), count ancestor/descendant pairs mod2,
    compare against oracle parity. Report exact mismatch counts per (n,L,kind).

Q2: does ANY scalar-priority treap reproduce oracle parity? (inference from Q1
    plus a fine-grained scalar search on n=3.)

Q3: characterize the bump directed graph: out-deg<=1? always increasing index?
    distinct edge sets for n=3 and their relative frequencies vs the table
    probabilities 4/15, 8/45, 1/3, 4/27, 2/27.
"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "code"))
from brute import simulate_order, outcome_parity


def build_treap_pairs_mod2(n, priority):
    """Count ancestor/descendant pairs mod 2 in the min-priority Cartesian
    tree (in-order = index order). Returns count%2."""
    # recursive min over [lo,hi) building parent links
    def build(lo, hi):
        if lo >= hi:
            return None
        r = min(range(lo, hi), key=lambda i: priority[i])
        lc = build(lo, r)
        rc = build(r + 1, hi)
        return r, lc, rc
    tree = build(0, n)

    # count ancestor/descendant pairs via subtree sizes
    total = 0
    def rec(node):
        nonlocal total
        if node is None:
            return 0
        r, lc, rc = node
        ls = rec(lc)
        rs = rec(rc)
        total += ls + rs          # each descendant pairs with the root
        return 1 + ls + rs
    rec(tree)
    return total % 2


def treap_parity(n, L, speeds, kind):
    if kind == 'a':
        # w_i = v_i / (L - 40*i)
        pri = [speeds[i] / (L - 40.0 * i) for i in range(n)]
    elif kind == 'b':
        # finish time (L-40*i)/v_i  -> min-priority = fastest finish
        pri = [(L - 40.0 * i) / speeds[i] for i in range(n)]
    else:
        pri = list(speeds)
    return build_treap_pairs_mod2(n, pri)


def q1(n_list, L_list, trials, seed=202401):
    rng = random.Random(seed)
    print("===== Q1: scalar-priority treap vs oracle parity =====")
    print(f"{'n':>3} {'L':>5} {'kind':>5} {'trials':>8} {'mismatch':>9}")
    kinds = ['a', 'b', 'c']
    for n in n_list:
        for L in L_list:
            acc = {k: 0 for k in kinds}
            tot = 0
            for _ in range(trials):
                speeds = [rng.expovariate(1.0) for _ in range(n)]
                op = outcome_parity(n, L, speeds)
                tot += 1
                for k in kinds:
                    if treap_parity(n, L, speeds, k) != op:
                        acc[k] += 1
            for k in kinds:
                print(f"{n:>3} {L:>5} {k:>5} {tot:>8} {acc[k]:>9}   ({100.0*acc[k]/tot:.2f}%)")


def q3(n, L, trials, seed=777):
    rng = random.Random(seed)
    from collections import Counter
    edge_counts = Counter()
    exemplars = {}
    outdeg_viol = 0
    idx_viol = 0
    for _ in range(trials):
        speeds = [rng.expovariate(1.0) for _ in range(n)]
        above = simulate_order(n, L, speeds)
        # reconstruct chronological edges by replay (same dynamics)
        state = [0]*n; pos = [40.0*j for j in range(n)]; edges = []
        while True:
            rowing = [j for j in range(n) if state[j]==0]
            if not rowing: break
            best = None
            for j in rowing:
                vj = speeds[j]; ft = (L-pos[j])/vj; k=None
                for kk in range(j+1,n):
                    if state[kk]==0: k=kk; break
                cands=[(ft,'F',j,None)]
                if k is not None and vj>speeds[k]:
                    cands.append(((pos[k]-pos[j])/(vj-speeds[k]),'C',j,k))
                for c in cands:
                    if c[0]==float('inf'): continue
                    if best is None or c[0]<best[0]-1e-15: best=c
            t,kind,j,k = best
            if kind=='F':
                state[j]=1; pos[j]=L
            else:
                state[j]=2; pos[j]=pos[k]; edges.append((j,k))
        # out-degree check: each boat bumps at most once
        from collections import Counter as C
        src = C(e[0] for e in edges)
        if any(c>1 for c in src.values()):
            outdeg_viol += 1
        if any(a>=b for a,b in edges):
            idx_viol += 1
        eset = tuple(sorted(edges))
        edge_counts[eset]+=1
        exemplars.setdefault(eset, speeds)
    print(f"\n===== Q3: bump-graph characterization, n={n}, L={L}, {trials} trials =====")
    print(f"samples with out-degree>1 (one boat bumping twice): {outdeg_viol}")
    print(f"samples with a non-increasing-index edge: {idx_viol}")
    print("distinct chronological edge sets and frequencies:")
    for eset,c in edge_counts.most_common():
        print(f"  edges={list(eset):20s} count={c:8d}  freq={c/trials:.6f}")
    print("  (table: none=4/15=0.2667, B->C=8/45=0.1778, A->B=1/3=0.3333,"
          " B->C,A->C=4/27=0.1481, A->B,B->C=2/27=0.0741)")
    return edge_counts


if __name__ == '__main__':
    trials_q1 = int(sys.argv[1]) if len(sys.argv) > 1 else 50000
    q1([3,4,5], [160.0,400.0,1800.0], trials_q1, seed=11)
    q3(3, 160.0, trials_q1, seed=99)
