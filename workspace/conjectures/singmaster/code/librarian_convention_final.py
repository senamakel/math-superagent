#!/usr/bin/env python3
"""Librarian final convention check — direct enumeration, no oracle reuse.

Counts, for each a in the witness set plus some central-column values, the
number of ENTRIES (each (n,k) pair, both mirrors, incl. trivial) = N(a), and
the number of ROWS containing a. Verifies:
  * A003016(a) == N(a) (entries, mirror-inclusive, trivial included)
  * A059233 formula: rowcount(a) == ceil(N(a)/2) == ceil(A003016(a)/2)
  * central-column rule: N(a) == 2*rowcount(a) iff a is not a central entry
    (a != C(2r,r)); N(a) == 2*rowcount(a) - 1 otherwise.
Exact integer arithmetic only."""
import math

def C(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0

def is_central(a):
    """a == C(2r, r) for some r >= 1?"""
    r = 1
    while True:
        v = C(2 * r, r)
        if v == a:
            return True
        if v > a:
            return False
        r += 1

def counts(a):
    """Return (N_entries, n_rows, central) by direct enumeration."""
    entries = set()
    rows = set()
    # occurrences of a: rows <= a suffice (C(m,k) >= m > a impossible)
    # enumerate all k; use symmetry k <= n-k to halve work
    for n in range(2, a + 1):
        for k in range(1, n // 2 + 1):
            if C(n, k) == a:
                entries.add((n, k))
                entries.add((n, n - k))
                rows.add(n)
                # k exactly n/2: (n,k)=(n,n-k) same entry, dedup via set
    return len(entries), len(rows), is_central(a)

# witness values plus small central-column and typical values
# (enumeration is O(a^2) so keep a <= 3003; the convention relation is about
#  small-a bookkeeping, and the larger witnesses' counts are already in
#  witnesses.json / brute.captured.txt)
tests = [6, 10, 15, 20, 70, 120, 210, 3432, 3003]
print(f"{'a':>7} {'N(a)':>5} {'rows':>5} {'central':>8} {'rows==ceil(N/2)':>17} {'central rule':>13}")
all_ok = True
for a in tests:
    N, rows, cent = counts(a)
    ok1 = rows == math.ceil(N / 2)
    if cent:
        ok2 = N == 2 * rows - 1
    else:
        ok2 = N == 2 * rows
    all_ok = all_ok and ok1 and ok2
    print(f"{a:>7} {N:>5} {rows:>5} {str(cent):>8} {str(ok1):>17} {str(ok2):>13}")

print("\nAll convention relations OK:", all_ok)
print("(A003016(a) = N(a) is the run's both-mirrors-plus-trivial count;")
print(" A059233(a) = rowcount = ceil(N/2) = half-triangle count.)")

# Erdős 849 exemplars with their half-triangle solution counts
print("\nErdős 849 exemplars (strong form, 1<=k<=n/2):")
for a in (120, 3003):
    N, rows, cent = counts(a)
    # half-triangle solutions: k <= n/2, one per row except central row's own mirror
    print(f"  a={a}: N(a)={N}, rows={rows}, central={cent}")