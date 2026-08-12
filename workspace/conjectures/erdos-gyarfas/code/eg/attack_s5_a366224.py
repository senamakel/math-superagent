"""Attack the S5 = A366224 coincidence.

Claim under test: the count of CONNECTED min-degree>=3 girth>=5 graphs (S5)
equals A366224, the count of 3-CONNECTED girth>=5 graphs.

Theoretical attack: joining two girth-5 min-deg-3 graphs at a single vertex
gives a connected min-deg-3 girth-5 graph with a CUT vertex (hence NOT
3-connected).  Smallest pieces could force a split already below n=19
(Petersen+Petersen).  So the identity is NOT a theorem and must break at the
first n with a non-3-connected girth>=5 min-deg>=3 survivor.

This script enumerates connected min-deg>=3 girth>=5 graphs via nauty-geng
(-c -d3 -t -f = connected, min-deg>=3, triangle-free, C4-free = girth>=5)
and counts how many are NOT 3-connected.  The first n with a non-3-connected
survivor falsifies S5 = A366224.

3-connectivity test: no 1- or 2-vertex separator.  Exact.
"""
import subprocess, sys, time
import networkx as nx
from lib.cycles import min_degree, girth

def is_3connected(G):
    if not nx.is_connected(G):
        return False
    nodes = list(G.nodes())
    # remove each vertex: graph must stay 2-connected (no cut vertex)
    for u in nodes:
        H = G.copy(); H.remove_node(u)
        if not nx.is_connected(H) or list(nx.articulation_points(H)):
            return False
    return True

def count(n):
    t0 = time.time()
    # -c connected, -d3 min degree 3, -t triangle-free, -f C4-free  => girth>=5
    cmd = ["nauty-geng", "-q", "-c", "-d3", "-t", "-f", str(n)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    lines = [l.strip() for l in proc.stdout.splitlines() if l.strip()]
    total = len(lines)
    non3c = 0
    first = None
    # exact girth/mindeg spot-verify is done by geng flags; but verify on all for small n
    for g6 in lines:
        G = nx.from_graph6_bytes(g6.encode("ascii"))
        if not is_3connected(G):
            non3c += 1
            if first is None:
                first = g6
    print(f"n={n}: S5={total}  non_3connected={non3c}  {'EQUAL-to-3conn' if non3c==0 else 'BREAKS identity'}  "
          f"({time.time()-t0:.0f}s)" + (f"  first_non3c={first}" if first else ""), flush=True)
    return total, non3c

if __name__ == "__main__":
    lo = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    hi = int(sys.argv[2]) if len(sys.argv) > 2 else 17
    for n in range(lo, hi + 1):
        count(n)
