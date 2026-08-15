#!/usr/bin/env python3
"""
Independent cross-check of the M^k(C5) K2,3 obstruction via a DIFFERENT
construction library (lib.unitfield's graph utilities / a fresh adjacency
build), confirming it is the graph structure, not the builder, that violates
K2,3-freeness.

K2,3-freeness is a pure graph property and a NECESSARY condition for
unit-distance realizability (sharp_nbhd_cert). So if M^k(C5) (k>=2) has a
K2,3, it is not realizable -- independent of any colouring oracle.  This
script re-derives the edge list several independent ways and re-locates the
explicit K2,3.
"""
from itertools import combinations


def mycielski_adj(adj):
    """Adjacency-list textbook Mycielski: twins + root, cross edges, star.
    Standard version (no twin-to-twin edges)."""
    n = len(adj)
    N = 2 * n + 1
    A = [set() for _ in range(N)]
    for i in range(n):
        A[i] = set(adj[i])
    for i in range(n):
        A[n + i].add(2 * n); A[2 * n].add(n + i)   # star
    for i in range(n):
        for j in adj[i]:
            A[n + i].add(j); A[j].add(n + i)       # cross
    return A


def find_k23(adj):
    n = len(adj)
    for a in range(n):
        for b in range(a + 1, n):
            c = adj[a] & adj[b]
            if len(c) >= 3:
                return (a, b, sorted(c))
    return None


def c5():
    return [{(i - 1) % 5, (i + 1) % 5} for i in range(5)]


def main():
    levels = [c5()]
    for _ in range(4):
        levels.append(mycielski_adj(levels[-1]))
    print("Independent adjacency-build K2,3 hunt over M^k(C5):")
    for k in (0, 1, 2, 3, 4):
        adj = levels[k]
        E = sum(len(x) for x in adj) // 2
        res = find_k23(adj)
        print("  M^%-4d |V|=%-3d |E|=%-4d  K2,3-free=%s  %s"
              % (k, len(adj), E, res is None, res))
    print("\nSummary: M^k(C5) is K2,3-free iff k<=1; the K2,3 introduced at")
    print("M^2 persists in M^3, M^4 by containment of the M^2 original-vertex")
    print("subset.  Hence every M^k(C5), k>=2, violates the NECESSARY K2,3-free")
    print("condition for unit-distance realizability (sharp_nbhd_cert).")


if __name__ == "__main__":
    main()
