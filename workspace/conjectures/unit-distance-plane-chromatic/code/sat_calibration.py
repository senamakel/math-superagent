#!/usr/bin/env python3
"""Independent complete k-colourability test via CNF + a real SAT solver.

This is the SECOND, independent route to the Moser spindle calibration that
brute.py (the tool_builder's oracle) already established. brute.py brute-forces
colouring with Python loops; this program encodes k-colourability as a CNF
formula and hands the search to real SAT solvers (Cadical153 and Minisat22 via
PySAT). The two routes share no search logic whatsoever.

The graph data (the 7-vertex Moser spindle edge list) is read from the capture
file brute.py produced (code/out/commands.log); it is treated as INPUT data,
not recomputed here. A from-scratch exact reconstruction of the standard Moser
spindle is also included to confirm the edge list independently (in the
`--reconstruct` mode).

Encoding of k-colourability:
  * Variables: x[i][c] = "vertex i has colour c",  for i in 0..n-1, c in 0..k-1.
    Mapped to DIMACS literals lit(i, c) = i*k + c + 1  (1-indexed).
  * Each vertex gets exactly one colour:
      - at least one:  ( x[i][0] | x[i][1] | ... | x[i][k-1] )
      - at most one:   for every pair c<d, ( ~x[i][c] | ~x[i][d] )
  * Proper colouring (per edge): for each edge (i,j) and each colour c,
      ( ~x[i][c] | ~x[j][c] )  -- i and j cannot share colour c.

No floating point anywhere: the graph is an integer edge list; CNF is integer
literals; the witness check is pure integer logic.
"""
import sys
import argparse

from pysat.formula import CNF
from pysat.solvers import Cadical153, Minisat22


# ---------------------------------------------------------------------------
# The graph data. EDGES is the integer edge list of the 7-vertex Moser
# spindle, taken from the tool_builder oracle capture (code/out/commands.log).
# Reconstructed independently in build_moser_edges() and compared.
# ---------------------------------------------------------------------------
EDGES = [(0, 1), (0, 2), (0, 4), (0, 5), (1, 2), (1, 3),
         (2, 3), (3, 6), (4, 5), (4, 6), (5, 6)]
NVERT = 7


def build_moser_edges():
    """Reconstruct the standard Moser spindle edge list from first principles,
    in exact arithmetic (Q(sqrt(3), sqrt(11))), independently of brute.py.

    The Moser spindle is two rhombi (each unit edge, each made of two
    equilateral triangles) sharing one apex vertex, rotated so the two far
    tips are at distance 1 (that unit segment is the spindle's chord).
    Vertices:
      A = far tip of rhombus 1
      u, v = the two unit vectors from A (u along x-axis)
      B = u + v  (near the far end of rhombus 1, other apex)
      A', u', v', B' = rhombus 2 = rhombus 1 rotated by theta, with chord
      |A - A'| = 1.  sin(theta/2) = 1/(2 sqrt(3)) so cos(theta)=5/6,
      sin(theta)=sqrt(11)/6.
    Edges: all unit-distance pairs.
    """
    from sympy import sqrt, S, simplify
    sqrt3 = sqrt(S(3))
    sqrt11 = sqrt(S(11))

    def rot(x, y, ct, st):
        return (x * ct - y * st, x * st + y * ct)

    A = (S(0), S(0))
    u = (S(1), S(0))
    v = (S(1) / 2, sqrt3 / 2)
    B = (u[0] + v[0], u[1] + v[1])          # u + v
    ct, st = S(5) / 6, sqrt11 / 6
    Ru = rot(u[0], u[1], ct, st)
    Rv = rot(v[0], v[1], ct, st)
    A2 = rot(A[0], A[1], ct, st)            # == A, since A is the origin
    B2 = rot(B[0], B[1], ct, st)            # u' + v'
    pts = [A, u, v, B, Ru, Rv, B2]

    edges = []
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            dx = pts[i][0] - pts[j][0]
            dy = pts[i][1] - pts[j][1]
            if simplify(dx * dx + dy * dy) == S(1):   # exact symbolic equality
                edges.append((i, j))
    return edges


def encode_kcol(edges, k, n):
    """Build the CNF for k-colourability of the graph (n vertices, edges).
    Returns (CNF object, lit function)."""
    cnf = CNF()

    def lit(i, c):
        return i * k + c + 1

    # exactly one colour per vertex
    for i in range(n):
        cnf.append([lit(i, c) for c in range(k)])          # at least one
        for c in range(k):
            for d in range(c + 1, k):
                cnf.append([-lit(i, c), -lit(i, d)])       # at most one
    # proper colouring
    for (i, j) in edges:
        for c in range(k):
            cnf.append([-lit(i, c), -lit(j, c)])
    return cnf, lit


def solve_k(edges, k, n, solver_cls):
    """Solve k-colourability. Returns (sat_bool, witness_or_None)."""
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


def verify_witness(edges, witness, n, k):
    """Independent pure-integer check that `witness` is a proper k-colouring.
    Knows nothing about the SAT encoding."""
    assert len(witness) == n
    for c in witness:
        assert 0 <= c < k, "colour out of range"
    for (i, j) in edges:
        if witness[i] == witness[j]:
            raise AssertionError(
                "edge (%d,%d) has equal colours %r" % (i, j, witness[i]))
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reconstruct", action="store_true",
                    help="recheck the edge list by exact reconstruction")
    args = ap.parse_args()

    edges = EDGES
    n = NVERT

    # independent reconstruction cross-check of the edge list itself
    if args.reconstruct:
        rec = build_moser_edges()
        print("reconstructed Moser edge list:", rec)
        print("matches input edge list:", sorted(rec) == sorted(edges))
        if sorted(rec) != sorted(edges):
            print("MISMATCH between input and reconstruction; using reconstructed")
            edges = sorted(rec)

    print("graph: n=%d, edges=%d" % (n, len(edges)))
    print("edge list:", edges)

    for solver_cls in (Cadical153, Minisat22):
        name = solver_cls.__name__
        for k in (3, 4):
            sat, witness = solve_k(edges, k, n, solver_cls)
            if sat:
                ok = verify_witness(edges, witness, n, k)
                print("[%s] k=%d: SAT (k-colourable) witness=%s "
                      "proper-check=%s" % (name, k, witness, ok))
            else:
                print("[%s] k=%d: UNSAT (not k-colourable)" % (name, k))

    print("No floating point used anywhere: graph is integer edges; CNF literals"
          " are integers; witness check is integer logic.")


if __name__ == "__main__":
    main()
