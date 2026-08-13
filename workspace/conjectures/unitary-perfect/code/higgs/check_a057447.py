#!/usr/bin/env python3
"""Cross-check a recursive 3-Higgs prime predicate against OEIS A057447.

OEIS definition, verbatim from https://oeis.org/A057447 (name line):

    A057447: a(n+1) = next prime such that a(n+1)-1 | (a(1)...a(n))^3.

with OFFSET 1,1 and the page's Mathematica seed {2}: so a(1) = 2 and each
further term is the least prime p > a(n) with (p-1) dividing the cube of the
product of all earlier terms.

This script:
  1. generates 3-Higgs primes exactly as the name line states (primes in
     increasing order; keep p iff (p-1) | (product of kept so far)^3);
  2. compares the first 58 terms against the DATA field of the OEIS page,
     transcribed into OEIS_A057447 below;
  3. verifies the five known unitary perfect numbers (A002827) by the unitary
     sigma identity sigma_star(n) == 2*n, and that the fifth term equals the
     product of the prime powers in A002827's EXAMPLE field;
  4. checks A002827's comment "The prime factors of a unitary perfect number
     are the Higgs primes (A057447)" against all five witnesses.

Exact integer arithmetic only; no floats. Prepared by the librarian; the
librarian has no shell, so this file has NOT yet been executed. Run it as:
    timeout 540 python3 code/higgs/check_a057447.py 2>&1 \
        | tee code/out/higgs_a057447.captured.txt; echo EXIT_CODE=$?
"""

import sys

# DATA field of https://oeis.org/A057447 — all 58 terms, exact transcription.
OEIS_A057447 = [
    2, 3, 5, 7, 11, 13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 101, 107, 109, 127, 131, 139, 149, 151, 157, 167, 173,
    179, 181, 191, 197, 199, 211, 223, 229, 233, 251, 263, 269, 271, 277,
    281, 283, 293, 311, 313, 317, 331, 347, 349, 359,
]

# A002827 DATA field — the run's five witnesses.
A002827 = [6, 60, 90, 87360, 146361946186458562560000]

# From A002827's EXAMPLE field: prime-power factorization of the fifth term.
FIFTH_FACTORS = [(2, 18), (3, 1), (5, 4), (7, 1), (11, 1), (13, 1), (19, 1),
                 (37, 1), (79, 1), (109, 1), (157, 1), (313, 1)]


def primes_up_to(n):
    """Sieve of Eratosthenes; trivial at this size."""
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = b"\x00" * (((n - i * i) // i) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def higgs3_terms(count):
    """First `count` 3-Higgs primes, exactly per the A057447 name line."""
    terms = []
    prod = 1  # product of all 3-Higgs primes found so far (exact integer)
    for p in primes_up_to(1_000_000):
        if len(terms) >= count:
            break
        if (p - 1) and (prod ** 3) % (p - 1) == 0:
            terms.append(p)
            prod *= p
    assert len(terms) == count, f"only reached {len(terms)} of {count} terms"
    return terms


def sigma_star(n):
    """Unitary sigma: product over p^a || n of (p^a + 1). Exact integers."""
    m, total, p = n, 1, 2
    while p * p <= m:
        if m % p == 0:
            pa = 1
            while m % p == 0:
                m //= p
                pa *= p
            total *= pa + 1
        p += 1
    if m > 1:
        total *= m + 1
    return total


def main():
    problems = []

    got = higgs3_terms(len(OEIS_A057447))
    if got == OEIS_A057447:
        print(f"3-Higgs recursion matches OEIS A057447 for all "
              f"{len(OEIS_A057447)} DATA terms.")
        print("First 30 terms: " + ", ".join(str(t) for t in got[:30]))
    else:
        problems.append("3-Higgs term mismatch")
        for i, (g, o) in enumerate(zip(got, OEIS_A057447)):
            print(f"  a({i + 1}) = {g} (OEIS: {o})"
                  + ("" if g == o else "   <-- MISMATCH"))
        if len(got) != len(OEIS_A057447):
            print(f"  length: generated {len(got)}, OEIS {len(OEIS_A057447)}")

    for n in A002827:
        ok = sigma_star(n) == 2 * n
        print(f"sigma_star({n}) == 2n : {ok}")
        if not ok:
            problems.append(f"witness {n} failed the unitary-perfect check")

    fifth = 1
    for p, e in FIFTH_FACTORS:
        fifth *= p ** e
    ok = fifth == A002827[-1]
    print(f"EXAMPLE factorization of the fifth term reproduces it: {ok}")
    if not ok:
        problems.append("fifth-term EXAMPLE factorization mismatch")

    higgs_set = set(got)
    for n in A002827:
        m, p, primes = n, 2, []
        while p * p <= m:
            if m % p == 0:
                primes.append(p)
                while m % p == 0:
                    m //= p
            p += 1
        if m > 1:
            primes.append(m)
        missing = [q for q in primes if q not in higgs_set]
        print(f"prime divisors of {n}: {primes}; "
              f"not 3-Higgs in first {len(got)} terms: {missing or 'none'}")
        if missing:
            problems.append(f"{n} has a prime divisor outside A057447")

    if problems:
        print("FAIL: " + "; ".join(problems))
        sys.exit(1)
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()