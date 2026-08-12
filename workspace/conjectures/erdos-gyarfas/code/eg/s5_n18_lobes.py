"""Characterize the 8-vertex lobes of the 3 extra S5(18) survivors to pin
down the structural break: are the lobes themselves girth-5 min-degree-3
graphs (which would make this a 2-sum of two such graphs)?"""
import networkx as nx
from lib.cycles import min_degree, girth

EXTRAS = [
    "Q????B?g?oA_GgOc?h?QGZ?AR??",
    "Q????B?g?oA_GgOc?h?QGZ?AR?G",
    "Q???C@?G?oA_@aA`[?@B?RSAQo?",
]

for g6 in EXTRAS:
    G = nx.from_graph6_bytes(g6.encode("ascii"))
    nodes = list(G.nodes())
    # find 2-vertex separator
    sep = None
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            H = G.copy(); H.remove_node(nodes[i]); H.remove_node(nodes[j])
            if not nx.is_connected(H):
                sep = (nodes[i], nodes[j]); break
        if sep: break
    u, v = sep
    H = G.copy(); H.remove_node(u); H.remove_node(v)
    comps = list(nx.connected_components(H))
    print(f"\n=== {g6} (n={G.number_of_nodes()}, m={G.number_of_edges()}) ===")
    print(f"  separators {u}(deg{dict(G.degree())[u]}) {v}(deg{dict(G.degree())[v]})")
    for ci, c in enumerate(comps):
        cset = set(c)
        sub = G.subgraph(cset).copy()
        # find the vertices in the lobe adjacent to u and v
        neigh_u = [w for w in cset if G.has_edge(u, w)]
        neigh_v = [w for w in cset if G.has_edge(v, w)]
        degs = sorted(dict(sub.degree()).values())
        g = girth(sub)
        print(f"  lobe {ci}: {len(cset)} vertices, internal deg_seq {degs}, "
              f"internal girth {g}, touches u:{len(neigh_u)}, v:{len(neigh_v)}")
