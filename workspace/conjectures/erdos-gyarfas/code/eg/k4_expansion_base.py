"""K4-expansion base step: expand K4's vertex 0 into a triangle.

K4 on vertices 0,1,2,3.  Replace vertex 0 by three new vertices x,y,z joined
in a triangle, and attach the three neighbours of 0 {1,2,3} to x,y,z
bijectively (identity bijection: 1-x, 2-y, 3-z; all 6 bijections are
isomorphic here because K4 is vertex-transitive).  All other K4 edges remain.

Result: |V| = 3 (old vertices left) + 3 (new triangle) = 6, not 8 —
this is exactly the shape described (only vertex 0 is replaced).  The graph
is 3-regular on 6 vertices: the triangular prism (two triangles joined by a
perfect matching).

Claim this tests: the single n=8 base step of the K4-expansion family
(the statement says 8; the construction as written gives 6 vertices)
contains a 4-cycle.  We print the true vertex count, the full cycle-length
set, and whether 4 is present.  Only this one base step — no expansion family.
"""
import networkx as nx

from lib.cycle_oracle import oracle

# K4 on vertices 0..3
K4 = nx.complete_graph(4)

# neighbours of vertex 0 that must be attached to the new triangle
nbrs_of_0 = list(K4[0])             # [1, 2, 3]
x, y, z = 4, 5, 6                   # three new triangle vertices
new_order = [x, y, z]               # identity bijection: 1->x, 2->y, 3->z

G = nx.Graph()
G.add_nodes_from(range(1, 7))       # old {1,2,3} (0 replaced) + new {4,5,6}
# every original K4 edge not incident to vertex 0
for u, v in K4.edges():
    if u == 0 or v == 0:
        continue
    G.add_edge(u, v)                # keeps 1-2, 1-3, 2-3 (a triangle)
# the new triangle on x,y,z
G.add_edges_from([(x, y), (y, z), (x, z)])
# attach the three neighbours of 0 bijectively to x,y,z
for nb, w in zip(nbrs_of_0, new_order):
    G.add_edge(nb, w)               # 1-x, 2-y, 3-z

print("K4-expansion base step:")
print("  n =", G.number_of_nodes(), " (old 3 + new triangle 3; the text says 8 —")
print("       read strictly, replacing one vertex of K4 gives 6; flagging the gap)")
print("  edges =", G.number_of_edges())
print("  degree sequence:", sorted(d for _, d in G.degree()))
print("  edges:", sorted(G.edges()))

lens = oracle(G)[1]
print("  full cycle-length set (oracle):", lens)
print("  3 present:", 3 in lens,
      "| 4 present:", 4 in lens,
      "| 5 present:", 5 in lens)

superset = {3, 4, 5}.issubset(set(lens))
claim = superset  # claim: cycle-length set is {3,4,5} or a superset of it
print("  claim '4 present, set is {3,4,5} or a superset':",
      "MATCH" if (4 in lens and superset) else "FAIL",
      "(4 present:", 4 in lens, ")")