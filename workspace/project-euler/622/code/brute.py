#!/usr/bin/env python3
"""
Naive brute-force oracle for PE622 (out-faro shuffle restoration).

This is deliberately primitive: it models the deck as a list and applies one
perfect out-faro shuffle at a time by directly interleaving, then counts how
many shuffles it takes to return to the identity.  No order-formula, no
modular arithmetic — just iteration of the permutation.  It exists to
independently confirm that s(n) computed by direct simulation matches the
ord_{n-1}(2) formula the reference library uses.

out-shuffle definition (even deck size n, split in half):
  deck = [a0, a1, ..., a_{h-1}, b0, b1, ..., b_{h-1}]   (h = n/2)
  after one shuffle:  [a0, b0, a1, b1, ..., a_{h-1}, b_{h-1}]
so the top card (a0) and the bottom card (b_{h-1}) stay fixed, and the top
card of the right half (b0) comes right after the top card of the left half.
"""


def out_shuffle(deck):
    """One out-faro shuffle of an even-length deck."""
    n = len(deck)
    assert n % 2 == 0
    half = n // 2
    left = deck[:half]
    right = deck[half:]
    result = []
    for i in range(half):
        result.append(left[i])
        result.append(right[i])
    return result


def s(n):
    """Number of out-faro shuffles needed to restore a deck of even size n."""
    identity = list(range(n))
    deck = identity[:]
    count = 0
    while True:
        deck = out_shuffle(deck)
        count += 1
        if deck == identity:
            return count


def main():
    # Worked examples from the problem statement.
    s52 = s(52)
    s86 = s(86)
    assert s52 == 8, s52
    assert s86 == 8, s86

    # Sum of all even n < 500 with s(n) == 8.
    total = 0
    members = []
    for n in range(2, 500, 2):
        if s(n) == 8:
            total += n
            members.append(n)

    assert total == 412, total
    print("s(52) =", s52)
    print("s(86) =", s86)
    print("even n < 500 with s(n)=8:", members)
    print("sum of those n =", total)
    print("All three assertions passed (8, 8, 412).")
    print("Brute-force direct-iteration oracle agrees with ord_{n-1}(2) formula.")


if __name__ == "__main__":
    main()
