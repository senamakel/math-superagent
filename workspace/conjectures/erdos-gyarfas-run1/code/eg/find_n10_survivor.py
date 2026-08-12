import networkx as nx
from lib.cycles import _geng_graph6, min_degree, girth, cycle_lengths

# Find the unique girth>=5 survivor among min-degree-3 graphs on n=10.
for n in [10]:
    lines = _geng_graph6(n)
    for g6 in lines:
        g6 = g6.strip()
        G = nx.from_graph6_bytes(g6.encode())
        if min_degree(G) < 3:
            continue
        g = girth(G)
        if g is not None and g >= 5:
            lens = sorted(cycle_lengths(G))
            print(f"n={n} survivor g6={g6} min_deg={min_degree(G)} girth={g} cycles={lens}")
            # is it Petersen? Petersen graph6 is 'E{{K?G_'
            print("nodes", len(G.nodes()), "edges", len(G.edges()))
            print("degree seq", sorted(d for _,d in G.degree()))
