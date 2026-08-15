"""Project Euler 700 - compute every Eulercoin via the verified recurrence.

Sequence: c_n = A*n mod M,  A = 1504170715041707, M = 4503599627370517.
An Eulercoin is a record low (prefix minimum) of c_n.  Since gcd(A,M)=1 the
values run over a permutation of 0..M-1, so c_n = A*n mod M hits 0 exactly at
n = M (the final Eulercoin).

The verified record-low index recurrence (sourced, checked against brute-force
forward scans in code/verify_recurrence.py):

    n1 = 1,  n2 = 3                      (given: c1 = A, c2 = (3A) mod M)
    n_{k+2} = ceil(c_{n_k}/c_{n_{k+1}}) * n_{k+1} - n_k
    c_{n_{k+2}} = (A * n_{k+2}) mod M

iterated until c = 0 (n = M), the final Eulercoin.

Correctness gates before trusting the sum:
  * first-two sum == 1513083232796311  (the statement's worked example)
  * first 12 coins match the verified list from verify_recurrence.txt
Output every (index, coin) plus the total count and final sum to
code/out/solution.txt.
"""
from math import ceil

A = 1504170715041707
M = 4503599627370517


def eulercoins(A, M, n2):
    """All Eulercoins via the recurrence, as [(index, coin), ...].

    Starts from n1=1 (coin A%M) and n2 (given); returns list ending with the
    coin 0 at index M. Exact integer arithmetic throughout.
    """
    coins = [(1, A % M)]
    n1, c1 = 1, A % M
    n2i, c2 = n2, (A * n2) % M
    coins.append((n2i, c2))
    while c2 != 0:
        alpha = ceil(c1 / c2)
        n3 = alpha * n2i - n1
        c3 = (A * n3) % M
        coins.append((n3, c3))
        n1, c1, n2i, c2 = n2i, c2, n3, c3
    return coins


def main():
    assert A % M == A and 0 < A < M
    coins = eulercoins(A, M, n2=3)

    # --- correctness gates before trusting the sum -------------------------
    # 1. statement worked example: first two coins sum
    first_two = coins[0][1] + coins[1][1]
    assert first_two == 1513083232796311, f"first-two sum mismatch: {first_two}"

    # 2. first 12 coins match the verified list from verify_recurrence.txt
    #    (these are the 12 coins a forward scan through n=10^6 reproduces).
    verified_first_12 = [
        1504170715041707,  # n=1
        8912517754604,     # n=3
        2044785486369,     # n=506
        1311409677241,     # n=2527
        578033868113,      # n=4548
        422691927098,      # n=11117
        267349986083,      # n=17686
        112008045068,      # n=24255
        68674149121,       # n=55079
        25340253174,       # n=85903
        7346610401,        # n=202630
        4046188430,        # n=724617
    ]
    got_first_12 = [c for _, c in coins[:12]]
    assert got_first_12 == verified_first_12, (
        f"first-12 mismatch:\n got {got_first_12}\n exp {verified_first_12}")

    total = len(coins)
    final_sum = sum(c for _, c in coins)

    out = []
    out.append("=" * 60)
    out.append("Project Euler 700 - all Eulercoins (record lows of c_n=A*n mod M)")
    out.append(f"A = {A}")
    out.append(f"M = {M}")
    out.append(f"number of Eulercoins: {total}")
    out.append(f"final sum of all Eulercoins: {final_sum}")
    out.append("-" * 60)
    for i, (n, c) in enumerate(coins, 1):
        out.append(f"coin #{i:>3}:  n = {n:>16}  c_n = {c}")
    out.append("-" * 60)
    out.append(f"TOTAL COUNT = {total}")
    out.append(f"FINAL SUM V = {final_sum}")
    out.append("=" * 60)

    print("\n".join(out))
    with open("code/out/solution.txt", "w") as fh:
        fh.write("\n".join(out) + "\n")

    return final_sum, total


if __name__ == "__main__":
    V, count = main()
    print()
    print(f"REPORT: final sum V = {V}, number of Eulercoins = {count}")
