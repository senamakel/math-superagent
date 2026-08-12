"""Find the 3 extra S5(18) survivors not in A366224: connected min-degree-3
girth>=5 (S5) that are NOT 3-connected. Uses tri-free+C4-free native
generation (=girth>=5 exactly) and a fast 2-connectivity pre-filter."""
import subprocess, networkx as nx, time
from collections import Counter


def is_3connected(G):
    nodes = list(G.nodes())
    for u in nodes:
        H = G.copy(); H.remove_node(u)
        if not nx.is_connected(H) or list(nx.articulation_points(H)):
            return False
    return True


def main():
    n = 18
    cmd = ["nauty-geng", "-q", "-c", "-d3", "-t", "-f", str(n)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    lines = [l.strip() for l in proc.stdout.splitlines() if l.strip()]
    print(f"total S5 survivors (girth>=5, mindeg>=3): {len(lines)}")

    not2conn = []
    t0 = time.time()
    for g6 in lines:
        G = nx.from_graph6_bytes(g6.encode("ascii"))
        # fast: 3-connected requires 2-connected
        arts = list(nx.articulation_points(G))
        if arts:
            not2conn.append((g6, arts[:3]))
    print(f"not 2-connected: {len(not2conn)}  ({time.time()-t0:.0f}s)")
    for g6, arts in not2conn:
        print("  not2conn:", g6, "articulations:", arts)

    # of the 2-connected ones, count non-3-connected (first few only)
    non3 = []
    t0 = time.time()
    for g6 in lines:
        G = nx.from_graph6_bytes(g6.encode("ascii"))
        if list(nx.articulation_points(G)):
            continue
        if not is_3connected(G):
            non3.append(g6)
            if len(non3) >= 10:
                break
    print(f"non-3-connected (2-connected but not 3): {len(non3)}  ({time.time()-t0:.0f}s)")
    for g6 in non3:
        print("  non3conn:", g6)


if __name__ == "__main__":
    main()