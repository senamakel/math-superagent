"""Push the no-4 survivor / 8-cycle check to n=15,16 (just below the >=17
bound). If every no-4 survivor has an 8-cycle there, the >=17 floor is
re-verified computationally on the exact class that could be a counterexample.
8-cycle test is polynomial; generation is the cost."""
import subprocess, networkx as nx
from lib.cycles import min_degree
from lib.egcheck import has_cycle_of_length
import time


def main():
    for n in [15, 16]:
        t0 = time.time()
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
        print(f"n={n}: no4_survivors={su}, missing_8cycle={no8}, {time.time()-t0:.0f}s", flush=True)


if __name__ == "__main__":
    main()