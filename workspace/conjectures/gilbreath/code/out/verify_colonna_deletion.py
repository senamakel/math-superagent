#!/usr/bin/env python3
"""Independent verification of claim colonna-deletion-left-edge-failure.

Colonna 2025-26 record-page footnote (asserted): removing one prime (7, 5, or 11)
from the prime list gives a 2-then-odds sequence with gaps <= 6 (<=4 for delete-5)
whose left edge fails. Explicit example: (2,3,5,11,13,17,19) gaps (1,2,6,2,4,2).

We verify: build each 2-then-odds sequence by deleting one prime from the real
primes, run the absolute-difference triangle exactly, and check whether the
second entry A_k(1) stays in {0,2} (the conjecture's equivalent form) for the
first D rows. The claim is that the left edge FAILS: some A_k(1) >= 4 (so
A_{k+1}(0) != 1).
"""
import json, sys

def sieve(n):
    bs = bytearray(b'\x01') * (n + 1)
    bs[0:2] = b'\x00\x00'
    for i in range(2, int(n**0.5) + 1):
        if bs[i]:
            bs[i*i::i] = b'\x00' * (((n - i*i)//i) + 1)
    return [i for i in range(n+1) if bs[i]]

def triangle(seq, D):
    """row 0 = seq; return list of rows A_0..A_D."""
    rows = [seq]
    cur = seq
    for _ in range(D):
        nxt = [abs(cur[i] - cur[i+1]) for i in range(len(cur) - 1)]
        rows.append(nxt)
        cur = nxt
    return rows

def check(seq, D, label):
    rows = triangle(seq, D)
    fail_row = None
    for k in range(1, D+1):
        e = rows[k][1]
        if e not in (0, 2):
            fail_row = k
            break
    # gaps of A_1 (consecutive differences of the original 2-then-odds seq)
    gaps = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    return dict(seq=seq[:20], gaps=gaps, fail_row=fail_row,
                A1=rows[1][:10], max_second=max(rows[k][1] for k in range(1, D+1)))

def main():
    D = 30
    primes = sieve(200)
    results = {}
    for victim in (5, 7, 11):
        seq = [p for p in primes if p != victim][:20]
        results[victim] = check(seq, D, f"delete-{victim}")
    print(json.dumps(results, indent=2))
    # verdict
    all_fail = all(r['fail_row'] is not None for r in results.values())
    print("VERDICT: all three deletions have A_k(1) escape {0,2} within",
          D, "rows:", all_fail)
    for v, r in results.items():
        print(f"  delete-{v}: first fail row {r['fail_row']}, gaps(max {max(r['gaps'])}) {r['gaps']}")

main()
