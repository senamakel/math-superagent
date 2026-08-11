"""Naive oracle for the Erdos-Gyarfas conjecture.

Given a graph, return:
  * its minimum degree, and
  * the exact set of its simple-cycle lengths.

The cycle-length enumeration is the naive, obviously-correct method: walk every
simple cycle by DFS and dedupe on the set of vertices on the cycle (which
determines the cycle uniquely in a simple graph). It is exponential in the
worst case, so it is only meant for the small sizes of the worked examples --
not for anything near the verification bound. Exact integer arithmetic; no
floating point anywhere.

Inputs accepted:
  * an adjacency list (list of lists of ints), or
  * a networkx Graph, or
  * a graph6 byte string (as produced by nauty-geng).

Checks by hand against the worked examples:
  * K4       : min degree 3, cycle lengths {3, 4}
  * K3,3     : min degree 3, cycle lengths {4, 6}
  * Petersen : min degree 3, girth 5, cycle lengths {5, 6, 8, 9}
  * cube Q3  : min degree 3, cycle lengths {4, 6, 8}
"""

from __future__ import annotations


def minimum_degree(adj):
    """Minimum vertex degree of the adjacency-list graph."""
    return min(len(neigh) for neigh in adj)


def cycle_lengths(adj):
    """The exact set of simple-cycle lengths, by naive DFS enumeration."""
    n = len(adj)
    lengths = set()           # lengths discovered so far
    seen_cycles = set()       # frozenset of vertices on each simple cycle

    for start in range(n):
        # stack holds (current node, path from start to current)
        stack = [(start, [start])]
        while stack:
            node, path = stack.pop()
            for w in adj[node]:
                if w == start and len(path) >= 3:
                    # path from start back to start is a simple cycle
                    seen_cycles.add(frozenset(path))
                elif w not in path:
                    stack.append((w, path + [w]))

    return {len(c) for c in seen_cycles}


def powers_of_two_cycle_lengths(cycle_lengths_set, min_k=2):
    """Which cycle lengths are powers of two (2^k, k >= min_k)."""
    k = min_k
    p = 1 << k
    out = set()
    while p <= max(cycle_lengths_set, default=0):
        if p in cycle_lengths_set:
            out.add(p)
        k += 1
        p = 1 << k
    return out


def has_power_of_two_cycle(cycle_lengths_set, min_k=2):
    """Whether any cycle length is a power of two (2^k, k >= min_k)."""
    return bool(powers_of_two_cycle_lengths(cycle_lengths_set, min_k))


def from_graph6(g6):
    """Adjacency list from a graph6 byte string (single graph)."""
    import networkx as nx
    G = nx.from_graph6_bytes(g6 if isinstance(g6, bytes) else g6.encode("ascii"))
    return [sorted(G.neighbors(v)) for v in range(G.number_of_nodes())]


def from_networkx(G):
    """Adjacency list from a networkx Graph (vertices 0..n-1)."""
    return [sorted(int(w) for w in G.neighbors(v)) for v in range(G.number_of_nodes())]


def report(adj, name):
    """Print the oracle's answer for one graph and return (deg, lengths)."""
    deg = minimum_degree(adj)
    lens = cycle_lengths(adj)
    powlens = powers_of_two_cycle_lengths(lens)
    print(f"{name}: min degree = {deg}, cycle lengths = {sorted(lens)}, "
          f"power-of-two cycle lengths = {sorted(powlens)}")
    return deg, lens, powlens


# ---------------------------------------------------------------------------
# The worked examples, built by hand so the answers can be stated independently
# of any library.
# ---------------------------------------------------------------------------
def run_here():
    import networkx as nx

    # K4: complete graph on {0,1,2,3}.
    K4 = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
    report(K4, "K4")

    # K3,3: complete bipartite parts {0,1,2} and {3,4,5}.
    K33 = [[3, 4, 5], [3, 4, 5], [3, 4, 5], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
    report(K33, "K3,3")

    # Petersen graph: outer 5-cycle 0-1-2-3-4-0, inner 5-cycle 5-6-7-8-9-5,
    # spokes i-(i+5).
    P = [[] for _ in range(10)]
    for i in range(5):
        P[i].append((i + 1) % 5)
        P[(i + 1) % 5].append(i)
    for i in range(5):
        j = 5 + ((i + 2) % 5)   # pentagram step: inner 5,7,9,6,8
        P[5 + i].append(j)
        P[j].append(5 + i)
    for i in range(5):
        P[i].append(i + 5)
        P[i + 5].append(i)
    report(P, "Petersen")

    # Cube Q3: binary strings of length 3, adjacent if Hamming distance 1.
    Q = [[] for _ in range(8)]
    for a in range(8):
        for b in range(a + 1, 8):
            if (a ^ b).bit_count() == 1:
                Q[a].append(b)
                Q[b].append(a)
    report(Q, "cube Q3")

    # Also exercise the graph6 path: K4 in graph6 is "C~" (from nauty). Check
    # it agrees with the hand-built K4 above.
    print("graph6 K4:", report(from_graph6("C~"), "K4[g6]"))


if __name__ == "__main__":
    run_here()
