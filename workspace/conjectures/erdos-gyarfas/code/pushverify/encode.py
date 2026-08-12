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

Symmetry breaking: we run without a lex-leader break (correctness over speed;
see driver), and instead validate every returned model independently.
"""
from pysat.formula import CNF
from pysat.card import CardEnc, EncType
from pysat.solvers import Cadical153

from lib.cycle_oracle import oracle
import networkx as nx


def edge_id(i, j):
    """Return variable number for undirected edge (i,j), 1-based for pysat."""
    if i > j:
        i, j = j, i
    # bijection: (i,j), 0<=i<j<n  ->  1 .. C(n,2)
    # use the standard row index
    return (i * (2 * n - i - 1)) // 2 + (j - i) + 1


n = None  # module-level n for edge_id; set by build_base


def _set_n(nn):
    global n
    n = nn


def build_base(nn):
    """CNF with degree>=3 and no-C4 constraints. Returns (cnf, var_count)."""
    global n
    _set_n(nn)
    cnf = CNF()
    top = n * (n - 1) // 2

    def eid(i, j):
        if i > j:
            i, j = j, i
        return (i * (2 * n - i - 1)) // 2 + (j - i) + 1

    # degree(u) >= 3 for every vertex u
    for u in range(n):
        lits = [eid(u, v) for v in range(n) if v != u]
        enc = CardEnc.atleast(lits=lits, bound=3, top_id=top,
                              encoding=EncType.seqcounter)
        top = enc.nv
        cnf.extend(enc.clauses)

    # no 4-cycle: for each 4-subset, forbid each of the 3 distinct cycles
    from itertools import combinations
    for (a, b, c, d) in combinations(range(n), 4):
        verts = [a, b, c, d]
        # 3 pairings of perfect matchings' complements: the three 4-cycles are
        # a-b-c-d-a, a-b-d-c-a, a-c-b-d-a  (each uses 4 of the 6 edges)
        cycles = [
            [eid(a, b), eid(b, c), eid(c, d), eid(d, a)],
            [eid(a, b), eid(b, d), eid(d, c), eid(c, a)],
            [eid(a, c), eid(c, b), eid(b, d), eid(d, a)],
        ]
        for cyc in cycles:
            cnf.append([-lit for lit in cyc])
    # fix local n
    return cnf, top


def model_to_graph(model):
    """Extract the graph from a solver model (list of ints)."""
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for lit in model:
        if lit > 0:
            # decode edge id to (i,j)
            eid = lit
            # find i: smallest such that i*(2n-i-1)/2 >= eid - 1... we stored
            # id = (i*(2n-i-1))//2 + (j-i) + 1 with 0<=i<j<n
            found = None
            for i in range(n):
                lo = (i * (2 * n - i - 1)) // 2 + 1          # j = i+1 -> id min
                hi = (i * (2 * n - i - 1)) // 2 + (n - 1 - i) + 1  # j=n-1 -> id max
                if lo <= eid <= hi:
                    j = i + (eid - lo) + 1
                    found = (i, j)
                    break
            if found is not None:
                G.add_edge(*found)
            else:
                raise ValueError(f"bad edge id {eid}")
    return G


def find_cycles_to_block(G, n):
    """Return list of C8 and C16 vertex-cycles in G (dedup)."""
    # use networkx simple_cycles to be independent of the oracle
    cycles = [c for c in nx.simple_cycles(G.to_directed()) if len(c) >= 3]
    blocks = []
    seen = set()
    for c in cycles:
        L = len(c)
        if L in (8, 16):
            # canonical key: rotate so min vertex first, then fix direction
            m = min(c)
            idx = c.index(m)
            rot = tuple(c[idx:] + c[:idx])
            rev = tuple([rot[0]] + list(reversed(rot[1:])))
            key = min(rot, rev)
            if key not in seen:
                seen.add(key)
                blocks.append(list(c))
    return blocks


def blocking_clause(cycle, n):
    """Negative clause forbidding the given cycle (list of vertex ids)."""
    lits = set()
    k = len(cycle)
    for t in range(k):
        i, j = cycle[t], cycle[(t + 1) % k]
        if i < j:
            lits.add(edge_id(i, j))
        else:
            lits.add(edge_id(j, i))
    return [-lit for lit in sorted(lits)]
