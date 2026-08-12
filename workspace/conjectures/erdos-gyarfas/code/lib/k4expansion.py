"""Membership test for the K4-triangle-expansion (cubic Apollonian dual) family.

The family is defined forward: start from K4 and repeatedly replace a
degree-3 vertex v by a triangle xyz, attaching the three neighbours of v to
x, y, z bijectively (each neighbour to exactly one triangle vertex).  Every
member is cubic (3-regular); at n vertices it has 3n/2 edges.  This is the
planar dual of the planar 3-tree / Apollonian (maximal planar, 3n-6 edge)
family — duality is a bijection and the size counts match A027610.

Reverse characterisation (the membership test here).  In a cubic graph a
triangle's three vertices each have exactly one outside neighbour (degree 3,
two edges inside the triangle).  Call a triangle CLEAN when those three
outside neighbours are pairwise distinct.  Contracting a clean triangle to a
single vertex yields a smaller cubic graph, and the forward expansion
reconstructs the larger graph from the smaller one bijectively (attach the
three outside neighbours to the new triangle).  Hence, exactly:

    G in family  <=>  G == K4  OR  (exists a clean triangle T with G/T in family)

The (=>) direction holds because the last triangle created in any forward
build is clean; the (<=) direction holds because any clean contraction is
reversed by the forward expansion.  So the recursion has no false positives.

The test is DFS over clean contractions with memoisation on the nauty
canonical form, so a shared state is only explored once.  On a single
n=24 graph the reachable contraction states are tiny.
"""
import networkx as nx
from networkx import Graph


def clean_triangles(G):
    """All clean triangles of cubic G: triangle with pairwise-distinct outside nbrs."""
    nbrs = {u: set(G[u]) for u in G}
    tris = set()
    for u in G:
        for v in G[u]:
            if u < v:
                for w in G[v]:
                    if u < w and w in nbrs[u]:
                        tris.add(tuple(sorted((u, v, w))))
    clean = []
    for t in tris:
        a, b, c = t
        na, nb, nc = nbrs[a] - {b, c}, nbrs[b] - {a, c}, nbrs[c] - {a, b}
        if len(na) == 1 and len(nb) == 1 and len(nc) == 1:
            outs = na | nb | nc
            if len(outs) == 3:            # pairwise distinct outside neighbours
                clean.append((t, tuple(outs)))
    return clean


def contract_triangle(G, tri):
    """Contract a clean triangle `tri` (3 vertices) to one new vertex. Cubic stays cubic."""
    inside = set(tri)
    outs = set()
    for v in tri:
        outs |= (set(G[v]) - inside)
    new = max(G.nodes()) + 1
    H = Graph()
    H.add_nodes_from([u for u in G if u not in inside])
    for u, v in G.edges():
        if u in inside or v in inside:
            continue
        H.add_edge(u, v)
    H.add_node(new)
    for w in outs:
        H.add_edge(new, w)
    return H


def canon(g6):
    """nauty canonical graph6 of one graph6 string."""
    import subprocess
    proc = subprocess.run(["nauty-labelg", "-q"], input=g6 + "\n",
                          capture_output=True, text=True)
    return proc.stdout.strip().splitlines()[0]


def in_k4_expansion_family(G, _memo=None):
    """True iff cubic G is in the K4-triangle-expansion family (recursive test)."""
    # relabel to 0..n-1 ints so ordering/`<` comparisons are well-defined
    G = nx.convert_node_labels_to_integers(G)
    n = G.number_of_nodes()
    degs = {d for _, d in G.degree()}
    if degs != {3}:
        return False                        # family is purely cubic
    if n == 4:
        return G.number_of_edges() == 6     # K4
    if _memo is None:
        _memo = {}
    key = canon(nx.to_graph6_bytes(G, header=False).decode().strip())
    if key in _memo:
        return _memo[key]
    result = False
    for tri, outs in clean_triangles(G):
        H = contract_triangle(G, tri)
        if in_k4_expansion_family(H, _memo):
            result = True
            break
    _memo[key] = result
    return result
