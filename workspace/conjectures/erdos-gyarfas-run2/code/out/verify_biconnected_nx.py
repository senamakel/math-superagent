"""Check the ear-decomposition generator (biconnected_gen.py) against an
independent, networkx-based count of 2-connected graphs, AND check whether it
misses triangle-free 2-connected graphs (it starts from a triangle and never
removes edges, so any output contains a triangle).

Independent enumeration on small n: all graphs on n labelled vertices that are
2-connected (networkx.is_biconnected), deduplicated by canonical labelling.
"""
import networkx as nx
from itertools import combinations, permutations

def canonical(n, edges):
    best = None
    for p in permutations(range(n)):
        bits = []
        for a in range(n):
            for b in range(a+1, n):
                u, v = p[a], p[b]
                bits.append((min(u, v), max(u, v)) in edges)
        s = "".join("1" if b else "0" for b in bits)
        if best is None or s < best:
            best = s
    return best

def count_2conn(n):
    V = list(range(n))
    all_e = list(combinations(V, 2))
    classes = set()
    for mask in range(1 << len(all_e)):
        edges = set()
        for i, e in enumerate(all_e):
            if (mask >> i) & 1:
                edges.add(e)
        G = nx.Graph(); G.add_nodes_from(V); G.add_edges_from(edges)
        if G.number_of_nodes() >= 3 and nx.is_biconnected(G):
            classes.add(canonical(n, edges))
    return len(classes)

for n in range(3, 7):
    print(f"independent n={n}: {count_2conn(n)} nonisomorphic 2-connected graphs")
