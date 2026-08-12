#!/usr/bin/env python3
"""Naive oracle for Project Euler 185 (Number Mind).

Given a secret sequence of digits and a set of guesses each paired with an
integer "correct" count (the number of positions at which the guess matches
the secret), find the unique secret string that satisfies all constraints.

This oracle is intentionally O(10^L * n) in the worst case (enumerating every
string of length L). It exists only to pin down the definition against the
statement's worked examples and to check the efficient solver on small sizes.
Do NOT point it at the 16-digit case (10^16 strings): the bound is chosen to
defeat exactly this method.
"""

from itertools import product


def parse_guesses(text):
    """Parse the statement block into a list of (string, count).

    Accepts lines like "90342 ;2" or "90342;2" or "90342 : 2".
    """
    guesses = []
    for raw_line in text.strip().splitlines():
        line = raw_line.strip()
        if not line:
            continue
        # split on the ; (may have surrounding spaces)
        if ";" in line:
            s, c = line.split(";", 1)
        else:
            raise ValueError(f"Cannot parse line: {line!r}")
        s = s.strip()
        c = int(c.strip())
        if not s.isdigit():
            raise ValueError(f"Guess is not a digit string: {s!r}")
        guesses.append((s, c))
    return guesses


def matches(secret, guess, count):
    """True iff secret and guess agree in exactly `count` positions."""
    return sum(a == b for a, b in zip(secret, guess)) == count


def solve(guesses):
    """Return sorted list of all secret strings satisfying every constraint."""
    length = len(guesses[0][0])
    # sanity: all guesses same length
    assert all(len(g) == length for g, _ in guesses)
    results = []
    for tup in product("0123456789", repeat=length):
        cand = "".join(tup)
        if all(matches(cand, g, c) for g, c in guesses):
            results.append(cand)
    return results


EXAMPLE = """
90342 ;2
70794 ;0
39458 ;2
34109 ;1
51545 ;2
12531 ;1
"""

# The 22-guess, 16-digit instance from problem.md. Embedded as data so the
# oracle's definition of the problem is pinned to the full statement. This is
# NOT solved by brute.py — 10^16 strings is the bound that defeats this method.
SIXTEEN = """
5616185650518293 ;2
3847439647293047 ;1
5855462940810587 ;3
9742855507068353 ;3
4296849643607543 ;3
3174248439465858 ;1
4513559094146117 ;2
7890971548908067 ;3
8157356344118483 ;1
2615250744386899 ;2
8690095851526254 ;3
6375711915077050 ;1
6913859173121360 ;1
6442889055042768 ;2
2321386104303845 ;0
2326509471271448 ;2
5251583379644322 ;2
1748270476758276 ;3
4895722652190306 ;1
3041631117224635 ;3
1841236454324589 ;3
2659862637316867 ;2
"""


def _selftest():
    """Check the 'correct count' semantics against the statement's inline
    example: sequence 1234, guess 2036 -> 1 correct digit."""
    assert matches("1234", "2036", 1), "inline example not reproduced"
    assert not matches("1234", "2036", 0)
    assert not matches("1234", "2036", 2)
    # a digit right but in the wrong place must not count
    assert matches("1234", "4321", 0)  # all four wrong-position, zero right


if __name__ == "__main__":
    _selftest()
    guesses = parse_guesses(EXAMPLE)
    print("Guesses (string, count):")
    for g, c in guesses:
        print(f"  {g} ;{c}")
    sols = solve(guesses)
    print(f"\nNumber of satisfying 5-digit secrets: {len(sols)}")
    for s in sols:
        print(f"  {s}")
    expected = "39542"
    print("\nStatement's claimed answer:", expected)
    print("Reproduced:", expected in sols)
