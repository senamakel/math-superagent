"""S5 vs A366224 identification probe — final runnable version.

S5(n)     = # connected min-degree-3 girth>=5 graphs on n vertices (one per
            isomorphism class).
A366224(n)= # connected 3-connected girth>=5 graphs on n vertices.
Conjecture under test: every connected min-degree-3 girth>=5 graph is
3-connected, i.e. S5(n) == A366224(n). Predicted A366224 values:
1@10, 0@11, 2@12, 4@13, 23@14, 149@15, 1670@16, 23882@17, 422194@18.

Method (exact, no exponential cycle enumeration):
  * Enumerate with `nauty-geng -q -c -d3 -t -f <n>`. -t = triangle-free,
    -f = C4-free, so together (with -c connected, -d3 min degree 3) they
    generate exactly the girth>=5 min-degree-3 connected class. Counting
    output lines gives S5(n) exactly. This is native to nauty: no BFS filter
    over the giant unfiltered geng -c -d3 output at n>=15.
  * Validate the native filter: (i) n=10 count must be 1 and that graph must
    be Petersen; (ii) at each n spot-check a sample of generated graphs for
    min_degree>=3 and BFS girth>=5.
  * 3-connectivity per graph, exact and certificate-producing: G is
    3-connected iff G-v is connected and articulation-free for every v
    (removing any 2 vertices keeps it connected). A failing v gives the
    separator: {v} if G-v is disconnected, else {v,a} for an articulation
    a of G-v. Cost per graph O(|V| * (|V|+|E|)) ~ polynomial, no cycle
    enumeration.
  * Non-3-connected survivors get their full exact cycle-length set from
    lib.cycles (only ever a handful of graphs).

Plus the structural machine check the identification predicts: the
vertex-amalgam of two Petersen graphs (identify vertex 0 of each copy,
n=19) — connected, min degree 3, girth 5, one vertex of degree 6, cut
vertex at the glued vertex => an S5(19) graph that is NOT 3-connected.
Built and checked from scratch, exact outputs printed.

Output: /workspace/code/out/s5_identification.txt
"""
import subprocess, time
from collections import deque
import networkx as nx

from lib.cycles import min_degree, girth as lib_girth, cycle_lengths


def bfs_girth(G):
    """Exact girth by BFS from every start vertex (shortest cycle through it)."""
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


def geng_lines(n):
    """All graph6 lines of connected min-degree-3 girth>=5 graphs on n"""
    cmd = ["nauty-geng", "-q", "-c", "-d3", "-t", "-f", str(n)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return [l.strip() for l in proc.stdout.splitlines() if l.strip()]


def is3c_with_cert(G):
    """Exact 3-vertex-connectivity test returning (bool, certificate).

    Certificate: None if 3-connected, else ('1-sep', {v}) proving v is an
    articulation point, or ('2-sep', {v,a}) proving {v,a} is a 2-separator.
    G is 3-connected iff G-v is connected and articulation-free for every v.
    """
    if G.number_of_nodes() < 4:
        return False, ('n<4', None)
    for v in G.nodes():
        H = G.copy()
        H.remove_node(v)
        if not nx.is_connected(H):
            return False, ('1-sep', v)
        arts = list(nx.articulation_points(H))
        if arts:
            return False, ('2-sep', (v, arts[0]))
    return True, None


def petersen_amalgam():
    """Vertex-amalgam of two Petersen graphs: identify vertex 0 of each copy.

    G has 19 vertices: label 0 is the glue vertex (degree 6), copy 1 keeps
    labels 1..9, copy 2 uses labels 11..19 (its vertex 0 maps to the glue
    vertex 0). Returns G.
    """
    P = nx.petersen_graph()           # vertices 0..9
    G = nx.Graph()
    G.add_node(0)                     # glue vertex
    # copy 1: Petersen vertex i (i != 0) keeps label i
    for u, v in P.edges():
        if u == 0:
            G.add_edge(0, v)
        elif v == 0:
            G.add_edge(0, u)
        else:
            G.add_edge(u, v)
    # copy 2: Petersen vertex i (i != 0) gets label 10+i; vertex 0 -> glue 0
    for u, v in P.edges():
        uu = 0 if u == 0 else u + 10
        vv = 0 if v == 0 else v + 10
        G.add_edge(uu, vv)
    return G


def main():
    pred = {10: 1, 11: 0, 12: 2, 13: 4, 14: 23,
            15: 149, 16: 1670, 17: 23882, 18: 422194}
    out = []

    def emit(*a):
        s = " ".join(str(x) for x in a)
        print(s, flush=True)
        out.append(s)

    emit("S5 vs A366224 identification probe")
    emit("=" * 64)
    which = subprocess.run(["which", "nauty-geng"],
                           capture_output=True, text=True).stdout.strip()
    emit("nauty-geng:", which, "| python networkx", nx.__version__)

    emit("")
    emit("Method validation:")
    # (0) Petersen is the unique n=10 graph and it is 3-connected
    g10 = geng_lines(10)
    G10 = nx.from_graph6_bytes(g10[0].encode("ascii"))
    emit(f"  n=10: S5={len(g10)} (must be 1); unique survivor is Petersen: "
         f"{nx.is_isomorphic(G10, nx.petersen_graph())}")
    ok3, cert = is3c_with_cert(G10)
    emit(f"  n=10 unique survivor 3-connected: {ok3} (cert {cert})")

    # (i) spot-check native generator: min_degree>=3 and girth>=5
    bad = 0
    for n in [12, 15, 17]:
        lines = geng_lines(n)[:200]
        for g6 in lines:
            G = nx.from_graph6_bytes(g6.encode("ascii"))
            if min_degree(G) < 3 or bfs_girth(G) is None or bfs_girth(G) < 5:
                bad += 1
        emit(f"  spot-check n={n}: {len(lines)} sampled, all min_deg>=3 & "
             f"girth>=5: {bad == 0}")
    if bad:
        emit("  !! SPOT-CHECK FAILED: native -t -f filter is wrong for this class")
    emit("")

    # (ii) per-order counts: S5, 3-connected, non-3-connected
    emit(f"{'n':>4} {'S5':>8} {'A366224':>9} {'3conn':>7} {'non3':>6} "
         f"{'match':>6}  scan-time")
    table = []
    all_non3 = []
    for n in list(range(10, 19)):
        t0 = time.time()
        lines = geng_lines(n)
        t_gen = time.time() - t0
        s5 = len(lines)
        t0 = time.time()
        n3 = 0
        non3 = []
        for g6 in lines:
            G = nx.from_graph6_bytes(g6.encode("ascii"))
            ok, cert = is3c_with_cert(G)
            if ok:
                n3 += 1
            else:
                non3.append((g6, cert))
        t_scan = time.time() - t0
        p = pred[n]
        match = "OK" if s5 == p else ("BREAK" if s5 > p else "below")
        emit(f"{n:>4} {s5:>8} {p:>9} {n3:>7} {len(non3):>6} {match:>6}  "
             f"gen {t_gen:.0f}s scan {t_scan:.0f}s")
        table.append((n, s5, n3, len(non3), p, match))
        for g6, cert in non3:
            all_non3.append((n, g6, cert))

    emit("")
    first_break = next(((n, len([x for x in all_non3 if x[0] == n]))
                        for n, *_ in table if n >= 15
                        and len([x for x in all_non3 if x[0] == n]) > 0), None)
    if not all_non3:
        emit("VERDICT: no non-3-connected S5 survivor on n=10..18")
        emit("         => S5(n) == A366224(n) HOLDS throughout the checked range")
    else:
        emit(f"VERDICT: identification BREAKS DOWN — first non-3-connected S5 "
             f"survivor at n = {all_non3[0][0]}")
        emit(f"         {len(all_non3)} non-3-connected survivors total")
        emit("")
        emit("Non-3-connected survivors (graph6, order, degree seq, "
             "certificate, exact cycle-length set):")
        for n, g6, cert in all_non3:
            G = nx.from_graph6_bytes(g6.encode("ascii"))
            degseq = sorted(d for _, d in G.degree())
            cyc = sorted(cycle_lengths(G))
            emit(f"  n={n}  g6={g6}")
            emit(f"    degree seq       = {degseq}")
            emit(f"    certificate      = {cert}")
            emit(f"    cycle-length set = {cyc}")

    emit("")
    emit("counts table (n, S5, 3conn, non3conn, A366224_pred, match):")
    for row in table:
        emit(f"  n={row[0]}: S5={row[1]} 3conn={row[2]} non3conn={row[3]} "
             f"A366224_pred={row[4]} match={row[5]}")

    # (iii) Petersen-amalgam machine check (predicted breaking structure, n=19)
    emit("")
    emit("Petersen-amalgam machine check (vertex-amalgam of two Petersen "
         "graphs, identify vertex 0 of each copy, n=19):")
    G = petersen_amalgam()
    degs = sorted(d for _, d in G.degree())
    emit(f"  order {G.number_of_nodes()} edges {G.number_of_edges()}")
    emit(f"  min degree = {min_degree(G)} (must be 3)")
    emit(f"  degree multiset = {degs}")
    emit(f"  connected = {nx.is_connected(G)}")
    arts = list(nx.articulation_points(G))
    emit(f"  articulation points = {arts}  (nonempty => NOT 3-connected)")
    ok3, cert = is3c_with_cert(G)
    emit(f"  3-connected = {ok3} (cert {cert})")
    g = bfs_girth(G)
    emit(f"  BFS girth = {g} (must be 5)")
    cyc = sorted(cycle_lengths(G))
    emit(f"  exact cycle-length set (lib.cycles) = {cyc}")
    emit(f"  (cycle lengths in each Petersen copy are 5,6,8,9; a simple "
         f"cycle crossing the glue vertex twice is impossible)")

    emit("")
    emit("done.")
    path = "/workspace/code/out/s5_identification.txt"
    with open(path, "w") as f:
        f.write("\n".join(out) + "\n")
    emit(f"Wrote {path}")


if __name__ == "__main__":
    main()