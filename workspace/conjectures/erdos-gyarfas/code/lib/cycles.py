"""Exact cycle-length and minimum-degree oracle for small graphs.

This module answers the questions the Erdős–Gyárfás run depends on: for a
given graph, what is its minimum degree, and what is the *exact* set of
lengths of simple cycles present. The cycle-length set is computed by
enumerating every simple cycle (via networkx.simple_cycles) and collecting
the set of their lengths. That is exact but exponential in the worst case, so
it is an *oracle*: use it only on small graphs (the sizes where the conjecture
is being checked exhaustively, roughly n <= 30 by cycle count). It is the
ground truth that everything else on this run is checked against.

Every function takes a networkx.Graph (simple, unweighted) and returns exact
Python integers / sets / booleans. No floating point anywhere.
"""

import networkx as nx


def min_degree(graph):
    """Minimum degree of ``graph`` (a networkx.Graph). Exact.

    An isolated vertex contributes degree 0; the empty graph returns 0. Uses
    the correct (not potential) degrees regardless of how the graph was built.
    """
    if graph.number_of_nodes() == 0:
        return 0
    return min(d for _, d in graph.degree())


def girth(graph):
    """Length of the shortest simple cycle, or None if the graph is acyclic.

    Exact. Uses a BFS from every vertex to find the shortest cycle through
    that vertex, then takes the minimum.
    """
    lengths = cycle_lengths(graph)
    return min(lengths) if lengths else None


def cycle_lengths(graph, max_nodes=None, cap=None):
    """Exact set of lengths of simple cycles in ``graph``.

    Enumerates every simple cycle via networkx.simple_cycles and collects the
    set of their lengths. ``cap`` is an optional safety limit on the number of
    cycles to enumerate (raises RuntimeError if exceeded) — the caller's guard
    against an unexpectedly large graph; it does not change the result for the
    graphs it returns on. ``max_nodes`` is passed straight to
    networkx.simple_cycles (limit on input size when the graph is huge; do not
    use for exactness-critical calls).
    """
    if cap is not None:
        it = _capped(nx.simple_cycles(graph), cap)
    else:
        it = nx.simple_cycles(graph)
    return {len(c) for c in it}


def _capped(iterator, cap):
    for i, item in enumerate(iterator):
        if i >= cap:
            raise RuntimeError(
                f"cycle_lengths exceeded cap of {cap} cycles; graph too large "
                "for the oracle — raise cap only if you understand the cost"
            )
        yield item


def has_power_of_two_cycle(graph, min_length=4):
    """True iff some simple cycle has length a power of two >= ``min_length``.

    The Erdős–Gyárfás conjecture concerns powers of two; 2 itself (=1,2) is
    not a cycle and length 4 is the first relevant one, hence default
    min_length=4. Exact.
    """
    n = 1
    while n < min_length:
        n *= 2
    for length in cycle_lengths(graph):
        if length >= min_length and _is_power_of_two(length):
            return True
    return False


def _is_power_of_two(x):
    return x > 0 and (x & (x - 1)) == 0


def power_of_two_cycle_lengths(graph, min_length=4):
    """The subset of cycle lengths that are powers of two >= min_length."""
    n = 1
    while n < min_length:
        n *= 2
    return sorted(
        l for l in cycle_lengths(graph)
        if l >= min_length and _is_power_of_two(l)
    )
