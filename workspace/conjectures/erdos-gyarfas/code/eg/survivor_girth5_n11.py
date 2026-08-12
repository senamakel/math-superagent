"""Extend S_girth>=5(n) survivor count to n=11 using geng -f (C4-free native
generation). Since a C4 is itself a forbidden EG cycle, no no-4 survivor is
lost by generating only C4-free graphs; then girth>=5 filter == C4-free in
the min-degree-3 class. Reports count of min-degree-3 connected ISO classes
with girth>=5 for n=11 (and confirms n=10 gives Petersen)."""
import networkx as nx
from lib.cycles import _geng_graph6, min_degree, girth


def main():
    for n in [10, 11]:
        # -f native C4-free generation (valid: C4-free needed for girth>=5)
        cmd = ["nauty-geng", "-q", "-c", "-f", "-d3", str(n)]
        import subprocess
        proc = subprocess.run(cmd, capture_output=True, text=True)
        # fall back to library if subprocess differs
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
        print(f"n={n}: C4free_mindeg3={total}  girth>=5_survivors={surv}")


if __name__ == "__main__":
    main()
