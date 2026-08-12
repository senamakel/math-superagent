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
