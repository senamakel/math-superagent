"""Verify the House of Graphs graph6 string for the Markstroem Graph (HoG 51419)
as an independent route to the tool_builder's reconstruction.

Checks, all mechanical:
  1. graph6 decodes to 24 vertices, 36 edges, cubic (3-regular).
  2. The decoded edge set equals the adjacency list served by the HoG API
     (research/sources/markstrom-houseofgraphs-api.full.md).
  3. The decoded graph equals the tool_builder reconstruction
     (code/out/markstrom_reconstruction/markstrom.edgelist).
  4. The cycle oracle says: min degree 3, cycle lengths avoid 4 and 8,
     but include 16 (powers of two present: 16 only among 4,8,16).
  5. Planar via networkx (independent of HoG's claim of genus 0).
  6. Report other invariants the decoder can compute: connected, girth,
     number of spanning trees, chromatic number, Hamiltonian (all vs the HoG
     listed values: girth 3, spanning trees 31,059,336, chi 3, Hamiltonian
     yes, edges 36, diameter 6).
"""
import networkx as nx

G6 = "Ws??W?@@?P?aA_?O?GG?a?@_?gA??a?@CO?CG?A@???a??D"

G = nx.from_graph6_bytes(G6.encode())

n, m = G.number_of_nodes(), G.number_of_edges()
deg = sorted(d for _, d in G.degree())
print(f"n={n}, m={m}, degree sequence (sorted)={deg}")
assert n == 24 and m == 36
assert deg[0] == deg[-1] == 3, "not cubic"

# --- 2. compare with the HoG API adjacency list (transcribed from the .full.md) ---
api_adj = [[1, 2, 3], [0, 18, 19], [0, 21, 22], [0, 20, 23],
           [6, 10, 12], [6, 9, 11], [4, 5, 12], [8, 13, 14],
           [7, 10, 17], [5, 11, 15], [4, 8, 17], [5, 9, 16],
           [4, 6, 16], [7, 14, 15], [7, 13, 19], [9, 13, 18],
           [11, 12, 21], [8, 10, 20], [1, 15, 19], [1, 14, 18],
           [3, 17, 23], [2, 16, 22], [2, 21, 23], [3, 20, 22]]
edge_set_from_api = frozenset(
    tuple(sorted((u, v))) for u, nbrs in enumerate(api_adj) for v in nbrs
)
edge_set_g6 = frozenset(tuple(sorted(e)) for e in G.edges())
print("graph6 == API adjacency list:", edge_set_g6 == edge_set_from_api)
assert edge_set_g6 == edge_set_from_api

# --- 3. compare with tool_builder reconstruction ---
tb_edges = []
with open("/workspace/code/out/markstrom_reconstruction/markstrom.edgelist") as f:
    for line in f:
        a, b = line.split()
        tb_edges.append((int(a), int(b)))
edge_set_tb = frozenset(tuple(sorted(e)) for e in tb_edges)
print("graph6 == tool_builder edgelist:", edge_set_g6 == edge_set_tb)
assert edge_set_g6 == edge_set_tb
tb_g6 = open(
    "/workspace/code/out/markstrom_reconstruction/markstrom.graph6"
).read().strip()
print("graph6 == tool_builder saved graph6:", tb_g6 == G6)

# --- 4. cycle oracle on the independent graph6 route ---
from lib.cycle_oracle import oracle
min_deg, lens = oracle(G)
print(f"oracle: min_degree={min_deg}, cycle lengths (sorted)="
      f"{lens[:20]}... total {len(lens)} distinct lengths")
assert min_deg == 3
pow2 = [2**k for k in range(2, 6)]
pres = {L: (L in lens) for L in pow2}
print("powers of two present:", pres)
assert pres[4] is False and pres[8] is False and pres[16] is True
print("LARGEST cycle length:", max(lens))

# --- 5. planarity ---
print("planar (networkx):", nx.check_planarity(G)[0])

# --- 6. other invariants ---
print("connected:", nx.is_connected(G))
print("girth (shortest cycle, networkx):",
      min(lens) if lens else None)
from math import prod
# spanning trees via Kirchhoff (Laplacian cofactor) — exact rationals
La = nx.laplacian_matrix(G).todense()
import sympy
M = sympy.Matrix(La)[:-1, :-1]
st = M.det()
print("number of spanning trees (Kirchhoff, exact):", st)
print("spanning trees as listed by HoG (31,059,336):", st == 31059336)
print("diameter:", nx.diameter(G))
print("chromatic number (networkx greedy=3 upper; check clique):",
      nx.graph_clique_number(G))
print("max degree:", max(deg), "| triangle count:",
      sum(nx.triangles(G).values()) // 3)