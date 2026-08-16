"""Canonical-hash deduplicated generation of 2-connected simple graphs by ear
decomposition (fast version).

THEOREM (ear decomposition; Diestel, Graph Theory, §3.1): a graph is
2-connected iff it can be built from a cycle by successively adding an ear
(a path with new internal vertices between two existing vertices, or a single
chord between two existing non-adjacent vertices). Seeding with every cycle
and closing under both ear types therefore generates exactly the class of
2-connected graphs (this is a construction of a well-defined class, not a
search over a candidate space).

Dedup replaces the pairwise exact-isomorphism scan (O(k^2) VF2 comparisons per
level, k = graphs at that level) with a canonical-form hash: each graph is
keyed by its Weisfeiler-Lehman graph hash, and exact VF2 isomorphism is checked
only within the (tiny) bucket of graphs sharing that hash. This is exact —
same-hash is necessary, not sufficient, so is-isomorphic is still resolved by
isomorphism within a bucket — and it turns the near-quadratic scan into a
near-linear one. WL-hash is cheap (polynomial), so per-graph work stays
polynomial.

Complexity: the 2-connected class is super-exponential, so generation is only
run to the N where the class is still tractable. Algebra of dedup: O(total
graphs) WL hashes + O(sum over buckets of bucket^2) VF2 checks; buckets are
typical singleton, so this is near-linear in the number of graphs.
"""

import networkx as nx
from networkx.algorithms.graph_hashing import weisfeiler_lehman_graph_hash


def _cycle_graph(n):
    return nx.cycle_graph(n)


def _add_path_ear(G, u, v, k):
    """New graph: path ear u-x1-...-xk-v, k>=1 new vertices, endpoints u,v existing."""
    H = G.copy()
    base = H.number_of_nodes()
    prev = u
    for i in range(k):
        w = base + i
        H.add_node(w)
        H.add_edge(prev, w)
        prev = w
    H.add_edge(prev, v)
    return H


def _add_chord(G, u, v):
    """New graph with edge (u,v) added (endpoints existing, non-adjacent)."""
    H = G.copy()
    H.add_edge(u, v)
    return H


def generate_2connected_levels_hash(n_target):
    """All 2-connected graphs on each vertex count 3..n_target, dedup by
    WL-hash bucket + exact VF2 within bucket. Returns dict n -> list of Graphs."""
    levels = {m: [] for m in range(3, n_target + 1)}
    buckets = {m: {} for m in range(3, n_target + 1)}  # level -> {wlhash: [graphs]}

    def add_to_level(H):
        m = H.number_of_nodes()
        if m > n_target:
            return False
        if m < 3:
            return False
        h = weisfeiler_lehman_graph_hash(H)
        for R in buckets[m].get(h, []):
            if nx.is_isomorphic(H, R):
                return False
        buckets[m].setdefault(h, []).append(H)
        levels[m].append(H)
        return True

    # Seed: every cycle.
    for l in range(3, n_target + 1):
        add_to_level(_cycle_graph(l))

    # Grrow: non-trivial ears push to higher levels, chords stay in-level (loop).
    worklist = [G for ms in levels.values() for G in ms]
    while worklist:
        G = worklist.pop()
        m = G.number_of_nodes()
        verts = list(G.nodes())
        for k in range(1, n_target - m + 1):
            for u in verts:
                for v in verts:
                    if u == v:
                        continue
                    H = _add_path_ear(G, u, v, k)
                    if add_to_level(H):
                        worklist.append(H)
        for i in range(len(verts)):
            for j in range(i + 1, len(verts)):
                u, v = verts[i], verts[j]
                if not G.has_edge(u, v):
                    H = _add_chord(G, u, v)
                    if add_to_level(H):
                        worklist.append(H)
    return levels


def min_degree(G):
    return min(dict(G.degree()).values()) if G.number_of_nodes() > 0 else 0
