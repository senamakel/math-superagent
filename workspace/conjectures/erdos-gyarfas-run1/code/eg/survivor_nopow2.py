"""Extend the EG survivor count: number of connected min-degree>=3 graphs on n
vertices (nauty-geng ISO classes) with NO 2-power cycle at all (length not in
{4,8,16,...}).  Uses exact cycle-length set.  Runs n <= 10 (Petersen n=10 is
the first n where a no-4 survivor exists, but it has an 8-cycle so is not a
survivor)."""
import networkx as nx
from lib.cycles import _geng_graph6, min_degree, cycle_lengths


def main():
    print("n | total_mindeg3 | no_pow2_cycle_survivors")
    for n in range(4, 11):
        lines = _geng_graph6(n)
        total = 0
        nop2 = 0
        for g6 in lines:
            G = nx.from_graph6_bytes(g6.strip().encode("ascii"))
            if min_degree(G) < 3:
                continue
            total += 1
            lens = cycle_lengths(G)
            if not any(x >= 4 and (x & (x - 1)) == 0 for x in lens):
                nop2 += 1
        print(f"{n:2d} | {total:12d} | {nop2}")


if __name__ == "__main__":
    main()
