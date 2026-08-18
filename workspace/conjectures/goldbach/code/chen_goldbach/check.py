"""Finite all-even Chen-prime Goldbach checker.

A Chen prime p means p is prime and p+2 is either prime or a semiprime
(product of two primes, with repetition allowed). For every even n in
[4, bound], this checks whether n is a sum of two Chen primes.

The program is evidence for claim G-structural-closure in
research/backward/full-goldbach-via-exceptional-set.md; it is not a proof of
that open claim or of binary Goldbach.
"""
from __future__ import annotations

import argparse
import time
from math import isqrt
from lib.goldbach import goldbach_partitions


def sieve(limit: int) -> bytearray:
    """Return exact primality flags for integers 0..limit."""
    prime = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        prime[0] = 0
    if limit >= 1:
        prime[1] = 0
    for p in range(2, isqrt(limit) + 1):
        if prime[p]:
            prime[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return prime


def chen_flags(bound: int) -> tuple[bytearray, bytearray]:
    """Return prime and Chen-prime flags through bound."""
    prime = sieve(bound + 2)
    semiprime = bytearray(bound + 3)
    # Every semiprime f*g has f <= sqrt(f*g), so only this outer range is needed.
    small_primes = [p for p in range(2, isqrt(bound + 2) + 1) if prime[p]]
    all_primes = [p for p in range(2, bound + 3) if prime[p]]
    for f in small_primes:
        for g in all_primes:
            product = f * g
            if product > bound + 2:
                break
            semiprime[product] = 1
    chen = bytearray(bound + 1)
    for p in range(2, bound + 1):
        chen[p] = prime[p] and (prime[p + 2] or semiprime[p + 2])
    return prime, chen


def check(bound: int, hard_count: int = 10) -> dict:
    """Check every even n through bound, stopping at the first failure.

    ``hardest_n`` holds the n whose smallest Chen witness p is largest,
    as (p, n) pairs sorted by p descending.  Diagnostic only.
    """
    started = time.perf_counter()
    prime, chen = chen_flags(bound)
    first_failure = None
    witness = None
    checked = 0
    hardest = []
    for n in range(4, bound + 1, 2):
        checked += 1
        for p in range(2, n // 2 + 1):
            if chen[p] and chen[n - p]:
                witness = (p, n - p)
                break
        else:
            first_failure = n
            witness = None
            break
        if len(hardest) < hard_count:
            hardest.append((p, n))
            hardest.sort(reverse=True)
        elif p > hardest[-1][0]:
            hardest[-1] = (p, n)
            hardest.sort(reverse=True)
    mod6 = check_mod6_4(chen, bound)
    return {
        "bound_requested": bound,
        "bound_reached": bound if first_failure is None else first_failure,
        "first_failure": first_failure,
        "witness_at_last_n": witness,
        "tested_numbers": checked,
        "hardest_n": hardest,
        "mod6_4_first_failure": mod6["first_failure"],
        "mod6_4_tested_numbers": mod6["tested_numbers"],
        "elapsed_seconds": time.perf_counter() - started,
    }


def check_mod6_4(chen: bytearray, bound: int) -> dict:
    """Using already-built flags, check the original n == 4 (mod 6) class."""
    checked = 0
    for n in range(4, bound + 1, 6):
        checked += 1
        for p in range(2, n // 2 + 1):
            if chen[p] and chen[n - p]:
                break
        else:
            return {"first_failure": n, "tested_numbers": checked}
    return {"first_failure": None, "tested_numbers": checked}


def census_all_even(chen: bytearray, bound: int, hard_count: int = 10) -> dict:
    """Scan every even n in [4, bound] without stopping at failures.

    Returns the failure list (even n with no Chen pair) and the n whose
    smallest Chen witness p is largest (as (p, n) sorted by p descending),
    plus the smallest witness p for each n as a list indexed by n//2.
    Diagnostic use only; the verification bound is set by `check`.
    """
    failures = []
    smallest_witness = [0] * (bound // 2 + 1)
    hardest = []
    for n in range(4, bound + 1, 2):
        p = 2
        while p <= n // 2:
            if chen[p] and chen[n - p]:
                break
            p += 1
        smallest_witness[n // 2] = p if p <= n // 2 else 0
        if p > n // 2:
            failures.append(n)
        elif len(hardest) < hard_count:
            hardest.append((p, n))
            hardest.sort(reverse=True)
        elif p > hardest[-1][0]:
            hardest[-1] = (p, n)
            hardest.sort(reverse=True)
    return {
        "failures": failures,
        "failures_mod6": sorted({n % 6 for n in failures}),
        "hardest_n": hardest,
        "smallest_witness": smallest_witness,
    }


def sanity() -> None:
    """Cross-check ordinary Goldbach against the existing naive oracle to 1000."""
    assert all(goldbach_partitions(n) for n in range(4, 1001, 2))
    prime, chen = chen_flags(20)
    assert prime[2] == 1 and prime[5] == 1 and prime[7] == 1
    assert prime[4] == 0 and prime[9] == 0
    assert chen[2] == 1 and chen[3] == 1 and chen[7] == 1
    print("sanity ordinary_goldbach_4_to_1000: PASS")
    print("hand classifications: p=2 -> 4=2*2; p=3 -> 5 prime; p=7 -> 9=3*3: PASS")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bound", type=int)
    parser.add_argument("--sanity", action="store_true")
    args = parser.parse_args()
    if args.sanity:
        sanity()
    result = check(args.bound)
    print(f"bound: {args.bound}")
    print(f"first_failure: {result['first_failure'] if result['first_failure'] is not None else 'none up to ' + str(args.bound)}")
    print(f"mod6_4_first_failure: {result['mod6_4_first_failure'] if result['mod6_4_first_failure'] is not None else 'none up to ' + str(args.bound)}")
    print(f"mod6_4_tested_numbers: {result['mod6_4_tested_numbers']}")
    print(f"witness_at_last_n: {result['witness_at_last_n']}")
    print(f"tested_numbers: {result['tested_numbers']}")
    print("hardest_n (n, smallest Chen witness p):")
    for p, n in result["hardest_n"]:
        print(f"  ({n}, {p})")
    print(f"wall_time_seconds: {result['elapsed_seconds']:.6f}")
    print(f"command: python -m chen_goldbach.check {args.bound}")
