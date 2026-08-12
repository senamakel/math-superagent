"""Test whether the Markström 24-graph (HoG 51419) is in the K4-triangle-expansion family.

A vertex-into-triangle expansion replaces a degree-3 vertex v (neighbours a,b,c)
by a triangle x,y,z, with a,b,c each attached to a distinct triangle vertex.
Reverse: contract a triangle whose 3 vertices each have exactly one external
neighbour (degree 3 in graph: 2 triangle edges + 1 external), giving a single
vertex v adjacent to those 3 external neighbours.

Membership test: starting from the Markström graph, apply reverse expansions
(triangle contractions) until either reaching K4 (member) or exhausting all
choices with none reaching K4 (not a member). We also record, per level, the
distinct (canonical) graphs reached, to see the whole trajectory.
"""
import sys
import itertools
import networkx as nx
from networkx import Graph


def triangles(G):
    """Yield all triangles as frozensets of 3 vertices."""
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


def contractible(G):
    """Yield triangles whose 3 vertices each have exactly one external neighbour.

    Each vertex of the triangle has degree 3 total: 2 inside the triangle, so
    exactly 1 external neighbour; and the 3 external neighbours must be distinct
    (no edge between two of them on the triangle? not required, just distinct)."""
    for t in triangles(G):
        ext = []
        ok = True
        for v in t:
            nbrs = set(G[v]) - t
            if len(nbrs) != 1:
                ok = False
                break
            ext.append(next(iter(nbrs)))
        if ok and len(set(ext)) == 3:
            yield (t, frozenset(ext))


def contract(G, t, ext):
    """Return graph with triangle t contracted to a vertex adjacent to ext."""
    new = "NEW"
    H = Graph()
    H.add_nodes_from(set(G) - set(t) | {new})
    for u, w in G.edges():
        if u in t or w in t:
            continue
        H.add_edge(u, w)
    for e in ext:
        H.add_edge(new, e)
    return H


def canon(G):
    return nx.graph6_to_bytes if False else nx.to_graph6_bytes(G, header=False).decode().strip()


def membership(G):
    """BFS over inverse expansions from G. Return depth-to-K4 and full graph set."""
    from collections import deque
    start = nx.to_graph6_bytes(G, header=False).decode().strip()
    seen = {start}
    # states: (current graph, depth)
    dq = deque([(G, 0)])
    best = None
    levels = {}
    while dq:
        H, d = dq.popleft()
        levels.setdefault(d, H.number_of_nodes())
        if H.number_of_nodes() == 4:
            # must be K4
            deg = sorted(dict(H.degree()).values())
            if H.number_of_edges() == 6:
                best = d
                break
        for t, ext in contractible(H):
            C = contract(H, t, ext)
            c = nx.to_graph6_bytes(C, header=False).decode().strip()
            if c not in seen:
                seen.add(c)
                dq.append((C, d + 1))
    return best, seen, levels


if __name__ == "__main__":
    g6 = "Ws??W?@@?P?aA_?O?GG?a?@_?gA??a?@CO?CG?A@???a??D"
    G = nx.from_graph6_bytes(g6.encode())
    G = nx.convert_node_labels_to_integers(G)
    G = nx.relabel_nodes(G, {i: str(i) for i in G.nodes()})
    print("vertices", G.number_of_nodes(), "edges", G.number_of_edges(),
          "cubic", set(dict(G.degree()).values()) == {3})
    print("triangles", sum(1 for _ in triangles(G)))
    best, seen, levels = membership(G)
    print("reached K4:", best is not None, "| depth to K4:", best)
    print("distinct inverse-generated graphs:", len(seen))
    print("node counts visited by level:", dict(sorted(levels.items())))
    if best is None:
        # report the stuck level
        print("MEMBERSHIP: NOT in K4-triangle-expansion family (could not reduce to K4)")
    else:
        print("MEMBERSHIP: in K4-triangle-expansion family, depth", best)
