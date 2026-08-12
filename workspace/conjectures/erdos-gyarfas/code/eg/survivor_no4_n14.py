"""No-4-cycle survivor sequence: #connected min-degree>=3 graphs on n vertices
with NO 4-cycle (triangles allowed). This is the exact EG first-barrier count.
geng -f generates C4-free natively (a C4 is forbidden for EG, so nothing is
lost); min-degree filter after. n=4..14."""
import subprocess, networkx as nx
from lib.cycles import min_degree


def main():
    for n in range(4, 15):
        cmd = ["nauty-geng", "-q", "-c", "-f", "-d3", str(n)]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        total = 0
        for g6 in proc.stdout.splitlines():
            g6 = g6.strip()
            if not g6:
                continue
            G = nx.from_graph6_bytes(g6.encode("ascii"))
            if min_degree(G) < 3:
                continue
            total += 1
        print(f"n={n}: no4cycle_mindeg3={total}", flush=True)


if __name__ == "__main__":
    main()
