"""Sequence of "obstruction survivors": connected min-degree-3 graphs on n
vertices whose girth clears successive power-of-two barriers.

A counterexample to EG must avoid cycles of length 4, 8, 16, ...  The first
barrier is 4: a min-degree-3 graph with no 4-cycle has girth >= 5.  Count, by
order n, the connected min-degree>=3 graphs (via nauty-geng, ISO classes) that
survive each barrier:
  S4(n) = graphs with girth >= 5            (no 4-cycle; the real first test)
These survivors are the only graphs that can possibly be counterexamples, so
their sequence says how the first obstacle prunes the search space.  Girth is
computed by BFS (polynomial), so this extends further than full cycle-length
enumeration.
"""

import networkx as nx
from lib.cycles import _geng_graph6, min_degree, girth


def main():
    print("n | total mindeg3 | girth>=5 (no 4-cyc) | fraction")
    print("--+---------------+---------------------+---------")
    for n in range(4, 10):
        lines = _geng_graph6(n)
        total = 0
        surv = 0
        for g6 in lines:
            G = nx.from_graph6_bytes(g6.encode("ascii"))
            if min_degree(G) < 3:
                continue
            total += 1
            g = girth(G)
            # girth None means acyclic (impossible here), >=5 means no 4-cycle
            if g is not None and g >= 5:
                surv += 1
        frac = (surv / total) if total else float("nan")
        print(f"{n:2d} | {total:13d} | {surv:19d} | {frac:.4f}")


if __name__ == "__main__":
    main()
