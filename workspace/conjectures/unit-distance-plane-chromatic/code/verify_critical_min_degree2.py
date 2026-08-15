"""Verify the graph-theory lemma (gap sharp-critical-degree) with an
independent correct SAT oracle (lib.critoracle), and cross-check the oracle
against lib.satcolor (calibrated library oracle).

Lemma:
(1) Every graph G with chi(G)=k contains a vertex-critical subgraph H with
    chi(H)=k (repeatedly delete a vertex while chi stays k).
(2) Every vertex-critical graph H with chi(H)=k has minimum degree >= k-1.
Conclusion: every 5-chromatic graph contains a 5-critical subgraph with
minimum degree >= 4.

Verified by complete enumeration over ALL simple graphs on up to N vertices.
This is the permitted brute-force-at-small-size oracle, not the method.
"""
import itertools
from lib import critoracle as co
from lib import satcolor as sc


def all_graphs(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for mask in range(1 << len(pairs)):
        yield [p for idx, p in enumerate(pairs) if mask >> idx & 1]


def delete_vertex(m, edges, v):
    """Return (m-1, edges) of the graph with vertex v removed, renumbered."""
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


def oracle_crosscheck(maxn=6):
    nm = 0
    for n in range(1, maxn + 1):
        for edges in all_graphs(n):
            k = co.chrom(n, edges)
            if not sc.is_k_colorable(edges, k, n)[0]:
                nm += 1
                print(f"  MISMATCH n={n} edges={edges}")
    return nm


def run(N):
    g_total = g_crit = g_bad1 = g_bad2 = 0
    max_k = 0
    for n in range(1, N + 1):
        for edges in all_graphs(n):
            g_total += 1
            k = co.chrom(n, edges)
            max_k = max(max_k, k)
            # --- part 2: every vertex-critical graph has min degree >= k-1 ---
            if is_vertex_critical(n, edges, k):
                g_crit += 1
                if min_degree(n, edges) < k - 1:
                    g_bad2 += 1
                    print(f"  BAD2 n={n} chi={k} edges={edges}")
            # --- part 1: greedy deletion yields vertex-critical same-chi ---
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
            if co.chrom(m, cur) != k:
                g_bad1 += 1
                print(f"  BAD1a n={n} edges={edges}")
                continue
            crit = is_vertex_critical(m, cur, k)
            if not crit:
                g_bad1 += 1
                print(f"  BAD1b n={n} edges={edges}")
    print(f"[1&2] graphs n<= {N}: total={g_total} vertex-critical={g_crit} "
          f"violations_part2={g_bad2} violations_part1={g_bad1} max_chi={max_k}")
    return g_bad1, g_bad2


def main():
    N = 6
    print("=== oracle cross-check (critoracle vs lib.satcolor) ===")
    print("cross-check mismatches:", oracle_crosscheck(N))
    print("=== lemma verification (complete over all graphs n<=%d) ===" % N)
    b1, b2 = run(N)
    print("RESULT:", "PASSED" if (b1 == 0 and b2 == 0) else "FAILED")


if __name__ == "__main__":
    main()
