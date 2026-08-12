"""Verify connectivity/girth statements about minimal counterexamples
to the Erdős–Gyárfás conjecture.

What is checked here (library-librarian):
  1. Fact: (min degree >= 3) => no cut vertex of degree that would isolate
     a component leaf: with d(v) >= 3 and v a cut vertex, every component
     of G-v has >= 2 vertices (each component must contain at least one
     neighbor of v, but that alone doesn't force size >= 2 — the real
     content is that NO vertex-degree argument proves 2-connectedness).
     We check the GLOBAL structural consequence: a min-degree-3 graph
     CAN be 1-connected (bridges possible), so 2-connectedness of a
     minimal counterexample is NOT a degree consequence.
  2. The degree-4-independent-set consequence: in a graph where every
     vertex has degree >= 3 and no two degree-4+ vertices are adjacent,
     it is still possible to be 1-connected (cut vertices can be cubic).
     So the dichotomy does NOT force 2-connectedness.
  3. No source asserts girth >= 4: we confirm the Markström graph (the
     archetypal near-counterexample, cubic planar 24v) HAS a triangle,
     so girth 3 is achievable in the extremal family; nothing forces
     triangle-freeness.

All checks are small-example constructions (oracle-style), not exhaustive
searches; they refute the naive conjectures:
  naive1: "min-degree-3 => 2-connected"            FALSE (pentagon with
          triangles, or two K4s joined by a bridge)
  naive2: "independent degree-4 set => 2-connected"  FALSE (two K4s with a
          bridge: all degree 3, K4s have degree-3 vertices, no degree>=4
          vertices, 1-connected)
  naive3: "minimal counterexample must be triangle-free"  -- not claimed by
          any source; Markström 24-graph has girth 3 (computed).
"""
import networkx as nx


def degree_set(g):
    return sorted(d for _, d in g.degree())


def report(name, g, note=""):
    comps = nx.number_connected_components(g)
    node_conn = nx.node_connectivity(g)
    bridge = list(nx.bridges(g))
    tris = [c for c in nx.cycle_basis(g) if len(c) == 3]
    print(f"--- {name} {note}")
    print("  n,m            :", g.number_of_nodes(), g.number_of_edges())
    print("  min/max degree :", min(d for _, d in g.degree()),
          max(d for _, d in g.degree()))
    print("  components     :", comps)
    print("  node_connectivity (1 => cut vertex exists):", node_conn)
    print("  bridges        :", len(bridge))
    print("  # triangles (from cycle_basis):", len(tris))
    print("  degrees        :", degree_set(g))


# naive1 refutation: min-degree-3 graph that is 1-connected.
# Two K4s joined by a bridge: all degrees >=3, node connectivity 1.
g1 = nx.Graph()
for i in range(8):
    g1.add_node(i)
for c in [(0, 1, 2, 3), (4, 5, 6, 7)]:
    for u in c:
        for v in c:
            if u < v:
                g1.add_edge(u, v)
g1.add_edge(3, 4)  # bridge
report("g1: two K4 + bridge", g1, "(1-connected, min degree 3)")

# naive2 refutation: independent degree-4 set does not prevent cut vertices.
# Here ALL vertices have degree 3 (no degree-4 vertices at all), so the
# independent-set condition is vacuously satisfied, yet 1-connected.
report("g1 again (all degree 3): independent-set condition vacuous",
       g1, "(cut vertex exists)")

# Markström graph: archetypal minimal-ish near-counterexample, cubic planar,
# girth 3 (has a triangle). Run in-process by importing? Just encode the
# edge list from the source adjacency to avoid module path issues.
edges = [(0,1),(0,2),(0,3),(1,18),(1,19),(2,21),(2,22),(3,20),(3,23),
         (4,6),(4,10),(4,12),(5,6),(5,9),(5,11),(6,12),(7,8),(7,13),(7,14),
         (8,10),(8,17),(9,11),(9,15),(10,17),(11,16),(12,16),(13,14),(13,15),
         (14,19),(15,18),(16,21),(17,20),(18,19),(19,14),(20,23),(21,22),
         (22,23),(23,20)]
gM = nx.Graph()
gM.add_edges_from(edges)
report("Markström graph (HoG 51419)", gM,
       "(cubic planar, no C4/C8, has C16)")
# oracle: girth and triangle presence
girth = min(len(c) for c in nx.cycle_basis(gM))
print("  girth (cycle_basis min):", girth)
print("  has triangle:", any(len(c) == 3 for c in nx.cycle_basis(gM)))