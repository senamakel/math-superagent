"""Extended minimal-x sweep for the six open classes + exact verification of structural criteria.

Criterion 1 (d = 3, excess e = 0): x = (n+3)/4 admits a 2-term split iff
    (nx)^2 has a divisor u with u == -nx (mod 3), u <= nx.
Since n = x = 1 (mod 3) here, -nx == 2 (mod 3), and a divisor of a square in a
given residue class mod 3 exists iff some prime p == 2 (mod 3) divides n or x.
Claim:  e = 0  <=>  exists prime p == 2 (mod 3) with p | n or p | (n+3)/4.

Criterion 2 (d = 7, excess e = 1): x = (n+7)/4, need u == -nx (mod 7).
n = 840k + r = r (mod 7) in {1,2,4}, x == 3n (mod 7) (4^-1 = 2... recomputed),
so -nx is a quadratic non-residue mod 7.  Claim: e = 1 (d = 7 works) iff
n*(n+7)/4 has a prime factor that is a quadratic non-residue mod 7.
(Exact criterion: the subgroup <p mod 7 : p | n*x> must contain -nx mod 7,
which for prime 7 means: some p | n*x is a QNR mod 7.)

Both criteria are checked EXACTLY row by row below (brute divisor enumeration
is ground truth; the subgroup criterion is the derived rule being tested).
"""
import json, time
from sympy import factorint, isprime, divisors
from fractions import Fraction

OPEN = [1, 121, 169, 289, 361, 529]
KMAX = 450
X_CAP = 3000          # x <= n/4 + X_CAP; excess never near this for n <= 380k

def two_term(n, x):
    """Return (y,z) solving d/(nx) = 1/y + 1/z with d = 4x - n, or None.
    u = d*y - nx, v = d*z - nx, uv = (nx)^2, u == -nx (mod d)."""
    d = 4 * x - n
    if d <= 0:
        return None
    nx = n * x
    M = (nx) ** 2
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
        check = Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n)
        if check and (best is None or (y, z) < best):
            best = (y, z)
    return best

def minimal_solution(n):
    x0 = (n + 3) // 4
    for x in range(x0, x0 + X_CAP + 1):
        r = two_term(n, x)
        if r is not None:
            return (x,) + r
    return None

def has_prime_in_class(v, cls):
    f = factorint(v)
    return any(p in cls for p in f)

QNR7 = {3, 5, 6}   # quadratic non-residues mod 7

def primes_2mod3_set():
    return {p for p in range(2, 2000) if isprime(p) and p % 3 == 2}

def main():
    t0 = time.time()
    rows = []
    for r in OPEN:
        for k in range(1 if r == 1 else 0, KMAX + 1):
            n = 840 * k + r
            sol = minimal_solution(n)
            if sol is None:
                print(f"r={r} k={k} n={n}: NO SOLUTION x <= n/4 + {X_CAP}")
                continue
            x, y, z = sol
            assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n)
            rows.append({'r': r, 'k': k, 'n': n, 'prime': bool(isprime(n)),
                         'x': x, 'y': y, 'z': z,
                         'excess': x - (n + 3) // 4, 'd': 4 * x - n})
    json.dump({'KMAX': KMAX, 'rows': rows}, open('code/out/extended_minimal_x.json', 'w'), indent=1)
    print(f"extended sweep: {len(rows)} solutions in {time.time()-t0:.1f}s")

    P23 = primes_2mod3_set()

    # ---- Criterion 1: e == 0 <=> p == 2 (mod 3) divides n or (n+3)/4 ----
    bad1 = []
    for row in rows:
        n = row['n']
        e0 = (row['excess'] == 0)
        cond = has_prime_in_class(n, P23) or has_prime_in_class((n + 3) // 4, P23)
        if e0 != cond:
            bad1.append((row['k'], row['r'], n, row['excess'], cond))
    print(f"criterion d=3: {len(rows)-len(bad1)}/{len(rows)} rows agree; mismatches: {bad1[:5]}")

    # ---- Criterion 2: d=7 works <=> n*(n+7)/4 has a QNR mod 7 prime ----
    bad2 = []
    for row in rows:
        n = row['n']
        x7 = (n + 7) // 4
        works = two_term(n, x7) is not None
        cond = has_prime_in_class(n, QNR7) or has_prime_in_class(x7, QNR7)
        if (row['excess'] == 1) != works:
            bad2.append(('internal', row['k'], row['r'], n))
        if works != cond:
            bad2.append(('criterion', row['k'], row['r'], n))
    print(f"criterion d=7: mismatches: {bad2[:5]} (count {len(bad2)})")

    # ---- minimality of excess: for e' < e, no split at x' = (n+4e'+3)/4 ----
    bad3 = []
    for row in rows:
        n = row['n']; e = row['excess']; x = row['x']
        for ep in range(0, e):
            xp = (n + 4 * ep + 3) // 4
            if two_term(n, xp) is not None:
                bad3.append((row['k'], row['r'], n, e, ep))
                break
    print(f"minimality exact: {len(rows)-len(bad3)}/{len(rows)} rows; violations: {bad3[:5]}")

    # ---- distribution of excess and max ----
    from collections import Counter
    cnt = Counter(row['excess'] for row in rows)
    print(f"excess distribution over all rows: {dict(sorted(cnt.items()))}")
    by_class = {}
    for row in rows:
        by_class.setdefault(row['r'], Counter())[row['excess']] += 1
    for r in OPEN:
        maxe = max(row['excess'] for row in rows if row['r'] == r)
        print(f"r={r}: max excess {maxe} at k = "
              f"{[row['k'] for row in rows if row['r']==r and row['excess']==maxe][:6]}")

    # ---- periodicity test of excess sequence per class ----
    for r in OPEN:
        arr = sorted([row for row in rows if row['r'] == r], key=lambda t: t['k'])
        es = [a['excess'] for a in arr]
        found = None
        for P in range(1, 60):
            if all(es[k] == es[k + P] for k in range(len(es) - P)):
                found = P
                break
        print(f"r={r}: excess sequence periodic with period {found} (smallest P<=59)" if found
              else f"r={r}: no period P<=59 over k <= {KMAX}")

    # ---- AP coverage: is {k : e(k)=0} containing a full residue class k = a mod M? ----
    hits = []
    for r in OPEN:
        e0s = {row['k'] for row in rows if row['r'] == r and row['excess'] == 0}
        for M in range(2, 61):
            for a in range(M):
                ap = set(range(a, KMAX + 1, M))
                if ap and ap <= e0s:
                    hits.append((r, M, a))
    print(f"full residue classes inside {{e=0}}: {hits}" if hits else
          f"no full residue class k=a mod M (M<=60) inside {{e=0}} for any class, k <= {KMAX}")

if __name__ == '__main__':
    main()