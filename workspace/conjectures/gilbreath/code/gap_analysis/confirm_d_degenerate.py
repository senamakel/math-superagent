#!/usr/bin/env python3
"""Confirm two things about the (D) audit:
 1. The trailing (bottom) entry of every delta(q_n), n=2..N, is the landed 1
    (A_{n-1}[0] == 1), so `exclude_last=False` forces the {0,2}-suffix scan to
    stop at position len-1 immediately --> c_n == 0 for every n. That makes
    the exclude_last=False "0 violations" DEGENERATE, not a second route.
 2. The honest exclude_last=True measurement (the {0,2}-cycle length proper)
    is the one that has 1133 violations.
"""
import sys
from collections import Counter

def primes_up_to(n):
    if n < 2:
        return []
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = b'\x00' * (((n - i * i) // i) + 1)
    return [i for i in range(n + 1) if sieve[i]]

def build_diagonals(ps, N):
    prev = None
    diags = [None]
    for n in range(1, N + 1):
        qn = ps[n - 1]
        cur = [0] * n
        cur[0] = qn
        if prev is not None:
            for k in range(1, n):
                cur[k] = abs(cur[k - 1] - prev[k - 1])
        diags.append(cur)
        prev = cur
    return diags

def zero_two_suffix_length(vec, exclude_last=False):
    end = len(vec)
    if exclude_last:
        end -= 1
    i = end - 1
    while i >= 0 and vec[i] in (0, 2):
        i -= 1
    return end - 1 - i

def main():
    N = 10001
    ps = primes_up_to(200000)[:N]
    N = len(ps)
    diags = build_diagonals(ps, N)

    # trailing entry of each diagonal
    not_one = [n for n in range(2, N + 1) if diags[n][-1] != 1]
    print(f"diagonals n=2..{N} whose bottom entry != 1: {len(not_one)} "
          f"(first 10: {not_one[:10]})")

    # c with exclude_last=False: expected all zero (stop at trailing 1)
    c0 = [0] * (N + 1)
    for n in range(2, N + 1):
        c0[n] = zero_two_suffix_length(diags[n], exclude_last=False)
    nonzero = [n for n in range(2, N + 1) if c0[n] != 0]
    print(f"exclude_last=False: c_n nonzero at {len(nonzero)} positions -> "
          f"{'DEGENERATE (identically 0)' if len(nonzero)==0 else 'NOT degenerate'}")

    c1 = [0] * (N + 1)
    for n in range(2, N + 1):
        c1[n] = zero_two_suffix_length(diags[n], exclude_last=True)
    dist = Counter()
    for n in range(3, N + 1):
        dist[c1[n] - c1[n - 1]] += 1
    viol = sum(v for d, v in dist.items() if d < -1)
    print(f"exclude_last=True (0-2-cycle length): violations of c_n >= c_nm1-1: {viol}")
    print(f"  max c value: {max(c1[2:])}")

if __name__ == "__main__":
    main()
