"""Exact digit-counting helpers for Project Euler 156.

f(n, d) = total occurrences of digit d in the base-10 representation of all
integers 0..n inclusive.  The place-value identity below computes it in
O(number of digits of n) arithmetic operations, no enumeration.
"""


def f_place_value(n, d):
    """Total occurrences of digit d in the decimal strings of 0..n inclusive.

    O(log10 n) time, O(1) space, exact integer arithmetic.
    Standard place-value decomposition: for each decimal position with value
    `factor`, the count of digit d contributed by that position is
        high * factor                 if digit at position < d
        high * factor + low + 1       if digit at position == d
        (high + 1) * factor           if digit at position > d
    where high = n // (factor*10) and low = n % factor.  This is the classical
    "count occurrences of a digit in 1..n" identity; for d in 1..9 the integer
    0 contributes nothing, so f(n,d) equals the count over 1..n.

    Verified against the brute-force oracle code/brute.py: agrees with
    f_naive on the statement's table f(n,1) for n=0..12, on f(22,2)=6, and on
    every solution the oracle's 0..300000 running-total scan reported.
    """
    total = 0
    factor = 1
    while factor <= n:
        low = n % factor
        cur = (n // factor) % 10
        high = n // (factor * 10)
        if cur < d:
            total += high * factor
        elif cur == d:
            total += high * factor + low + 1
        else:
            total += (high + 1) * factor
        factor *= 10
    return total