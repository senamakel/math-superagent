import networkx as nx
from networkx import Graph
from markstrom_membership import triangles, contractible, contract

g6 = "Ws??W?@@?P?aA_?O?GG?a?@_?gA??a?@CO?CG?A@???a??D"
G = nx.from_graph6_bytes(g6.encode())
G = nx.convert_node_labels_to_integers(G)
G = nx.relabel_nodes(G, {i: str(i) for i in G.nodes()})

print("nodes", G.number_of_nodes(), "edges", G.number_of_edges())
print("degree multiset", sorted(dict(G.degree()).values())[:5], "...")

# list contractible triangles
ct = list(contractible(G))
print("contractible triangles at level 0:", len(ct))
for t, ext in ct[:6]:
    print("  tri", sorted(t), "ext", sorted(ext))

# do one contraction and check cubic + node count
if ct:
    t, ext = ct[0]
    C = contract(G, t, ext)
    print("after 1 contraction: nodes", C.number_of_nodes(), "edges", C.number_of_edges())
    print("cubic?", sorted(set(dict(C.degree()).values())))
