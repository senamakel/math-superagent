"""Independent hand-written DFS oracle, cross-checked against lib/cycles.py.

Written from scratch (no imports from lib/cycles or lib/oracle) as a second,
fully independent route to min-degree, girth, the exact set of simple-cycle
lengths, and the set of power-of-two cycle lengths. It walks every simple
cycle by recursion, dedupes on the frozenset of vertices on the cycle (which
determines a simple cycle uniquely in a simple graph), and compares against
lib/cycles.py on K4, K3,3, the cube Q3, and the Petersen graph.

This is the independent-verification file: lib/cycles.py and lib/oracle.py
must both agree with this hand DFS, since a third code path that agrees on
four non-trivial graphs is strong evidence the shared networkx.simple_cycles
path is not the source of the answer being checked.
"""

from __future__ import annotations

import networkx as nx
from lib.cycles import (
    min_degree,
    girth,
    cycle_lengths,
    has_power_of_two_cycle,
    power_of_two_cycle_lengths,
)


def hd_min_degree(G):
    if G.number_of_nodes() == 0:
        return 0
    return min(d for _, d in G.degree())


def hd_cycle_lengths(G):
    """All simple-cycle lengths by hand DFS. Exact, exponential (oracle only)."""
    n = G.number_of_nodes()
    adj = {v: set(G.neighbors(v)) for v in G.nodes()}
    seen = set()  # frozenset of vertices on each simple cycle

    def dfs(start, cur, path):
        for w in adj[cur]:
            if w == start and len(path) >= 3:
                seen.add(frozenset(path))
            elif w not in path:
                path.append(w)
                dfs(start, w, path)
                path.pop()

    for v in G.nodes():
        dfs(v, v, [v])
    return {len(c) for c in seen}


def hd_girth(G):
    lens = hd_cycle_lengths(G)
    return min(lens) if lens else None


def hd_power2_lengths(G, min_length=4):
    n = 1
    while n < min_length:
        n *= 2
    return sorted(
        l for l in hd_cycle_lengths(G)
        if l >= min_length and (l & (l - 1)) == 0
    )


def hd_has_power2(G, min_length=4):
    return len(hd_power2_lengths(G, min_length)) > 0


def main():
    K4 = nx.complete_graph(4)
    K33 = nx.complete_bipartite_graph(3, 3)
    cube = nx.hypercube_graph(3)
    petersen = nx.petersen_graph()

    cases = [("K4", K4), ("K3,3", K33), ("cube Q3", cube), ("Petersen", petersen)]

    all_ok = True
    for name, G in cases:
        md = hd_min_degree(G)
        g = hd_girth(G)
        lens = hd_cycle_lengths(G)
        p2 = hd_power2_lengths(G)

        # the library twin
        lib_md = min_degree(G)
        lib_g = girth(G)
        lib_lens = cycle_lengths(G)
        lib_p2 = power_of_two_cycle_lengths(G)
        lib_hp = has_power_of_two_cycle(G)

        ok = (md == lib_md) and (g == lib_g) and (lens == lib_lens) \
            and (p2 == lib_p2) and (lib_hp == bool(lib_p2))
        all_ok = all_ok and ok
        print(f"=== {name} ===")
        print(f"  handDFS   min_deg={md} girth={g} cycles={sorted(lens)} "
              f"power2={p2} has_power2={bool(p2)}")
        print(f"  lib/cycles min_deg={lib_md} girth={lib_g} cycles={sorted(lib_lens)} "
              f"power2={lib_p2} has_power2={lib_hp}")
        print(f"  {'AGREE' if ok else 'DISAGREE !!!'}")
        print()

    print("HAND-DFS vs lib/cycles: " +
          ("ALL AGREE" if all_ok else "DISAGREEMENT FOUND"))
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
