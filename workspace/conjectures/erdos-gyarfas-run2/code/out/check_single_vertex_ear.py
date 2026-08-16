"""Verify the single-vertex-ear construction lemma needed for segmented/resume
generation:

LEMMA: every 2-connected graph G on n vertices is obtained from a 2-connected
graph H on n-1 vertices by adding ONE new vertex x adjacent exactly to two
existing vertices (a, b) — i.e. H = G - x is 2-connected on n-1 vertices with
a and b the two neighbours of x.

Equivalently: G has a vertex x with G - x 2-connected. (a, b = N(x) work as
the length-1 path ear.)

If this holds for every small 2-connected graph, then to generate all n-vertex
2-connected graphs it is enough to take every cached (n-1)-vertex graph and add
one length-1 ear; lower levels never need re-processing. This is what a resume
from a cached level boundary relies on.
"""
import networkx as nx
from lib.biconnected_gen_hash import generate_2connected_levels_hash

def lemma_holds(G):
    n = G.number_of_nodes()
    for x in G.nodes():
        Hx = G.copy()
        Hx.remove_node(x)
        if Hx.number_of_nodes() == 0:
            continue
        if nx.is_connected(Hx):
            if len(list(nx.bridges(Hx))) == 0:  # no bridges == 2-connected (n-1>=2)
                return True
    return False

fails = []
for n in range(3, 7):
    levels = generate_2connected_levels_hash(n)
    for G in levels[n]:
        if n <= 2:
            continue
        if not lemma_holds(G):
            fails.append((n, sorted(G.edges())))
            if len(fails) > 5:
                break
    print(f"n={n}: 2conn={len(levels[n])}  lemma failures so far={len(fails)}")
print("LEMMA FAILURES:", fails if fails else "NONE (every 2-connected graph has a vertex whose removal leaves it 2-connected)")
