"""Independent exact-Fraction verification of the equality-case max-product bound.

This program recomputes everything from scratch with its own code and
fractions.Fraction — it does NOT read or trust code/equality_case.py.  The only
objects are exact rational numbers and exact integer factorisations; nothing
enumerates or searches for unitary perfect numbers.

Mathematical setting (the claim being verified):
    n = 2^a * prod_i p_i^{e_i} unitary perfect.  The 2-adic budget identity
    sum_i v2(p_i^{e_i}+1) = a+1 (proved in the workspace) gives the equality
    case omega(odd part) = a+1, which holds iff every odd unitary component
    q_i = p_i^{e_i} is 1 (mod 4).  Dividing sigma*(n)=2n by n then forces
        prod_{i=1}^{a+1} (1 + 1/q_i) = 2^{a+1}/(2^a+1) =: T(a).
    (1+1/q) is strictly decreasing in q, so the left side is < = its maximum
    over the a+1 SMALLEST admissible component sizes, one per distinct odd
    prime:  q = p if p=1 (mod 4), q = p^2 if p=3 (mod 4).  If that maximum,
    M(a), is strictly below T(a), the equality case is impossible for that a.

Complexity: polynomial in the number of components (≤ 31 components, primes
found by trial division up to ~200).  No search over n.
"""
import math
from fractions import Fraction


def is_prime(n):
    """Trial division, exact.  Not called on any number above ~200 here."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def admissible_sizes(count):
    """The `count` smallest admissible component sizes q == 1 (mod 4), one per
    distinct odd prime, ascending: q = p if p == 1 (mod 4), else q = p*p.

    Generate over all odd primes up to BOUND, sort by size, then slice to
    `count`.  A safety assertion confirms that the largest taken value is
    strictly smaller than the smallest admissible size from any prime beyond
    BOUND, guaranteeing the set is genuinely minimal.
    """
    BOUND = 800
    sizes = []
    for p in range(3, BOUND + 1, 2):
        if is_prime(p):
            sizes.append(p if p % 4 == 1 else p * p)
    sizes.sort()
    assert len(sizes) >= count, (BOUND, count)
    got = sizes[:count]
    q = BOUND + 1
    while not is_prime(q):
        q += 2
    min_future = q if q % 4 == 1 else q * q
    assert got[-1] < min_future, (got[-1], min_future, BOUND)
    return got


def T(a):
    """Exact target 2^(a+1)/(2^a+1)."""
    return Fraction(2 ** (a + 1), 2 ** a + 1)


def M(a):
    """Exact max of prod(1+1/q) over the a+1 smallest admissible sizes."""
    prod = Fraction(1)
    for q in admissible_sizes(a + 1):
        prod *= Fraction(q + 1, q)
    return prod


def factor(n):
    """Exact integer factorisation by trial division."""
    f = {}
    m = n
    c = 2
    while c * c <= m:
        while m % c == 0:
            f[c] = f.get(c, 0) + 1
            m //= c
        c += 1 if c == 2 else 2
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


results = []
def report(name, ok, detail=""):
    results.append(ok)
    print(f"{'PASS' if ok else 'FAIL':>4}  {name}" + (f"  [{detail}]" if detail else ""))


# ----------------------------------------------------------------------
# Point 1: a = 1.  T(1) = 4/3 exactly; max product over the 2 smallest
# admissible sizes is (1+1/5)(1+1/9) = 4/3 exactly; {5,9} is the odd part
# of 90 = 2^1 * 3^2 * 5^1.
# ----------------------------------------------------------------------
print("=" * 78)
print("Point 1: a = 1")
print("=" * 78)
t1 = T(1)
print(f"  T(1) = 2^2/(2^1+1) = {t1}  == Fraction(4,3)? {t1 == Fraction(4, 3)}")
report("T(1) == Fraction(4,3) exactly", t1 == Fraction(4, 3), str(t1))

sizes1 = admissible_sizes(2)
maxprod1 = M(1)
print(f"  2 smallest admissible sizes: {sizes1}")
print(f"  (1+1/5)(1+1/9) = {maxprod1}  == Fraction(4,3)? {maxprod1 == Fraction(4, 3)}")
report("max product (1+1/5)(1+1/9) == Fraction(4,3) exactly", maxprod1 == Fraction(4, 3), str(maxprod1))

f90 = factor(90)
odd_set = {p ** e for p, e in f90.items() if p != 2}
print(f"  factor(90) = {f90}")
print(f"  odd part of 90 (prime powers) = {sorted(odd_set)}")
report("{5,9} is the odd part of 90 = 2^1*3^2*5^1", f90 == {2: 1, 3: 2, 5: 1} and odd_set == {5, 9},
       "90 = " + " * ".join(f"{p}^{e}" for p, e in sorted(f90.items())))

# ----------------------------------------------------------------------
# Point 2: a = 8.  2^8+1 = 257 prime;  prod(p^e+1)=2n forces (2^a+1)|n so 257
# is a forced component; the max product with 257 forced is the 8 smallest
# admissible sizes excluding 257, times (1+1/257); confirm < T(8) = 512/257.
# ----------------------------------------------------------------------
print()
print("=" * 78)
print("Point 2: a = 8")
print("=" * 78)
seed = 2 ** 8 + 1
print(f"  2^8 + 1 = {seed}")
td_prime = all(seed % d != 0 for d in range(2, math.isqrt(seed) + 1))
print(f"  trial division over 2..isqrt({seed})={math.isqrt(seed)} finds no divisor: {td_prime}")
report("2**8+1 == 257 and 257 prime (trial division to sqrt(257))", seed == 257 and td_prime)

print("  Since sigma*(n) = (2^a+1)*prod(p^e+1) = 2n and gcd(2^a+1, 2) = 1, the")
print("  unitary divisor 2^a+1 forces (2^a+1) | (odd part of n); at a = 8 the")
print("  odd part is divisible by the prime 257, hence 257 is a forced odd")
print("  component, and the minimal admissible power of 257 is 257 itself")
print("  (257 == 1 mod 4), so the component contributes at least (1 + 1/257).")

sizes_no257 = [q for q in admissible_sizes(9) if q != 257][:8]
assert len(sizes_no257) == 8, sizes_no257
prod8 = Fraction(1)
for q in sizes_no257:
    prod8 *= Fraction(q + 1, q)
M8 = prod8 * Fraction(258, 257)
T8 = T(8)
print(f"  8 smallest admissible sizes excluding 257: {sizes_no257}")
print(f"  M(8) = prod over {sizes_no257} times (1+1/257) = {M8}")
print(f"  M(8) as float = {float(M8):.9f}")
print(f"  T(8) = 512/257 = {T8}  ({float(T8):.9f})")
print(f"  M(8) < T(8)? {M8 < T8},  deficit = {float(T8 - M8):.9f}")
report("a=8 max-product bound < T(8)=Fraction(512,257)", T8 == Fraction(512, 257) and M8 < T8,
       f"M8={M8} < T8={T8}")

# ----------------------------------------------------------------------
# Point 3: mod-4 admissibility of the residue classes.
# ----------------------------------------------------------------------
print()
print("=" * 78)
print("Point 3: admissible sizes are exactly those == 1 (mod 4)")
print("=" * 78)
print(f"  3 % 4 = {3 % 4}  (prime p == 3 mod 4: p itself NOT admissible, p ≡ 3)")
print(f"  7 % 4 = {7 % 4}  (same)")
print(f"  9 % 4 = {9 % 4}  (3^2 admissible)")
print(f"  49 % 4 = {49 % 4}  (7^2 admissible)")
ok3 = (3 % 4 == 3 and 7 % 4 == 3 and 9 % 4 == 1 and 49 % 4 == 1)
sizes30 = admissible_sizes(31)
ok3 &= all(q % 4 == 1 for q in sizes30)          # every admissible size is 1 mod 4
ok3 &= len(set(sizes30)) == len(sizes30)          # distinct primes -> distinct sizes
report("3,7 are 3 (mod 4) i.e. not admissible; 9=3^2, 49=7^2 are 1 (mod 4) i.e. admissible",
       ok3, f"first 31 admissible sizes all ≡1 mod4, distinct: {sizes30[:12]} ...")

# ----------------------------------------------------------------------
# Point 4: table a = 2..30, assert M(a) < T(a) for 2 <= a <= 28 and
# M(29) >= T(29).
# ----------------------------------------------------------------------
print()
print("=" * 78)
print("Point 4: table  a = 2..30,  M(a) vs T(a) in exact arithmetic")
print("=" * 78)
print(f"{'a':>3} {'k=a+1':>6} {'T(a)':>12} {'M(a)':>30} {'M(a) < T(a)':>12}")
all_lt = True
for a in range(2, 31):
    ta, ma = T(a), M(a)
    lt = ma < ta
    if 2 <= a <= 28 and not lt:
        all_lt = False
    print(f"{a:>3} {a + 1:>6} {float(ta):>12.9f} {float(ma):>30.18f} {str(lt):>12}")
print()
print(f"  M(a) < T(a) for every a in 2..28? {all_lt}")
print(f"  M(29) >= T(29)? {M(29) >= T(29)}   (M(29)={M(29)}, T(29)={T(29)})")
report("M(a) < T(a) for all 2 <= a <= 28", all_lt)
report("M(29) >= T(29)", M(29) >= T(29), f"M(29)={M(29)}, T(29)={T(29)}")

print()
print("=" * 78)
point_ok = [
    all(results[0:3]),   # point 1: a = 1, T(1) = max product = 4/3, {5,9} odd part of 90
    all(results[3:5]),   # point 2: 257 prime, forced component, a=8 bound < T(8)
    results[5],          # point 3: mod-4 admissibility
    all(results[6:8]),   # point 4: table 2..30, M < T for 2..28 and M(29) >= T(29)
]
print(f"VERDICTS: {sum(point_ok)}/4 points PASS  ->  {'ALL FOUR POINTS PASS' if all(point_ok) else 'SOME POINT FAILED'}")
print("=" * 78)
raise SystemExit(0 if all(point_ok) else 1)