#!/usr/bin/env python3
"""
Complete k-colourability via CNF + real SAT solvers (PySAT Cadical153).

encode_kcol(edges, k, n) -> (CNF, lit):  x[i][c] = "vertex i has colour c".
  * exactly one colour per vertex,
  * for each edge (i,j) and each colour c, not both i and j have c.

is_k_colorable(edges, k, n) -> (bool, witness): complete; witness is a proper
  k-colouring when SAT, None when UNSAT.  verify_witness() re-checks the
  witness in pure integer logic, independently of the encoding.

Calibrated on the 7-vertex Moser spindle: k=3 UNSAT, k=4 SAT with a
proper-checked witness (matches code/sat_calibration.py and code/brute.py).
"""
from pysat.formula import CNF
from pysat.solvers import Cadical153


def encode_kcol(edges, k, n):
    cnf = CNF()

    def lit(i, c):
        return i * k + c + 1

    for i in range(n):
        cnf.append([lit(i, c) for c in range(k)])
        for c in range(k):
            for d in range(c + 1, k):
                cnf.append([-lit(i, c), -lit(i, d)])
    for (i, j) in edges:
        for c in range(k):
            cnf.append([-lit(i, c), -lit(j, c)])
    return cnf, lit


def is_k_colorable(edges, k, n, solver_cls=Cadical153):
    """Complete k-colourability. Returns (sat_bool, witness_or_None)."""
    cnf, lit = encode_kcol(edges, k, n)
    with solver_cls(bootstrap_with=cnf.clauses) as s:
        sat = s.solve()
        witness = None
        if sat:
            model = s.get_model()
            witness = [None] * n
            for i in range(n):
                for c in range(k):
                    if model[lit(i, c) - 1] > 0:
                        witness[i] = c
                        break
        return sat, witness


def verify_witness(edges, witness, k):
    """Independent pure-integer check that witness is a proper k-colouring."""
    for c in witness:
        assert 0 <= c < k, "colour out of range"
    for (i, j) in edges:
        if witness[i] == witness[j]:
            raise AssertionError(
                "edge (%d,%d) has equal colours %r" % (i, j, witness[i]))
    return True
