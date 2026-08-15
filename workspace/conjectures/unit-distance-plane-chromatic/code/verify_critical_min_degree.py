"""Verify the graph-theory lemma (gap sharp-critical-degree).

Lemma. (1) Every graph G with chi(G) = k contains a *vertex-critical* subgraph
H with chi(H) = k: repeatedly delete a vertex v while chi(G - v) stays k; the
minimal survivor is vertex-critical (chi(H - w) <= k-1 for every vertex w).

(2) Every vertex-critical graph H with chi(H) = k has minimum degree >= k-1:
if a vertex v had degree <= k-2, take a (k-1)-colouring of H - v (exists since
H is vertex-critical so chi(H-v) <= k-1) and give v a colour unused on its
<= k-2 neighbours, contradicting chi(H) = k.

Conclusion: every 5-chromatic graph contains a 5-critical subgraph with
minimum degree >= 4.

The classical "k-critical" notion (every proper *subgraph* not just G-v is
(k-1)-colourable) implies vertex-critical, so the vertex-critical version proved
and checked here is the weaker, more robust hypothesis the degree argument
actually needs.

Method: exhaustive exact computation over ALL simple graphs on up to N
vertices. chrom(n,edges) is a complete exact k-colourability test (DSATUR
backtracking). This is allowed as an oracle/verification at small n; it checks
the collection of all graphs up to size N rather than one hand-picked example.
"""
import itertools
from lib.coloring import chromatic_colorable


def chrom(n, edges):
    """Exact chromatic number of an n-vertex graph (1..n). Complete."""
    for k in range(1, n + 1):
        ok, _ = chromatic_colorable(n, edges, k)
        if ok:
            return k
    return n  # exhaustive colouring with n colours always works


def del_vertex(n, edges, v):
    """Remove vertex v from an n-vertex graph, renumbering remaining vertices
    0..n-2 by identity order, returning (n-1, new_edges)."""
    rem = [u for u in range(n) if u != v]
    mp = {u: i for i, u in enumerate(rem)}
    sub = [(mp[a], mp[b]) for (a, b) in edges if a != v and b != v]
    return len(rem), sub


def is_vertex_critical(n, edges, k):
    """True iff chi(G)=k and chi(G - v) <= k-1 for every vertex v."""
    if chrom(n, edges) != k:
        return False
    for v in range(n):
        m, sub = del_vertex(n, edges, v)
        if chromatic_colorable(m, sub, k - 1)[0]:
            continue
        return False
    return True


def min_degree(n, edges):
    deg = [0] * n
    for (a, b) in edges:
        deg[a] += 1
        deg[b] += 1
    return min(deg) if n else 0


def all_graphs(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for mask in range(1 << len(pairs)):
        edges = [p for idx, p in enumerate(pairs) if mask >> idx & 1]
        yield edges


def main():
    N = 6  # 1..6: 2 + 8 + 64 + 1024 + 32768 = 33866 graphs
    g_total = g_crit = g_badpart2 = 0
    # Part 2: every vertex-critical graph with chi=k has min degree >= k-1.
    max_k_seen = 0
    for n in range(1, N + 1):
        for edges in all_graphs(n):
            g_total += 1
            k = chrom(n, edges)
            if k > max_k_seen:
                max_k_seen = k
            if is_vertex_critical(n, edges, k):
                g_crit += 1
                if min_degree(n, edges) < k - 1:
                    g_badpart2 += 1
                    print(f"  VIOLATION part2: n={n} chi={k} edges={edges}")
    print(f"[part2] all graphs n<= {N}: total={g_total} vertex-critical={g_crit} "
          f"violations(min_deg<chi-1)={g_badpart2} max_chi={max_k_seen}")

    # Part 1: every graph contains a vertex-critical subgraph of the same chi.
    fail1 = 0
    checked = 0
    for n in range(1, N + 1):
        for edges in all_graphs(n):
            k = chrom(n, edges)
            # greedy vertex deletion while chi stays k (chi cannot go below 1)
            verts = list(range(n))
            cur = edges
            m = n
            changed = True
            while changed:
                changed = False
                for v in list(range(m)):
                    mm, sub = del_vertex(m, cur, v)
                    if chrom(mm, sub) == k:
                        m = mm
                        cur = sub
                        changed = True
                        break
            # verify the survivor is vertex-critical with chi=k
            if chrom(m, cur) != k:
                fail1 += 1
                continue
            crit = all(chromatic_colorable(m - 1,
                                           del_vertex(m, cur, v)[1], k - 1)[0]
                       for v in range(m))
            if not crit:
                fail1 += 1
            checked += 1
            # min degree of the 5-critical survivor is exactly the k=5 case;
            # also check the whole conclusion for chi>=5 via part2 already done.
    print(f"[part1] graphs where greedy deletion failed to yield a "
          f"vertex-critical same-chi subgraph: {fail1}/{checked}")

    print("RESULT:", "PASSED" if (g_badpart2 == 0 and fail1 == 0) else "FAILED")


if __name__ == "__main__":
    main()
