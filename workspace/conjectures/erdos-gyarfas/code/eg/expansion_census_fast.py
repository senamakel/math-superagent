"""Census of the K4-triangle-expansion family (Markström's construction), fast.

Optimised sibling of expansion_census.py. Identical semantics — start from K4
and repeatedly replace a degree-3 vertex by a triangle attached bijectively to
its three neighbours; at each even size n record the number of isomorphism
classes in the family, how many avoid a C4, and how many avoid both C4 and C8.

Three changes make it fast enough to reach n=24 inside a 600 s budget:

1. **Batched labelg.** All generated graphs for one size are written as
   newline-separated graph6 lines to a single nauty-labelg subprocess, which
   returns one canonical graph6 line per input in order. This replaces one
   subprocess spawn per graph (~250 k spawns at n=22) with one spawn per level.

2. **Targeted exact cycle checks instead of full enumeration.** We only need
   to know *whether* a C4 and *whether* a C8 exist, not the full cycle-length
   set, so:
     - has_c4(G): an O(n^2 * deg) neighbour-pair test — a 4-cycle
       u-a-v-b-u exists iff two distinct vertices share >= 2 common neighbours.
     - has_c8(G): a bounded DFS for a simple path of 7 edges whose endpoints
       are adjacent, i.e. a simple 8-cycle; branching <= 2 per step (cubic).
   Both are exact and much faster than enumerating every simple cycle. C8 is
   only evaluated on C4-free graphs (a graph with a C4 can't "avoid both").

3. **Checkpointing.** Each completed size is written to out/ so a budget
   timeout still saves every level that finished.

Cross-check: this fast version reproduces the known table n=4..20 (classes
1,1,1,3,7,24,93,434,2110; avoidsC4 1,1,2,5,15,50; avoidsC4C8 all 0) and, on
the C4-free classes, agrees with lib.cycle_oracle. Verification census only.
"""
import subprocess
import sys
import os
import itertools
import networkx as nx
from networkx import Graph


def batch_canonical(graphs):
    """Canonical graph6 of each graph in `graphs`, order preserved, one labelg call."""
    # graph6 lines, one per graph (no header)
    lines = []
    for G in graphs:
        t = nx.to_graph6_bytes(G, header=False).decode().strip()
        lines.append(t)
    inp = "\n".join(lines) + "\n"
    proc = subprocess.run(["nauty-labelg", "-q"], input=inp,
                          capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"labelg failed: {proc.stderr}")
    out = [ln.strip() for ln in proc.stdout.splitlines() if ln.strip()]
    assert len(out) == len(graphs), (len(out), len(graphs), proc.stderr)
    return out


def has_c4(G):
    """Exact: does G contain a simple 4-cycle? O(n^2 * deg)."""
    nodes = list(G.nodes())
    for i in range(len(nodes)):
        u = nodes[i]
        for j in range(i + 1, len(nodes)):
            v = nodes[j]
            common = set(G[u]) & set(G[v])
            if len(common) >= 2:
                return True
    return False


def has_c8(G):
    """Exact: does G contain a simple 8-cycle? Bounded DFS.

    A simple 8-cycle is a path of 7 edges on 8 distinct vertices whose two
    endpoints are adjacent. For each start s we DFS only into unused vertices
    (branching <= 2 at each step in a cubic graph), to depth 7 edges.
    """
    adj = {u: set(G[u]) for u in G}
    nodes = list(G)

    def search(s):
        # path: list of distinct vertices, path[0]=s; used = set(path)
        def dfs(cur, used, depth):
            if depth == 7:
                # 8 distinct vertices on the path; closing edge cur -> s
                return s in adj[cur]
            for nb in adj[cur]:
                if nb not in used:
                    used.add(nb)
                    if dfs(nb, used, depth + 1):
                        return True
                    used.remove(nb)
            return False
        return dfs(s, {s}, 0)

    for s in nodes:
        if search(s):
            return True
    return False


def expand(G):
    """All graphs from one cubic G by one vertex-into-triangle expansion."""
    for v in list(G.nodes()):
        nbrs = list(G[v])
        base = list(G.nodes()) + ["x", "y", "z"]
        for perm in itertools.permutations(nbrs):
            H = Graph()
            H.add_nodes_from(base)
            for u, w in G.edges():
                if u == v or w == v:
                    continue
                H.add_edge(u, w)
            x, y, z = "x", "y", "z"
            H.add_edges_from([(x, y), (y, z), (x, z)])
            for nb, tri in zip(perm, [x, y, z]):
                H.add_edge(nb, tri)
            H.remove_node(v)
            yield H


def load_canon(path):
    """Read canonical graph6 lines from a checkpoint file into a set."""
    with open(path) as f:
        return {l.strip() for l in f if l.strip()}


def main(maxn, outdir, resume_from=None, resume_n=0):
    """If resume_from is a canon file at size resume_n, continue from it."""
    os.makedirs(outdir, exist_ok=True)
    if resume_from is not None:
        canon = load_canon(resume_from)
        n = resume_n
        # rebuild the results table from any previously written level files
        results = []
        for m in range(4, n + 1, 2):
            p = os.path.join(outdir, f"level_{m}.txt")
            if os.path.exists(p):
                with open(p) as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("n="):
                            continue
                        if not line or line[0].isalpha():
                            continue
                        parts = line.split()
                        if len(parts) == 4 and parts[0].isdigit():
                            results.append(tuple(map(int, parts)))
        if not results:
            results = [(4, 1, 0, 0)]
        print(f"resumed from n={n} with {len(canon)} classes, "
              f"{len(results)} history rows", flush=True)
    else:
        G = nx.complete_graph(4)
        pool = [G]
        canon = set(batch_canonical(pool))          # K4 alone
        n = 4
        results = [(4, 1, 0, 0)]                    # (n, classes, avoidsC4, avoidsC4C8)
        print(f"n=4  classes=1  avoidsC4=0  avoidsC4C8=0", flush=True)
    while n + 2 <= maxn:
        # expand every current class
        gen_pool = []
        for c in canon:
            H = nx.from_graph6_bytes(c.encode())
            gen_pool.extend(expand(H))
        canon = set(batch_canonical(gen_pool))
        n += 2
        avoids_c4 = 0
        avoids_both = 0
        c4free = []
        for c in canon:
            H = nx.from_graph6_bytes(c.encode())
            dseq = [d for _, d in H.degree()]
            assert set(dseq) == {3} and len(H) == n, (len(H), dseq)
            if not has_c4(H):
                avoids_c4 += 1
                c4free.append(H)
        for H in c4free:
            if not has_c8(H):
                avoids_both += 1
        results.append((n, len(canon), avoids_c4, avoids_both))
        line = (f"n={n}  classes={len(canon)}  avoidsC4={avoids_c4}  "
                f"avoidsC4C8={avoids_both}")
        print(line, flush=True)
        # checkpoint
        with open(os.path.join(outdir, f"level_{n}.txt"), "w") as f:
            f.write(line + "\n")
            f.write("n classes avoidsC4 avoidsC4C8\n")
            for r in results:
                f.write(" ".join(map(str, r)) + "\n")
        # save the canonical reps so the run can be resumed from this level
        with open(os.path.join(outdir, f"level_{n}.canon"), "w") as f:
            f.write("\n".join(sorted(canon)) + "\n")
    return results


if __name__ == "__main__":
    maxn = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    outdir = sys.argv[2] if len(sys.argv) > 2 else "/workspace/code/out/expansion_census"
    main(maxn, outdir)
