"""Sequence of obstruction survivors (n <= 8, avoid n=9 hang).

Counts connected min-degree-3 graphs on n vertices whose girth clears each
power-of-two barrier. The first barrier is 4: no 4-cycle means girth >= 5.
The second barrier is 8: no 8-cycle and no 4-cycle means girth >= 9 (but
girth is a lower bound; a graph of girth g has no cycles shorter than g, so
clearing length-4 and length-8 requires girth not hitting 4 or 8 --- but girth
>= 5 only clears 4. To clear 8 we need no cycle of length exactly 8, which
girth >= 9 guarantees but girth = 5..8 does not. So the exact survivor counts
need cycle-length sets, not girth. Here we record girth-based survivors only
as the cheap first prune, plus exact no-4 survivors via cycle set.

Uses exact cycle-length oracle (lib.cycles) for the true no-power-of-2 counts,
and BFS girth for the first-barrier (no-4) count.
"""
import networkx as nx
from lib.cycles import _geng_graph6, min_degree, girth, cycle_lengths


def main():
    print("n | total_mindeg3 | girth>=5 (no 4) | no_pow2_cycle | survivors")
    print("--+---------------+------------------+---------------+----------")
    for n in range(4, 9):
        lines = _geng_graph6(n)
        total = 0
        no4 = 0
        nop2 = 0
        for g6 in lines:
            G = nx.from_graph6_bytes(g6.encode("ascii"))
            if min_degree(G) < 3:
                continue
            total += 1
            g = girth(G)
            if g is not None and g >= 5:
                no4 += 1
            lens = cycle_lengths(G)
            if not any(x >= 4 and (x & (x - 1)) == 0 for x in lens):
                nop2 += 1
        print(f"{n:2d} | {total:13d} | {no4:16d} | {nop2:13d} | {nop2:9d}")


if __name__ == "__main__":
    main()
