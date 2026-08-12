"""Lazy-SAT driver for the (2,2)-shaped cut-vertex Erdős–Gyárfás push.

Loop (CDCL-style, fresh Cadical153 per solve, clause learning across calls
preserved by accumulating the blocking clauses in the base CNF):
  1. build base CNF: partition + deg(v)=4 + exactly-2-in-A/B + deg>=3 others
     + no C4  (encode_shape.build_base_shape)
  2. solve
  3. UNSAT  -> theorem: no (2,2)-shaped graph on n avoids 4, 8, 16.
  4. SAT    -> decode graph, run the independent full cycle oracle
     (lib.cycle_oracle.all_simple_cycles).  If it has NO power-of-two cycle at
     all, that is a counterexample to Erdős–Gyárfás: report model + full cycle
     set + verify the shape independently.  Otherwise block every distinct
     C4/C8/C16 it contains (only C8/C16 matter here — C4 is already in base but
     blocking is harmless) and re-solve.
  5. iteration cap ~2000 as a safety valve.

A model is only believed after an *independent* oracle check (cycle set) and an
*independent* shape check (partition, deg(v)=4, exactly-2-in-A/B, no A-B edges,
min deg).  'not-converged' (iteration cap) is not a result.

Usage:  python shape_sat.py N [maxiter] [timeout_per_solve]
Logs to /workspace/code/out/cutvertex/shape_sat/.
"""
import sys, os, time
import networkx as nx

from pysat.solvers import Cadical153
from pysat.formula import CNF

from pushverify.encode import arg_edge_id
from cutvertex.encode_shape import build_base_shape
from lib.cycle_oracle import oracle, all_simple_cycles


OUT = "/workspace/code/out/cutvertex/shape_sat"


def _eid(i, j, n):
    from pushverify.encode import edge_id
    return edge_id(i, j, n)


def canon(cycle):
    k = len(cycle)
    m = min(cycle)
    i = cycle.index(m)
    rot = tuple(cycle[i:] + cycle[:i])
    rev = tuple([rot[0]] + list(reversed(rot[1:])))
    return min(rot, rev)


def decode_model(model, n, atoms):
    """Graph + shape from a Cadical model."""
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for lit in model:
        if lit > 0 and lit <= n * (n - 1) // 2:
            G.add_edge(*arg_edge_id(lit, n))
    v = atoms['v']
    inA = {i: (atoms['inA'][i] in model) for i in atoms['inA']}
    return G, inA


def check_shape_independent(G, n, v, inA):
    """Independent re-verification of the shape from the decoded graph."""
    A = [i for i in range(n) if i != v and inA[i]]
    B = [i for i in range(n) if i != v and not inA[i]]
    assert len(A) + len(B) + 1 == n
    # no edges between A and B
    for i in A:
        for j in B:
            if G.has_edge(i, j):
                return False, "edge between A and B"
    # deg(v) exactly 4, exactly 2 neighbours in A, 2 in B
    vs = [w for w in G[v]]
    if len(vs) != 4:
        return False, "deg(v)!=4"
    na = sum(1 for w in vs if inA[w])
    nb = sum(1 for w in vs if not inA[w])
    if na != 2 or nb != 2:
        return False, f"v-neighbours split {na}/{nb}"
    # every other vertex deg>=3
    for u in range(n):
        if u != v and G.degree[u] < 3:
            return False, f"deg({u})<3"
    return True, "ok"


def solve_n(n, max_iter=2000, timeout=600):
    os.makedirs(OUT, exist_ok=True)
    log = open(f"{OUT}/shape_n{n}.log", "a")
    log.write(f"=== n={n} start {time.asctime()}\n")
    t_total = time.monotonic()
    base, top, atoms = build_base_shape(n)
    nbase = len(base.clauses)
    log.write(f"base: n={n} vars~{top} clauses={nbase}\n")
    print(f"n={n} base clauses={nbase}")
    added = []
    added_keys = set()
    it = 0
    while True:
        it += 1
        if it > max_iter:
            msg = f"n={n} iter={it} NOT-CONVERGED (cap {max_iter})"
            print(msg); log.write(msg + "\n"); log.flush(); log.close()
            return {"status": "NOT-CONVERGED", "iterations": it}
        cnf = base.copy()
        for cl in added:
            cnf.append(cl)
        s = Cadical153(bootstrap_with=cnf.clauses)
        t0 = time.monotonic()
        if timeout > 0:
            sat = s.solve_limited(expect_interrupt=False)
            # solve_limited returns None in manual mode only with interrupt handling;
            # use a wall-clock guard below instead.
        else:
            sat = s.solve()
        dt = time.monotonic() - t0
        if timeout > 0 and (sat is None or dt > timeout):
            # wall-clock guard: treat as not solved this iteration
            msg = (f"n={n} iter={it} solve-timeout ({dt:.1f}s>{timeout}s) "
                   f"-> NOT-CONVERGED")
            print(msg); log.write(msg + "\n"); log.flush(); log.close()
            s.delete()
            return {"status": "NOT-CONVERGED", "iterations": it}
        if not sat:
            msg = (f"n={n} iter={it} UNSAT  solve={dt:.1f}s "
                   f"total={time.monotonic()-t_total:.1f}s blocked={len(added)} "
                   f"total_clauses={len(cnf.clauses)}")
            print(msg); log.write(msg + "\n")
            log.write(f"=== n={n} UNSAT {time.asctime()}\n")
            log.close(); s.delete()
            return {"status": "UNSAT", "iterations": it}
        model = s.get_model()
        s.delete()
        G, inA = decode_model(model, n, atoms)
        # independent shape check
        ok, why = check_shape_independent(G, n, atoms['v'], inA)
        # independent full cycle oracle
        md, lens = oracle(G)
        pow2 = {L for L in lens if L >= 4 and L & (L - 1) == 0}
        if not pow2:
            g6 = nx.to_graph6_bytes(G, header=False).decode()
            an = sorted([i for i in inA if inA[i]])
            bn = sorted([i for i in inA if not inA[i]])
            msg = (f"n={n} iter={it} ** SAT: COUNTEREXAMPLE ** min_deg={md} "
                   f"cycle_set={sorted(lens)} shapeshape={ok} A={an} B={bn} "
                   f"graph6={g6}")
            print(msg); log.write(msg + "\n")
            with open(f"{OUT}/counterexample_n{n}.g6", "w") as f:
                f.write(g6 + "\n")
                f.write(f"# n={n} min_deg={md} cycle_set={sorted(lens)}\n")
                f.write(f"# A={an} B={bn} v={atoms['v']} shape_ok={ok}\n")
            log.close()
            return {"status": "SAT-COUNTEREXAMPLE", "iterations": it,
                    "graph": G, "lens": lens}
        # gather all distinct C4/C8/C16 cycles and block them
        cycles = set()
        for c in all_simple_cycles(G):
            if len(c) in (4, 8, 16):
                cycles.add(canon(c))
        nblk = 0
        for cyc in cycles:
            lits = set()
            k = len(cyc)
            for t in range(k):
                i, j = cyc[t], cyc[(t + 1) % k]
                lits.add(_eid(i, j, n))
            cl = tuple(sorted(-x for x in lits))
            if cl not in added_keys:
                added_keys.add(cl)
                added.append(list(cl))
                nblk += 1
        msg = (f"n={n} iter={it} model md={md} cycle_set={sorted(lens)} "
               f"pow2={sorted(pow2)} new_block={nblk} cumulative={len(added)} "
               f"shape_ok={ok} solve={dt:.1f}s "
               f"total={time.monotonic()-t_total:.1f}s")
        print(msg); log.write(msg + "\n"); log.flush()


if __name__ == "__main__":
    n = int(sys.argv[1])
    mi = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
    tp = float(sys.argv[3]) if len(sys.argv) > 3 else 600
    solve_n(n, max_iter=mi, timeout=tp)
