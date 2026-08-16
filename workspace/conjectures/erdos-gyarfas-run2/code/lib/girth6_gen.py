"""Exact generation of 2-connected graphs with girth >= g by open ear
decomposition, with girth-pruning and canonical-hash dedup. Generalizes
lib.girth5_gen to an arbitrary seed cycle length C_seed and a pruning floor.

THEOREM (open ear decomposition; Diestel, Graph Theory, Sec 3.1): a graph is
2-connected iff it has an open ear decomposition, and every such decomposition
of a 2-connected graph can be started from ANY of its cycles. Adding ears only
ever ADDS edges, never removes them, so every intermediate graph of an ear
decomposition is an edge-subgraph of the final graph. Hence:
  - if the final graph has girth >= g, every intermediate graph also has
    girth >= g (a <=g-cycle cannot be created and then destroyed), so pruning
    any intermediate graph that contains a cycle of length < g cannot discard
    a girth>=g graph;
  - every 2-connected girth-g graph contains a g-cycle and (Whitney / the same
    theorem) has an ear decomposition STARTING at that g-cycle, so seeding with
    C_g and closing under ears with girth >= g kept reaches the whole class.

CRITICAL seed/subclass correspondence: the ear decomposition of a graph that
contains a g-cycle can be started at that g-cycle, and every graph produced
from a C_g seed still CONTAINS that seed as a subgraph. Therefore, for graphs
of exactly girth g (no shorter cycle), the C_g-seeded generator reaches exactly
the 2-connected girth-g graphs:
  - C5 seed, prune girth>=5: every reached graph contains the original 5-cycle
    (ears only add edges/vertices, the seed persists), so it has a 5-cycle and
    girth exactly 5. Reaches exactly the 2-connected girth-5 graphs.
  - C6 seed, prune girth>=6: every reached graph contains a 6-cycle, and prune
    forbids girth<6, so girth exactly 6. Reaches exactly the 2-connected
    girth-6 graphs.
(For a general girth-g graph containing a g-cycle this is exactly the girth-g
class; the only graphs a C_g seed misses are those of girth != g, i.e. graphs
of larger girth with no g-cycle — none exist below the Moore-bound floor of the
degree class this module is used for, min-degree>=3: girth-7 needs >=22
vertices, so on n<=16 the girth-6 seed together with the girth-5 seed cover
the entire girth>=5 class.)

Girth measured as the shortest cycle length by per-edge BFS (for each edge uv,
delete it and find the shortest u-v path; min over edges of path_length+1).
Correct for simple graphs.

Dedup: Weisfeiler-Lehman graph-hash bucket + exact VF2 isomorphism within the
bucket (same hash is necessary, not sufficient) — exact, near-linear in the
number of graphs emitted. Per-graph work (girth test + hash + dedup) is
polynomial.

Complexity: the 2-connected class is super-exponential, but the girth>=g
subclass below the Moore-bound floor of the degree class is tiny; this module
is only run in that range. The girth-pruning is what makes n=16 feasible: each
intermediate graph must stay girth>=g, which brutally restricts the search on
the min-degree>=3 class.
"""

import networkx as nx
from networkx.algorithms.graph_hashing import weisfeiler_lehman_graph_hash


def girth(G):
    """Shortest cycle length of a simple graph (None if acyclic)."""
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
    """New graph with edge (u,v) added (endpoints existing, non-adjacent)."""
    H = G.copy()
    H.add_edge(u, v)
    return H


def generate_2connected_girth_atleast(n_target, seed_len, min_girth):
    """All 2-connected graphs on each vertex count 3..n_target with girth >=
    min_girth, seeded with the cycle C_seed (seed_len), dedup by WL-hash + exact
    VF2 within bucket. Returns dict n -> list of Graphs.

    With C_seed = min_girth this reaches exactly the 2-connected graphs of
    girth exactly min_girth (every reached graph contains the seed cycle, and
    pruning forbids anything shorter).
    """
    levels = {m: [] for m in range(3, n_target + 1)}
    buckets = {m: {} for m in range(3, n_target + 1)}

    def add_to_level(H):
        m = H.number_of_nodes()
        if m > n_target:
            return False
        if girth(H) < min_girth:
            return False  # prune: a <g-cycle can never be removed by later ears
        h = weisfeiler_lehman_graph_hash(H)
        for R in buckets[m].get(h, []):
            if nx.is_isomorphic(H, R):
                return False
        buckets[m].setdefault(h, []).append(H)
        levels[m].append(H)
        return True

    # Seed: the C_seed cycle.
    add_to_level(nx.cycle_graph(seed_len))

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


def generate_2connected_girth6(n_target):
    """All 2-connected graphs of girth exactly 6 on <= n_target vertices;
    seeded with C6, pruned at girth>=6. Returns dict n -> list of Graphs."""
    return generate_2connected_girth_atleast(n_target, seed_len=6, min_girth=6)


def generate_2connected_girth5(n_target):
    """All 2-connected graphs of girth exactly 5 on <= n_target vertices;
    seeded with C5, pruned at girth>=5. Returns dict n -> list of Graphs."""
    return generate_2connected_girth_atleast(n_target, seed_len=5, min_girth=5)


def continue_girth_atleast_by_level(levels, buckets, n_target, min_girth,
                                    next_level):
    """Grow a partially-generated class (levels dict n->[Graph], buckets dict
    n->{wlhash:[Graph]} for dedup) from graphs of size >= next_level up to
    n_target, keeping girth >= min_girth. Mutates levels/buckets in place.
    Returns the new levels dict. Used to resume generation from a cached lower
    boundary without redoing it."""
    worklist = [G for m in range(next_level, n_target + 1) if m in levels
                for G in levels[m]]
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
                    if _try_add(H, levels, buckets, n_target, min_girth):
                        worklist.append(H)
        for i in range(len(verts)):
            for j in range(i + 1, len(verts)):
                u, v = verts[i], verts[j]
                if not G.has_edge(u, v):
                    H = _add_chord(G, u, v)
                    if _try_add(H, levels, buckets, n_target, min_girth):
                        worklist.append(H)
    return levels


def _try_add(H, levels, buckets, n_target, min_girth):
    """Shared add-to-level helper used by the resume generator."""
    m = H.number_of_nodes()
    if m > n_target:
        return False
    if girth(H) < min_girth:
        return False
    h = weisfeiler_lehman_graph_hash(H)
    for R in buckets.setdefault(m, {}).get(h, []):
        if nx.is_isomorphic(H, R):
            return False
    buckets[m].setdefault(h, []).append(H)
    levels.setdefault(m, []).append(H)
    return True


def min_degree(G):
    return min(dict(G.degree()).values()) if G.number_of_nodes() > 0 else 0
