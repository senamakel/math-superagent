"""Exact integer oracle for the Erdos ternary-digits conjecture.

Conjecture (Erdos 1979): for every n > 8 the base-3 expansion of 2**n
contains at least one digit 2. The known counterexamples to "all n work"
are the three witnesses n = 0 (1_3), n = 2 (11_3), n = 8 (100111_3).

Three float-free functions:

    digit_free(n)
        True iff the base-3 expansion of 2**n contains no digit 2.
        Exact integer arithmetic (materialises 2**n only for the n given).

    sieve_count(k)
        |A_k| where
            A_k = { r mod 2*3^(k-1) : the low k ternary digits of
                    2^r mod 3^k lie in {0,1} }.
        Computed by an exact bijection (see THEORY below), O(k) big-int
        work, never enumerating the 2^(k-1) residues in the set.

    finite_check(lo, hi)
        Every n in [lo, hi] with digit_free(n); returns the exempt set.

THEORY behind sieve_count -- the counting obstruction, stated exactly.
The order of 2 modulo 3^k is 2*3^(k-1) = phi(3^k) (2 is a primitive root
modulo 3^k; its order mod 3^n is 2*3^(n-1)).  Hence the map
    r mod 2*3^(k-1)  ->  2^r mod 3^k
is a BIJECTION from Z/(2*3^(k-1))Z onto the unit group (Z/3^k)^x.
For 0 <= v < 3^k the k base-3 digits of v are all of its digits, so

    A_k  <->  { v < 3^k : 3 does not divide v and the k base-3 digits
                           of v lie in {0,1} }              (bijection)

The unit condition 3 not divide v forces the units digit to be odd; among
{0, 1} only the digit 1 is odd, so the units digit is fixed to 1 and the
remaining k-1 digits are each freely 0 or 1.  Therefore

    |A_k| = 2^(k-1).

This is the "counting obstruction" of problem.md, established here by
bijection rather than enumeration.  sieve_count(k) returns 2^(k-1) for
every k, which is verified against naive enumeration (direct_count) and
against survivor lifting (lift_count) for every k where those are feasible.
"""


def to_base3(m):
    """Base-3 digit string of m (most significant first). m >= 0."""
    if m == 0:
        return "0"
    digs = []
    while m > 0:
        digs.append(str(m % 3))
        m //= 3
    return "".join(reversed(digs))


def digit_free(n):
    """True iff base-3 of 2**n avoids the digit 2. Exact integer arithmetic."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return True  # 2^0 = 1 = 1_3
    m = 2 ** n
    while m > 0:
        if m % 3 == 2:
            return False
        m //= 3
    return True


def _low_k_digits_free(val, k):
    """True iff the low k base-3 digits of val (0 <= val < 3**k) avoid 2."""
    for _ in range(k):
        if val % 3 == 2:
            return False
        val //= 3
    return True


def direct_count(k):
    """Enumerate EVERY r mod 2*3^(k-1), count low-k-digit-free images.

    Deliberately naive: O(2*3^(k-1)) pow calls. Valid only for small k.
    Used to verify sieve_count on the small instances where enumeration
    is feasible.  This is the oracle; sieve_count must match it there.
    """
    if k < 1:
        raise ValueError("k must be >= 1")
    m = 3 ** k
    period = 2 * 3 ** (k - 1)
    cnt = 0
    for r in range(period):
        if _low_k_digits_free(pow(2, r, m), k):
            cnt += 1
    return cnt


def lift_count(k):
    """|A_k| by survivor lifting, modulo 3^k only.

    Maintains the actual surviving residue set; the set has exactly
    2^cur elements at level cur, so this is exponential SPACE and is
    only usable for small k.  Kept purely as an independent check of
    the closed form on feasible k.  See module docstring of the old
    oracle: each class r has three lifts r, r+L, r+2L (L=2*3^(cur-1))
    whose low digits repeat, so only digit cur is newly constrained.
    """
    if k < 1:
        raise ValueError("k must be >= 1")
    A = {0}
    cur = 1
    while cur < k:
        L = 2 * 3 ** (cur - 1)
        next_mod = 3 ** (cur + 1)
        g = pow(2, L, next_mod)
        p3k = 3 ** cur  # scale of the digit being checked
        Anext = set()
        for r in A:
            base = pow(2, r, next_mod)
            gp = 1
            for j in range(3):
                v = (base * gp) % next_mod
                d = (v // p3k) % 3
                if d in (0, 1):
                    Anext.add(r + j * L)
                gp = gp * g % next_mod
        A = Anext
        cur += 1
    return len(A)


def sieve_count(k):
    """|A_k| by the exact bijection, in O(k) big-int work. No enumeration.

    Rests on 2 being a primitive root modulo 3^k (order 2*3^(k-1)), so
    A_k is in bijection with the {0,1}-digit units below 3^k; the units
    digit is forced to 1 and the other k-1 digits are free, giving
    |A_k| = 2^(k-1).  Verified against direct_count and lift_count on the
    small k where those run.
    """
    if k < 1:
        raise ValueError("k must be >= 1")
    return 2 ** (k - 1)


def finite_check(lo, hi):
    """List of n in [lo, hi] (inclusive) with digit_free(n) true."""
    return [n for n in range(lo, hi + 1) if digit_free(n)]
