"""Push S5 to n=18: count connected min-degree>=3 girth>=5 (native
triangle-free+C4-free) = should be A366224(18)=422194. Time-box the
3-connectivity sample check on 500 graphs (structural probe, not full count)."""
import subprocess, networkx as nx, time, random
from lib.cycles import min_degree, girth

def count(n):
    t0 = time.time()
    cmd = ["nauty-geng", "-q", "-c", "-d3", "-t", "-f", str(n)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    lines = [l.strip() for l in proc.stdout.splitlines() if l.strip()]
    print(f"n={n}: geng -c -d3 -t -f raw count = {len(lines)}  ({time.time()-t0:.0f}s)", flush=True)
    return lines

if __name__ == "__main__":
    lines = count(18)
    print(f"S5(18)={len(lines)}; A366224(18) predicts 422194", flush=True)
    # sample 500 for 3-connectivity
    random.seed(1)
    sample = random.sample(lines, min(500, len(lines)))
    t0 = time.time()
    non3c = 0
    for g6 in sample:
        G = nx.from_graph6_bytes(g6.encode("ascii"))
        ok = True
        for u in list(G.nodes()):
            H = G.copy(); H.remove_node(u)
            if not nx.is_connected(H) or list(nx.articulation_points(H)):
                ok = False; break
        if not ok:
            non3c += 1
            print("  NON-3CONN sampled:", g6)
    print(f"sampled {len(sample)} survivors: non_3connected={non3c} ({time.time()-t0:.0f}s)", flush=True)