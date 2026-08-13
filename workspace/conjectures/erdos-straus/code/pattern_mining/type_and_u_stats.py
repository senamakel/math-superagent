"""Type (divisibility-by-n) statistics and divisor u = d*y - n*x structure.

For every minimal-x solution stored in code/out/extended_minimal_x.json
(2705 rows, six open classes, k <= 450):
  * type: which of x, y, z are divisible by n (0, 1, or 2 of them; 3 is
    impossible since 4/n = sum and z would exceed... check anyway)
  * u = d*y - n*x with d = 4x - n: the smaller factor of (n*x)^2 used by the
    two-term split.  Verify u | (n*x)^2, u == -n*x (mod d), u <= n*x, and that
    y, z are recovered exactly from u.
  * u-structure: is u prime? a prime power? does u divide n*x (vs only
    (n*x)^2, meaning some exponent > v_p(nx), i.e. u needs the square)?  size
    of u relative to n*x, number of distinct prime factors.

Purpose: the type counts confront the Elsholtz-Tao type I/II obstruction as
glossed in memory ("odd perfect squares have no type-I/II solutions"), and the
u-structure shows what divisor shape a polynomial family would need to use.
"""
import json
from collections import Counter, defaultdict
from fractions import Fraction
from sympy import factorint, isprime
from math import gcd

rows = json.load(open('code/out/extended_minimal_x.json'))['rows']
print(f"rows: {len(rows)}")

type_cnt = Counter()
type_by_class = defaultdict(Counter)
type_by_excess = defaultdict(Counter)
u_stats = Counter()
u_prime_cnt = 0
u_needssquare = 0
u_divides_nx = 0
ratio_bins = Counter()
u_omega = Counter()
errors = []
u_is_smallest_qualifying = 0
u_checked = 0

for row in rows:
    n, x, y, z, e = row['n'], row['x'], row['y'], row['z'], row['excess']
    r = row['r']
    assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n)
    d = 4 * x - n
    nx = n * x
    M = nx * nx
    # recover u from the stored smaller denominator y
    u = d * y - nx
    assert (nx + u) % d == 0 and y == (nx + u) // d
    assert u > 0 and u <= nx and M % u == 0
    v = M // u
    assert (nx + v) % d == 0 and z == (nx + v) // d
    assert (nx + u) % d == 0  # u == -nx mod d comes from this
    # type: how many of x,y,z divisible by n
    t = (x % n == 0, y % n == 0, z % n == 0)
    tc = sum(t)
    type_cnt[tc] += 1
    type_by_class[r][tc] += 1
    type_by_excess[e][tc] += 1
    if tc == 1:
        which = 'x' if t[0] else ('y' if t[1] else 'z')
        type_cnt[('1-of-3', which)] += 1
    if tc == 2:
        which = ''.join(c for c, tt in zip('xyz', t) if tt)
        type_cnt[('2-of-3', which)] += 1
    # u-structure
    u_checked += 1
    if isprime(u):
        u_prime_cnt += 1
    f = factorint(u)
    if len(f) == 1:
        u_stats['prime power'] += 1
    if nx % u == 0:
        u_divides_nx += 1
        u_stats['u | nx'] += 1
    else:
        u_stats['u | (nx)^2 only'] += 1
        # a prime whose exponent in u exceeds its exponent in nx
        for p, a in f.items():
            vp = 0
            t_ = nx
            while t_ % p == 0:
                t_ //= p
                vp += 1
            if a > 2 * vp:
                errors.append(('exp overflow', r, row['k'], n, p, a, vp))
                break
            if a > vp:
                u_needssquare += 1
                break
    rr = u / nx
    rb = ('<0.01' if rr < 0.01 else '0.01-0.1' if rr < 0.1
          else '0.1-0.5' if rr < 0.5 else '0.5-1.0')
    ratio_bins[rb] += 1
    u_omega[len(f)] += 1

print("\n-- type: how many of x,y,z are divisible by n (exact) --")
print(f"all rows: {dict(type_cnt)}")
for r in sorted(type_by_class):
    print(f"r={r:>3}: {dict(type_by_class[r])}")
print(f"among rows with e>=6: { {e: dict(type_by_excess[e]) for e in sorted(type_by_excess) if e >= 6} }")

print("\n-- u-structure (u = d*y - n*x, the smaller factor of (n*x)^2) --")
print(f"u prime: {u_prime_cnt}/{u_checked}")
print(f"u is a prime power: {u_stats['prime power']}")
print(f"u divides n*x: {u_divides_nx}   u needs (n*x)^2 (some exponent doubled): {u_needssquare}")
print(f"u/nx ratio bins: {dict(ratio_bins)}")
print(f"u distinct-prime-count distribution: {dict(u_omega)}")
print(f"exp-overflow errors: {len(errors)} ({errors[:3]})")