"""Count NO4(17) = number of connected min-degree>=3 C4-free graphs on 17
vertices, and how many lack an exact 8-cycle (NO8(17)).

This is the first term that would falsify the pattern-finder's numeric law
NO4(n) ~= K * 3^n * (n-10)!, K in [5.258,5.363]e-5, which predicts
NO4(17) in [34.22M, 34.90M] (nominal ~34.56M).  Outside [25M, 45M] flags
an enumeration bug or a break in the law.

Method (identical to the n=10..16 sweep, survivor_no4_no8_sweep_n10_16.py):
nauty-geng -q -c -f -d3 17  (connected, min-degree>=3, C4-free generated
natively -- a C4 is itself a forbidden 2-power cycle, and (-d3) filters
min-degree, so NO4 counts exactly; geng -f keeps only C4-free graphs).
8-cycle test: exact bounded-depth-8 DFS (lib.egcheck.has_cycle_of_length).

This is a single counting enumeration at one order (n=17), not the EG search;
it is the oracle term that tests the law.  Costs ~10-30 min.

Run: cd /workspace && PYTHONPATH=/workspace/code python code/eg/count_no4_n17.py
"""

import subprocess
import sys
import time

import networkx as nx

from lib.cycles import min_degree
from lib.egcheck import has_cycle_of_length

N = 17


def main():
    t0 = time.time()
    print("counting NO4(17): connected min-degree>=3 C4-free graphs on 17 vertices",
          flush=True)
    cmd = ["nauty-geng", "-q", "-c", "-f", "-d3", str(N)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        print("geng failed:", proc.stderr[-2000:], file=sys.stderr)
        sys.exit(1)
    lines = proc.stdout.splitlines()
    print(f"geng emitted {len(lines)} raw lines (C4-free, connected, deg>=3)", flush=True)

    no4 = 0
    no8 = 0
    first_no8 = None
    for idx, g6 in enumerate(lines):
        g6 = g6.strip()
        if not g6:
            continue
        G = nx.from_graph6_bytes(g6.encode("ascii"))
        no4 += 1
        if not has_cycle_of_length(G, 8):
            no8 += 1
            if first_no8 is None:
                first_no8 = g6
                print("  !! first NO-8-cycle graph:", g6, flush=True)
        if idx % 5000000 == 0 and idx > 0:
            print(f"  ...{idx} scanned ({time.time()-t0:.0f}s)", flush=True)

    dt = time.time() - t0
    print(f"RESULT: NO4(17) = {no4}")
    print(f"RESULT: NO8(17) = {no8}  (graphs lacking an exact 8-cycle)")
    if first_no8 is not None:
        print("  (first such graph6:", first_no8, ")")
    print(f"elapsed {dt:.0f}s")


if __name__ == "__main__":
    main()
