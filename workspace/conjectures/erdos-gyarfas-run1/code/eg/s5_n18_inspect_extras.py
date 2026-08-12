"""Inspect the 3 non-3-connected S5(18) survivors (the extras over A366224).
All are 2-connected not 3-connected, girth>=5, min-degree>=3. Find their
vertex-separator structure and decomposition to understand the split."""
import networkx as nx
from lib.cycles import min_degree, girth

EXTRAS = [
    "Q????B?g?oA_GgOc?h?QGZ?AR??",
    "Q????B?g?oA_GgOc?h?QGZ?AR?G",
    "Q???C@?G?oA_@aA`[?@B?RSAQo?",
]

for g6 in EXTRAS:
    G = nx.from_graph6_bytes(g6.encode("ascii"))
    n = G.number_of_nodes()
    m = G.number_of_edges()
    degs = sorted(dict(G.degree()).values())
    g = girth(G)
    md = min_degree(G)
    print(f"\n=== graph6 {g6} ===")
    print(f"  n={n} m={m} min_deg={md} girth={g} degree_seq={degs}")
    # find a 2-vertex separator removal that disconnects
    nodes = list(G.nodes())
    sep = None
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            H = G.copy(); H.remove_node(nodes[i]); H.remove_node(nodes[j])
            if not nx.is_connected(H):
                sep = (nodes[i], nodes[j])
                break
        if sep: break
    print(f"  a 2-vertex separator: {sep}")
    if sep:
        u, v = sep
        H = G.copy(); H.remove_node(u); H.remove_node(v)
        comps = list(nx.connected_components(H))
        print(f"  components after removing separator: sizes {sorted(len(c) for c in comps)}")
        # degree of the separator vertices into components
        for w in (u, v):
            ng = set(G.neighbors(w)) - {u, v}
            print(f"  separator vertex {w} deg={G.degree(w)}, neighbors-to-components: "
                  f"{sorted((len([x for x in ng if x in c]) for c in comps), reverse=True)}")
    # articulation-free check confirm
    arts = list(nx.articulation_points(G))
    print(f"  articulation points: {arts} (empty means 2-connected)")
