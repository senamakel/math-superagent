"""Check n=12..14 no-4 survivors all have an 8-cycle (polynomial 8-cycle
test), confirming none is an EG counterexample below the 17-vertex floor."""
import subprocess, networkx as nx
from lib.cycles import min_degree
from lib.egcheck import has_cycle_of_length


def main():
    for n in [12, 13, 14]:
        cmd = ["nauty-geng", "-q", "-c", "-f", "-d3", str(n)]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        su = 0
        no8 = 0
        for g6 in proc.stdout.splitlines():
            g6 = g6.strip()
            if not g6:
                continue
            G = nx.from_graph6_bytes(g6.encode("ascii"))
            if min_degree(G) < 3:
                continue
            su += 1
            if not has_cycle_of_length(G, 8):
                no8 += 1
                print(f"  n={n}: NO 8-cycle! graph6={g6}")
        print(f"n={n}: no4_survivors={su}, missing_8cycle={no8}", flush=True)


if __name__ == "__main__":
    main()
