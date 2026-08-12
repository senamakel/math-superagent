"""Count S5(17) = #connected min-degree>=3 girth>=5 graphs on 17 vertices
(geng -c -d3 -t -f native = triangle-free & C4-free = girth>=5) and compare
with OEIS A366224(17)=23882. Also count 3-connected survivors (should be all
of them if the S5=A366224 identification holds and the sequence predictions
are right)."""
import subprocess, networkx as nx, time
from lib.cycles import min_degree, girth

def count(n):
    t0 = time.time()
    cmd = ["nauty-geng", "-q", "-c", "-d3", "-t", "-f", str(n)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    lines = [l.strip() for l in proc.stdout.splitlines() if l.strip()]
    print(f"n={n}: geng -c -d3 -t -f raw count = {len(lines)}  ({time.time()-t0:.0f}s)", flush=True)
    return lines

if __name__ == "__main__":
    lines = count(17)
    # spot-verify filter: all are min-degree>=3 girth>=5
    from collections import Counter
    bad = 0
    for g6 in lines[:100]:
        G = nx.from_graph6_bytes(g6.encode("ascii"))
        if min_degree(G) < 3 or girth(G) is None or girth(G) < 5:
            bad += 1
            print("BAD:", g6, min_degree(G), girth(G))
    print(f"spot-check first 100: {100-bad}/100 pass girth>=5 & mindeg>=3")

    # count 3-connected ones exactly (they should equal A366224 3-connected count)
    t0 = time.time()
    n3c = 0
    for g6 in lines:
        G = nx.from_graph6_bytes(g6.encode("ascii"))
        ok = True
        for u in list(G.nodes()):
            H = G.copy(); H.remove_node(u)
            if not nx.is_connected(H) or list(nx.articulation_points(H)):
                ok = False; break
        if ok:
            n3c += 1
    print(f"n=17: S5={len(lines)}, 3-connected={n3c} (A366224 says 23882)", flush=True)
    print(f"time {time.time()-t0:.0f}s")