"""Reproduce base cases and measure girth-6 generation scale.

Base cases required by the task:
  (1) girth-5 on n=10: exactly 1 graph, the Petersen graph (min-deg>=3).
  (2) girth-6 on n=14: the Heawood graph (cubic, smallest girth-6) must be
      found among the min-deg>=3 girth-6 graphs, and it must have an 8-cycle.
Also measure the raw (unfiltered) girth-6 counts on n=12,13,14 to estimate how
far the boundary can be pushed inside the 600s budget.
"""
import time
import networkx as nx
from lib.girth6_gen import (generate_2connected_girth6,
                            generate_2connected_girth5, girth, min_degree)
from lib.erdos_gyarfas import has_power_of_two_cycle

def build_heawood():
    adj = {v: set() for v in range(14)}
    for i in range(7):
        for p in ((i) % 7, (i + 1) % 7, (i + 3) % 7):
            adj[i].add(7 + p)
            adj[7 + p].add(i)
    G = nx.Graph()
    G.add_nodes_from(range(14))
    for v, nb in adj.items():
        for w in nb:
            G.add_edge(v, w)
    return G

t0 = time.time()
g5 = generate_2connected_girth5(10)
print(f"girth5 to n=10 time {time.time()-t0:.1f}s")
md = [G for G in g5.get(10, []) if min_degree(G) >= 3]
print(f"  girth-5 n=10 min-deg>=3 count = {len(md)}")
for G in md:
    print(f"    girth={girth(G)} min_deg={min_degree(G)} n_edges={G.number_of_edges()} "
          f"pow2={has_power_of_two_cycle({v:set(G.neighbors(v)) for v in G.nodes()})}")

t0 = time.time()
hw = build_heawood()
print(f"\nHeawood: n={hw.number_of_nodes()} girth={girth(hw)} min_deg={min_degree(hw)}")
print(f"  Heawood has power-of-two cycle: {has_power_of_two_cycle({v:set(hw.neighbors(v)) for v in hw.nodes()})}")

# measure girth-6 raw counts at n=12,13,14 (no min-deg filter, to see scale)
for n in (12, 13, 14):
    t0 = time.time()
    levels = generate_2connected_girth6(n)
    el = time.time() - t0
    raw = levels.get(n, [])
    md = [G for G in raw if min_degree(G) >= 3]
    print(f"girth6 to n={n}: time {el:.1f}s  raw@{n}={len(raw)}  min_deg>=3@{n}={len(md)}")
