"""Count connected min-degree>=3 graphs by order n via nauty-geng (-c -d3),
and girth>=5 survivors. Mirrors code/eg/bruteforce_bound.py and
code/eg/girth_survivors.py so the numbers match what tool_builder runs.

Reports the exact count for each n so it can be compared with OEIS A007112.
"""
import networkx as nx
from lib.cycles import _geng_graph6, min_degree, girth

def main():
    for n in range(4, 10):
        lines = _geng_graph6(n)
        total = 0
        surv = 0
        for g6 in lines:
            G = nx.from_graph6_bytes(g6.strip().encode())
            if min_degree(G) < 3:
                continue
            total += 1
            g = girth(G)
            if g is not None and g >= 5:
                surv += 1
        print(f"n={n}: total_mindeg3={total}  girth>=5_survivors={surv}")

if __name__ == "__main__":
    main()
