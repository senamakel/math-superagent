"""Generate + cache the 2-connected girth-6 class to a target n, with timing.
Reads existing cache if present; else generates from scratch for the requested
n_target and writes json. Prints per-n raw and min-deg>=3 counts and the enum time.
"""
import json, os, sys, time
import networkx as nx
from lib.girth6_gen import generate_2connected_girth6, min_degree

OUT = os.path.join(os.path.dirname(__file__))

def main(n_target):
    cache = os.path.join(OUT, f"girth6_class_n{n_target}.json")
    t0 = time.time()
    if os.path.exists(cache):
        data = json.load(open(cache))
        levels = {}
        for rec in data:
            levels.setdefault(rec["n"], []).append(nx.Graph(rec["edges"]))
        print(f"cache loaded (time {time.time()-t0:.1f}s)")
        elapsed = 0.0
    else:
        levels = generate_2connected_girth6(n_target)
        elapsed = time.time() - t0
        # write cache: n -> edge lists
        recs = []
        for n, gs in levels.items():
            for G in gs:
                recs.append({"n": n, "edges": sorted(sorted(e) for e in G.edges())})
        json.dump(recs, open(cache, "w"))
        print(f"generated to n={n_target} in {elapsed:.1f}s, cache written")
    for n in sorted(levels):
        raw = levels[n]
        md = [G for G in raw if min_degree(G) >= 3]
        print(f"  girth6 n={n}: raw={len(raw)}  min_deg>=3={len(md)}")
    print(f"TOTAL {time.time()-t0:.1f}s")

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    main(n)
