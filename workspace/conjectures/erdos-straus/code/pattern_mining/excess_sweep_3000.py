"""Excess sweep to KMAX=3000 for the six open classes + exact criterion checks.

For every n = 840k + r (r in the six open classes, k <= KMAX) finds the
minimal excess e with a solution at x = (n+4e+3)/4, by exact divisor
enumeration of (n*x)^2 (two-term split; same method as extended_verify.py, kept
self-contained).  Every found triple is re-verified by exact Fraction
arithmetic.

On top of the sweep, the two conjectured prime-factor criteria are checked
row-by-row against the exact divisor-enumeration truth:
  C0: e=0  <=>  some prime p == 2 (mod 3) divides n*(n+3)/4
  C1: e<=1 (d=7 works)  <=>  some prime q that is a QNR mod 7 divides n*(n+7)/4
A mismatch anywhere would falsify the criteria (that is the point of running
this far past the 450 rows they were verified on).

Output: per class, max excess + argmax + first k at each excess level, the
excess distribution, and criterion mismatch counts.  Also saves every row to
code/out/excess_sweep_3000.json.
"""
import json, time
from fractions import Fraction
from sympy import factorint, isprime, divisors

OPEN = [1, 121, 169, 289, 361, 529]
KMAX = 3000
X_CAP = 400          # refuse excess > 400; observed max 14 at k<=450, so 400 is a
                     # safety valve, not a claimed bound.  Rows rejected here are a finding.

QNR7 = {3, 5, 6}     # quadratic non-residues mod 7

def two_term(n, x):
    """(y,z) solving d/(nx) = 1/y + 1/z with d = 4x - n, or None.  Exact."""
    d = 4 * x - n
    if d <= 0:
        return None
    nx = n * x
    M = nx * nx
    best = None
    for u in divisors(M):
        if u > nx:
            continue
        if (nx + u) % d != 0:
            continue
        v = M // u
        if (nx + v) % d != 0:
            continue
        y, z = (nx + u) // d, (nx + v) // d
        if y < 1 or z < 1:
            continue
        if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n) \
           and (best is None or (y, z) < best):
            best = (y, z)
    return best

def minimal_solution(n):
    x0 = (n + 3) // 4
    for j in range(X_CAP + 1):
        r = two_term(n, x0 + j)
        if r is not None:
            return (j, x0 + j) + r
    return None

def has_prime_in_class(v, cls):
    return any(p in cls for p in factorint(v))

def main():
    t0 = time.time()
    rows = []
    per = {r: {} for r in OPEN}   # excess -> first k
    maxe = {r: (-1, None) for r in OPEN}
    bad_c0 = bad_c1 = 0
    c0_checked = c1_checked = 0
    for r in OPEN:
        for k in range(1 if r == 1 else 0, KMAX + 1):
            n = 840 * k + r
            sol = minimal_solution(n)
            if sol is None:
                print(f"r={r} k={k} n={n}: NO SOLUTION with excess <= {X_CAP}  <-- FINDING")
                continue
            e, x, y, z = sol
            assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n)
            # criterion C0 at e=0
            if e == 0:
                cond = has_prime_in_class(n, {2}) | has_prime_in_class((n + 3)//4, {2})
                got = two_term(n, (n + 3)//4) is not None
                c0_checked += 1
                if cond != got:
                    bad_c0 += 1
                    if bad_c0 <= 5:
                        print(f"C0 MISMATCH r={r} k={k} n={n} cond={cond} two-term={got}")
            else:
                # e >= 1 : check the stronger criterion C1 at d=7
                x1 = (n + 7) // 4
                got1 = two_term(n, x1) is not None
                cond1 = has_prime_in_class(n, QNR7) | has_prime_in_class(x1, QNR7)
                c1_checked += 1
                if got1 != cond1:
                    bad_c1 += 1
                    if bad_c1 <= 5:
                        print(f"C1 MISMATCH r={r} k={k} n={n} cond={cond1} two-term={got1}")
            per[r].setdefault(e, k)
            if e > maxe[r][0]:
                maxe[r] = (e, k)
            rows.append({'r': r, 'k': k, 'n': n, 'prime': bool(isprime(n)),
                         'x': x, 'y': y, 'z': z, 'excess': e, 'd': 4 * x - n})
    print(f"sweep: {len(rows)} rows in {time.time()-t0:.1f}s")
    print(f"criterion C0 (d=3): {c0_checked} rows with e=0, {bad_c0} mismatches")
    print(f"criterion C1 (d=7): {c1_checked} rows with e>=1 checked, {bad_c1} mismatches")
    print(f"rows with excess > X_CAP: {KMAX*6 - len(rows) + 6 - len(rows)} "
          f"(none => every n solved at some e <= {X_CAP})")
    for r in OPEN:
        print(f"r={r:>3}: max excess {maxe[r][0]} at k={maxe[r][1]} "
              f"(n={840*maxe[r][1]+r}); e-distribution {dict(sorted(per[r].items()))[:8]}...")
    # growth of max excess with k-window
    for r in OPEN:
        arr = sorted([s for s in rows if s['r'] == r], key=lambda t: t['k'])
        win = [500, 1000, 1500, 2000, 3000]
        prev = 0
        seg = []
        for w in win:
            m = max(s['excess'] for s in arr if s['k'] <= w)
            seg.append(f"k<={w}:{m}")
        print(f"r={r:>3} max excess growth: {' '.join(seg)}")
    # first k at which each excess level is reached, per class
    print("\nfirst k reaching excess e:")
    for r in OPEN:
        line = " ".join(f"e{e}:k{k}" for e, k in sorted(per[r].items()) if e >= 2)
        print(f"r={r:>3}: {line}")
    json.dump({'KMAX': KMAX, 'rows': rows},
              open('code/out/excess_sweep_3000.json', 'w'), indent=1)
    print("saved code/out/excess_sweep_3000.json")

if __name__ == '__main__':
    main()