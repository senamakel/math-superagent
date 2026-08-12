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
    # networkx.simple_cycles only works on directed graphs. Convert the
    # undirected graph to a bidirected digraph (each edge u-v becomes arcs
    # u->v and v->u). Each undirected simple cycle of length L appears in the
    # digraph as exactly two length-L directed cycles (one per orientation),
    # so the *set* of lengths is unchanged. The digraph also produces spurious
    # 2-cycles (u->v->u) where the undirected graph has just an edge, which we
    # drop by keeping only lengths >= 3.
    dig = nx.DiGraph()
    dig.add_nodes_from(graph.nodes())
    for u, v in graph.edges():
        dig.add_edge(u, v)
        dig.add_edge(v, u)
    if cap is not None:
        it = _capped(nx.simple_cycles(dig), cap)
    else:
        it = nx.simple_cycles(dig)
    return {len(c) for c in it if len(c) >= 3}


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


def exists_delta3_no_power2_cycle(n, lines=None):
    """True iff some connected graph on ``n`` vertices has min degree >= 3 and
    contains no cycle of power-of-two length (>=4). This is the Erdős–Gyárfás
    counterexample predicate.

    ``lines`` is an iterable of graph6 strings for connected min-degree-3 graphs
    on n vertices (one per isomorphism class), produced by e.g.
    ``nauty-geng -q -c -d3 n``. If it is None, the function generates that set
    itself via nauty-geng. Exact; the enumeration is what is exponential, so
    n must stay small (this is the oracle edge).
    """
    if lines is None:
        lines = _geng_graph6(n)
    for g6 in lines:
        g6 = g6.strip()
        if not g6:
            continue
        G = nx.from_graph6_bytes(g6.encode())
        if min_degree(G) >= 3 and not has_power_of_two_cycle(G):
            return True
    return False


def _geng_graph6(n):
    import subprocess
    proc = subprocess.run(
        ["nauty-geng", "-q", "-c", "-d3", str(n)],
        capture_output=True, text=True, check=True,
    )
    return proc.stdout.splitlines()


def report_delta3_no_power2(n, lines=None):
    """Return (count_checked, counterexamples) where counterexamples is a list
    of graph6 strings of graphs on n vertices with min degree >=3 and no
    power-of-two cycle. Every min-degree-3 connected graph on n vertices (up to
    iso) is checked. Exact."""
    if lines is None:
        lines = _geng_graph6(n)
    seen = 0
    counterexamples = []
    for g6 in lines:
        g6 = g6.strip()
        if not g6:
            continue
        G = nx.from_graph6_bytes(g6.encode())
        if min_degree(G) < 3:
            continue
        seen += 1
        if not has_power_of_two_cycle(G):
            counterexamples.append(g6)
    return seen, counterexamples
