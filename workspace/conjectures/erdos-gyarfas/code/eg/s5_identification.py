"""S5 vs A366224 identification probe.

S5(n)  = number of connected min-degree-3 girth>=5 graphs on n vertices (one
         per isomorphism class).
A366224(n) = number of connected 3-connected girth>=5 graphs on n vertices.

The conjecture under test: every connected min-degree-3 girth>=5 graph is
3-connected, i.e. S5(n) == A366224(n). Predicted values of A366224:
149@15, 1670@16, 23882@17, 422194@18.

Method (exact, no exponential cycle enumeration):

  * Enumerate relational graphs with `nauty-geng -q -c -d3 -t -f <n>`. The
    `-t` (triangle-free) and `-f` (C4-free) filters, combined with connected
    `-c` and min-degree-3 `-d3`, generate exactly the connected min-degree-3
    girth>=5 graphs (girth 5 = tri-free & C4-free on a min-degree-3 graph).
    This is native to nauty, so the count is exact and cheap.
  * Cross-check on a sample that native S5 equals a BFS girth>=5 filter +
    min_degree>=3 filter over `geng -q -c -d3` (the unfiltered connected
    min-degree-3 set), to prove the native filter loses nothing.
  * For each S5 survivor test 3-connectivity exactly via
    networkx.node_connectivity == 3 (min degree 3 caps connectivity at 3, so
    3-connected iff node_connectivity == 3). node_connectivity is exact
    (max-flow based), polynomial, no cycle enumeration.
  * Record every non-3-connected survivor: graph6, order, degree sequence, a
    certificate (a 1-separator = articulation point, or a 2-separator
    {a,b}), and its full exact cycle-length set from lib.cycles (only for the
    small non-3-connected examples, where full enumeration is cheap).

Output goes to code/out/s5_identification.txt.
"""
import subprocess, time, sys
import networkx as nx
from lib.cycles import min_degree, cycle_lengths


def bfs_girth(G):
    """Exact girth via BFS: shortest cycle through each vertex."""
    from collections import deque
    best = None
    for s in G.nodes():
        dist = {s: 0}
        parent = {s: -1}
        q = deque([s])
        while q:
            v = q.popleft()
            for w in G.neighbors(v):
                if w not in dist:
                    dist[w] = dist[v] + 1
                    parent[w] = v
                    q.append(w)
                elif parent[v] != w and parent[w] != v:
                    L = dist[v] + dist[w] + 1
                    if best is None or L < best:
                        best = L
    return best


def is_3connected(G):
    """Exact: graph is 3-vertex-connected iff node_connectivity == 3 (min
    degree 3 caps vertex connectivity at 3). Requires >= 4 vertices."""
    if G.number_of_nodes() < 4:
        return False
    return nx.node_connectivity(G) == 3


def certificate(G, g6):
    """Return (kind, separator) proving non-3-connectivity:
    ('1-sep', [v]) an articulation point, or ('2-sep', [a,b]) a 2-separator."""
    # 1-separator?
    arts = list(nx.articulation_points(G))
    if arts:
        return ('1-sep', [arts[0]])
    # 2-separator: find any pair whose removal disconnects
    nodes = list(G.nodes())
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            H = G.copy()
            H.remove_node(nodes[i]); H.remove_node(nodes[j])
            if not nx.is_connected(H):
                return ('2-sep', [nodes[i], nodes[j]])
    return None


def count(n, out):
    t0 = time.time()
    cmd = ["nauty-geng", "-q", "-c", "-d3", "-t", "-f", str(n)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    lines = [l.strip() for l in proc.stdout.splitlines() if l.strip()]
    s5 = len(lines)
    n3c = 0
    non3 = []
    for g6 in lines:
        G = nx.from_graph6_bytes(g6.encode("ascii"))
        if is_3connected(G):
            n3c += 1
        else:
            non3.append(g6)
    dt = time.time() - t0
    return s5, n3c, non3, dt


def crosscheck(n):
    """Verify native S5 == BFS-girth-filtered count on geng -c -d3."""
    cmd = ["nauty-geng", "-q", "-c", "-d3", str(n)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    native = set(l.strip() for l in proc.stdout.splitlines() if l.strip())
    cnt = 0
    for g6 in native:
        G = nx.from_graph6_bytes(g6.encode("ascii"))
        if min_degree(G) >= 3 and bfs_girth(G) is not None and bfs_girth(G) >= 5:
            cnt += 1
    return cnt


def main():
    pred = {15: 149, 16: 1670, 17: 23882, 18: 422194}
    out = []
    def emit(*a):
        s = " ".join(str(x) for x in a)
        print(s, flush=True)
        out.append(s)

    emit("S5 vs A366224 identification probe")
    emit("=" * 60)
    emit("Environment: nauty-geng at", subprocess.run(
        ["which", "nauty-geng"], capture_output=True, text=True).stdout.strip())
    emit("")

    # (a) cross-check native geng filter == BFS girth filter on small n
    for n in [10, 11, 12, 13, 14]:
        nl = subprocess.run(["nauty-geng", "-q", "-c", "-d3", "-t", "-f", str(n)],
                            capture_output=True, text=True).stdout.splitlines()
        bfs = crosscheck(n)
        if len(nl) != bfs:
            emit(f"CROSSCHECK FAIL n={n}: native={len(nl)} bfs_girth={bfs}")
        else:
            emit(f"crosscheck n={n}: native geng girth5 = {len(nl)} == BFS girth5 OK")

    # n=10 must be Petersen (unique)
    P = nx.petersen_graph()
    g10 = subprocess.run(["nauty-geng", "-q", "-c", "-d3", "-t", "-f", "10"],
                         capture_output=True, text=True).stdout.splitlines()
    G10 = nx.from_graph6_bytes(g10[0].encode("ascii"))
    emit(f"n=10 unique survivor is Petersen: {nx.is_isomorphic(G10, P)}")

    emit("")
    emit(f"{'n':>4} {'S5':>9} {'3conn':>9} {'non3conn':>9} {'A366224 pred':>12} {'match':>6}  time")
    table = []
    all_non3 = []
    for n in list(range(10, 19)):
        s5, n3c, non3, dt = count(n, out)
        p = pred.get(n)
        m = "=" if (p is not None and s5 == p) else ("-" if p is None else "X")
        emit(f"{n:>4} {s5:>9} {n3c:>9} {len(non3):>9} {str(p):>12} {m:>6}  {dt:.0f}s")
        table.append((n, s5, n3c, len(non3), p, m))
        for g6 in non3:
            all_non3.append((n, g6))

    emit("")
    if not all_non3:
        emit("VERDICT: no non-3-connected S5 survivor found on n=10..18")
        emit("         => identification S5(n) == A366224(n) HOLDS up to n=18")
    else:
        emit(f"VERDICT: identification BREAKS DOWN at n = {all_non3[0][0]}")
        emit(f"         {len(all_non3)} non-3-connected S5 survivors total")
        emit("")
        emit("Non-3-connected survivors (graph6, order, degree seq, certificate, cycle-length set):")
        for n, g6 in all_non3:
            G = nx.from_graph6_bytes(g6.encode("ascii"))
            degseq = sorted(d for _, d in G.degree())
            cert = certificate(G, g6)
            cyc = sorted(cycle_lengths(G))
            emit(f"  n={n}  g6={g6}")
            emit(f"    degree seq       = {degseq}")
            emit(f"    certificate      = {cert[0]} separator {cert[1]}")
            emit(f"    cycle-length set = {cyc}")
    emit("")
    emit("counts table (n, S5, 3conn, non3conn):")
    for row in table:
        emit(f"  n={row[0]}: S5={row[1]} 3conn={row[2]} non3conn={row[3]} A366224_pred={row[4]}")

    with open("/workspace/code/out/s5_identification.txt", "w") as f:
        f.write("\n".join(out) + "\n")
    emit("\nWrote code/out/s5_identification.txt")


if __name__ == "__main__":
    main()
