"""Check the wedge-of-two-triangles claim from durable memory.
A wedge of two triangles sharing exactly one vertex: does it have min degree 3?
Plain computation below. (Context-curator verification, not a solver result.)
"""
import networkx as nx

# wedge of two triangles sharing vertex 0
G = nx.Graph()
G.add_edges_from([(0,1),(0,2),(1,2)])  # triangle 1
G.add_edges_from([(0,3),(0,4),(3,4)])  # triangle 2 (shares 0)

d = dict(G.degree())
print("n =", G.number_of_nodes(), " m =", G.number_of_edges())
print("degrees:", sorted(d.values()))
print("min degree =", min(d.values()))
print("has cut vertex 0 (nx):", not nx.is_connected(G) or not nx.is_connected(nx.restricted_view(G, [0], [])) is False)
# direct: node connectivity
print("node connectivity =", nx.node_connectivity(G))
