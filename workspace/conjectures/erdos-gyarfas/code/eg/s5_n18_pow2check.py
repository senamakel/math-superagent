"""Check the 3 extra S5(18) survivors for 8-cycles / any power-of-two cycle.
These are the first non-3-connected girth-5 min-degree-3 graphs. Do any of
them lack an 8-cycle (= near-counterexample to EG at n=18)?"""
import networkx as nx
from lib.egcheck import has_cycle_of_length, has_power_of_two_cycle

EXTRAS = [
    "Q????B?g?oA_GgOc?h?QGZ?AR??",
    "Q????B?g?oA_GgOc?h?QGZ?AR?G",
    "Q???C@?G?oA_@aA`[?@B?RSAQo?",
]
for g6 in EXTRAS:
    G = nx.from_graph6_bytes(g6.encode("ascii"))
    c8 = has_cycle_of_length(G, 8)
    pow2 = has_power_of_two_cycle(G)
    print(f"{g6}: 8-cycle={c8}, has_power_of_two_cycle={pow2}")
