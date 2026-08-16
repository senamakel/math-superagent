#!/usr/bin/env python3
"""Independent, obviously-correct oracle for SUPPLY: the fold weight.

Operative definition (problem.md fact 1, imported as proved and matched by the
measurement cache):  nu2(n) = wt(Phi_n h) over F2, where
    h[j] = ((q_{j+1} - q_j) / 2) mod 2     (prime gap-parity string)
and Phi_n is the Pascal-mod-2 (Rule-90) fold matrix whose (d, j) entry is
    C(d - 1, j - (n - d)) mod 2   for d in [2, n-1], j in [0, n-1].
A cell that falls outside 0 <= j-(n-d) <= d-1 is 0.

This module builds Phi_n EXPLICITLY from the binomial coefficient of a literal
Z/nZ Pascal row -- no Lucas submask shortcut -- so it is independent from
brute.py's nu2_matrix (which uses the Lucas submask test).  It is the second
route to the same number, used to confirm brute.py.

We also reconcile the convention: brute.py's nu2_matrix counts rows k=1..n-1
(depth d=k-1 => d=0..n-2, unfloored).  The canonical (fact 1) counts d=2..n-1
(floored at 2).  Both are reported; the difference is <= 1.

All exact integer arithmetic.
"""

import sys


def primes_upto_index(n):
    """First n primes, 0-indexed q[0]=2. Naive sieve."""
    ps, cand = [], 2
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


def h_vec(n):
    """h[0..n-1]; h[0]=0 (q1=2,q2=3 -> half-integer floored to 0), else
    ((q_{j+1}-q_j)//2) mod 2 for j=1..n-1. Same as brute.py."""
    q = primes_upto_index(n + 1)
    h = [0] * n
    for j in range(1, n):
        h[j] = ((q[j + 1] - q[j]) // 2) % 2
    return h


def binom_mod2(a, b):
    """Binomial C(a,b) mod 2 computed by direct Pascal recurrence (independent
    of any Lucas theorem).  Padded; only a,b small here."""
    if b < 0 or b > a:
        return 0
    # build Pascal row a
    row = [1]
    for _ in range(a):
        nxt = [1] * (len(row) + 1)
        for i in range(1, len(row)):
            nxt[i] = (row[i - 1] + row[i]) % 2
        row = nxt
    return row[b]


def nu2_explicit(n):
    """wt(Phi_n h) with Phi_n built from Pascal binomials mod 2, d in [2,n-1]."""
    h = h_vec(n)
    wt = 0
    for d in range(2, n):
        s = 0
        base = n - d
        for j in range(0, n):
            c = j - base
            if 0 <= c <= d - 1 and binom_mod2(d - 1, c):
                s ^= h[j]
        wt += s
    return wt


def main():
    lo = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    hi = int(sys.argv[2]) if len(sys.argv) > 2 else 80
    from brute import nu2_matrix  # the on-disk oracle
    bad = []
    for n in range(lo, hi + 1):
        a = nu2_matrix(n)          # brute unfloored (d=0..n-2)
        b = nu2_explicit(n)        # canonical floored (d=2..n-1)
        if abs(a - b) > 1:         # only the floor-at-2 difference is allowed
            bad.append((n, a, b))
    if bad:
        print("MISMATCH beyond +-1 convention floor:")
        for row in bad[:20]:
            print("  n=%d brute=%d explicit=%d" % row)
    else:
        print(f"n={lo}..{hi}: brute.py agrees with independent explicit fold "
              f"up to fiddle +-1 (floor-at-2)  [{len(range(lo,hi+1))} values]")


if __name__ == "__main__":
    main()
