"""Adjacency-list convenience layer over the shelved oracle, lib.cycles.

This module used to be a third, independent copy of the DFS cycle-length
oracle (adjacency-list flavoured), alongside code/brute.py and lib/cycles.py.
Those copies were the run ignoring its own library, so under consolidation the
two compute-cores (minimum degree, cycle-length set) now come from the single
shelved definition in `lib.cycles`. This file keeps its original public API
-- a graph described as an adjacency list (list of lists of ints, vertices
0..n-1) -- and converts to a networkx.Graph before delegating, so every answer
it returns is produced by the same code as every other caller on the run.

Its `powers_of_two_cycle_lengths` / `has_power_of_two_cycle` operate on the
returned set of cycle lengths (min_k >= 2 semantics): these are conveniences
kept here for the adjacency-list callers, and are exact integer arithmetic.

All-exact, no floats. Exponential only inside lib.cycles (small graphs only).
The results this returns are identical in value to what lib/cycles.py returns
on the same graph; the correctness of the core rests on lib/cycles.py, which
is verified against code/eg/hand_dfs_check.py and code/verify_cycles.py on
K4, K3,3, the Petersen graph and the cube Q3.
"""

from __future__ import annotations

import networkx as nx

from lib.cycles import min_degree as _md, cycle_lengths as _cl


def minimum_degree(adj):
    """Minimum vertex degree of an adjacency-list graph (list of lists)."""
    return _md(_to_graph(adj))


def cycle_lengths(adj):
    """Exact set of simple-cycle lengths of an adjacency-list graph."""
    return _cl(_to_graph(adj))


def powers_of_two_cycle_lengths(lengths, min_k=2):
    """Which lengths in the set are powers of two 2^k with k >= min_k."""
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


def _to_graph(adj):
    """Adjacency list (vertices 0..n-1) -> networkx.Graph (simple, undirected)."""
    G = nx.Graph()
    G.add_nodes_from(range(len(adj)))
    for u, neigh in enumerate(adj):
        for v in neigh:
            if u < v:
                G.add_edge(u, v)
    return G


def from_graph6(g6):
    """Adjacency list from a single graph6 byte/str (as nauty-geng prints)."""
    G = nx.from_graph6_bytes(g6 if isinstance(g6, bytes) else g6.encode("ascii"))
    return [sorted(int(w) for w in G.neighbors(v)) for v in range(G.number_of_nodes())]


def from_networkx(G):
    """Adjacency list from a networkx Graph (vertices relabelled 0..n-1)."""
    return [sorted(int(w) for w in G.neighbors(v)) for v in range(G.number_of_nodes())]
