"""Extract the C16 (and C8) profile of the K4-triangle-expansion family from on-disk canon files.

The census recorded only avoidsC4 and avoidsC4C8 per level. This script reads the
saved canonical graph6 classes and computes, per level n, the EG-relevant profile:

  total         : number of isomorphism classes
  avoidsC4      : no 4-cycle
  avoidsC4C8    : no 4-cycle and no 8-cycle
  avoidsC4C16   : no 4-cycle and no 16-cycle   (NEW — never computed before)
  avoidsC4C8C16 : no 4, 8, or 16-cycle        (the full power-of-two-free count for n<=24)

Verification: total and avoidsC4 must reproduce the census table
(1,1,1,3,7,24,93,434,2110,11002,58713 and 0,0,0,1,1,2,5,15,50,202,807).
"""
import os
import sys
import networkx as nx
from networkx import Graph


def has_c4(G):
    nodes = list(G.nodes())
    for i in range(len(nodes)):
        u = nodes[i]
        for j in range(i + 1, len(nodes)):
            v = nodes[j]
            common = set(G[u]) & set(G[v])
            if len(common) >= 2:
                return True
    return False


def has_closed_cycle(G, L):
    """Exact: does G contain a simple cycle of length L? (bounded simple DFS)"""
    adj = {u: set(G[u]) for u in G}

    def search(s):
        def dfs(cur, used, depth):
            if depth == L - 1:
                return s in adj[cur]
            for nb in adj[cur]:
                if nb not in used:
                    used.add(nb)
                    if dfs(nb, used, depth + 1):
                        return True
                    used.remove(nb)
            return False
        return dfs(s, {s}, 0)

    for s in G:
        if search(s):
            return True
    return False


def main(outdir):
    results = []
    for n in range(4, 26, 2):
        path = os.path.join(outdir, f"level_{n}.canon")
        if not os.path.exists(path):
            continue
        with open(path) as f:
            classes = [l.strip() for l in f if l.strip()]
        total = len(classes)
        aC4 = aC4C8 = aC4C16 = aC4C8C16 = 0
        for c in classes:
            G = nx.from_graph6_bytes(c.encode())
            h4 = has_c4(G)
            if not h4:
                aC4 += 1
                h8 = has_closed_cycle(G, 8)
                h16 = has_closed_cycle(G, 16)
                if not h8:
                    aC4C8 += 1
                if not h16:
                    aC4C16 += 1
                if not h8 and not h16:
                    aC4C8C16 += 1
        results.append((n, total, aC4, aC4C8, aC4C16, aC4C8C16))
        print(f"n={n:2d}  total={total:6d}  avoidsC4={aC4:4d}  avoidsC4C8={aC4C8:3d}  "
              f"avoidsC4C16={aC4C16:4d}  avoidsC4C8C16={aC4C8C16:3d}", flush=True)
    return results


if __name__ == "__main__":
    outdir = sys.argv[1] if len(sys.argv) > 1 else "/workspace/code/out/expansion_census"
    main(outdir)
