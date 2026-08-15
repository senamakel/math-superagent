#!/usr/bin/env python3
"""
Separate two claims that reduction_audit.py's (D) conflates:
  1. ROW-DIRECTION block lemma (PROVED in this run): if row A_k has a leading
     {0,2} block of length b_k, then b_{k+1} >= b_k - 1  (erosion at most 1
     per row step).  This is the run's step law.
  2. DIAGONAL-COORDINATE claim (audit's (D)): the 0-2 SUFFIX length c_n of the
     anti-diagonal delta(q_n) must satisfy c_n >= c_{n-1} - 1.

We verify (1) directly on row block lengths, and measure (2), so we can say
exactly which one holds and which one is refuted.
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

def leading_block_len(row):
    """Length of maximal prefix of row (from index 1) all in {0,2}
    (excludes the leading entry at index 0)."""
    n = 0
    for v in row[1:]:
        if v in (0, 2):
            n += 1
        else:
            break
    return n

def build_full_triangle(ps, depth):
    rows = [list(ps[:depth + 1])]
    for k in range(depth):
        r = rows[-1]
        rows.append([abs(r[i] - r[i + 1]) for i in range(len(r) - 1)])
    return rows

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

    # ---- claim 1: row-direction block lemma b_{k+1} >= b_k - 1 ----
    # rows A_0..A_{200} from first 201 primes (need depth 200)
    rows = build_full_triangle(ps, 200)
    b = [leading_block_len(rows[k]) for k in range(len(rows))]
    row_erosion_viol = 0
    for k in range(1, min(len(b), 200)):  # compare consecutive rows
        if b[k] < b[k - 1] - 1:
            row_erosion_viol += 1
    print(f"[claim 1] row block lengths over rows 0..{len(b)-1}:")
    print(f"   b[0..20] = {b[:21]}")
    print(f"   row-direction erosion violations b_k < b_{{k-1}}-1: {row_erosion_viol}")
    print(f"   (block lemma PROVED in this run; expected 0)")

    # ---- claim 2: diagonal-0-2-suffix c_n >= c_{n-1} - 1 ----
    diags = build_diagonals(ps, N)
    c = [0] * (N + 1)
    for n in range(2, N + 1):
        c[n] = zero_two_suffix_length(diags[n], exclude_last=True)
    d2_viol = 0
    dist = Counter()
    for n in range(3, N + 1):
        d = c[n] - c[n - 1]
        dist[d] += 1
        if d < -1:
            d2_viol += 1
    print(f"\n[claim 2] diagonal 0-2 suffix c_n (exclude_last=True):")
    print(f"   violations c_n < c_{{n-1}}-1: {d2_viol} over {N-2} extensions")
    # are the rows and the diagonal measuring the same thing?
    # c_n for the bottom of the triangle vs row block of A_{n-1}:
    # delta(q_n)[-1] = A_{n-1}[0] = 1; the suffix of delta(q_n) near the
    # bottom corresponds to EARLY COLUMNS of late rows, not to one row's block.
    # Show explicitly that c_n tracks something transversal to b_k.

    # sensitivity: how many of the claim-2 violations would survive a
    # different convention?  measure with exclude_last=False.
    c2 = [0] * (N + 1)
    for n in range(2, N + 1):
        c2[n] = zero_two_suffix_length(diags[n], exclude_last=False)
    d2_viol2 = 0
    for n in range(3, N + 1):
        if c2[n] < c2[n - 1] - 1:
            d2_viol2 += 1
    print(f"[claim 2 sensitive] violations with exclude_last=False: {d2_viol2}")

    # The bottom entry of every delta(q_n) that ends a successful prefix is 1,
    # so excluding it (the {0,2}-cycle vs the landed 1) is the intended reading.
    # Report both so the reader sees the result is not convention-dependent.

if __name__ == "__main__":
    main()
