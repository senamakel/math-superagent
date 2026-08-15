"""Verify the record-low recurrence for Project Euler 700.

Sequence: c_n = a*n mod m, with
    a = 1504170715041707
    m = 4503599627370517
Eulercoin = term strictly smaller than all previous terms (prefix minimum / record low).

The recurrence (from research/summaries/record-low-recurrence.md):
    n_{k+2} = ceil(c_{n_k} / c_{n_{k+1}}) * n_{k+1} - n_k
gives the indices of successive record lows, starting n_1 = 1.

This script has two independent checks:
  1. Brute force the prefix minima for the first N terms and confirm the
     recurrence-generated indices/values match for the first several Eulercoins.
  2. Reproduce the stated worked example: sum of first two Eulercoins
     = 1513083232796311.
"""
from math import ceil

A = 1504170715041707
M = 4503599627370517

from math import gcd as _gcd

def _check_hypotheses():
    """The recurrence and the 'sequence is a permutation' fact need gcd(A,M)=1
    and 0 < A < M. Confirm them so the claim's hypotheses truly hold here."""
    assert 0 < A < M, "need A < M"
    g = _gcd(A, M)
    print("gcd(A, M) =", g)
    assert g == 1, "recurrence/permutation needs gcd(A,M)=1"
    return g


def recurrence_eulercoins(limit_terms=None):
    """Generate Eulercoin values via the index recurrence.

    n_1 = 1, c_1 = A.
    n_2 = first n>1 with c_n < c_1 = A.
    Then n_{k+2} = ceil(c_{n_k}/c_{n_{k+1}})*n_{k+1} - n_k.
    """
    c1 = A
    # first record low after index 1: smallest n with a*n mod m < A.
    # This is not generally easy to find by scanning; but for the worked
    # check we know the second Eulercoin value from the statement.
    # Here we verify the recurrence given known successive coins.
    return None  # placeholder; real verification below


def brute_first_record_lows(num_coins):
    """Brute force: scan c_n = a*n mod m, record new prefix minima."""
    coins = []
    running_min = None
    n = 1
    c = A % M
    coins.append((n, c))
    running_min = c
    n = 2
    while len(coins) < num_coins:
        c = (A * n) % M
        if c < running_min:
            coins.append((n, c))
            running_min = c
        n += 1
    return coins


def recurrence_from_seed(coins):
    """Given the first two (n,val) record lows, extend via recurrence."""
    out = list(coins)
    while True:
        nk, ck = out[-2]
        nk1, ck1 = out[-1]
        if ck1 == 0:
            break
        alpha = ceil(ck / ck1)
        nk2 = alpha * nk1 - nk
        if nk2 <= nk1:
            break
        # value at index nk2 should equal the new record low
        ck2 = (A * nk2) % M
        out.append((nk2, ck2))
    return out


if __name__ == "__main__":
    # 1. Reproduce the worked example.
    first_coins = brute_first_record_lows(2)
    print("First two Eulercoins (brute):", first_coins)
    s = sum(c for _, c in first_coins)
    print("Sum of first two:", s)
    assert s == 1513083232796311, f"Worked example FAILED: {s}"
    print("Worked example sum MATCHES 1513083232796311\n")

    # 2. Cross-check: first two coins brute == recurrence seed.
    assert first_coins[0] == (1, A), first_coins[0]
    assert first_coins[1][1] == 8912517754604, first_coins[1]
    print("Second Eulercoin (brute) =", first_coins[1][1])
    print("Statement says 8912517754604")
    assert first_coins[1][1] == 8912517754604
    print("Second Eulercoin value MATCHES.\n")

    # 3. Verify recurrence: extend from the two known coins and compare
    #    against brute force for the next several Eulercoins.
    seed = first_coins[:2]
    rec = recurrence_from_seed(seed)
    brute = brute_first_record_lows(len(rec))
    print("Recurrence sequence (n, value):")
    for r in rec:
        print("   ", r)
    print("\nBrute sequence:")
    for b in brute:
        print("   ", b)
    match = rec == brute
    print("\nRecurrence == brute for", len(rec), "Eulercoins:", match)
    assert match, "Recurrence disagrees with brute force!"
    print("Recurrence verified against brute force.")
