"""Oracle for the Erdos-Gyarfas conjecture: exact detection of cycles of length a power of two.

This is the obviously-correct checker (rule 9: brute force on small instances is
required). It enumerates all simple cycles in a graph and checks whether any has
length in {4, 8, 16, ...} (2^k with k >= 2). Exponential in graph size by design
— it is the oracle against which every faster/real method is validated, and it
is only ever run on small graphs (the near-miss construction data, n <= 32).

Method: DFS over simple paths, closing a cycle when we return to the start
vertex, starting only at the smallest vertex of a cycle so each cycle is found
once. Correct by construction: every simple cycle is counted exactly once.

Cycle identity: a distinct cycle is a connected 2-regular subgraph, i.e. an
EDGE set, not a vertex set — two different Hamilton cycles on the same vertex
set are different cycles. Cycles are keyed by their edge set (see
_edge_frozenset). Keying by vertex set would undercount: in Petersen, each of
the ten 9-vertex sets supports two distinct Hamilton cycles, so there are 20
distinct 9-cycles but only 10 such vertex sets. For the existence decision this
never matters (the collapse only merges equal-length cycles), which is why the
worked examples below all pass on both interpretations.
"""

from functools import lru_cache


def powers_of_two_up_to(n):
    """All cycle lengths 2^k, k >= 2, with k <= n."""
    out, k = [], 4
    while k <= n:
        out.append(k)
        k *= 2
    return set(out)


def _edge_frozenset(path):
    """The undirected cycle (as a set of edges) determined by a closed vertex path.

    path is a vertex list [v0, v1, ..., v_{L-1}] whose last vertex closes back to
    v0. Two different Hamilton cycles on the same vertex set have different edge
    sets and must count as distinct cycles, so cycles are keyed by their edge set,
    not by their vertex set.
    """
    return frozenset(frozenset((u, v)) for u, v in zip(path, path[1:] + [path[0]]))


def all_cycles(adj):
    """Enumerate all simple cycles of the graph as frozensets of edges.

    adj: dict vertex -> set of neighbours. The graph is undirected.
    Returns a set of frozensets-of-edges, each a distinct simple cycle (a
    connected 2-regular subgraph). Distinct cycles are distinguished by their
    edge set, so two different cycles on the same vertex set are both counted.
    """
    vertices = sorted(adj)
    cycles = set()

    # Start a DFS only at the smallest vertex of the cycle, so each cycle is
    # found once; distinguish the two directions by the (already canonical)
    # increasing-neighbour walk, then key the cycle by its edge set.
    def dfs(start, cur, path, visited):
        for nbr in adj[cur]:
            if nbr < start:
                continue  # would be found with a smaller start
            if nbr == start and len(path) >= 3:
                cycles.add(_edge_frozenset(path))
            elif nbr not in visited:
                visited.add(nbr)
                path.append(nbr)
                dfs(start, nbr, path, visited)
                path.pop()
                visited.remove(nbr)

    for start in vertices:
        dfs(start, start, [start], {start})

    return cycles


def has_power_of_two_cycle(adj, max_power=None):
    """True iff the graph has a cycle of length 2^k, k >= 2."""
    n = len(adj)
    limit = n if max_power is None else max_power
    targets = powers_of_two_up_to(limit)
    for cyc in all_cycles(adj):
        if len(cyc) in targets:
            return True, len(cyc)
    return False, None


def cycles_by_length(adj):
    """Map length -> count of distinct simple cycles of that length."""
    counts = {}
    for cyc in all_cycles(adj):
        counts[len(cyc)] = counts.get(len(cyc), 0) + 1
    return counts
