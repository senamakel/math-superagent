#!/usr/bin/env python3
"""Naive oracle for Project Euler 185 (Number Mind).

Enumerates every candidate sequence of the given digit length and keeps those
that match ALL the constraints: for each (guess, count), the candidate agrees
with the guess in exactly `count` positions. Exact integer arithmetic; purely a
correctness oracle, deliberately not optimised. The full 16-digit instance is
10^16 candidates and is NOT meant to be run here — that bound defeats exactly
this method. Use it on the small worked example(s) only.

Usage:
    python brute.py
runs the built-in 5-digit worked example and reports matching sequences and
how many there are.
"""

from itertools import product


def matching_sequences(guesses, length):
    """Return the list of candidate digit-strings matching all constraints.

    guesses: iterable of (guess_string, exact_position_count).
    length : number of digits in the secret sequence.
    """
    matches = []
    for digits in product("0123456789", repeat=length):
        cand = "".join(digits)
        ok = True
        for guess, need in guesses:
            same = sum(1 for g, c in zip(guess, cand) if g == c)
            if same != need:
                ok = False
                break
        if ok:
            matches.append(cand)
    return matches


def main():
    # Worked example from the statement: 5-digit secret.
    guesses = [
        ("90342", 2),
        ("70794", 0),
        ("39458", 2),
        ("34109", 1),
        ("51545", 2),
        ("12531", 1),
    ]
    length = 5
    print(f"length = {length}, {len(guesses)} guesses, exhaustive over 10^{length} candidates ...")
    matches = matching_sequences(guesses, length)
    print(f"matching sequences: {matches}")
    print(f"count = {len(matches)}")
    if len(matches) == 1:
        print(f"unique sequence = {matches[0]}")
    print("worked-example expected: ['39542'], count 1")


if __name__ == "__main__":
    main()
