"""Focused verification of the load-bearing conclusion: every 5-chromatic
graph contains a 5-critical subgraph with minimum degree >= 4.

Uses the corrected SAT oracle (lib.critoracle, cross-checked against
lib.satcolor = 0 mismatches). Exhaustive over all graphs with chi >= 5 on
n <= 6 vertices, reporting the critical subgraph found and its min degree.
"""
import itertools
from lib import critoracle as co


def all_graphs(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for mask in range(1 << len(pairs)):
        yield [p for idx, p in enumerate(pairs) if mask >> idx & 1]


def delete_vertex(m, edges, v):
    rem = [u for u in range(m) if u != v]
    mp = {u: i for i, u in enumerate(rem)}
    sub = [(mp[a], mp[b]) for (a, b) in edges if a != v and b != v]
    return m - 1, sub


def is_vertex_critical(n, edges, k):
    if co.chrom(n, edges) != k:
        return False
    for v in range(n):
        m, sub = delete_vertex(n, edges, v)
        if not co.is_k_colorable(m, sub, k - 1):
            return False
    return True


def min_degree(n, edges):
    deg = [0] * n
    for (a, b) in edges:
        deg[a] += 1
        deg[b] += 1
    return min(deg) if n else 0


def critical_reduction(n, edges, k):
    """Greedy delete vertices while chi stays k; return (m,cur,critical?)."""
    m, cur = n, edges
    changed = True
    while changed:
        changed = False
        for v in range(m):
            mm, sub = delete_vertex(m, cur, v)
            if co.chrom(mm, sub) == k:
                m, cur = mm, sub
                changed = True
                break
    return m, cur, is_vertex_critical(m, cur, k)


def main():
    N = 6
    n_5chrom = 0
    n_fail = 0
    five_crit_sizes = {}
    for n in range(1, N + 1):
        for edges in all_graphs(n):
            k = co.chrom(n, edges)
            if k < 5:
                continue
            n_5chrom += 1
            m, sub, crit = critical_reduction(n, edges, k)
            if not (crit and co.chrom(m, sub) == k):
                n_fail += 1
                print(f"  FAIL reduction n={n} edges={edges}")
                continue
            # k is >=5 and critical subgraph is k-critical.
            if min_degree(m, sub) < k - 1:
                n_fail += 1
                print(f"  FAIL min_degree n={n} k={k} edges={edges} sub={sub}")
            if k == 5:
                five_crit_sizes[m] = five_crit_sizes.get(m, 0) + 1
    print(f"5-chromatic graphs n<= {N}: {n_5chrom}")
    print(f"failures (no k-critical same-chi subgraph, or min_deg<k-1): {n_fail}")
    print("5-critical subgraph sizes found (m: count):", dict(sorted(five_crit_sizes.items())))
    print("RESULT:", "PASSED" if n_fail == 0 else "FAILED")


if __name__ == "__main__":
    main()
