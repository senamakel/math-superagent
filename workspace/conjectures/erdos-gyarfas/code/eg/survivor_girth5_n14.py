"""Extend S5(n) = #connected min-degree>=3 with girth>=5 (no 4-cycle, the
first EG barrier) to n=12..14 via geng -f native C4-free generation.
Cheap: C4-free is generated natively, girth computed by BFS (polynomial).
Reports total C4-free min-degree-3 and the girth>=5 survivors."""
import subprocess, networkx as nx
from lib.cycles import girth, min_degree


def main():
    for n in [12, 13, 14]:
        cmd = ["nauty-geng", "-q", "-c", "-f", "-d3", str(n)]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        total = 0
        surv = 0
        for g6 in proc.stdout.splitlines():
            g6 = g6.strip()
            if not g6:
                continue
            G = nx.from_graph6_bytes(g6.encode("ascii"))
            if min_degree(G) < 3:
                continue
            total += 1
            g = girth(G)
            if g is not None and g >= 5:
                surv += 1
        print(f"n={n}: C4free_mindeg3={total}  girth>=5_survivors={surv}", flush=True)


if __name__ == "__main__":
    main()
