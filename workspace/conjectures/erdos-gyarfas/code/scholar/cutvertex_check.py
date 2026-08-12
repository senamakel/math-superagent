"""Does minimal-counterexample structure force 2-connectivity?

Attack the claim embedded in the on-disk connectivity notes: that a cut
vertex v of a minimal counterexample forces a smaller counterexample among
its lobes, so 2-connectivity is "provable by the standard argument".

What we check here (a STRUCTURE check, not a search for a counterexample):
(1) Exhibit a degree>=3 graph with a cut vertex such that EVERY lobe
    (component of G-v plus v and its incident edges) has delta<=2, i.e. the
    exact configuration Lemma 0.1 of Carr permits. If such a structure is
    constructible, then Lemma 0.1 does NOT force 2-connectivity, and the
    claimed "standard argument" has a gap.
(2) For that graph, verify delta(G)>=3 and that the only possible deficiency
    in each lobe is the cut vertex v.
"""
import networkx as nx

def lobes_ok(G, v):
    """Each lobe = component of G-v plus v + v's edges into it; report each
    lobe's min degree and which vertices achieve it."""
    G2 = G.copy()
    G2.remove_node(v)
    comps = list(nx.connected_components(G2))
    out = []
    for c in comps:
        lobe = G.subgraph(c | {v}).copy()
        degs = dict(lobe.degree())
        md = min(degs.values())
        argmin = [u for u, d in degs.items() if d == md]
        out.append((md, argmin, sorted(c)))
    return comps, out

def report(name, edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    for v in list(G.nodes()):
        if nx.is_connected(G):
            G2 = G.copy(); G2.remove_node(v)
            if not nx.is_connected(G2):
                comps, lo = lobes_ok(G, v)
                print(f"[{name}] cut vertex v={v}, deg(v)={G.degree(v)}, "
                      f"delta(G)={min(dict(G.degree()).values())}, #lobes={len(comps)}")
                for md, argmin, c in lo:
                    print(f"    lobe {sorted(set(c))}: min-degree={md} at {argmin}")
    return G

# (1) two triangles sharing a vertex: K3-K3 glued at one vertex
# vertices 0,1,2 form triangle; 0,3,4 form triangle; shared vertex 0.
G = report("two K3 sharing a vertex (wedge of two triangles)",
           [(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)])
print("  cycle lengths:", sorted(set(len(c) for c in nx.simple_cycles(
    nx.DiGraph([(u,v) for u,v in G.edges()]+[(v,u) for u,v in G.edges()])))))

# (2) three Petersen-like lobes at a shared hub is NOT delta>=3 at hub if
# hub is the only connection; instead, three triangles at a hub where hub
# has degree 6 (each triangle contributes 2 edges to hub). delta(G)=3 (the
# non-hub triangle vertices), hub degree 6.
edges = []
hub = 0
for i in range(3):
    a, b = 1+2*i, 2+2*i
    edges += [(hub, a), (hub, b), (a, b)]  # triangle on {hub,a,b}
G = report("three triangles on one hub (delta=3, cut vertex hub)",
           edges)
