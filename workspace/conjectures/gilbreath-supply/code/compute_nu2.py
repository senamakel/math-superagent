#!/usr/bin/env python3
"""Extract the integer sequences for pattern analysis.

1. nu2(n) for n = 1..N: the central SUPPLY quantity, exact by the literal
   definition (maximal {0,2} suffix of the right diagonal through column n,
   counted 2s), streaming one row at a time per column.
2. h[j] = ((q_{j+1} - q_j)//2) mod 2 : the prime gap-parity bit string.

This is the raw material for analyze_sequence / find_linear_recurrence /
oeis_lookup. Exact integer arithmetic throughout.
"""

import sys


def primes_upto_index(n):
    ps = []
    cand = 2
    while len(ps) < n:
        ok = True
        for p in ps:
            if p * p > cand:
                break
            if cand % p == 0:
                ok = False
                break
        if ok:
            ps.append(cand)
        cand += 1
    return ps


def nu2(n, ps=None):
    if n < 1:
        return 0
    row = ps if ps is not None else primes_upto_index(n)
    diag = [row[n - 1]]
    while len(row) > 1:
        row = [abs(row[i] - row[i + 1]) for i in range(len(row) - 1)]
        diag.append(row[-1])
    count2 = 0
    for k in range(n - 1, -1, -1):
        v = diag[k]
        if v == 0 or v == 2:
            if v == 2:
                count2 += 1
        else:
            break
    return count2


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    # primes up to the largest needed: q_N
    ps = primes_upto_index(N)
    # h[j] = ((q_{j+1} - q_j)//2) mod 2, j = 0..N-2
    h = [((ps[j + 1] - ps[j]) // 2) % 2 for j in range(N - 1)]
    out = []
    for n in range(1, N + 1):
        out.append(nu2(n, ps[:n]))
    print("nu2:")
    print(out)
    print("h (prime gap parity, j=0..%d):" % (N - 2))
    print(h)
    # ratios for sanity
    print("nu2/n ratios at selected n:")
    for n in [50, 100, 200, 300, 400]:
        if n <= N:
            print(f"  n={n}: {out[n-1]}/{n} = {out[n-1]/n:.4f}")


if __name__ == "__main__":
    main()
