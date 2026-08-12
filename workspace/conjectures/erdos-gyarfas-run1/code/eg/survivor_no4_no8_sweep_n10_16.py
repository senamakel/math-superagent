"""Re-derive the no-4 / missing-8-cycle sweep, n = 10..16.

For each n, enumerate every connected min-degree>=3 C4-free graph via
``nauty-geng -q -c -f -d3 n`` (C4-free generated natively: a C4 is itself a
power-of-two cycle, so no Erdos-Gyarfas counterexample is lost) and print:

  (a) NO4(n)   : total count of such graphs
  (b) NO8(n)   : count that lack a cycle of length exactly 8

If NO8(n) == 0 for every n in 10..16, the claim that every no-4 surrogate
below n=17 has an 8-cycle is re-derived computationally, reproducing the
known >=17 vertex floor for EG counterexamples.

8-cycle test: bounded-depth simple-path DFS (has_cycle_of_length in
lib/egcheck), exact and polynomial per graph; generation is the cost.
Pool sizes: 1,655,659 graphs at n=16, ~9s per n on this machine.

Run: cd /workspace && PYTHONPATH=/workspace/code python code/eg/survivor_no4_no8_sweep_n10_16.py
"""

import subprocess
import time

import networkx as nx

from lib.cycles import min_degree
from lib.egcheck import has_cycle_of_length


def main():
    print("sweep: connected min-degree>=3 C4-free graphs, n=10..16 (nauty-geng -q -c -f -d3)")
    print("n | NO4(n) | NO8(n) = no 8-cycle | time")
    grand_no4 = 0
    grand_no8 = 0
    for n in range(10, 17):
        t0 = time.time()
        cmd = ["nauty-geng", "-q", "-c", "-f", "-d3", str(n)]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        no4 = 0
        no8 = 0
        for g6 in proc.stdout.splitlines():
            g6 = g6.strip()
            if not g6:
                continue
            G = nx.from_graph6_bytes(g6.encode("ascii"))
            if min_degree(G) < 3:
                continue
            no4 += 1
            if not has_cycle_of_length(G, 8):
                no8 += 1
                if no8 <= 3:
                    print(f"    !! n={n}: NO 8-cycle graph6={g6}")
        dt = time.time() - t0
        grand_no4 += no4
        grand_no8 += no8
        print(f"{n:2d} | {no4:9d} | {no8:8d} | {dt:5.1f}s", flush=True)
    print("TOTAL: NO4 pool across n=10..16 =", grand_no4,
          "| lacking an 8-cycle =", grand_no8)
    if grand_no8 == 0:
        print("RESULT: every no-4 surrogate in 10..16 has an 8-cycle "
              "-> no EG counterexample below 17 vertices (>=17 floor reproduced).")
    else:
        print("RESULT: found", grand_no8, "graphs lacking an 8-cycle — "
              "see lines above (potential counterexample candidates).")


if __name__ == "__main__":
    main()