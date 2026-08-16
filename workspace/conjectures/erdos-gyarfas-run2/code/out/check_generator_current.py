"""Run the current ear-decomposition generator and compare its counts of
2-connected graphs with an independent networkx enumeration, on small n.

The generator seeds with ALL cycles (length 3..N) and closes under path ears and
chords, so it should now count all 2-connected graphs. Verify counts against an
independent brute-force enumeration (all edge subsets, is_biconnected, canonical
dedup) for n = 3..6.
"""
import networkx as nx
from itertools import combinations, permutations
from lib.biconnected_gen import generate_2connected_levels

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

print("Running generator (n_target=6)...")
levels = generate_2connected_levels(6)
for n in range(3, 7):
    gen = len(levels.get(n, []))
    indep = count_2conn_all(n)
    print(f"n={n}: generator={gen}  independent-all-2conn={indep}  {'MATCH' if gen==indep else 'DIFF'}")
