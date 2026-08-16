"""Verify the two load-bearing lemmas of the adopted approach
(research/approaches/edge-deletion-2adic-transfer.md) on all 2-connected
min-degree>=3 graphs on n <= 8.

Lemma A (reduction exists): every 2-connected graph G with delta(G) >= 3 has a
chord e = ab such that H = G - e is 2-connected and delta(H) >= 2.
   (Classical: minimally-2-connected graphs have min degree 2, so a delta>=3
   2-connected graph is not minimally 2-connected; the last ear in an open-ear
   decomposition is a single chord. The numeric check confirms the existence of
   at least one such chord on every graph in the class up to n=8.)

Lemma B (cycle transfer): for any such e = ab with H = G - e, the cycle-length
set satisfies C(G) = C(H) U { |P|+1 : P a simple a-b path in H }.
   Reasoning, not enumeration: every simple cycle of G either avoids e (it is
   a cycle of H) or contains e (it is an a-b path of H with e appended), so the
   identity holds for EVERY edge e, independently of 2-connectivity or degree.
   The oracle check below confirms it mechanically on the chosen primary chord
   for every graph in the class, by direct enumeration of C(G), C(H), and the
   a-b path lengths.

Runs on the committed generator path (lib.biconnected_gen_hash), NOT ad-hoc
regeneration. n=4..8 delta>=3: 1 + 3 + 19 + 149 + 2581 = 2753 graphs.
Expected wall time: ~40s (generation ~27s + checks ~12s).
"""
import networkx as nx
from lib.biconnected_gen_hash import generate_2connected_levels_hash


def min_degree(G):
    return min(dict(G.degree()).values()) if G.number_of_nodes() > 0 else 0


def adj_of(G):
    return {v: set(G.neighbors(v)) for v in G.nodes()}


def cycle_length_set(adj):
    """Set of lengths of all simple cycles (via lib.erdos_gyarfas.all_cycles)."""
    from lib.erdos_gyarfas import all_cycles
    return {len(c) for c in all_cycles(adj)}


def simple_path_lengths(adj, a, b):
    """All lengths of simple a-b paths in the graph (excluding the trivial path)."""
    out = set()
    seen_vertices = {a}
    path_len = 0

    def dfs(cur):
        nonlocal path_len
        for nbr in adj[cur]:
            if nbr == b and path_len + 1 >= 2:
                out.add(path_len + 1)
            elif nbr not in seen_vertices:
                seen_vertices.add(nbr)
                path_len += 1
                dfs(nbr)
                path_len -= 1
                seen_vertices.remove(nbr)

    dfs(a)
    return out


def find_transfer_chord(G):
    """Return (a, b, H_adj) for a chord e=ab with G-e 2-connected and delta>=2,
    or None if none exists (would refute Lemma A)."""
    for a, b in G.edges():
        H = G.copy()
        H.remove_edge(a, b)
        if nx.is_biconnected(H) and min_degree(H) >= 2:
            return a, b, adj_of(H)
    return None


def main(N=8):
    levels = generate_2connected_levels_hash(N)
    n_graphs = 0
    # Lemma A: existence of a transfer chord (G-e 2-connected, delta>=2).
    for n in range(3, N + 1):
        for G in levels.get(n, []):
            if min_degree(G) < 3:
                continue
            n_graphs += 1
            Ga = adj_of(G)
            C_G = cycle_length_set(Ga)
            res = find_transfer_chord(G)
            if res is None:
                print(f"LEMMA A FAILS at n={n}: no transfer chord for {sorted(G.edges())}")
                return
            a, b, Ha = res
            C_H = cycle_length_set(Ha)
            P = simple_path_lengths(Ha, a, b)
            predicted = C_H | {p + 1 for p in P}
            if predicted != C_G:
                print(f"LEMMA B FAILS at n={n}:")
                print("  edges:", sorted(G.edges()), " chord:", (a, b))
                print("  C(G) =", sorted(C_G))
                print("  predicted =", sorted(predicted))
                print("  C(H) =", sorted(C_H), " path lens:", sorted(P))
                return
    for n in range(3, N + 1):
        cnt = sum(1 for G2 in levels.get(n, []) if min_degree(G2) >= 3)
        print(f"  n={n}: {cnt} graphs")
    print(f"BOTH LEMMAS VERIFIED on all {n_graphs} two-connected delta>=3 graphs, n<={N}")


if __name__ == "__main__":
    main()
