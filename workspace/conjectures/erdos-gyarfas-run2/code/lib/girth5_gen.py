"""Exact generation of 2-connected graphs with girth >= 5 by ear decomposition,
with girth-pruning and canonical-hash dedup.

THEOREM (open ear decomposition; Diestel, Graph Theory, Sec 3.1): a graph is
2-connected iff it has an open ear decomposition, and every open ear
decomposition of a 2-connected graph can be started from ANY of its cycles.
Adding ears only ever ADDS edges, never removes them, so every intermediate
graph of an ear decomposition is an edge-subgraph of the final graph. Therefore
if the final graph has girth >= 5 (no cycle of length <= 4), every intermediate
graph also has girth >= 5; conversely, pruning any intermediate graph that has
a cycle of length <= 4 cannot discard any girth>=5 graph.

Completeness for girth-5 graphs: a graph of girth 5 contains a 5-cycle, and
(Whitney / Diestel) has an open ear decomposition starting at any chosen cycle,
so seeding with C5 and closing under ears with girth>=5 kept reaches every
2-connected girth-5 graph. (For general girth>=g, seed with C_g.) Graphs of
girth > 5 are NOT reached by the C5 seed, but on vertex counts below the
Moore-bound floor for girth 6 (>= 14 for min-degree 3) there are none among
min-degree>=3 graphs, which is the only class this module is used for.

Girth is measured as the shortest cycle length (per-edge BFS: for each edge
(u,v), delete it and find the shortest u-v path; taking the min of path_length
+ 1 over edges gives the girth). Correct for simple graphs.

Dedup by Weisfeiler-Lehman graph-hash bucket + exact VF2 isomorphism within the
bucket (same-hash is necessary, not sufficient) — exact, near-linear in the
number of graphs emitted.

Complexity: the 2-connected class is super-exponential, but the girth-5 subclass
below the Moore-bound floor (n <= 11 for min-degree 3) is tiny; this module is
only run in that range. Per-graph work (girth test + hash + dedup) is polynomial.
"""

import networkx as nx
from networkx.algorithms.graph_hashing import weisfeiler_lehman_graph_hash


def girth(G):
    """Shortest cycle length of a simple graph (None if acyclic / no cycle)."""
    best = None
    for u, v in G.edges():
        H = G.copy()
        H.remove_edge(u, v)
        try:
            d = nx.shortest_path_length(H, u, v)
        except nx.NetworkXNoPath:
            continue
        cand = d + 1
        if best is None or cand < best:
            best = cand
    return best


def _add_path_ear(G, u, v, k):
    """New graph: path ear u-x1-...-xk-v, k>=1 new internal vertices, endpoints existing."""
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
    H = G.copy()
    H.add_edge(u, v)
    return H


def generate_2connected_girth_atleast5(n_target):
    """All 2-connected graphs on each vertex count 3..n_target with girth >= 5,
    dedup by WL-hash bucket + exact VF2. Returns dict n -> list of Graphs.

    Only the C5 seed is used, so this reaches exactly the 2-connected graphs of
    girth 5 (plus graphs of girth >=5 built from a 5-cycle). For min-degree>=3
    on n <= 11 there are no girth>=6 graphs (Moore bound), so this is the whole
    girth-5 min-degree-3 class in that range.
    """
    levels = {m: [] for m in range(3, n_target + 1)}
    buckets = {m: {} for m in range(3, n_target + 1)}

    def add_to_level(H):
        m = H.number_of_nodes()
        if m > n_target:
            return False
        if girth(H) < 5:
            return False  # prune: a <=4-cycle can never be removed by later ears
        h = weisfeiler_lehman_graph_hash(H)
        for R in buckets[m].get(h, []):
            if nx.is_isomorphic(H, R):
                return False
        buckets[m].setdefault(h, []).append(H)
        levels[m].append(H)
        return True

    # Seed: the 5-cycle (the only valid girth-5 base; larger cycles would build
    # graphs of girth >= their length, which do not arise as min-degree-3 below
    # the Moore-bound floor).
    add_to_level(nx.cycle_graph(5))

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
