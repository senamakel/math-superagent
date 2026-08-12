"""Base CNF for the (2,2)-shaped cut-vertex Erdős–Gyárfás push.

Question: does there exist a simple graph on n vertices, {v} ∪ A ∪ B, with
  * |A|+|B|+1 = n,  no edges between A and B,
  * deg(v) = 4, with exactly 2 neighbours of v in A and exactly 2 in B,
  * every other vertex has degree >= 3,
  * no cycle of length 4, 8, or 16?

This module builds the *base* CNF: the partition + degree(v)=4 + exactly-2-in-A
/ exactly-2-in-B shape, every-other-vertex degree>=3, and NO-4-CYCLE (direct,
complete, as in encode.py).  C8 and C16 are left to the lazy blocking loop in
shape_sat.py: blocking a specific cycle found by the oracle is sound (a graph
that avoids C8/C16 entirely violates none of those clauses), so UNSAT of the
final CNF means no shaped graph on n avoids 4, 8 and 16 together.

Vertex variables (all 1-based):
  edge(i,j)   in 1..C(n,2)        —— same bijection as pushverify.encode
  inA[i]      for i != v          —— 1 = i in A, 0 = i in B
  p[i]        = edge(v,i) AND inA[i]   (aux: "i is a v-neighbour lying in A")
  q[i]        = edge(v,i) AND NOT inA[i] (aux: "i is a v-neighbour lying in B")

Exports:
    build_base_shape(n, v=0) -> (cnf, top, atoms)
        atoms = {'inA': {i: var}, 'p': {i: var}, 'q': {i: var}, 'v': v}
    (plus edge_id / arg_edge_id re-exported from pushverify.encode)
"""
from pysat.formula import CNF
from pysat.card import CardEnc, EncType

from pushverify.encode import edge_id, arg_edge_id  # reuse the bijection


def build_base_shape(n, v=0):
    cnf = CNF()
    EV = n * (n - 1) // 2
    top = EV  # highest edge variable

    others = [i for i in range(n) if i != v]
    # --- partition atoms: one per non-v vertex
    inA = {}
    nxt = top + 1
    for i in others:
        inA[i] = nxt
        nxt += 1
    top = nxt - 1
    # --- no edges between A and B: if edge(i,j) then inA[i]==inA[j]
    for a in range(len(others)):
        for b in range(a + 1, len(others)):
            i, j = others[a], others[b]
            e = edge_id(i, j, n)
            # forbid i in A & j in B & e  ;  forbid i in B & j in A & e
            cnf.append([-inA[i], inA[j], -e])
            cnf.append([inA[i], -inA[j], -e])

    # --- deg(v)=4
    nbrs = [edge_id(v, i, n) for i in others]
    enc = CardEnc.equals(lits=nbrs, bound=4, top_id=top,
                         encoding=EncType.seqcounter)
    top = enc.nv
    cnf.extend(enc.clauses)

    # --- exactly 2 v-neighbours in A and exactly 2 v-neighbours in B.
    # p[i] = edge(v,i) AND inA[i];  q[i] = edge(v,i) AND NOT inA[i]
    p, q = {}, {}
    for i in others:
        ev = edge_id(v, i, n)
        # p
        top += 1; p[i] = top
        cnf.append([-ev, -inA[i], p[i]])
        cnf.append([ev, -p[i]])
        cnf.append([inA[i], -p[i]])
        # q
        top += 1; q[i] = top
        cnf.append([-ev, inA[i], q[i]])
        cnf.append([ev, -q[i]])
        cnf.append([-inA[i], -q[i]])
    encA = CardEnc.equals(lits=[p[i] for i in others], bound=2, top_id=top,
                          encoding=EncType.seqcounter)
    top = encA.nv
    cnf.extend(encA.clauses)
    encB = CardEnc.equals(lits=[q[i] for i in others], bound=2, top_id=top,
                          encoding=EncType.seqcounter)
    top = encB.nv
    cnf.extend(encB.clauses)

    # --- degree >= 3 for every other vertex
    for u in others:
        lits = [edge_id(u, w, n) for w in range(n) if w != u]
        enc = CardEnc.atleast(lits=lits, bound=3, top_id=top,
                              encoding=EncType.seqcounter)
        top = enc.nv
        cnf.extend(enc.clauses)

    # --- no 4-cycle (direct, complete)
    from itertools import combinations
    for (a, b, c, d) in combinations(range(n), 4):
        e = lambda i, j: edge_id(i, j, n)
        cycles = [
            (e(a, b), e(b, c), e(c, d), e(d, a)),
            (e(a, b), e(b, d), e(d, c), e(c, a)),
            (e(a, c), e(c, b), e(b, d), e(d, a)),
        ]
        for cyc in cycles:
            cnf.append([-lit for lit in cyc])

    atoms = {'inA': inA, 'p': p, 'q': q, 'v': v}
    return cnf, top, atoms
