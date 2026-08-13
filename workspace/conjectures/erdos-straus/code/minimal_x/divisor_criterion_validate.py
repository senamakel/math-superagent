"""Exact divisor-residue criterion for minimal excess, verified against brute force
on every row (k <= 450, all six open classes, 2705 solutions).

Exact claim.  For n = 4m+1 and candidate x_e = (n + 4e + 3)/4 with d_e = 4e+3,
    a split d_e/(n x_e) = 1/y + 1/z (positive integers y, z) exists
    iff  -n*x_e (mod d_e)  is the residue of some divisor u of (n x_e)^2.

Proof sketch (the two-way equivalence is elementary and complete):
  (u -> split)  If u | (n x)^2 and u = -nx (mod d), let v = (n x)^2/u.
  Then v = -nx (mod d) too (multiply both sides of (nx)^2 = u*v by u^-1).
  min(u,v) <= nx, and y = (nx+u)/d, z = (nx+v)/d are positive integers with
  d/(nx) = 1/y + 1/z and so 4/n = 1/x + 1/y + 1/z.
  (split -> u)  If y, z work, u := d*y - nx divides (nx)^2 with u = -nx (mod d).
So the criterion is exact, not heuristic.  This program checks it on:
  * the minimal excess e of every row (must hold);
  * every e' < e (must fail) — these e' are exactly where the earlier
    subgroup-only test broke down.
"""
import json, time
from sympy import factorint, divisors
from fractions import Fraction

rows = json.load(open('code/out/extended_minimal_x.json'))['rows']

def two_term(n, x):
    d = 4 * x - n
    if d <= 0:
        return None
    nx = n * x
    M = nx * nx
    for u in divisors(M):
        if u > nx:
            continue
        if (nx + u) % d != 0:
            continue
        v = M // u
        if (nx + v) % d != 0:
            continue
        y, z = (nx + u) // d, (nx + v) // d
        if y >= 1 and z >= 1 and Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n):
            return (y, z)
    return None

def divisor_residue_criterion(n, e):
    """Exact criterion: is -n*x_e mod d_e the residue of a divisor of (n x_e)^2?"""
    d = 4 * e + 3
    x = (n + 4 * e + 3) // 4
    if 4 * x - n != d:
        return False
    nx = n * x
    target = (-nx) % d
    # residues of divisors of (nx)^2: exponents 0..2*v_q(nx)
    f = factorint(nx)
    residues = {1}
    for q, vq in f.items():
        r = q % d
        new = set()
        for a in range(0, 2 * vq + 1):
            for s in residues:
                new.add((s * pow(r, a, d)) % d)
        residues = new
    return target in residues

def main():
    t0 = time.time()
    bad_min = []   # criterion says yes at minimal e (must be true)
    bad_less = []  # criterion says yes at e' < e (must be false)
    bad_brute = [] # criterion says yes but brute force says no (or vice versa)
    checked = 0
    for row in rows:
        n, e = row['n'], row['excess']
        x = row['x']
        assert two_term(n, x) is not None, f"brute force disagrees at minimal x: n={n} x={x}"
        if not divisor_residue_criterion(n, e):
            bad_min.append((row['k'], row['r'], n, e))
        for ep in range(e):
            if divisor_residue_criterion(n, ep):
                bad_less.append((row['k'], row['r'], n, e, ep))
            # and the brute-force check at that e'
            works = two_term(n, (n + 4 * ep + 3) // 4) is not None
            if divisor_residue_criterion(n, ep) != works:
                bad_brute.append((row['k'], row['r'], n, e, ep, works))
        checked += 1

    print(f"rows checked: {checked}")
    print(f"criterion holds at minimal e on all rows: {checked - len(bad_min)}/{checked}  violations: {bad_min[:5]}")
    print(f"criterion fails for all e'<e: {checked - len(bad_less)} (violations {len(bad_less)}: {bad_less[:5]})")
    print(f"brute-force agreement everywhere: {checked - len(bad_brute)}/{checked}  violations: {bad_brute[:5]}")
    print(f"done in {time.time()-t0:.1f}s")

if __name__ == '__main__':
    main()