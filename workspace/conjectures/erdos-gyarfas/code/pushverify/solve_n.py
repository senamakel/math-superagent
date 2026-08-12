"""Driver: lazy-SAT search for a C4,C8,C16-free graph on n vertices.

CDCL-style loop over a growing CNF:
  1. build base CNF (degree>=3, no C4)
  2. solve with Cadical153
  3. UNSAT -> report UNSAT (a theorem: no such graph on n vertices)
  4. SAT  -> decode graph, run the independent cycle oracle (full exact cycle
     set); if it has no power-of-two cycle at all, that is a counterexample to
     Erdős–Gyárfás: report model + graph6 (the run has found something huge).
     Otherwise block every distinct C4/C8/C16 it contains and re-solve.
  5. iteration bound as a safety valve; each Cadical call fresh (clause
     learning across calls is preserved by the accumulated blocking clauses).

Usage:  python solve_n.py N [timeout_per_solve_seconds]
Writes status and any model's graph6 to code/out/pushverify/.
"""
import sys
import time
from itertools import combinations

from pysat.solvers import Cadical153

from encode import (build_base, find_bad_cycles, blocking_clause,
                    arg_edge_id, edge_id)
from lib.cycle_oracle import oracle
import networkx as nx


def decode_model(model, n):
    """Graph from a Cadical model (list of ints, positive = true)."""
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for lit in model:
        if lit > 0 and lit <= n * (n - 1) // 2:
            G.add_edge(*arg_edge_id(lit, n))
    return G


def solve_n(n, timeout_per_solve=900, max_iter=200000, outdir="/workspace/code/out/pushverify"):
    import os
    os.makedirs(outdir, exist_ok=True)
    base, _top = build_base(n)
    added = []            # accumulated blocking clauses (learned literals)
    added_keys = set()    # dedupe
    t_total = time.monotonic()
    it = 0
    log = open(f"{outdir}/log_n{n}.txt", "a")
    log.write(f"=== n={n} start {time.asctime()} base_clauses={len(base.clauses)}\n")
    log.flush()
    while True:
        it += 1
        if it > max_iter:
            log.write(f"ITER_LIMIT after {it} iterations\n")
            log.close()
            return {"status": "ITER_LIMIT", "iterations": it}
        cnf = base.copy()
        for cl in added:
            cnf.append(cl)
        s = Cadical153(bootstrap_with=cnf.clauses)
        t0 = time.monotonic()
        sat = s.solve()
        dt = time.monotonic() - t0
        if not sat:
            msg = (f"n={n} iter={it} UNSAT  solve={dt:.1f}s "
                   f"total={time.monotonic()-t_total:.1f}s blocked={len(added)}")
            print(msg)
            log.write(msg + "\n")
            log.write(f"=== n={n} UNSAT {time.asctime()}\n")
            log.close()
            s.delete()
            return {"status": "UNSAT", "iterations": it}
        model = s.get_model()
        s.delete()
        G = decode_model(model, n)
        md, lens = oracle(G)              # independent full cycle-length check
        pow2 = {L for L in lens if L >= 4 and L & (L - 1) == 0}
        if not pow2:                      # no power-of-two cycle at all
            g6 = nx.to_graph6_bytes(G, header=False).decode()
            msg = (f"n={n} iter={it} ** SAT: COUNTEREXAMPLE ** min_deg={md} "
                   f"cycle_set={sorted(lens)} graph6={g6}")
            print(msg)
            log.write(msg + "\n")
            with open(f"{outdir}/model_n{n}.g6", "w") as f:
                f.write(g6 + "\n")
                f.write(f"# n={n} min_degree={md} cycle_set={sorted(lens)}\n")
            log.close()
            return {"status": "SAT-COUNTEREXAMPLE", "iterations": it,
                    "graph": G, "lens": lens}
        bad = find_bad_cycles(G, n)       # C4/C8/C16 cycles of the model
        c4 = len([c for c in bad if len(c) == 4])
        nblk = 0
        for cyc in bad:
            cl = tuple(blocking_clause(cyc, n))
            if cl not in added_keys:
                added_keys.add(cl)
                added.append(list(cl))
                nblk += 1
        msg = (f"n={n} iter={it} model md={md} cycle_set={sorted(lens)} "
               f"pow2={sorted(pow2)} bad_cycles={len(bad)} (C4={c4}) "
               f"new_clauses={nblk} cumulative={len(added)} solve={dt:.1f}s "
               f"total={time.monotonic()-t_total:.1f}s")
        print(msg)
        log.write(msg + "\n")
        log.flush()


if __name__ == "__main__":
    n = int(sys.argv[1])
    tps = float(sys.argv[2]) if len(sys.argv) > 2 else 900
    res = solve_n(n, timeout_per_solve=tps)
    print("RESULT:", res)