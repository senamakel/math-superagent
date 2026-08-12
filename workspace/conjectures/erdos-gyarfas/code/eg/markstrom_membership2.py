"""Clean membership test: is the Markström 24-graph in the K4-triangle-expansion family?

The family (counted by A027610) = graphs reachable from K4 by repeatedly
replacing a degree-3 vertex v by a triangle x,y,z, attaching v's 3 neighbours
bijectively to x,y,z. Every family member is cubic.

Inverse move: contract a triangle whose 3 vertices each have exactly one
external neighbour (all distinct). In a cubic graph this is automatic for any
triangle (each triangle vertex has degree 3: 2 internal + 1 external), and
contracting preserves cubicness. So a graph is in the family IFF iterating
these contractions can reach K4 — and every intermediate is cubic.

We use fresh integer node ids so no label collision, and we prune any
contraction whose result is not cubic (a true inverse never leaves the cubic
class). If this clean BFS cannot reach K4 from the Markström graph, then the
graph is NOT in the family.

Positive control: a known forward expansion must reverse to K4.
"""
import sys
import networkx as nx
from networkx import Graph
from collections import deque


def triangles(G):
    """Yield all triangles as frozensets."""
    adj = {u: set(G[u]) for u in G}
    seen = set()
    for u in G:
        for v in adj[u]:
            if v <= u:
                continue
            for w in adj[v]:
                if w <= v:
                    continue
                if w in adj[u]:
                    t = frozenset((u, v, w))
                    if t not in seen:
                        seen.add(t)
                        yield t


def contractible_triangles(G):
    """Triangles whose 3 vertices have distinct single external neighbours."""
    out = []
    for t in triangles(G):
        ext = []
        ok = True
        for v in t:
            nbrs = set(G[v]) - set(t)
            if len(nbrs) != 1:
                ok = False
                break
            ext.append(next(iter(nbrs)))
        if ok and len(set(ext)) == 3:
            out.append((t, frozenset(ext)))
    return out


def contract(G, t, ext):
    """Contract triangle t to a fresh vertex; assert result is cubic."""
    new = max(G) + 1
    H = Graph()
    H.add_nodes_from([n for n in G if n not in t] + [new])
    for u, w in G.edges():
        if u in t or w in t:
            continue
        H.add_edge(u, w)
    for e in ext:
        H.add_edge(new, e)
    return H


def canon(G):
    # relabel to 0..n-1 by degree then id for a stable canonical-ish key
    labels = {old: i for i, old in enumerate(sorted(G.nodes()))}
    R = nx.relabel_nodes(G, labels)
    return nx.to_graph6_bytes(R, header=False).decode().strip()


def in_family(G):
    """Return (bool member, dict depth->#graphs reached, min_node ever)."""
    start = canon(G)
    seen = {start}
    dq = deque([(G, 0)])
    depth_counts = {}
    reduced = False
    while dq:
        H, d = dq.popleft()
        depth_counts[d] = depth_counts.get(d, 0) + 1
        if H.number_of_nodes() == 4:
            if H.number_of_edges() == 6:      # K4
                return True, depth_counts
            continue
        for t, ext in contractible_triangles(H):
            C = contract(H, t, ext)
            degs = set(dict(C.degree()).values())
            if degs != {3}:                   # prune non-cubic (not a true inverse)
                continue
            c = canon(C)
            if c not in seen:
                seen.add(c)
                dq.append((C, d + 1))
    return False, depth_counts


def expand_cubic(G, v):
    """Forward vertex-into-triangle expansion (for the positive control)."""
    nbrs = list(G[v])
    import itertools
    x, y, z = max(G) + 1, max(G) + 2, max(G) + 3
    H = Graph()
    H.add_nodes_from([n for n in G if n != v] + [x, y, z])
    for u, w in G.edges():
        if u == v or w == v:
            continue
        H.add_edge(u, w)
    H.add_edges_from([(x, y), (y, z), (x, z)])
    for nb, tri in zip(nbrs, [x, y, z]):
        H.add_edge(nb, tri)
    return H


if __name__ == "__main__":
    # positive control
    K4 = nx.complete_graph(4)
    E = expand_cubic(K4, 0)
    assert set(dict(E.degree()).values()) == {3} and E.number_of_nodes() == 6
    member, dc = in_family(E)
    print("POSITIVE CONTROL: forward-expanded K4 reverses to family member:", member)
    print("   depth counts:", dc)
    assert member, "control failed"

    g6 = "Ws??W?@@?P?aA_?O?GG?a?@_?gA??a?@CO?CG?A@???a??D"
    G = nx.from_graph6_bytes(g6.encode())
    G = nx.convert_node_labels_to_integers(G)
    print("Markström: nodes", G.number_of_nodes(), "edges", G.number_of_edges(),
          "cubic", set(dict(G.degree()).values()) == {3})
    member, dc = in_family(G)
    print("MARKSTRÖM MEMBER:", member)
    print("   depth counts (cubic-only branches):", dc)
