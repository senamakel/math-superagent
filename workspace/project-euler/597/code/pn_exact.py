#!/usr/bin/env python3
"""Exact p(n,L) for small n by enumerating the arrangement of outcome-
separating lines in the speed simplex, then measuring each cell's exact area
and the race outcome at its representative point.

Speeds v_j ~ Exp(1) iid. Race outcome is invariant to common scaling, so
normalize: (v0,v1,...) uniform on the unit simplex (Dirichlet(1,..,1)).
In (v0,v1) coords (v2=1-v0-v1 for n=3) the simplex is the triangle
{v0>=0,v1>=0,v0+v1<=1}; density = 2 (area of triangle = 1/2), so
p(n,L) = 2 * (sum of plain areas of even-parity cells).

Candidate event times (chronological building blocks):
  F_j  = (L - 40 j)/v_j                finish of boat j
  C_ab = 40 (a-b)/(v_a - v_b)          catch time: boat a catches b (a<b)
A cell is a region of the simplex where the mutual order of all candidate
event times (and sign of every v_a-v_b) is constant -> race outcome constant.
Separating lines: v_a=v_b and equality of any two candidate times (all linear
after cross-multiplying).

We subdivide the simplex triangle by these lines, get exact polygon faces,
evaluate the race at an interior rational point of each face (exact_race.py),
and sum face areas weighted by parity.
"""
import sys, os, itertools, math
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_race import outcome_parity_exact   # exact rational race oracle


def candidates(n, L):
    """Return list of candidate event-time descriptors (name, type, j, k)."""
    evs = []
    for j in range(n):
        evs.append((f'F{j}', 'F', j, None))
    for a in range(n):
        for b in range(a + 1, n):
            evs.append((f'C{a}{b}', 'C', a, b))
    return evs


def time_expr(ev, L, v):
    """Symbolic rational expression for a candidate event time in vars v[].
    Returns a Fractions-built function; evaluated at a point."""
    name, typ, j, k = ev
    if typ == 'F':
        # (L - 40j)/v_j
        return (L - 40 * j) / v[j]
    else:
        # 40*(k-j)/(v_j - v_k)
        return F(40) * (k - j) / (v[j] - v[k])


def eval_time(ev, L, fracs):
    name, typ, j, k = ev
    if typ == 'F':
        return F(L - 40 * j) / fracs[j]
    else:
        return F(40) * (k - j) / (fracs[j] - fracs[k])


def separating_lines(n, L):
    """Return list of linear equations on (v0,...,v_{n-1}) as (coeffs, c)
    meaning sum coeff[i] v_i + c = 0, given in coordinates on a hyperplane.
    We work with the n-1 free coordinates v0..v_{n-2} (v_{n-1} = 1 - sum).
    Return lines as dict index->coeff over free vars and const term, sign
    function evaluating the LHS at a point (with substitution)."""
    evs = candidates(n, L)
    lines = []
    # catch-existence: v_a - v_b = 0
    for a in range(n):
        for b in range(a + 1, n):
            lines.append(('vex', a, b))
    # equality of any two candidate times: T_1 = T_2  =>  linear equation
    for (e1, e2) in itertools.combinations(evs, 2):
        lines.append(('eq', e1, e2))
    return lines, evs


def lhs_value(line, L, fracs):
    """Value of the linear form (positive/negative/zero) at point fracs."""
    kind = line[0]
    if kind == 'vex':
        _, a, b = line
        return fracs[a] - fracs[b]
    else:
        _, e1, e2 = line
        return eval_time(e1, L, fracs) - eval_time(e2, L, fracs)


def main():
    n_ = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    bits = sys.argv[2:] if len(sys.argv) > 2 else ['160']
    for L in bits:
        L = int(L)
        # Build the constrained set of candidate times actually realisable is
        # complex; use Monte Carlo verification instead for now.
        print(f"n={n_} L={L}: arrangement enumeration deferred (see code/run_p3_exact.py)")


if __name__ == '__main__':
    main()
