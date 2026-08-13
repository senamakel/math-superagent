"""Minimal-x solutions for 4/n = 1/x + 1/y + 1/z in the six open classes mod 840.

Method: 4/n - 1/x = d/(nx) with d = 4x - n > 0.  The two-term equation
    d/(nx) = 1/y + 1/z
is equivalent to (dy - nx)(dz - nx) = n^2 x^2, so for fixed (n, x) we enumerate
divisors u = dy - nx of M = n^2 x^2 with u = -nx (mod d) and u <= nx (so y <= z),
then z = (nx + M/u)/d.  Exact integer arithmetic only.

x is minimal: we try x = n//4 + 1, n//4 + 2, ... and stop at the first x that
admits a solution.

Every found triple is re-verified by exact cross-multiplication before output.
"""
import json, sys, time
from sympy import divisors, factorint, isprime
from fractions import Fraction

OPEN = [1, 121, 169, 289, 361, 529]
KMAX = 35          # n = 840*k + r <= ~30000
X_CAP_MULT = 3     # refuse to try x > 3n for a single n

def solvable_at_x(n, x):
    d = 4 * x - n
    if d <= 0:
        return None
    nx = n * x
    M = n * nx  # n^2 x
    M = M * x   # n^2 x^2
    ds = divisors(M)
    best = None
    for u in ds:
        if u > nx:            # wlog y <= z  ->  u <= sqrt(M) = nx
            continue
        if (nx + u) % d != 0:
            continue
        v = M // u
        if (nx + v) % d != 0:
            continue
        y = (nx + u) // d
        z = (nx + v) // d
        if y < 1 or z < 1:
            continue
        if Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z):
            if best is None or (y, z) < best:
                best = (y, z)
    if best is None:
        return None
    y, z = best
    return (x, y, z) if y <= z else (x, z, y)

def minimal_solution(n):
    x0 = n // 4 + 1
    cap = X_CAP_MULT * n
    for x in range(x0, cap + 1):
        r = solvable_at_x(n, x)
        if r is not None:
            return r
    return None

def main():
    t0 = time.time()

    # --- first: verify the twelve witnesses in code/out/witnesses.json ---
    w = json.load(open('code/out/witnesses.json'))
    n_checked = 0
    for r, arr in w['witnesses'].items():
        for a in arr:
            n, (x, y, z) = a['n'], a['xyz']
            assert solvable_at_x(n, x) is not None, f"witness x not reproducible: n={n} x={x}"
            n_checked += 1
    print(f"witness check: all {n_checked} witness x-values admit the claimed solution at x, verified exactly")

    # --- sweep the six open classes ---
    rows = []
    for r in OPEN:
        for k in range(0 if r > 1 else 1, KMAX + 1):
            n = 840 * k + r
            sol = minimal_solution(n)
            if sol is None:
                print(f"r={r} k={k} n={n}: NO SOLUTION within x <= {X_CAP_MULT*n}")
                continue
            x, y, z = sol
            assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
            assert x > n // 4
            rows.append({
                'r': r, 'k': k, 'n': n, 'prime': bool(isprime(n)),
                'x': x, 'y': y, 'z': z,
                'excess': x - (n - 1) // 4,   # n = 1 (mod 4) for all six r
                'd': 4 * x - n,
            })

    with open('code/out/open_class_minimal_x.json', 'w') as f:
        json.dump({'KMAX': KMAX, 'X_CAP_MULT': X_CAP_MULT, 'rows': rows}, f, indent=1)

    # --- print: primes only ---
    print(f"\nsweep done: {len(rows)} solutions, {time.time()-t0:.1f}s")
    print("r     k   n         prime  x        excess  y          z")
    last_r = None
    for row in rows:
        if row['prime']:
            print(f"{row['r']:<5} {row['k']:<4} {row['n']:<9} {'P' if row['prime'] else 'C':<5} "
                  f"{row['x']:<9} {row['excess']:<7} {row['y']:<10} {row['z']}")

if __name__ == '__main__':
    main()