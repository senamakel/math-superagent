#!/usr/bin/env python3
"""Extra validation for the SAT calibration: compare the NUMBER of proper
k-colourings obtained two independent ways:
  (1) brute-force enumeration of all colourings (pure Python, the oracle),
  (2) SAT-based enumeration via Cadical153 blocking-clause search (real solver).
Both count how many proper k-colourings the 7-vertex Moser spindle has. These
must agree exactly for every k. This is a stronger check than SAT/UNSAT alone.
Edge list is the same integer edge list, exact; no floats anywhere.
"""
import sys
from itertools import product

from pysat.formula import CNF
from pysat.solvers import Cadical153

from sat_calibration import EDGES, NVERT, encode_kcol


def brute_count(edges, k, n):
    """Exhaustive: try every assignment, require proper. Oracle route."""
    count = 0
    witnesses = []
    for assign in product(range(k), repeat=n):
        ok = all(assign[i] != assign[j] for (i, j) in edges)
        if ok:
            count += 1
            if len(witnesses) < 3:
                witnesses.append(list(assign))
    return count, witnesses


def sat_count(edges, k, n, limit_models=200000):
    """SAT route: find one model at a time, block it, repeat. Real solver."""
    cnf0, lit = encode_kcol(edges, k, n)
    seen = set()
    clauses = list(cnf0.clauses)
    count = 0
    with Cadical153(bootstrap_with=clauses) as s:
        while True:
            sat = s.solve()
            if not sat:
                break
            model = s.get_model()
            witness = [None] * n
            for i in range(n):
                for c in range(k):
                    if model[lit(i, c) - 1] > 0:
                        witness[i] = c
            key = tuple(witness)
            if key in seen:
                raise AssertionError("blocking clause failed to block model")
            seen.add(key)
            count += 1
            # block this exact colouring
            s.add_clause([-lit(i, witness[i]) for i in range(n)])
            if count >= limit_models:
                break
    return count


def main():
    edges, n = EDGES, NVERT
    print("graph: n=%d, edges=%d, edge list=%s" % (n, len(edges), edges))
    for k in range(1, 6):
        bc, _ = brute_count(edges, k, n)
        sc = sat_count(edges, k, n)
        agree = (bc == sc)
        print("k=%d  brute_count=%d  sat_count=%d  agree=%s"
              % (k, bc, sc, agree))
        if not agree:
            print("MISMATCH in proper k-colouring counts")
            sys.exit(1)
    print("count cross-check: all k agree exactly; no floats used.")


if __name__ == "__main__":
    main()
