#!/usr/bin/env python3
"""Direct-definition oracle for SUPPLY (problem.md), no linearisation.

Builds the literal absolute-difference triangle of the primes,
    A_0(i) = q_{i+1}                       (i >= 0)
    A_{k+1}(i) = | A_k(i) - A_k(i+1) |     (i >= 0)
extracts the right diagonal through column n,
    delta_k(n) = A_k(n - 1 - k),   k = 0 .. n-1
and reads it from its bottom end (k = n-1 down to k = 0) as the longest
unbroken run of cells whose value is 0 or 2 -- the maximal {0,2} suffix --
and counts the number of 2s in that run.

nu2(n) = number of 2s in the maximal {0,2} suffix of the diagonal.

This is the check that brute.py (which trusts the linearisation
nu2 = wt(Phi_n h) via Lucas) is faithful to the actual definition.
Exact integer arithmetic; O(n^2) time, O(n^2) space. Deliberately naive.

CONVENTION (problem.md): the suffix is floored at index 2 (the canonical
lib.rightdiag.cycle_and_nu2), i.e. we start scanning the run of {0,2} cells
from the bottom but the run's 2-count is taken over the segment whose lowest
index is at least 2. In practice we take the maximal suffix of the diagonal
(in bottom-up order) whose values are all in {0,2} and whose earliest
(deepest-origin) cell has index k >= 2, then count the 2s in it.
"""

import sys


def primes_upto_index(n):
    """First n primes, 0-indexed q[0]=2, q[1]=3, ...  Need up to q_{n}."""
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


def diagonal(n):
    """The right diagonal delta_k(n) = A_k(n-1-k) for k = 0..n-1, as a list
    indexed by k (k=0 is the top cell q_n, k=n-1 is the bottom cell)."""
    q = primes_upto_index(n)
    # build A_0 as a dict keyed by column: A_0(i) for i = 0..n-1
    row = {i: q[i] for i in range(n)}
    diag = [None] * n
    diag[0] = row[n - 1]           # A_0(n-1) = q_n
    for k in range(1, n):          # row k, keep columns 0..n-1-k
        new = {}
        for i in range(n - k):
            new[i] = abs(row[i] - row[i + 1])
        row = new
        diag[k] = row[n - 1 - k]   # A_k(n-1-k)
    return diag


def nu2_direct(n):
    """Number of 2s in the maximal {0,2} suffix of the diagonal of column n,
    floored at index 2."""
    diag = diagonal(n)
    # scan from the bottom (k = n-1) upward, collecting the run of {0,2} cells
    twos = 0
    k = n - 1
    while k >= 2 and diag[k] in (0, 2):
        if diag[k] == 2:
            twos += 1
        k -= 1
    return twos


def main():
    sizes = [int(a) for a in sys.argv[1:]] or [20, 50, 100]
    for n in sizes:
        v = nu2_direct(n)
        print(f"n={n}  nu2_direct={v}  nu2/n={v / n:.4f}")


if __name__ == "__main__":
    main()
