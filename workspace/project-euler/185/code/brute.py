#!/usr/bin/env python3
"""Naive brute-force oracle for Project Euler 185 (Number Mind).

For a given length L and a list of (guess_string, c_i) constraints, enumerate
ALL 10**L candidate digit strings (itertools.product over digits) and report
exactly those for which, against every guess, the number of positions where
candidate[j] == guess[j] equals c_i. This is the obvious-correctness oracle.

Run ONLY on the L=5 worked example (10^5 candidates). The L=16 main instance
has 10^16 candidates and is deliberately NOT enumerated (that is impossible by
brute force).
"""

import itertools
import sys


def brute_force(L, constraints):
    """Return the list of satisfying candidate digit strings (str).

    constraints: iterable of (guess_string, c_i).
    """
    matches = []
    for digits in itertools.product("0123456789", repeat=L):
        cand = "".join(digits)
        ok = True
        for guess, c in constraints:
            hit = sum(1 for j in range(L) if cand[j] == guess[j])
            if hit != c:
                ok = False
                break
        if ok:
            matches.append(cand)
    return matches


def main():
    # ---- L=5 worked example from the problem statement ----
    L5 = 5
    constraints5 = [
        ("90342", 2),
        ("70794", 0),
        ("39458", 2),
        ("34109", 1),
        ("51545", 2),
        ("12531", 1),
    ]

    sols5 = brute_force(L5, constraints5)
    print("=== L=5 instance (brute force over all 10^5 strings) ===")
    print(f"length L          : {L5}")
    print(f"number of guesses : {len(constraints5)}")
    print(f"candidates checked: {10**L5}")
    print(f"number of satisfying strings: {len(sols5)}")
    for s in sols5:
        print(f"  {s}")

    if len(sols5) == 1 and sols5[0] == "39542":
        print("CONFIRMED: the unique answer for L=5 is 39542.")
        print("(Uniqueness: exactly 1 of the 100000 candidate strings matched "
              "all six counts.)")
        return 0
    else:
        print("NOT confirmed as expected unique 39542.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
