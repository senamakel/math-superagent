"""Eliminate the equality case omega(odd) = a+1 of the 2-adic budget corollary.

Setting.  n = 2^a * prod_i p_i^{e_i} unitary perfect.  The workspace proves
    sum_i v2(p_i^{e_i} + 1) = a + 1      (exact budget identity)
so omega := omega(odd part) <= a + 1, with EQUALITY iff every odd unitary
component satisfies p^e = 1 (mod 4).

This program bounds the equality case from above.  No enumeration of n: the
only object searched is the multiset of admissible component SIZES, and the
argument is a maximum, not a hunt.

In the equality case, dividing sigma*(n) = 2n by n:

    (1 + 2^-a) * prod_{i=1}^{a+1} (1 + 1/q_i) = 2,
    hence  prod_{i=1}^{a+1} (1 + 1/q_i) = 2^{a+1} / (2^a + 1)  =: T(a),

with q_i = p_i^{e_i} = 1 (mod 4), the p_i distinct odd primes.

Upper bound.  prod (1 + 1/q_i) is strictly decreasing in each q_i, so it is
maximised by taking the a+1 SMALLEST admissible component sizes over distinct
odd primes.  For a prime p the minimal admissible power is
    p     if p = 1 (mod 4),
    p^2   if p = 3 (mod 4)   (p itself is 3 mod 4, p^2 is 1 mod 4).
If that maximum is < T(a), the equality case is impossible for that a.
"""
from fractions import Fraction

def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0: return False
        d += 2
    return True

def minimal_admissible(count):
    """Minimal component size = 1 mod 4, one per odd prime, ascending.
    
    Generate admissible sizes for odd primes up to a generous bound, sort
    all, then slice to `count`.  Assert that the count-th smallest is below
    the smallest admissible size from any prime beyond the bound, so the
    truncation is safe (not missing any genuinely smaller value).
    """
    BOUND = 800
    sizes = []
    for p in range(3, BOUND + 1, 2):
        if is_prime(p):
            sizes.append(p if p % 4 == 1 else p * p)
    sizes.sort()
    assert len(sizes) >= count, (BOUND, count)
    got = sizes[:count]
    # Safety: the next prime after BOUND must contribute an admissible size
    # strictly larger than the largest we took.
    q = BOUND + 1
    while not is_prime(q):
        q += 2
    min_future = q if q % 4 == 1 else q * q
    assert got[-1] < min_future, (got[-1], min_future, BOUND)
    return got

MIN_Q = minimal_admissible(200)

print("minimal admissible component sizes (1 mod 4), first 12:", MIN_Q[:12])
print("  note 9 = 3^2 and 49 = 7^2 enter as squares since 3, 7 = 3 (mod 4)")
print()

def max_product(k):
    """Largest possible prod (1+1/q) over k components, distinct odd primes,
    every component 1 mod 4."""
    prod = Fraction(1)
    for q in MIN_Q[:k]:
        prod *= Fraction(q + 1, q)
    return prod

print(f"{'a':>5} {'omega=a+1':>9} {'T(a)=2^(a+1)/(2^a+1)':>22} {'max product':>14} {'equality case':>16}")
first_survivor = None
for a in range(1, 121):
    k = a + 1
    T = Fraction(2 ** (a + 1), 2 ** a + 1)
    M = max_product(k)
    ok = M >= T
    if ok and first_survivor is None:
        first_survivor = a
    if a <= 20 or a % 10 == 0 or (first_survivor is not None and a <= first_survivor + 2):
        print(f"{a:>5} {k:>9} {float(T):>22.9f} {float(M):>14.9f} "
              f"{'possible' if ok else 'IMPOSSIBLE':>16}")

print()
print(f"smallest a whose equality case survives the bound: {first_survivor}")
print()

# The a = 8 case in exact arithmetic, with the forced prime spelled out.
print("=" * 68)
print("The a = 8 case in exact arithmetic")
print("=" * 68)
seed = 2 ** 8 + 1
print(f"  2^8 + 1 = {seed}, prime: {is_prime(seed)}")
print(f"  so 257 | n and 257 must itself be one of the odd components")
T8 = Fraction(2 ** 9, seed)
print(f"  odd components must satisfy  prod (1+1/q) = {T8} = {float(T8):.9f}")
print(f"  with exactly 9 components, all = 1 (mod 4), one of them a power of 257")
best = Fraction(1)
used = []
for q in MIN_Q:
    if len(used) == 8: break
    if q == 257: continue
    used.append(q); best *= Fraction(q + 1, q)
best_with_257 = best * Fraction(258, 257)
used.append(257)
print(f"  most generous admissible multiset: {sorted(used)}")
print(f"  its product = {float(best_with_257):.9f}  <  {float(T8):.9f}")
print(f"  deficit = {float(T8 - best_with_257):.9f}")
print(f"  EQUALITY CASE a=8 IMPOSSIBLE: {best_with_257 < T8}")

print()
print("=" * 68)
print("Witness set check: the bound must not kill any known number")
print("=" * 68)
KNOWN = [6, 60, 90, 87360, 146361946186458562560000]
def factor(n):
    fs = {}; m = n; c = 2
    while c * c <= m:
        while m % c == 0: fs[c] = fs.get(c, 0) + 1; m //= c
        c += 1 if c == 2 else 2
    if m > 1: fs[m] = fs.get(m, 0) + 1
    return fs
for n in KNOWN:
    f = factor(n); a = f.pop(2); w = len(f)
    eq = (w == a + 1)
    allmod4 = all((p ** e) % 4 == 1 for p, e in f.items())
    print(f"  n={n}: a={a} omega={w} equality={eq} all components 1 mod 4={allmod4}"
          + ("   <- in scope" if eq else "   (not in the equality case, untouched)"))
