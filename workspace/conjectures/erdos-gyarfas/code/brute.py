"""Naive oracle for the Erdos-Gyarfas conjecture.

Given a finite simple graph, return its minimum degree and the exact set of
its cycle lengths.  Obviously correct rather than fast: minimum degree by
counting neighbours, cycle lengths by brute-force enumeration of all simple
cycles.  Exact integer arithmetic throughout.

Exports:
    minimum_degree(G) -> int
    cycle_lengths(G)  -> frozenset[int]   (set of lengths of all simple cycles)
    oracle(G)         -> (min_degree, cycle_lengths)

Validation (hand-checkable answers, reproduced by __main__):
    K4      min degree 3, cycles {3, 4}
    K3,3    min degree 3, cycles {4, 6}
    cube    min degree 3, cycles {4, 6, 8}
    Petersen min degree 3, cycles {5, 6, 8, 9}
"""
import networkx as nx


def minimum_degree(G):
    """Minimum degree of graph G, exact integer."""
    return min(d for _, d in G.degree())


def cycle_lengths(G):
    """Exact set of cycle lengths present in G.

    Enumerates every simple cycle by brute force (networkx.simple_cycles),
    so this is O(sum of all simple cycles) — fine for a hand-check oracle on
    tiny graphs, never the method at full size.
    """
    # simple_cycles on the bidirected graph yields length-2 "cycles" (one edge
    # forward and back); a genuine cycle in a simple graph has length >= 3.
    lengths = {len(c) for c in nx.simple_cycles(G.to_directed()) if len(c) >= 3}
    return frozenset(lengths)


def oracle(G):
    """Return (min_degree, sorted tuple of cycle lengths)."""
    return minimum_degree(G), tuple(sorted(cycle_lengths(G)))


def _builtins():
    """The hand-checkable graphs from the brief."""
    return {
        "K4": (nx.complete_graph(4), (3, (3, 4))),
        "K3,3": (nx.complete_bipartite_graph(3, 3), (3, (4, 6))),
        "cube": (nx.hypercube_graph(3), (3, (4, 6, 8))),
        "Petersen": (nx.petersen_graph(), (3, (5, 6, 8, 9))),
    }


if __name__ == "__main__":
    print("brute.py oracle — minimum degree and exact cycle-length set")
    ok = True
    for name, (G, expected) in _builtins().items():
        got = oracle(G)
        match = "MATCH" if got == expected else "MISMATCH"
        if got != expected:
            ok = False
        print(f"  {name:10s} min_deg={got[0]:2d} cycles={got[1]}  "
              f"expected={expected}  -> {match}")
    print("ALL MATCH" if ok else "MISMATCHES PRESENT")
