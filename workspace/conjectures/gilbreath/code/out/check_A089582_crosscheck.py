#!/usr/bin/env python3
"""Cross-check the run's own A_k(1) second-entry data against OEIS A089582,
the catalogue sequence "From Gilbreath's conjecture" (d_k(2) for k > 1).

A089582 first 105 terms (copied from research/sources/oeis-A089582-second-entry-sequence.full.md):
2,0,2,2,2,2,2,2,0,0,0,0,0,0,2,2,0,2,2,0,0,2,2,2,0,0,0,2,2,0,2,0,0,0,2,2,
0,0,0,0,0,0,2,2,0,2,2,0,2,0,0,2,0,2,2,2,2,0,0,0,0,0,0,2,0,0,2,2,0,0,2,2,
0,2,0,0,0,0,0,2,0,2,2,2,2,2,0,0,2,2,0,0,2,2,0,0,0,0,2,2,2,2,0,0,0

The run's generator (code/lib/gilbreath.py) computes the same A_k(1).
This program recomputes A_0..A_105 second entries from the primes with the
oracle generator and compares term-by-term with the catalogue list.
"""
import sys

A089582 = [
2,0,2,2,2,2,2,2,0,0,0,0,0,0,2,2,0,2,2,0,0,2,2,2,0,0,0,2,2,0,2,0,0,0,2,2,
0,0,0,0,0,0,2,2,0,2,2,0,2,0,0,2,0,2,2,2,2,0,0,0,0,0,0,2,0,0,2,2,0,0,2,2,
0,2,0,0,0,0,0,2,0,2,2,2,2,2,0,0,2,2,0,0,2,2,0,0,0,0,2,2,2,2,0,0,0]

def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            sieve[p*p::p] = b'\x00' * (((n - p*p) // p) + 1)
    return [i for i in range(n + 1) if sieve[i]]

def second_entries(depth):
    """A_k(1) for k = 1..depth, exact integer arithmetic, one row at a time."""
    # need depth + 2 primes to have rows of length >= 2 down to depth
    # actually we need primes[0..depth+1] for a triangle of depth rows with
    # width >= 2 at the last row: row k has width W-k, needs W >= depth+2.
    W = depth + 2
    # generate primes up to a bound with at least W primes
    import math
    n = 2
    while True:
        ps = primes_upto(n)
        if len(ps) >= W:
            break
        n *= 2
    row = ps[:W]
    out = []
    for _ in range(depth):
        row = [abs(row[i] - row[i+1]) for i in range(len(row) - 1)]
        out.append(row[1])
    return out

def main():
    depth = len(A089582)  # 105
    got = second_entries(depth)
    mismatches = [(i+1, got[i], A089582[i]) for i in range(depth) if got[i] != A089582[i]]
    print(f"checked {depth} terms of A_k(1) against OEIS A089582")
    print(f"mismatches: {len(mismatches)}")
    for k, g, a in mismatches[:10]:
        print(f"  k={k}: run={g} catalogue={a}")
    if not mismatches:
        print("MATCH: the run's A_k(1) sequence agrees with the OEIS catalogue A089582 for k=1..105.")
    # sanity: exactly the run's published small values
    print("first 10:", got[:10])  # expect 2,0,2,2,2,2,2,2,0,0
    ok10 = got[:10] == [2,0,2,2,2,2,2,2,0,0]
    print("first-10 matches problem.md A_1..A_5 second entries:", ok10)
    return 0 if not mismatches else 1

if __name__ == "__main__":
    sys.exit(main())