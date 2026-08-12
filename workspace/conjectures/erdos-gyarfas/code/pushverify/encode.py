"""Lazy-SAT encoding of the Erdős–Gyárfás push-verification question.

Question: does there exist a simple graph on n vertices with minimum degree
>= 3 and no 4-cycle, no 8-cycle, no 16-cycle?  For n <= 24 (indeed n < 32) the
only powers of two a cycle can have are {4, 8, 16}, so UNSAT of this question
is exactly the theorem "no counterexample to Erdős–Gyárfás on <= n vertices".

Encoding (declarative, over boolean adjacency vars x_uv, one per unordered pair
u<v):
  - degree(u) >= 3  :  CardEnc.atleast(bound=3) over the n-1 incident vars.
  - no 4-cycle      :  complete, direct.  For each 4-subset {a,b,c,d}, forbid
                       each of the 3 distinct 4-cycles on those vertices with a
                       "not all four edges" clause.
  - no 8 / no 16    :  lazy.  The direct count is C(n,8)*7!/2 (~1.9e9 at n=24),
                       so we solve the C4+degree base, take a model, find its
                       C8/C16 with the cycle oracle, add one blocking clause per
                       found cycle, and iterate until UNSAT.

Soundness of UNSAT: every blocking clause forbids one specific cycle that some
returned model really had.  If a graph G had no C8 and no C16 at all, it would
satisfy every blocking clause (it contains none of those specific cycles), so
G would be a model of the final CNF.  Hence UNSAT of the final CNF = no graph
on n vertices avoids 4, 8, and 16 simultaneously.  The C4 part is direct, not
lazy, so it is never left to the loop.

All functions take n explicitly; no module-level state.

Exports:
    edge_id(i, j, n)        -> 1-based variable of edge {i,j}, a bijection
    arg_edge_id(eid, n)     -> (i,j) with i<j  (inverse of edge_id)
    build_base(n)           -> (CNF with degree>=3 + no-C4, top_var)
    blocking_clause(cycle, n) -> [neg vars] forbidding that specific cycle
    find_bad_cycles(G, n)   -> set of vertex-tuples of all C4/C8/C16 in G
"""
from itertools import combinations

from pysat.formula import CNF
from pysat.card import CardEnc, EncType

import networkx as nx


# ---------------------------------------------------------------------------
# edge variable bijections
# ---------------------------------------------------------------------------

def edge_id(i, j, n):
    """1-based variable for undirected edge (i,j), 0<=i<j<n.

    Bijection: pairs (0,1..n-1), (1,2..n-1), ... map to 1..C(n,2).
    Offset before row i: i*(n-1) - i*(i-1)/2 (that many pairs with first
    index < i), then position j-i within row i.
    """
    if i > j:
        i, j = j, i
    return i * (n - 1) - i * (i - 1) // 2 + (j - i)


def arg_edge_id(eid, n):
    """Inverse of edge_id: given 1-based variable, return (i, j), i<j."""
    for i in range(n):
        lo = i * (n - 1) - i * (i - 1) // 2 + 1
        hi = i * (n - 1) - i * (i - 1) // 2 + (n - 1 - i)
        if lo <= eid <= hi:
            return i, i + (eid - lo) + 1
    raise ValueError(f"edge id {eid} out of range for n={n}")


# ---------------------------------------------------------------------------
# the CNF
# ---------------------------------------------------------------------------

def build_base(n):
    """CNF: degree(u)>=3 for all u, and no 4-cycle.  Returns (cnf, top_var)."""
    cnf = CNF()
    top = n * (n - 1) // 2  # highest edge variable

    # degree(u) >= 3: sequential-counter cardinality, incremental nv
    for u in range(n):
        lits = [edge_id(u, v, n) for v in range(n) if v != u]
        enc = CardEnc.atleast(lits=lits, bound=3, top_id=top,
                              encoding=EncType.seqcounter)
        top = enc.nv
        cnf.extend(enc.clauses)

    # no 4-cycle: for each 4-subset, forbid each of the 3 distinct cycles on
    # those vertices (the 3 cycles use 4 of the 6 edges each; every C4 of G is
    # one of these, so the clauses forbid exactly the C4s).
    for (a, b, c, d) in combinations(range(n), 4):
        e = lambda i, j: edge_id(i, j, n)  # noqa: E731
        cycles = [
            (e(a, b), e(b, c), e(c, d), e(d, a)),
            (e(a, b), e(b, d), e(d, c), e(c, a)),
            (e(a, c), e(c, b), e(b, d), e(d, a)),
        ]
        for cyc in cycles:
            cnf.append([-lit for lit in cyc])
    return cnf, top


# ---------------------------------------------------------------------------
# lazy blocking helpers
# ---------------------------------------------------------------------------

def find_bad_cycles(G, n):
    """All distinct simple cycles of length 4, 8, or 16 in G (canonical keys).

    Every simple cycle is enumerated (networkx.simple_cycles on the bidirected
    graph, length >= 3), and each of length in {4,8,16} is stored under a
    canonical key (rotated so the minimum vertex is first, direction chosen so
    the second vertex is the smaller of the two neighbours of the minimum).
    """
    out = set()
    for c in nx.simple_cycles(G.to_directed()):
        L = len(c)
        if L < 3 or L not in (4, 8, 16):
            continue
        m = min(c)
        k = c.index(m)
        rot = tuple(c[k:] + c[:k])
        rev = tuple([rot[0]] + list(reversed(rot[1:])))
        out.add(min(rot, rev))
    return out


def blocking_clause(cycle, n):
    """Negative clause forbidding the given cycle (iterable of vertex ids)."""
    lits = set()
    k = len(cycle)
    for t in range(k):
        i, j = cycle[t], cycle[(t + 1) % k]
        lits.add(edge_id(i, j, n))
    return [-lit for lit in sorted(lits)]