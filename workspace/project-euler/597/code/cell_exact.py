#!/usr/bin/env python3
"""Compact exact-cell enumerator for p(n,L) (PE 597): n<=4 oracle.

Speeds normalized: v on the (n-1)-simplex (i.i.d. Exp -> Dirichlet(1..1),
uniform). Race outcome is piecewise-constant in v; separating set is a
hyperplane arrangement (candidate times are const/(linear)), parity constant
per open cell (numerically verified). Cells sliced with exact rational
arithmetic, each cell's exact volume times Dirichlet density (n-1)! summed for
even-parity cells.

Cell counts: n=3 -> 32 (17 even), n=4 -> 1202 (595 even). Values:
  p(2,L)=L/(2L-40): 160->4/7, 400->10/19, 1800->45/89
  p(3,160)=56/135, p(3,400)=542/1377, p(3,1800)=2237/5742
  p(4,400)=521/1020=0.5107843137 (given!),
  p(4,1800)=166802/317985=0.5245593346
"""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "toolkits"))
from fractions import Fraction as F
import math
from arr_enum import enumerate_cells, leaf_interior
from exact_race import outcome_parity_exact


def p_exact(n, L, verbose=False):
    t0 = time.time()
    leaves, planes = enumerate_cells(n, L, verbose=verbose)
    d = n - 1
    even_vol = F(0)
    even_count = 0
    for poly, svec in leaves:
        pt = leaf_interior(poly)
        if pt is None:
            continue
        s = sum(F(x) for x in pt)
        speeds = [F(x) for x in pt] + [F(1) - s]
        par = outcome_parity_exact(n, L, speeds)
        even_count += (par == 0)
        if par == 0:
            even_vol += poly.volume()
    p = math.factorial(d) * even_vol
    return p, even_vol, even_count, len(leaves), time.time() - t0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:]]
    n = int(args[0])
    L = int(args[1])
    p, even_vol, even_count, nleaves, dt = p_exact(n, L)
    print(f"n={n} L={L}")
    print(f"  cells={nleaves}  even_cells={even_count}  ({dt:.1f}s)")
    print(f"  p(n,L) = {p}  = {float(p):.12f}")