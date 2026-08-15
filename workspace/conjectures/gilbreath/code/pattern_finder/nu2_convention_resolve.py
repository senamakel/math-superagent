#!/usr/bin/env python3
"""Resolve which nu2 convention matches Granville's supply quantity.

Two implementations exist in the run and they disagree in magnitude:
  - gap_parity style:  window tail = d[2:-1], walk from end while in {0,2} with i>0
  - incremental cyc:   window body = diag[:-1], walk from end while in {0,2} with i>2

Compute both on the SAME diagonal through the same q and tabulate, so the
discrepancy source (window + floor) is pinned down exactly.  Also recompute the
literal Granville definition: nu2 = #{c_s = 2 : c_s in the maximal {0,2} suffix
of the diagonal eps}, where eps is the maximal {0,2} suffix of the diagonal.
"""
from lib.gilbreath import primes_up_to

P = primes_up_to(200_000)


def diag_through(n):
    """delta(q_n) = [A_0[n], A_1[n-1], ..., A_n[0]] (0-indexed q list)."""
    # build via incremental recurrence
    D = [P[0]]                      # delta(q_1)
    for i in range(2, n + 1):
        newD = [0]*i
        newD[0] = P[i-1]
        for k in range(1, i):
            newD[k] = abs(newD[k-1] - D[k-1])
        D = newD
    return D


def cyc_floor2(diag):
    body = diag[:-1]
    i = len(body)
    while i > 2 and body[i-1] in (0, 2):
        i -= 1
    return body[i:].count(2)


def gapparity_floor0(diag):
    tail = diag[2:-1]
    i = len(tail)
    while i > 0 and tail[i-1] in (0, 2):
        i -= 1
    return tail[i:].count(2)


def literal_suffix(diag):
    """maximal {0,2} suffix of the whole diagonal; count 2s."""
    i = len(diag)
    while i > 0 and diag[i-1] in (0, 2):
        i -= 1
    return diag[i:].count(2)


print("n  len_diag  floor2(d[0:-1])  floor0(d[2:-1])  literal(d[0:])")
for n in [50, 100, 200, 400, 500]:
    d = diag_through(n)
    print("%-4d %-8d %-16d %-16d %-15d" % (
        n, len(d), cyc_floor2(d), gapparity_floor0(d), literal_suffix(d)))
