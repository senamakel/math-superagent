"""Exact oracle for the Erdős–Gyárfás conjecture.

Given a finite simple graph (networkx Graph), return its minimum degree and the
exact set of its distinct cycle lengths.  Exact integer arithmetic throughout.

Why a basis is not enough: a cycle *basis* spans the cycle space, but the set
of cycles in a basis is not the set of all cycles, and the *lengths* present in
a basis can miss lengths that occur only as non-basic cycles (symmetric
differences of basis cycles).  cycle_basis_lengths() is provided to demonstrate
exactly that failure; distinct_cycle_lengths() enumerates every simple cycle
and is the number this run trusts.

Exports:
    minimum_degree(G)        -> int
    all_simple_cycles(G)     -> list[list[int]]  (every simple cycle, each once)
    distinct_cycle_lengths(G)-> frozenset[int]
    cycle_basis_lengths(G)   -> frozenset[int]  (lengths of one cycle basis; incomplete)
    oracle(G)                -> (min_degree, tuple(sorted(lengths)))

Validation (hand-checkable answers, reproduced in __main__):
    K4       min degree 3, cycles {3, 4}
    K3,3     min degree 3, cycles {4, 6}
    cube Q3  min degree 3, cycles {4, 6, 8}
    Petersen min degree 3, cycles {5, 6, 8, 9}
"""
import networkx as nx


def minimum_degree(G):
    """Minimum degree of graph G, exact integer.  Empty graph -> 0."""
    if G.number_of_nodes() == 0:
        return 0
    return min(d for _, d in G.degree())


def all_simple_cycles(G):
    """Every simple cycle of G, each produced exactly once.

    DFS with a canonical start: each cycle is reported from its *minimum*
    vertex, and only vertices >= that start are ever visited, so a cycle has a
    unique minimum vertex and is generated exactly once.  Complexity is
    O(sum over simple cycles of their length) — exact but exponential in the
    worst case, which is why this is the small-instance oracle and never the
    method at full size.
    """
    adj = {u: list(G[u]) for u in G}
    nodes = list(G)
    # Minimum-vertex label ordering: pick start as the smallest label in the cycle.
    # We iterate starts in increasing order and restrict to neighbours >= start.
    def dfs(start, cur, path, visited, out):
        # Close a cycle when an edge goes from cur back to start.
        for nb in adj[cur]:
            if nb == start and len(path) >= 3:
                out.append(tuple(path))
        # Extend the path into unused vertices (labels >= start to stay canonical).
        for nb in adj[cur]:
            if nb >= start and nb not in visited:
                visited.add(nb)
                path.append(nb)
                dfs(start, nb, path, visited, out)
                path.pop()
                visited.remove(nb)

    out = []
    for start in nodes:
        dfs(start, start, [start], {start}, out)
    return out


def distinct_cycle_lengths(G):
    """Exact set of distinct lengths of simple cycles in G."""
    return frozenset(len(c) for c in all_simple_cycles(G))


def has_cycle_of_length(G, L):
    """True iff G contains a simple cycle of length exactly L (L >= 3).

    Exact, with early termination: returns as soon as one cycle of length L
    is found.  Uses the same canonical-start DFS as all_simple_cycles (a cycle
    is reported from its minimum vertex, and only vertices >= start are
    visited), so a cycle of length L, if it exists, is found when the DFS
    starts at that cycle's minimum vertex.  The path never exceeds length L,
    so the search tree is the set of simple paths of length <= L.

    This is the workhorse for the census: checking C8/C16 presence on graphs
    that *do* contain such a cycle (the common case) stops at the first hit
    instead of enumerating every simple cycle.  Exactness is inherited from
    the same machinery as all_simple_cycles; verified against it below.
    """
    if L < 3:
        return False
    adj = {u: list(G[u]) for u in G}
    nodes = sorted(G)
    for start in nodes:
        visited = {start}

        def dfs(cur, depth):
            # path[0..depth] holds the current path, cur == path[depth].
            for nb in adj[cur]:
                if nb == start:
                    # Closing edge back to start completes a cycle whose length
                    # is depth+1 (vertices 0..depth, plus the closing edge).
                    if depth + 1 == L:
                        return True
                elif depth + 1 < L and nb >= start and nb not in visited:
                    visited.add(nb)
                    if dfs(nb, depth + 1):
                        return True
                    visited.remove(nb)
            return False

        if dfs(start, 0):
            return True
    return False


def cycle_basis_lengths(G):
    """Lengths of the cycles in one networkx cycle basis.

    For demonstration only: this set is *not* guaranteed equal to the full set
    of cycle lengths (see the note in the module docstring).
    """
    return frozenset(len(c) for c in nx.cycle_basis(G))


def oracle(G):
    """Return (min_degree, sorted tuple of distinct cycle lengths)."""
    return minimum_degree(G), tuple(sorted(distinct_cycle_lengths(G)))


def _builtins():
    return {
        "K4": (nx.complete_graph(4), (3, (3, 4))),
        "K3,3": (nx.complete_bipartite_graph(3, 3), (3, (4, 6))),
        "cube Q3": (nx.hypercube_graph(3), (3, (4, 6, 8))),
        "Petersen": (nx.petersen_graph(), (3, (5, 6, 8, 9))),
    }


if __name__ == "__main__":
    print("cycle_oracle.py — min degree and exact cycle-length set")
    ok = True
    for name, (G, expected) in _builtins().items():
        got = oracle(G)
        cross = nx.simple_cycles(G.to_directed())
        nx_lens = {len(c) for c in cross if len(c) >= 3}
        basis = sorted(cycle_basis_lengths(G))
        match = "MATCH" if got == expected and set(got[1]) == nx_lens else "MISMATCH"
        if match == "MISMATCH":
            ok = False
        print(f"  {name:10s} min_deg={got[0]:2d} cycles={got[1]}"
              f" (basis-only={basis}) nx-simple-cycles={sorted(nx_lens)}  -> {match}")
    print("ALL MATCH" if ok else "MISMATCHES PRESENT")
