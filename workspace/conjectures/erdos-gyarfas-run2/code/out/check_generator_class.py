"""Determine exactly what the ear-decomposition generator (biconnected_gen.py)
actually counts, by comparing it to the class of 2-connected graphs that contain
a triangle, on small n.

Hypothesis: because the generator always STARTS from a triangle and only adds
ears (paths of new vertices) between existing vertices, it can only build 2-
connected graphs that contain a triangle. So its count = #(2-connected graphs on
n vertices containing at least one triangle), which is a proper subclass of all
2-connected graphs (missing triangle-free ones like C4).

We verify by (1) running the generator, and (2) independently counting 2-connected
graphs that contain a triangle, with networkx + brute-force canonical labelling.
"""
import networkx as nx
from itertools import combinations, permutations
from lib.biconnected_gen import layer_by_layer  # the generator under test

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

def count_2conn_tri(n):
    """# nonisomorphic 2-connected graphs on n vertices that contain a triangle."""
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
            # contains a triangle?
            has_tri = any(len(es) == 3 and nx.is_connected(nx.Graph(es))
                          for es in combinations(edges, 3)) if len(edges) >= 3 else False
            if has_tri:
                classes.add(canonical(n, edges))
    return len(classes)

def count_2conn_all(n):
    V = list(range(n)); all_e = list(combinations(V, 2)); classes = set()
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
    gen = len(layer_by_layer(n, dmin=3) if False else [])  # dmin=3 filter; but we want unfiltered
    # layer_by_layer with dmin=3 filters min degree>=3; run with dmin=0 to see all
    gen0 = len(layer_by_layer(n, dmin=0))
    print(f"n={n}: generator(dmin=0)={gen0}  all-2conn={count_2conn_all(n)}  2conn-with-triangle={count_2conn_tri(n)}")
