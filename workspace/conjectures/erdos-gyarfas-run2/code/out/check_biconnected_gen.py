"""Correctness check for the 2-connected graph generator: reproduce the known
counts of nonisomorphic 2-connected graphs (OEIS A002218), and independently
verify a selection of the generated graphs by an exhaustive small reference
(only up to n=6 where 2^15 = 32768 graphs, fast).

OEIS A002218 (nonisomorphic 2-connected graphs on n vertices):
n=3: 1, n=4: 1, n=5: 4, n=6: 19, n=7: 121, n=8: 1042, n=9: 12594, n=10: 196600...
"""

import sys
sys.path.insert(0, "/workspace/code")
from lib.biconnected_gen import generate_2connected_levels
import networkx as nx

KNOWN = {3: 1, 4: 1, 5: 4, 6: 19, 7: 121, 8: 1042, 9: 12594}

N = 8
levels = generate_2connected_levels(N, dump_every=0)
print("Generator counts vs OEIS A002218:")
ok = True
for n in range(3, N + 1):
    got = len(levels[n])
    want = KNOWN.get(n)
    mark = "OK" if want is not None and got == want else "?"
    if want is not None and got != want:
        ok = False
        mark = "MISMATCH"
    print(f"  n={n}: generated={got}  OEIS={want}  {mark}")

# independent exhaustive reference only for n<=6
import itertools
def ref_count(n):
    edges = list(itertools.combinations(range(n), 2))
    reps = []
    for mask in itertools.product([0, 1], repeat=len(edges)):
        G = nx.Graph()
        G.add_nodes_from(range(n))
        for e, b in zip(edges, mask):
            if b:
                G.add_edge(*e)
        if n <= 2 or not nx.is_biconnected(G):
            continue
        if not any(nx.is_isomorphic(G, R) for R in reps):
            reps.append(G)
    return len(reps)

print("\nIndependent exhaustive reference (n<=6):")
for n in range(3, 7):
    r = ref_count(n)
    g = len(levels[n])
    mm = "OK" if r == g else "MISMATCH"
    if r != g:
        ok = False
    print(f"  n={n}: exhaustive={r} generator={g} {mm}")

print("\nALL COUNTS MATCH" if ok else "\nSOME MISMATCH — FIX GENERATOR")
