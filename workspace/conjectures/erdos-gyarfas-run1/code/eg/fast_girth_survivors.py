"""Polynomial-BFS girth survivor counter.

Counts connected min-degree>=3 graphs on n vertices (nauty-geng ISO classes)
whose girth >= G (BFS girth, polynomial, no exponential cycle enumeration).
This gives the "survivor" sequences that can only be counterexamples to EG:
the first barrier (no 4-cycle) is girth>=5, the next (no 8-cycle) is girth>=9,
etc.  Run at the largest n that geng + BFS-girth allows.
"""
import sys
import networkx as nx
from lib.cycles import _geng_graph6, min_degree


def bfs_girth(G):
    """Shortest cycle length via BFS from every vertex (polynomial, exact)."""
    best = None
    for s in G.nodes():
        dist = {s: 0}
        parent = {s: -1}
        from collections import deque
        q = deque([s])
        while q:
            v = q.popleft()
            for w in G.neighbors(v):
                if w not in dist:
                    dist[w] = dist[v] + 1
                    parent[w] = v
                    q.append(w)
                elif parent[v] != w and parent[w] != v:
                    L = dist[v] + dist[w] + 1
                    if best is None or L < best:
                        best = L
    return best


def main():
    gmin = int(sys.argv[1]) if len(sys.argv) > 1 else 5   # survivor girth floor
    nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 9
    print(f"n | total_mindeg3 | girth>={gmin}_survivors")
    for n in range(4, nmax + 1):
        lines = _geng_graph6(n)
        total = 0
        surv = 0
        for g6 in lines:
            g6 = g6.strip()
            if not g6:
                continue
            G = nx.from_graph6_bytes(g6.encode())
            if min_degree(G) < 3:
                continue
            total += 1
            g = bfs_girth(G)
            if g is not None and g >= gmin:
                surv += 1
        print(f"{n} | {total} | {surv}")


if __name__ == "__main__":
    main()
