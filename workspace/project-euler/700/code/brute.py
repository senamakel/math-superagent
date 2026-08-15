"""Naive oracle for Project Euler 700 "Eulercoin".

Sequence: c_n = A * n mod M,  n = 1, 2, 3, ...
    A = 1504170715041707
    M = 4503599627370517
An Eulercoin is a term strictly smaller than every previously found Eulercoin
(the running-prefix-minimum sequence, in order of occurrence).

Obviously correct: one forward pass over c_n, one modular multiply per step,
record a new Eulercoin whenever c_n < current running minimum. Exact integer
arithmetic throughout. No cleverness — this is the oracle that later,
efficient methods are checked against.

Worked examples this must reproduce (from the statement):
    a_1 = 1504170715041707                  (1st Eulercoin, at n = 1)
    a_2 = 3008341430083414 = 2*A            (not a coin)
    a_3 = 8912517754604                     (2nd Eulercoin, at n = 3)
    sum of first 2 Eulercoins = 1513083232796311
"""
import sys
from math import gcd

A = 1504170715041707
M = 4503599627370517

# Default scan limit: a few hundred thousand terms. Far too small to reach the
# full answer (the sequence only terminates when the running minimum reaches
# 1, which happens only at astronomically large n), but large enough that the
# forward scan stabilizes: past the last Eulercoin found in range no new coin
# appears for the remainder, which is what the oracle can certify here.
DEFAULT_LIMIT = 300000


def scan_eulercoins(limit_terms):
    """Scan c_n = (A*n) mod M forward for limit_terms terms.

    Returns (coins, last_n_new_coin, total_terms).
        coins          : list of (n, value) Eulercoins in order of occurrence
        last_n_new_coin: index of the last term that produced a new Eulercoin
                         (or None if no coin was ever found)
        total_terms    : the scan length actually run
    """
    coins = []
    running_min = None
    last_n_new_coin = None
    for n in range(1, limit_terms + 1):
        c_n = (A * n) % M
        if running_min is None or c_n < running_min:
            coins.append((n, c_n))
            running_min = c_n
            last_n_new_coin = n
    return coins, last_n_new_coin, limit_terms


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_LIMIT
    assert limit >= 3

    g = gcd(A, M)
    assert 0 < A < M and g == 1

    print("Eulercoin brute-force oracle")
    print("  A =", A)
    print("  M =", M)
    print("  gcd(A, M) =", g)
    print("  scan limit (terms) =", limit)

    # --- Worked-example reproduction (small, independent slice) -----------
    # Exact terms the statement quotes, computed bare so any definitional
    # mistake shows up here first.
    a1 = A % M                 # n = 1
    a2 = (2 * A) % M           # n = 2
    a3 = (3 * A) % M           # n = 3
    print("\nWorked-example terms (bare modular arithmetic):")
    print("  a_1 =", a1)
    print("  a_2 =", a2)
    print("  a_3 =", a3)
    assert a1 == A, "a_1 should equal A"
    assert a2 == 2 * A, "a_2 should equal 2A (< M)"
    assert a3 == 8912517754604, "a_3 should be 8912517754604"

    # --- Full forward scan ------------------------------------------------
    coins, last_new, terms = scan_eulercoins(limit)
    first_two_sum = coins[0][1] + coins[1][1]
    print("\nTotal Eulercoins found within scan limit:", len(coins))
    if coins:
        print("Sum of all Eulercoins found within scan limit:",
              sum(v for _, v in coins))
        print("Last term (within scan) at which a new Eulercoin appeared: n =",
              last_new)
        print("From n =", last_new + 1, "to n =", terms,
              "no further Eulercoin appeared.")

    print("\nFirst several Eulercoins (n, value):")
    for n, v in coins[:10]:
        print("   n =", n, " value =", v)
    if len(coins) > 10:
        print("   ... (%d more)" % (len(coins) - 10))

    # --- Worked-example sum check -----------------------------------------
    print("\nSum of first 2 Eulercoins =", first_two_sum)
    assert first_two_sum == 1513083232796311, \
        f"Worked example sum FAILED: {first_two_sum}"
    print("Worked example sum MATCHES 1513083232796311")

    # Structure assertions implied by the statement.
    assert coins[0] == (1, A), coins[0]
    assert coins[1][1] == 8912517754604
    print("\nAll worked-example assertions passed.")


if __name__ == "__main__":
    main()
