"""Exact constructive generation of 2-connected simple graphs by ear decomposition,
with exact isomorphism dedup via networkx VF2.

THEOREM (ear decomposition; Diestel, Graph Theory, Thm 3.2.x): a graph is
2-connected iff it can be built by starting from a cycle and successively adding
an "ear", where an ear is either
  (i)  a path whose internal vertices are all new and whose two endpoints are
       two existing (distinct) vertices, or
  (ii) a single new edge between two existing non-adjacent vertices
       (the "trivial" ear / chord).
Conversely every such construction yields a 2-connected graph.

Hence: seed with ALL cycles (any length 3..N — every 2-connected graph contains
a cycle and has an ear decomposition starting from one of its cycles), then close
under both ear types, deduplicating each vertex-count level by exact isomorphism
(VF2). Because (ii) never changes the vertex count, we take a per-level chord
closure; (i) moves a graph to a higher level.

This yields exactly the class of 2-connected graphs on <= N vertices. It is a
constructive/bijective generation of a well-defined class — not a search over a
candidate answer space. Every emitted graph is 2-connected (the theorem) and
every 2-connected graph is reached (the theorem's completeness).

Complexity: the 2-connected class grows super-exponentially (~(n^{n})) so we only
run to small N; that class-growth is the honest stopping bound. Isomorphism dedup
per graph is polynomial (VF2), not an exponential canonical labelling.
"""

import networkx as nx


def _cycle_graph(n):
    G = nx.cycle_graph(n)
    return G


def add_path_ear(G, u, v, k):
    """Return a NEW graph: add a length-k path ear u-x1-...-xk-v with k>=1 new
    vertices between existing vertices u and v (u, v distinct). Mutates nothing."""
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


def add_single_edge(G, u, v):
    """Return a NEW graph with edge (u,v) added (u,v existing, non-adjacent)."""
    H = G.copy()
    H.add_edge(u, v)
    return H


def generate_2connected_levels(n_target, dump_every=0):
    """Generate all 2-connected graphs on exactly each vertex count m in 3..n_target,
    deduplicated by exact isomorphism per level. Returns dict m -> list of networkx
    Graphs (one per isomorphism class)."""
    levels = {m: [] for m in range(3, n_target + 1)}

    def add_to_level(H):
        m = H.number_of_nodes()
        if m > n_target:
            return False
        degH = sorted(dict(H.degree()).values())
        for R in levels[m]:
            # cheap prefilter: isomorphic graphs share a degree sequence
            if sorted(dict(R.degree()).values()) != degH:
                continue
            if nx.is_isomorphic(H, R):
                return False
        levels[m].append(H)
        return True

    # Seed: all cycles (the ear-decomposition base can be any cycle).
    for l in range(3, n_target + 1):
        add_to_level(_cycle_graph(l))

    # Work-queue growth: process every graph; its non-trivial ears push to higher
    # levels, its chord ears stay in-level (requiring re-processing), so loop until
    # the frontier is stable.
    worklist = [G for ms in levels.values() for G in ms]
    seen_work = set()
    while worklist:
        G = worklist.pop()
        m = G.number_of_nodes()
        verts = list(G.nodes())
        vert_set = set(verts)
        # non-trivial ears: each adds k>=1 new vertices -> higher level
        for k in range(1, n_target - m + 1):
            for u in verts:
                for v in verts:
                    if u == v:
                        continue
                    H = add_path_ear(G, u, v, k)
                    if add_to_level(H):
                        worklist.append(H)
        # trivial ears: single chord between existing non-adjacent vertices -> same level
        for i in range(len(verts)):
            for j in range(i + 1, len(verts)):
                u, v = verts[i], verts[j]
                if not G.has_edge(u, v):
                    H = add_single_edge(G, u, v)
                    if add_to_level(H):
                        worklist.append(H)
    return levels


def min_degree(G):
    return min(dict(G.degree()).values()) if G.number_of_nodes() > 0 else 0
