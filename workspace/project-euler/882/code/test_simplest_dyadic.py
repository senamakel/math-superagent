#!/usr/bin/env python3
"""Validate simplest_dyadic.simplest_between against an independent birthday
oracle.

Independent route to "simplest dyadic strictly between a<b":
  birthday(x) for x = N + f (N>=0 integer, f in [0,1) dyadic, x >= 0):
      f == 0      -> birthday = N            (0 -> 0)
      f > 0       -> birthday = N + len(binary_digits(f)) + 1
  birthday(-x) = birthday(x).  (Sign-expansion length; see the worked
  derivation in this run's notes.)

Oracle: over all dyadics with birthday <= B that lie strictly in (a,b), return
the one with minimal birthday (ties impossible for strict dyadics).  Compare to
simplest_between on many random positive/negative/fractional intervals.
"""
import random
from fractions import Fraction
from toolkits.simplest_dyadic import simplest_between


def binary_digits(f):
    """Number of binary digits of dyadic f in (0,1), f=m/2^n with m<n."""
    k = 0
    while f.denominator > 1:
        f *= 2
        k += 1
    return k  # actually floor, but f dyadic terminates


def birthday(x):
    x = abs(x)
    if x == 0:
        return 0
    n = x.numerator // x.denominator          # integer part
    f = x - n
    if f == 0:
        return n
    return n + binary_digits(f) + 1


def dyadics_with_birthday(maxb):
    """All dyadics (as Fractions) with birthday <= maxb, including negatives.
    Enumerate generously: m/2^k with k <= maxb and |square| bounded.
    We generate via integer part and fractional digits directly instead."""
    out = set()
    out.add(Fraction(0))
    for b in range(1, maxb + 1):
        for n in range(0, b + 1):            # integer part 0..b
            # f with birthday(f) = b - n - 1 <= would-be, i.e. binary digits = b-n-1
            rem = b - n                       # birthday = n + digits + 1 => digits = b-n-1
            digits = rem - 1
            if digits < 0:
                if digits == -1:             # f == 0 (pure integer)
                    out.add(Fraction(n))
                continue
            for m in range(1, 2 ** digits):
                f = Fraction(m, 2 ** digits)
                if f < 1:
                    out.add(Fraction(n) + f)
    # negatives
    return out | {-x for x in out}


def birthday_oracle(a, b, maxb):
    """Simplex dyadic strictly in (a,b) with smallest birthday, by enumeration."""
    best = None
    best_b = None
    for x in dyadics_with_birthday(maxb):
        if a < x < b:
            bb = birthday(x)
            if best_b is None or bb < best_b:
                best_b = bb
                best = x
    return best


def main():
    random.seed(12345)
    pairs = []
    # fixed tricky cases
    for (a, b) in [(0,1),(1,2),(0,2),(Fraction(1,2),2),(-1,1),
                   (Fraction(1,4),Fraction(1,2)),(Fraction(1,4),1),
                   (Fraction(3,4),Fraction(7,4)),(-2,-1),(0,Fraction(1,8)),
                   (Fraction(5,2),3),(1,3)]:
        pairs.append((Fraction(a), Fraction(b)))
    # random dyadic pairs
    for _ in range(20000):
        d = random.randint(1, 6)
        x = Fraction(random.randint(0, 40), 2 ** random.randint(0, 4))
        y = Fraction(random.randint(0, 40), 2 ** random.randint(0, 4))
        a, b = (x, y) if x < y else (y, x)
        if a == b:
            continue
        pairs.append((a, b))

    bad = 0
    for a, b in pairs:
        got = simplest_between(a, b)
        want = birthday_oracle(a, b, 22)
        if want is None:
            # no dyadic with birthday<=22; fall back: just check interval incl
            # a known dyadic must exist since reals dense; increase bound once
            want = birthday_oracle(a, b, 30)
        if got != want:
            bad += 1
            if bad <= 10:
                print(f"MISMATCH simplest_between({a},{b})={got}, oracle={want}, "
                      f"birthdays got={birthday(got)} want={birthday(want) if want is not None else None}")
    print(f"checked {len(pairs)} intervals, mismatches = {bad}")
    return bad


if __name__ == "__main__":
    import sys
    sys.exit(1 if main() else 0)
