#!/usr/bin/env python3
"""Brute-force oracle for Project Euler 185 (Number Mind).

For a given length L and a list of (guess_string, c_i) constraints, enumerate
ALL 10**L candidate digit strings and report exactly those for which, against
every guess, the number of positions where candidate[j] == guess[j] equals c_i.

This is the naive, obviously-correct oracle. It is only run on the small L=5
instance (10^5 candidates); the full L=16 main instance has 10^16 candidates
and is deliberately NOT enumerated here.
"""

import itertools
import sys


def brute_force(L, constraints):
    """Return the list of satisfying candidate digit strings (exact, ints->str).

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
    # ---- L=5 example from the problem statement ----
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
    print("=== L=5 instance ===")
    print(f"length L          : {L5}")
    print(f"number of guesses : {len(constraints5)}")
    print(f"candidates checked: {10**L5}")
    print(f"number of satisfying strings: {len(sols5)}")
    for s in sols5:
        print(f"  {s}")

    if len(sols5) == 1 and sols5[0] == "39542":
        print("CONFIRMED: the unique answer for L=5 is 39542.")
    else:
        print("NOT confirmed as expected unique 39542.")
        sys.exit(1)

    # ---- L=16 main instance ----
    L16 = 16
    constraints16 = [
        ("5616185650518293", 2),
        ("3847439647293047", 1),
        ("5855462940810587", 3),
        ("9742855507068353", 3),
        ("4296849643607543", 3),
        ("3174248439465858", 1),
        ("4513559094146117", 2),
        ("7890971548908067", 3),
        ("8157356344118483", 1),
        ("2615250744386899", 2),
        ("8690095851526254", 3),
        ("6375711915077050", 1),
        ("6913859173121360", 1),
        ("6442889055042768", 2),
        ("2321386104303845", 0),
        ("2326509471271448", 2),
        ("5251583379644322", 2),
        ("1748270476758276", 3),
        ("4895722652190306", 1),
        ("3041631117224635", 3),
        ("1841236454324589", 3),
        ("2659862637316867", 2),
    ]
    print()
    print("=== L=16 instance ===")
    print(f"length L          : {L16}")
    print(f"candidates would be: {10**16}  (10^16)")
    print("NOT attempted: full brute force on L=16 would require 10^16 "
          "enumerations and does not terminate quickly. Only L=5 is verified "
          "by brute force here.")


if __name__ == "__main__":
    main()
