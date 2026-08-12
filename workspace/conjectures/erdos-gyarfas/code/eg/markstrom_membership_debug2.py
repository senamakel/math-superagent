import networkx as nx
from networkx import Graph
from collections import deque
from markstrom_membership import contractible, contract, triangles

g6 = "Ws??W?@@?P?aA_?O?GG?a?@_?gA??a?@CO?CG?A@???a??D"
G = nx.from_graph6_bytes(g6.encode())
G = nx.convert_node_labels_to_integers(G)
G = nx.relabel_nodes(G, {i: str(i) for i in G.nodes()})

def canon(G):
    return nx.to_graph6_bytes(G, header=False).decode().strip()

start = canon(G)
seen = {start}
dq = deque([(G, 0)])
by_depth = {}
while dq:
    H, d = dq.popleft()
    by_depth.setdefault(d, []).append((H.number_of_nodes(), H.number_of_edges(),
                                       sorted(set(dict(H.degree()).values()))))
    if d >= 4:
        continue
    for t, ext in contractible(H):
        new = "NEW"
        C = Graph()
        C.add_nodes_from(set(H) - set(t) | {new})
        for u, w in H.edges():
            if u in t or w in t:
                continue
            C.add_edge(u, w)
        for e in ext:
            C.add_edge(new, e)
        c = canon(C)
        if c not in seen:
            seen.add(c)
            dq.append((C, d + 1))

for d in sorted(by_depth):
    entries = by_depth[d]
    distinct_n = sorted(set(e[0] for e in entries))
    cubic = sorted(set(e[2][0] if e[2] else None for e in entries))
    print(f"depth {d}: {len(entries)} graphs, node counts {distinct_n}, cubic sets {cubic}")
