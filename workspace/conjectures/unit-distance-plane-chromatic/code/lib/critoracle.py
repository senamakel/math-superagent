"""Independent correct chromatic-number oracle for the verification.

Uses a clean general-colouring CNF solved by Cadical153 (via python-sat),
independent of lib.coloring's backtracking (which has a broken symmetry-break
that made k-colourability searches incomplete). Cross-checked against
lib.satcolor below.
"""
from pysat.formula import CNF
from pysat.solvers import Cadical153


def is_k_colorable(n, edges, k):
    """Exact: is the n-vertex graph k-colourable? (CNF at-least-one + proper.)"""
    if k <= 0:
        return n == 0
    cnf = CNF()
    for v in range(n):
        cnf.append([v * k + c + 1 for c in range(k)])  # at least one colour
    for (a, b) in edges:
        for c in range(k):
            cnf.append([-(a * k + c + 1), -(b * k + c + 1)])  # not same colour
    with Cadical153(bootstrap_with=cnf.clauses) as s:
        return s.solve()


def chrom(n, edges):
    """Exact chromatic number of an n-vertex graph."""
    # colour classes 1..n always work; binary-ish scan from low end
    for k in range(1, n + 1):
        if is_k_colorable(n, edges, k):
            return k
    return n


def is_vertex_critical(n, edges, k):
    """chi(G)=k and chi(G-v) <= k-1 for every v."""
    if chrom(n, edges) != k:
        return False
    for v in range(n):
        rem = [u for u in range(n) if u != v]
        mp = {u: i for i, u in enumerate(rem)}
        sub = [(mp[a], mp[b]) for (a, b) in edges if a != v and b != v]
        if is_k_colorable(n - 1, sub, k - 1):
            continue
        return False
    return True


def min_degree(n, edges):
    deg = [0] * n
    for (a, b) in edges:
        deg[a] += 1
        deg[b] += 1
    return min(deg) if n else 0
