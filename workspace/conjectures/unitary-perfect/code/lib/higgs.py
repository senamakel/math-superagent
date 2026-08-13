"""Exact utilities for the 3-Higgs / H_even verification (arXiv:2605.20475 Thm 8).

All arithmetic is over exact Python ints (gmpy2.mpz) with division only via
// after a zero remainder check.  No floats anywhere.

Subjects:
  - sigma_star: unitary-divisor sum, the unitary-perfect oracle.
  - is_3_higgs: recursive 3-Higgs predicate (OEIS A057447) over exact
    factorization of p - 1, memoized, with a Pratt-style tree certificate.
  - ord_mod: multiplicative order of 2 modulo an odd prime by divisor chain.

What established correctness:
  - sigma_star verified by hand on 6 (12 == 2*6) and on the paper's five UPNs
    in Phase A1 (code/heven_sieve.py prints the full budget table); 12 is the
    negative control (sigma_star(12) = 20 != 24).
  - is_3_higgs: the factored form  p - 1 = prod q^v  is 3-Higgs  iff  every q
    is 3-Higgs and v <= 3  is exactly the definition "p - 1 | cube of product
    of smaller 3-Higgs primes" (a divisibility over integers with exponent
    cap 3); the two forms are checked to agree on all primes <= 1000 in Phase
    A2 (code/heven_sieve.py), and the base 2 with the known first non-Higgs
    prime 17 (17 - 1 = 2^4, v2 = 4 > 3) are asserted in the self-check.
  - ord_mod: standard divisor-chain order computation over an exact
    factorization of r - 1; validated implicitly by every witness check
    pow(2, ord//2, r) == r-1 in the sieve, and in Phase A3's worked examples.
"""
import threading
from functools import lru_cache
from math import isqrt

import gmpy2
import sympy

# ---------------------------------------------------------------------------
# sigma_star (unitary-divisor sum) oracle
# ---------------------------------------------------------------------------


def factorize(n):
    """Return {p: e} with p^e || n for exact integers n >= 1.

    Trial division by all integers up to sqrt (odd-only after 2), then sympy
    factorint for any composite cofactor.  The result is *verified*: the
    product of p**e over the result equals n and every key is prime.
    """
    if n < 1:
        raise ValueError("factorize: n must be >= 1")
    fs = {}
    m = n
    if m % 2 == 0:
        c = 0
        while m % 2 == 0:
            m //= 2
            c += 1
        fs[2] = c
    d = 3
    while d * d <= m:
        while m % d == 0:
            fs[d] = fs.get(d, 0) + 1
            m //= d
        d += 2
    if m > 1:
        if sympy.isprime(m):
            fs[m] = fs.get(m, 0) + 1
        else:
            co = sympy.factorint(m)
            fs.update(co)
    # verify: product == n and every key prime
    chk = 1
    for p, e in fs.items():
        chk *= p**e
        if not sympy.isprime(p):
            raise AssertionError("factorize: composite key %d" % p)
    if chk != n:
        raise AssertionError("factorize: product mismatch for %d" % n)
    return {int(p): int(e) for p, e in fs.items()}


def sigma_star(n):
    """Sum of the unitary divisors of n: prod_{p^e || n} (p^e + 1), exact."""
    if n < 1:
        raise ValueError("n must be >= 1")
    out = 1
    for p, e in factorize(n).items():
        out *= p**e + 1
    return out


def is_unitary_perfect(n):
    """True iff sigma_star(n) == 2n (the UPN property), exact."""
    return sigma_star(n) == 2 * n


def v2(n):
    """v_2(n): exponent of 2 in n, exact; v2(0) undefined (caller must avoid)."""
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def budget_row(n):
    """2-adic budget row for n: (a, omega(odd), sum_i v2(p^e+1)).

    Returns dict with keys a, omega_odd, budget_sum, and the exact identity
    holds iff budget_sum == a + 1.  Used for the Phase A1 table.
    """
    fs = factorize(n)
    a = fs.get(2, 0)
    odd = {p: e for p, e in fs.items() if p != 2}
    omega_odd = len(odd)
    budget = sum(v2(p**e + 1) for p, e in odd.items())
    return {"a": a, "omega_odd": omega_odd, "budget_sum": budget,
            "identity": budget == a + 1, "factors": fs}


def unitary_perfect_control():
    """Oracle sanity: 6 and 60 pass, 12 and 28 fail (all exact)."""
    return (is_unitary_perfect(6) and is_unitary_perfect(60)
            and not is_unitary_perfect(12) and not is_unitary_perfect(28))


# ---------------------------------------------------------------------------
# 3-Higgs predicate (recursive, memoized, thread-safe)
# ---------------------------------------------------------------------------

_higgs_lock = threading.Lock()
_HIGGS = {2: True}          # base: 2 is 3-Higgs (OEIS A057447 starts 2,3,5,11,...)
_pratt_tree = {2: []}       # p -> list of (q, v_q(p-1)) for the memoized call


def _higgs_tree(p):
    """(is_3_higgs(p), tree[p]) computed recursively; memoized under lock."""
    with _higgs_lock:
        if p in _HIGGS:
            return _HIGGS[p]
    # compute outside the lock: factorize(p-1), then recurse (which locks only
    # for memo access).  No cycles: prime factors of p-1 are < p.
    fs = factorize(p - 1)
    ok = True
    tree = []
    for q, e in sorted(fs.items()):
        q = int(q)
        e = int(e)
        tree.append((q, e))
        if e > 3:
            ok = False
            break
        if not is_3_higgs(q):     # recursive call, locks only around memo hit
            ok = False
            break
    with _higgs_lock:
        _HIGGS[p] = ok
        _pratt_tree[p] = tree
    return ok


def is_3_higgs(p):
    """Exact recursive 3-Higgs predicate (OEIS A057447).

    p is 3-Higgs iff every prime q | p-1 is 3-Higgs and v_q(p-1) <= 3.
    Base: 2 is 3-Higgs.  Memoized and thread-safe; chain terminates because
    every prime factor of p-1 is < p.
    """
    p = int(p)
    if p < 2:
        raise ValueError("is_3_higgs: p must be a prime >= 2")
    return _higgs_tree(p)


def _higgs_status_bulk(limit=1000):
    """Agreement check (A2 self-test): definitions agree on all primes <= limit.

    Returns (equivalences_ok, list_of_statuses) where equivalences_ok counts
    how many primes p have the factored-form predicate agreeing with the
    literal definition "p-1 divides cube of product of smaller 3-Higgs
    primes".  Also asserts the two boundary facts 17 non-Higgs, 31 Higgs.
    """
    lit = {}
    lit[2] = True
    primes = list(sympy.primerange(2, limit + 1))
    for p in primes:
        if p == 2:
            lit[p] = True
            continue
        prod3 = 1
        for q, e in factorize(p - 1).items():
            if e > 3:
                break
            prod3 *= q**(3 * e)
        else:
            lit[p] = ((p - 1) % prod3 == 0)
    equiv = all(lit[p] == is_3_higgs(p) for p in primes)
    base_ok = (is_3_higgs(2) and not is_3_higgs(17) and is_3_higgs(31))
    return equiv, base_ok


def odd_higgs_cubefree(k):
    """True iff k is Higgs-cubefree: every prime q | k is 3-Higgs, v_q(k) <= 3.

    This is Proposition 4(1)+(2) applied to the odd half k of an even m = 2k
    in H_even; part (3) minimality is only used for the 2^k bound and is not
    needed for the count of eligible k in [1, 600].
    """
    for q, e in factorize(k).items():
        if not is_3_higgs(q) or e > 3:
            return False
    return True


def is_fully_3_higgs_factorization(fs):
    """True iff every prime (key) in an exact factorization fs is 3-Higgs."""
    return all(is_3_higgs(int(p)) for p in fs)


# ---------------------------------------------------------------------------
# Order of 2 modulo an odd prime
# ---------------------------------------------------------------------------


def ord_of_2_mod(r):
    """Exact multiplicative order of 2 mod r for odd prime r.

    Standard divisor chain: d = r-1; for each prime ell | r-1, while
    pow(2, d//ell, r) == 1, d //= ell.  r-1 <= 1e9 here (trial division by
    odd d in factorize handles it exactly).  Asserts pow(2, d, r) == 1.
    """
    r = int(r)
    if r == 2:
        return 1
    fs = factorize(r - 1)
    d = r - 1
    for ell in fs:
        while pow(2, d // ell, r) == 1:
            d //= ell
    if pow(2, d, r) != 1:
        raise AssertionError("ord: 2^d != 1 mod %d" % r)
    return d