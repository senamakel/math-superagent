"""Probe the two mechanisms the structural encoding relies on.

1. pysat CardEnc.atleast(lits, bound, output=aux, ...) with EncType.seqcounter
   must be an EXACT indicator: for every assignment of the k literals,
       (exists extension with aux True)  iff  sum(lits) >= bound
     (exists extension with aux False)  iff  sum(lits) <= bound-1
   checked exhaustively over all 2^k assignments for k in 2..6, all bounds.
   Also: the aux var and all helper vars must lie in (top_id, enc.nv].

2. igraph canonical_permutation() must give one canonical key per
   isomorphism class: random relabelings of a graph must produce the same
   key, non-isomorphic graphs different keys.  This is the exact iso-class
   counter for the instrumented driver (nauty/networkx pairwise VF2 would be
   too slow in the CEGAR loop).

Usage: python code/pushverify/probe_structural.py
"""
from pysat.card import CardEnc, EncType
from pysat.solvers import Cadical153
import networkx as nx
import igraph
import random
from itertools import combinations


def _assump_sat(clauses, forced_lits):
    """SAT of clauses under assumptions forced_lits (list of non-zero ints)."""
    s = Cadical153(bootstrap_with=clauses)
    r = s.solve(assumptions=forced_lits)
    s.delete()
    return r is True


def check_atleast_output_exact():
    print("== CardEnc.atleast(output=aux) exact-indicator semantics ==")
    ok = True
    for k in range(2, 7):
        for bound in range(0, k + 1):
            top = k
            aux = top + 1
            enc = CardEnc.atleast(lits=list(range(1, k + 1)), bound=bound,
                                  output=aux, top_id=top,
                                  encoding=EncType.seqcounter)
            used = {abs(l) for cl in enc.clauses for l in cl}
            assert aux in used, (k, bound, "aux not used")
            assert max(used) <= enc.nv and min(used) > top, \
                (k, bound, "var outside (top_id, enc.nv]")
            for mask in range(1 << k):
                forced = []
                for b in range(k):
                    forced.append((b + 1) if (mask >> b) & 1 else -(b + 1))
                cnt = bin(mask).count("1")
                sat_t = _assump_sat(enc.clauses, forced + [aux])
                sat_f = _assump_sat(enc.clauses, forced + [-aux])
                if (cnt >= bound) != sat_t or (cnt < bound) != sat_f:
                    print(f"  k={k} bound={bound} mask={mask:0{k}b} cnt={cnt}: "
                          f"aux=True sat={sat_t} aux=False sat={sat_f} "
                          f"-- NOT an exact indicator")
                    ok = False
                    break
            top = enc.nv
    print("  result:", "OK: aux <-> (sum >= bound) exactly, all k<=6" if ok
          else "FAIL")
    return ok


def check_atmost_output_neg():
    """Fallback: atmost(lits, bound=3, output=-aux) gives (sum<=3) <-> -aux,
    i.e. aux <-> (sum >= 4).  Exact equivalence checked the same way."""
    print("== CardEnc.atmost(bound=3, output=-aux) exact-indicator semantics ==")
    ok = True
    for k in range(2, 7):
        for bound in range(3, 4):          # only bound=3 is used by the driver
            top = k
            aux = top + 1
            enc = CardEnc.atmost(lits=list(range(1, k + 1)), bound=bound,
                                 output=-aux, top_id=top,
                                 encoding=EncType.seqcounter)
            used = {abs(l) for cl in enc.clauses for l in cl}
            assert aux in used, (k, bound, "aux not used")
            for mask in range(1 << k):
                forced = []
                for b in range(k):
                    forced.append((b + 1) if (mask >> b) & 1 else -(b + 1))
                cnt = bin(mask).count("1")
                sat_t = _assump_sat(enc.clauses, forced + [aux])
                sat_f = _assump_sat(enc.clauses, forced + [-aux])
                if (cnt >= 4) != sat_t or (cnt < 4) != sat_f:
                    print(f"  k={k} bound={bound} mask={mask:0{k}b} cnt={cnt}: "
                          f"-- NOT exact")
                    ok = False
                    break
            top = enc.nv
    print("  result:", "OK: aux <-> (sum >= 4) exactly (atmost-3 route)" if ok
          else "FAIL")
    return ok


def check_igraph_canonical():
    print("== igraph canonical_permutation as iso-class key ==")
    ok = True
    # small host of non-isomorphic graphs (some pairs: C4 vs C4+diagonal,
    # K3+K3 vs C6, Petersen vs K5,5 edge-cases avoided -- all differ in deg seq)
    candidates = [
        nx.complete_graph(4),
        nx.cycle_graph(4),
        nx.cycle_graph(5),
        nx.petersen_graph(),
        nx.complete_graph(5),
        nx.cycle_graph(6),
        nx.circular_ladder_graph(5),          # prism
        nx.complete_bipartite_graph(3, 3),
    ]
    keys = {}
    for i, G in enumerate(candidates):
        kl = []
        for trial in range(20):
            perm = list(range(G.number_of_nodes()))
            random.shuffle(perm)
            H = nx.relabel_nodes(G, {v: perm[v] for v in G.nodes()})
            g = igraph.Graph(n=H.number_of_nodes())
            g.add_edges(list(H.edges()))
            canon = g.canonical_permutation()
            # key: adjacency of the graph permuted by the canonical ordering
            P = [0] * len(canon)
            for v, c in enumerate(canon):
                P[c] = v
            key = tuple(sorted(tuple(sorted(P[a], P[b]) if P[a] < P[b]
                                          else (P[b], P[a]))
                               for a, b in H.edges()))
            kl.append(key)
        if len(set(kl)) != 1:
            print(f"  graph {i}: relabelings gave {len(set(kl))} different "
                  f"canonical keys -- NOT canonical")
            ok = False
        keys.setdefault(kl[0], []).append(i)
    if len(keys) != len(candidates):
        print(f"  collision: {len(candidates)} graphs, {len(keys)} keys")
        ok = False
    print("  result:", "OK: canonical key stable under relabel, distinct "
                       "classes distinct" if ok else "FAIL")
    return ok


def iso_table_hint():
    """Pack canonical-keys + count graph6-labeled/iso by brute force at n=10:
    NOT run here (too many graphs); just sanity-check the packing on the
    one meaningful case: does the Petersen graph get ONE iso key no matter
    the vertex numbering?"""
    print("== graph6-labeled vs iso canonical pack (sanity, Petersen) ==")
    G = nx.petersen_graph()
    keys = set()
    for trial in range(100):
        perm = list(range(10))
        random.shuffle(perm)
        H = nx.relabel_nodes(G, {v: perm[v] for v in G.nodes()})
        g = igraph.Graph(n=10)
        g.add_edges([(int(a), int(b)) for a, b in H.edges()])
        canon = g.canonical_permutation()
        P = [0] * len(canon)
        for v, c in enumerate(canon):
            P[c] = v
        key = tuple(sorted((min(P[a], P[b]), max(P[a], P[b]))
                           for a, b in H.edges()))
        keys.add(key)
    print(f"  100 relabelings of Petersen -> {len(keys)} canonical key(s)")
    return len(keys) == 1


if __name__ == "__main__":
    r1 = check_atleast_output_exact()
    r2 = check_atmost_output_neg()
    r3 = check_igraph_canonical()
    r4 = iso_table_hint()
    print("ALL OK" if (r1 and r2 and r3 and r4) else "SOME CHECKS FAILED")