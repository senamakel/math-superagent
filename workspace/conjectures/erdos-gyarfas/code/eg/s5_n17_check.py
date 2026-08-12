"""Cross-check: geng -t -f native (triangle-free + C4-free = girth>=5) counts
must match the earlier BFS-girth = 23 at n=14, then extend S5 to n=17,18 and
compare with OEIS A366224 (3-connected girth>=5): predictions 23882, 422194.

Also: on a time-boxed subset of the n=17 survivors, test true 3-connectivity
(articulation scan) to probe the structural reason for the A366224 match.
"""
import subprocess, networkx as nx, time


def count(n):
    t0 = time.time()
    cmd = ["nauty-geng", "-q", "-c", "-d3", "-t", "-f", str(n)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    n_g6 = len([l for l in proc.stdout.splitlines() if l.strip()])
    print(f"n={n}: geng -c -d3 -t -f count = {n_g6}   ({time.time()-t0:.0f}s)", flush=True)
    return proc.stdout.splitlines()


def is_3connected(G):
    """G is 3-vertex-connected iff G - u has no articulation point for every u."""
    nodes = list(G.nodes())
    for u in nodes:
        H = G.copy()
        H.remove_node(u)
        if len(H) and (not nx.is_connected(H) or nx.articulation_points(H)):
            return False
    return True


if __name__ == "__main__":
    # cross-check at n=14 (expect 23)
    out14 = count(14)
    # verify first few are girth>=5 min-degree>=3 via BFS (spot check)
    from lib.cycles import min_degree, girth
    ok = 0
    for g6 in out14[:50]:
        if not g6.strip():
            continue
        G = nx.from_graph6_bytes(g6.strip().encode("ascii"))
        assert min_degree(G) >= 3 and girth(G) >= 5, f"bad graph {g6}"
        ok += 1
    print(f"spot-check: {ok} first n=14 graphs all girth>=5 & mindeg>=3")

    for n in [17]:
        lines = count(n)
        non3c = 0
        checked = 0
        t0 = time.time()
        for g6 in lines:
            if not g6.strip():
                continue
            G = nx.from_graph6_bytes(g6.strip().encode("ascii"))
            if not is_3connected(G):
                non3c += 1
                print(f"  NON-3CONNECTED survivor at n={n}: {g6}", flush=True)
            checked += 1
            if checked >= 3000:
                break
        print(f"n={n}: 3-connectivity checked on {checked} survivors, non_3connected={non3c} ({time.time()-t0:.0f}s)", flush=True)