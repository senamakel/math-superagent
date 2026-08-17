"""Exact 6-vertex-condition embedding-count checker for the Conway 99 family.

The t-vertex condition (Hestenes-Higman 1971; Reichard Def 4): fix a "graph
type" (S, x0, y0) where S is a graph on t vertices with two distinguished
vertices x0, y0.  For a pair (x, y) of vertices of the host graph G, the number
of *induced* subgraphs of G that are isomorphic to S with x0 -> x, y0 -> y must
depend only on whether (x, y) is an edge, a non-edge, or x == y.  If this holds
for every type of order <= t and every pair, G satisfies the t-vertex condition.

For our host graphs we only discriminate the ADJACENT vs NON-ADJACENT classes
(the types below have x0 != y0, so the x == y class is always 0 and carries no
information).  The two hosts are the rank-3 / vertex-transitive controls:

    rook(3)  = srg(9,4,1,2)       (3x3 rook's graph = Paley(9))
    bvls     = srg(243,22,1,2)    (Berlekamp-van Lint-Seidel graph)

By vertex-transitivity the automorphism group is transitive on vertices, on
directed edges and on (non-adjacent) ordered pairs, so EVERY t-vertex embedding
count of every type must be a single constant on each adjacency class.  This is
the mandatory control pass: it catches any checker bug, because a bug
(unsound canonical form, a missing induced/non-induced distinction, an
off-by-one in the distinguished pair) almost always breaks constancy on at
least one of these two hosts.

We count induced embeddings as *injective maps* of V(S) into V(G) with
x0 -> x, y0 -> y whose image has exactly the adjacency pattern of S (both edges
present and non-edges absent).  The number of *distinct induced subgraphs* is
that count divided by |Aut(S) fixing x0,y0|, a constant independent of (x,y),
so constancy of the two measures is equivalent.  Exact integer arithmetic
throughout (Python ints; 243-bit adjacency bitsets, no floats).

Types checked (see TYPE defs below):
  n3   -- two disjoint triangles joined by exactly 2 cross edges (a-d, b-e).
          This is the 6-vertex type over the n3 configuration that runs the
          Makhnev n3>=1 lever.  Two distinguished-pair choices:
            (a, d) ADJACENT       (a, e) NON-ADJACENT
  C6   -- a 6-cycle, pair (x0,y0) adjacent (two consecutive cycle vertices).
  T2   -- two triangles joined by exactly 1 cross edge (a-d), pair (a,d) ADJ.

Complexity: O(P * b) where P = number of (x,y) pairs of the adjacency class
and b is the per-pair branching of the 4-vertex induced-embedding recursion.
With 243-bit bitset candidate intersection b is small (the type's adjacency
stridently constrains each additional vertex).  P <= C(243,2) = 29403.
"""
import itertools

import numpy as np

from lib.srg import rook, bvls_graph


# ---------------------------------------------------------------------------
# Bitset adjacency of the host graph
# ---------------------------------------------------------------------------
class Host:
    """Host graph G with vertex set {0..n-1}, bitset neighbourhoods."""

    def __init__(self, A):
        A = np.asarray(A, dtype=np.int64)
        self.n = A.shape[0]
        self.A = A
        self.N = []
        for i in range(self.n):
            bits = 0
            for j in range(self.n):
                if A[i, j]:
                    bits |= 1 << j
            self.N.append(bits)
        self.ALL = (1 << self.n) - 1
        # adj[x][y]: 1 edge, 0 non-edge (x!=y)
        self.adj = np.array(A, dtype=np.int64)

    def matching_edges(self):
        return [(x, y) for x in range(self.n) for y in range(x + 1, self.n) if self.adj[x, y]]

    def non_edges(self):
        return [(x, y) for x in range(self.n) for y in range(x + 1, self.n) if not self.adj[x, y]]


# ---------------------------------------------------------------------------
# The embedding counter
# ---------------------------------------------------------------------------
def count_induced_embeddings(G, S_adj, x0, y0, x, y):
    """Number of induced embeddings of the 6-vertex type (S_adj, x0, y0) into G
    mapping x0 -> x, y0 -> y.

    S_adj: dict {(u,v): 0/1} over the 6 labels, symmetric, 0 diagonal, giving
    the exact adjacency pattern of S (1 = required edge, 0 = required non-edge).
    We return the number of INJECTIVE maps f: V(S) -> V(G) with f(x0)=x,
    f(y0)=y such that the induced subgraph on f(V(S)) equals S (edges present
    where S has edges AND non-edges present where S has non-edges).
    """
    labels = [u for u in S_adj if isinstance(u, str) or True][:0]  # placeholder
    # derive the 6 labels from the keys of S_adj
    labels = sorted({u for (u, v) in S_adj for u in (u, v)})
    if x0 not in labels or y0 not in labels:
        raise ValueError("distinguished vertices must be labels of S")
    # start adjacency must match
    if (x == y) != (x0 == y0):
        return 0
    if x != y and (G.adj[x, y] != S_adj.get((x0, y0), S_adj.get((y0, x0)))):
        return 0
    if x == y:
        # our types have x0 != y0, so x == y admits 0 embeddings
        return 0

    extra = [u for u in labels if u != x0 and u != y0]  # 4 additional labels
    used = (1 << x) | (1 << y)
    # placement order: most-constrained-first is not essential at this size

    def rec(placed):  # placed: dict label -> gvertex (x0,y0 already in)
        if len(placed) == len(labels):
            return 1
        u = next(l for l in extra if l not in placed)
        # candidate mask: v must (a) be unused, (b) match S's row to every
        # already-placed label/vertex pair (both edge and non-edge constraints).
        cand = G.ALL & ~used
        for p, gv in placed.items():
            req_edge = S_adj.get((u, p))
            if req_edge is None:
                req_edge = S_adj.get((p, u))
            if req_edge == 1:
                cand &= G.N[gv]
            elif req_edge == 0:
                cand &= ~G.N[gv]
        total = 0
        while cand:
            v = (cand & -cand).bit_length() - 1
            cand &= cand - 1
            placed[u] = v
            total += rec(placed)
            del placed[u]
        return total

    return rec({x0: x, y0: y})


# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------
def _mk(edges, verts):
    """Symmetric 0/1 adjacency dict over verts with exactly `edges` (set of
    unordered pairs) set to 1 and all other distinct pairs set to 0."""
    verts = list(verts)
    D = {}
    for i, u in enumerate(verts):
        D[(u, u)] = 0
        for j, v in enumerate(verts):
            if i != j:
                D[(u, v)] = 1 if frozenset((u, v)) in edges else 0
    return D


# n3 type: triangles {a,b,c},{d,e,f} joined by exactly 2 edges a-d, b-e.
N3_EDGES = {frozenset(('a', 'b')), frozenset(('b', 'c')), frozenset(('c', 'a')),
            frozenset(('d', 'e')), frozenset(('e', 'f')), frozenset(('f', 'd')),
            frozenset(('a', 'd')), frozenset(('b', 'e'))}
N3_VERT = ['a', 'b', 'c', 'd', 'e', 'f']
N3 = _mk(N3_EDGES, N3_VERT)

# 6-cycle, pair (x0,y0) = two consecutive vertices (an edge of the cycle).
C6_EDGES = {frozenset(('a', 'b')), frozenset(('b', 'c')), frozenset(('c', 'd')),
            frozenset(('d', 'e')), frozenset(('e', 'f')), frozenset(('f', 'a'))}
C6_VERT = ['a', 'b', 'c', 'd', 'e', 'f']
C6 = _mk(C6_EDGES, C6_VERT)

# two triangles joined by exactly one cross edge a-d.
T2_EDGES = {frozenset(('a', 'b')), frozenset(('b', 'c')), frozenset(('c', 'a')),
            frozenset(('d', 'e')), frozenset(('e', 'f')), frozenset(('f', 'd')),
            frozenset(('a', 'd'))}
T2_VERT = ['a', 'b', 'c', 'd', 'e', 'f']
T2 = _mk(T2_EDGES, T2_VERT)


def aut_stabilizer(S_adj, x0, y0):
    """|Aut(S) fixing x0,y0| by brute force over the 6! label permutations."""
    labels = sorted({u for (u, v) in S_adj for u in (u, v)})
    n = 0
    for perm in itertools.permutations(labels):
        if perm[labels.index(x0)] != x0 or perm[labels.index(y0)] != y0:
            continue
        ok = True
        for u in labels:
            for v in labels:
                if S_adj[(u, v)] != S_adj[(perm[labels.index(u)], perm[labels.index(v)])]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            n += 1
    return n


def summary(name, G, S_adj, x0, y0, class_pairs):
    """Compute the embedding count for every pair in class_pairs (a list of
    (x,y) with x<y).  Returns (counts:list, distinct_set, constant:bool)."""
    counts = [count_induced_embeddings(G, S_adj, x0, y0, x, y) for (x, y) in class_pairs]
    return counts, set(counts), (len(set(counts)) == 1)


def run_host(name, G):
    edges = G.matching_edges()
    non_edges = G.non_edges()
    print("\n" + "=" * 88)
    print("HOST %s: n=%d, edges=%d, non-edges=%d, vertex-transitive (rank-3 control)"
          % (name, G.n, len(edges), len(non_edges)))
    print("=" * 88)

    def report(tname, S_adj, x0, y0, pairs, note):
        counts, distinct, const = summary(tname, G, S_adj, x0, y0, pairs)
        aut = aut_stabilizer(S_adj, x0, y0)
        # distinct induced subgraphs = embeddings / aut_stabilizer (constant)
        sub_cnt = counts[0] // aut if counts else 0
        print("\n  type %-4s pair (x0,y0)=(%s,%s) %s  over %d pairs of the class"
              % (tname, x0, y0, note, len(pairs)))
        print("      embedding counts: min=%d max=%d distinct_values=%s constant_within_class=%s"
              % (min(counts), max(counts), sorted(distinct), const))
        print("      per-(x,y) embeddings = %s ; induced-subgraph count = %s  (|Aut fix (x0,y0)|=%d)"
              % (counts[0] if counts else 0,
                 (counts[0] // aut if counts and counts[0] % aut == 0 else (counts[0], '/' + str(aut) if counts else '')),
                 aut))
        if not const:
            print("      *** NON-CONSTANT: the vertex condition FAILS here.  "
                  "This is expected only if the checker has a bug (controls are rank-3).")
        return const

    ok = True
    # --- n3 type, two distinguished-pair choices ---
    ok &= report('n3', N3, 'a', 'd', edges, '[ADJ]')
    ok &= report('n3', N3, 'a', 'e', non_edges, '[NONADJ]')
    # --- structurally simple types that DO occur (real nonzero control) ---
    ok &= report('C6', C6, 'a', 'b', edges, '[ADJ]')
    ok &= report('T2', T2, 'a', 'd', edges, '[ADJ]')
    return ok


def main():
    print("CAPI: code/out/six_vc_n3_type.py -- exact 6-vertex-condition embedding checker")
    print("CAPI: definition: Reichard Def 4 (induced subgraphs of a type, count per fixed pair")
    print("CAPI:   depends only on edge/non-edge).  Hosts = vertex-transitive rank-3 controls")
    print("CAPI:   rook(3)=srg(9,4,1,2) and bvls=srg(243,22,1,2), so EVERY type must be")
    print("CAPI:   constant on each adjacency class.  Exact ints, 243-bit bitsets.")
    print("=" * 88)

    hosts = [("rook(3) srg(9,4,1,2)", Host(rook(3))),
             ("bvls srg(243,22,1,2)", Host(bvls_graph()))]
    all_ok = True
    for name, G in hosts:
        all_ok &= run_host(name, G)

    print("\n" + "=" * 88)
    print("CONTROL PASS: every type is constant within each adjacency class on BOTH "
          "vertex-transitive hosts: %s" % ("PASS" if all_ok else "FAIL"))
    if all_ok:
        print("The counting is self-consistent: no checker bug detected at the rank-3 controls.")
    print("=" * 88)


if __name__ == "__main__":
    main()
