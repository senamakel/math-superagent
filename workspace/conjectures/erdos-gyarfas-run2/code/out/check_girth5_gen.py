"""Validate girth5_gen against the full 2-connected generator filtered by girth
AND min-degree>=3 — the only class the chord-deletion scan uses.

The pruning argument (only C5 seed + keep girth>=5) is only claimed COMPLETE
for the min-degree>=3 class: a min-degree-3 girth>=5 graph below the Moore-bound
floor (n<=11) has girth exactly 5, so it has a 5-cycle and a C5 ear-decomposition
base. Pure C6/C7 (girth 6, min-degree 2) are correctly excluded by the delta>=3
filter, and there are no min-degree-3 girth>=6 graphs below 14 vertices.
"""
import networkx as nx
from lib.girth5_gen import generate_2connected_girth_atleast5, girth, min_degree
from lib.biconnected_gen_hash import generate_2connected_levels_hash


def canon_edges(G):
    from lib.canonical import canonical_key
    return canonical_key(G)


def main(N=7):
    print(f"{'n':>3} | d3_girth>=5(g5gen) | d3_girth>=5(full) | match")
    ok = True
    full_levels = generate_2connected_levels_hash(N)
    for n in range(5, N + 1):
        from_gen = [G for G in generate_2connected_girth_atleast5(n).get(n, [])
                    if min_degree(G) >= 3]
        full = [G for m, gs in full_levels.items() for G in gs
                if G.number_of_nodes() == n and girth(G) >= 5 and min_degree(G) >= 3]
        k_gen = {canon_edges(G) for G in from_gen}
        k_full = {canon_edges(G) for G in full}
        match = k_gen == k_full
        ok = ok and match
        print(f"{n:>3} | {len(k_gen):>12} | {len(k_full):>14} | {str(match):>5}")
        if not match:
            only_full = k_full - k_gen
            print(f"       only in full: {len(only_full)}")
            for k in only_full:
                pass
    print("ALL MATCH" if ok else "MISMATCH")


if __name__ == "__main__":
    main()
