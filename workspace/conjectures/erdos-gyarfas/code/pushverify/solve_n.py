"""Driver: lazy-SAT search for a C4,C8,C16-free graph on n vertices.

For a given n, runs the CDCL-style loop:
  1. build base CNF (degree>=3, no C4)
  2. solve; if UNSAT -> report UNSAT (a theorem)
  3. if SAT, extract graph, run the cycle oracle independently, report its
     full cycle set; if it contains no 4,8,16 -> SAT (found a counterexample!)
  4. else block every distinct C8 and C16 it contains, re-solve.

Usage:  python solve_n.py 16
Writes status + any model's graph6 to code/out/pushverify/.
"""
import sys
import time
from pysat.solvers import Cadical153

from encode import build_base, model_to_graph, find_cycles_to_block, blocking_clause, edge_id
from lib.cycle_oracle import oracle
import networkx as nx


def decode_model_edges(model, n):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for lit in model:
        if lit > 0:
            eid = lit
            for i in range(n):
                lo = (i * (2 * n - i - 1)) // 2 + 1
                hi = (i * (2 * n - i - 1)) // 2 + (n - 1 - i) + 1
                if lo <= eid <= hi:
                    j = i + (eid - lo) + 1
                    G.add_edge(i, j)
                    break
    return G


def solve_n(n, timeout_per_solve=600, max_iter=100000):
    base, top = build_base(n)
    added = []  # list of extra clauses (blocking)
    t_total = time.monotonic()
    iter_count = 0
    last_status = None
    while True:
        iter_count += 1
        if iter_count > max_iter:
            last_status = "ITER_LIMIT"
            break
        cnf = base.copy()
        for cl in added:
            cnf.append(cl)
        solver = Cadical153(bootstrap_with=cnf.clauses)
        t0 = time.monotonic()
        sat = solver.solve()
        dt = time.monotonic() - t0
        if not sat:
            last_status = "UNSAT"
            print(f"n={n} iter={iter_count} UNSAT  (this solve {dt:.1f}s, "
                  f"total {time.monotonic()-t_total:.1f}s, blocked={len(added)})")
            solver.delete()
            return {"status": "UNSAT"}
        model = solver.get_model()
        solver.delete()
        G = decode_model_edges(model, n)
        md, lens = oracle(G)   # independent check: full exact cycle set
        lens4 = {L for L in lens if L in (4, 8, 16)}
        # report every cycle length <= 31 present
        pow2 = {L for L in lens if L & (L - 1) == 0 and L >= 4}
        if not pow2:
            # no power-of-two cycle at all -> this is a counterexample
            g6 = nx.to_graph6_bytes(G, header=False).decode()
            print(f"n={n} iter={iter_count} ** SAT (counterexample) ** "
                  f"min_deg={md} cycle_set={lens} graph6={g6}")
            with open(f"code/out/pushverify/model_n{n}.g6", "w") as f:
                f.write(g6 + "\n")
                f.write(f"# min_degree={md} cycle_set={sorted(lens)}\n")
            return {"status": "SAT", "graph": G, "lens": lens}
        # found C8/C16 (and/or C4 — C4 shouldn't appear but be safe): block them
        cycles = find_cycles_to_block(G, n)
        # include C4 cycles too as a safety net (should be none)
        from itertools import combinations
        allblocks = set()
        for c in nx.simple_cycles(G.to_directed()):
            if len(c) >= 3:
                L = len(c)
                if L in (4, 8, 16):
                    allblocks.add(tuple(c))
        nblk = 0
        for c in allblocks:
            clause = blocking_clause(list(c), n)
            # avoid duplicate clauses
            if tuple(sorted(clause)) not in {tuple(sorted(t)) for t in added}:
                added.append(clause)
                nblk += 1
        print(f"n={n} iter={iter_count} model min_deg={md} "
              f"cycles={sorted(lens)} blocked_cycles={len(allblocks)} "
              f"new_clauses={nblk} pow2_present={sorted(pow2)}")

    return {"status": last_status}


if __name__ == "__main__":
    import os
    os.makedirs("code/out/pushverify", exist_ok=True)
    n = int(sys.argv[1])
    res = solve_n(n)
    print("RESULT:", res)
