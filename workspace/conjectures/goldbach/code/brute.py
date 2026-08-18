#!/usr/bin/env python3
"""Demonstration script: the naive Goldbach oracle against the worked
examples of problem.md.

The oracle itself now lives in code/lib/goldbach.py (one source of truth):
is_prime, goldbach_partitions, satisfies_goldbach, verify_partitions,
HAND_COUNTS_4_50.  This script imports it and runs it on the three worked
examples the problem statement fixes, plus the hand-counted sanity sweep
over even n in [4, 50].

Statement it bears on (problem.md / GOAL.md, formalised in
code/lean/Lib/Statement.lean, witnessed in code/lean/Lib/GoldbachOracle.lean):
every even n > 2 is a sum of two primes, p + q = n, p, q prime.

Deliberately naive and deliberately small: the oracle is the reference the
fast method is checked against; it is never pointed at the literature's
verification bound (~4e18), which is chosen to defeat exactly this method.

Complexity per query: O(n * sqrt(n)) time, O(#partitions) space; n <= 50 here.
"""

from lib.goldbach import (
    HAND_COUNTS_4_50,
    goldbach_partitions,
    is_prime,
    satisfies_goldbach,
    verify_partitions,
)


def main() -> None:
    ok = True

    print("=== Worked examples from problem.md ===")

    # Example 1: "4 = 2 + 2 is a valid representation" (p, q need not be distinct)
    got = goldbach_partitions(4)
    agree1 = got == [(2, 2)] and satisfies_goldbach(4)
    print("example 1: '4 = 2 + 2 is a valid representation'")
    print(f"  partitions(4) = {got}")
    print(f"  satisfies_goldbach(4) = {satisfies_goldbach(4)}")
    print(f"  agree? {agree1}")
    ok = ok and agree1

    # Example 2: "n = 2 has no representation (1 is not prime) and is
    # excluded by hypothesis, not a counterexample"
    got = goldbach_partitions(2)
    agree2 = got == [] and not satisfies_goldbach(2)
    print("example 2: 'n = 2 has no representation (1 is not prime)'")
    print(f"  partitions(2) = {got}")
    print(f"  satisfies_goldbach(2) = {satisfies_goldbach(2)} "
          f"(excluded by n > 2, not a counterexample)")
    print(f"  agree? {agree2}")
    ok = ok and agree2

    # Example 3: "1 is not prime"  (the reason 2 = 1 + 1 fails)
    agree3 = is_prime(1) is False
    print("example 3: '1 is not prime'")
    print(f"  is_prime(1) = {is_prime(1)}")
    print(f"  agree? {agree3}")
    ok = ok and agree3

    print()
    print("=== Hand-checked sanity sweep (same scale as the examples) ===")
    # Hand-counted partition numbers for even n in [4, 50]; the oracle must
    # reproduce every one.  Counts verified by hand above the code.
    sweep_ok = True
    for n, expected in HAND_COUNTS_4_50.items():
        assert verify_partitions(n, expected), f"n={n}"
        sweep_ok = sweep_ok and satisfies_goldbach(n)
    print(f"  every even n in [4, 50] satisfies Goldbach? {sweep_ok}")
    print(f"  hand-counted partition numbers 4..50 all reproduced? {sweep_ok}")
    ok = ok and sweep_ok

    print()
    print(f"ALL WORKED EXAMPLES MATCHED: {ok}")
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
