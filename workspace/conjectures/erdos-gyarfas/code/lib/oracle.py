"""Exact oracle for the Erdos-Gyarfas conjecture: minimum degree and cycle lengths.

This is the run's base checker. Every claim about small graphs later in the run
rests on this file being right, so it is deliberately naive: cycle lengths come
from walking every simple cycle by DFS and deduping on the vertex sets. Exact
integer arithmetic, no floats.

Verified two ways (both must be re-run if this file changes):
  1. by hand on K4, K3,3, the Petersen graph, and the cube Q3 -- answers stated
     independently of any library;
  2. against networkx.simple_cycles on the same four graphs.
All four matched (see code/brute.py, which reproduces them).

NOTE ON COMPLEXITY: cycle-length enumeration is exponential in the worst case,
so call it only on small graphs (<= ~12 vertices). It is the oracle, not the
method; the efficient structural work is elsewhere.
"""

from __future__ import annotations


def minimum_degree(adj):
    """Minimum vertex degree of an adjacency-list graph (list of lists)."""
    return min(len(neigh) for neigh in adj)


def cycle_lengths(adj):
    """Exact set of simple-cycle lengths, by naive DFS enumeration.

    adj: list of lists, vertices 0..n-1, no self-loops or duplicate edges.
    Returns a set of cycle lengths. A cycle is identified by the set of its
    vertices (unique in a simple graph), so duplicates are eliminated by
    storing frozensets.
    """
    seen_cycles = set()        # frozenset of vertices on each simple cycle
    for start in range(len(adj)):
        stack = [(start, [start])]
        while stack:
            node, path = stack.pop()
            for w in adj[node]:
                if w == start and len(path) >= 3:
                    seen_cycles.add(frozenset(path))
                elif w not in path:
                    stack.append((w, path + [w]))
    return {len(c) for c in seen_cycles}


def powers_of_two_cycle_lengths(lengths, min_k=2):
    """Which lengths in the set are powers of two 2^k with k >= min_k.

    The conjecture uses k >= 2 (cycles of length 4, 8, 16, ...): a simple graph
    has no cycles of length 1 or 2, so k=0,1 are vacuous. Pass a different
    min_k if a formal convention includes them.
    """
    top = max(lengths, default=0)
    out = set()
    k, p = min_k, 1 << min_k
    while p <= top:
        if p in lengths:
            out.add(p)
        k += 1
        p = 1 << k
    return frozenset(out)


def has_power_of_two_cycle(lengths, min_k=2):
    """True iff any cycle length is a power of two (2^k, k >= min_k)."""
    return len(powers_of_two_cycle_lengths(lengths, min_k)) > 0


def from_graph6(g6):
    """Adjacency list from a single graph6 byte/str (as nauty-geng prints)."""
    import networkx as nx
    b = g6 if isinstance(g6, bytes) else g6.encode("ascii")
    G = nx.from_graph6_bytes(b)
    return [sorted(int(w) for w in G.neighbors(v)) for v in range(G.number_of_nodes())]


def from_networkx(G):
    """Adjacency list from a networkx Graph (vertices relabelled 0..n-1)."""
    return [sorted(int(w) for w in G.neighbors(v)) for v in range(G.number_of_nodes())]
