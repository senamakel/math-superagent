"""Correct independent count of induced 5-cycles (pentagons) on BvLS(243,22,1,2).

An induced C5 is 5 vertices with 5 edges and every induced degree exactly 2.
(5 vertices, 5 edges, all degrees 2 in a simple graph => exactly one 5-cycle.)

Anchor at a directed edge (a,b); the pentagon is a-b-c-d-e-a with
  c in N(b)\{a}, c not adj a (else chord)
  d in N(c)∩N(e)  (d the vertex after c; e the vertex before a)
  e in N(a)\{b}
and the 5-set is then verified with an exact full induced-degree==2 check so
no loose criterion admits a non-C5 (the bug in the previous attempt, which
counted C4-with-pendant shapes).

Each induced C5 is anchored at exactly 10 directed edges, so divide by 10.
Exact integer arithmetic only. Entry guard: rook(3) induced C5 = 0.
"""
import numpy as np
from lib.srg import bvls_graph, rook

def is_induced_C5(A, verts):
    """verts: 5 distinct vertices; True iff they induce exactly a 5-cycle."""
    adj = A  # numpy
    s = list(verts)
    for i, v in enumerate(s):
        deg = sum(1 for j in range(len(s)) if i != j and bool(adj[v, s[j]]))
        if deg != 2:
            return False
    # degrees all 2; count edges must be 5 (automatically: sum deg=10/2=5)
    return True

def count_induced_C5(A):
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    adj = [set(np.nonzero(A[i])[0]) for i in range(n)]
    total = 0
    for a in range(n):
        for b in adj[a]:
            for c in adj[b]:
                if c == a:
                    continue
                if c in adj[a]:          # chord a-c, cannot be induced C5 anchor
                    continue
                for e in adj[a]:
                    if e == b or e == c:
                        continue
                    if e in adj[b]:      # chord b-e
                        continue
                    # d = common neighbour of c and e, distinct, not adj a or b
                    for d in adj[c]:
                        if d == a or d == b or d == e:
                            continue
                        if d not in adj[e]:
                            continue
                        if d in adj[a] or d in adj[b]:  # chords
                            continue
                        if is_induced_C5(A, (a, b, c, d, e)):
                            total += 1
    assert total % 10 == 0, total
    return total // 10

Ar = rook(3)
g = count_induced_C5(Ar)
print("rook(3) induced C5:", g, " expect 0, match:", g == 0)

B = bvls_graph()
cnt = count_induced_C5(B)
form = 243 * 22 * 20 * 18 // 5
print("BvLS induced C5:", cnt)
print("closed form n*k*(k-2)*(k-4)/5:", form)
print("MATCH:", cnt == form)
