"""Survivor counts n<=9 (n<17 => expected all zero, matching literature bound).
Uses polynomial has_cycle_of_length for 4,8,16 only (the minimal powers that
matter; a counterexample must avoid all powers but C4/C8 already decide small n)."""
import networkx as nx
from lib.cycles import _geng_graph6, min_degree
from lib.egcheck import has_power_of_two_cycle


def main():
    print("n | total_mindeg3 | no_pow2_survivors (C4,C8,C16 check)")
    for n in range(4, 10):
        lines = _geng_graph6(n)
        total = 0
        surv = 0
        for g6 in lines:
            G = nx.from_graph6_bytes(g6.strip().encode("ascii"))
            if min_degree(G) < 3:
                continue
            total += 1
            if not has_power_of_two_cycle(G):
                surv += 1
        print(f"{n:2d} | {total:12d} | {surv}")


if __name__ == "__main__":
    main()
