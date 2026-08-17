# Checks the multiplicity-index-avoidance dimension count.
# For a partition m_1..m_r of n with r>=5 distinct roots, M = max m_j.
# Hard indices = [M, n-1], count n-M. Free root parameters ~ r-1 (after translation).
# A pure dimension count "overdetermines" only if n-M > r-1.
# Also record the literature multiplicity constraint M <= n-3 (Laterveer-Ounaiës:
# a root of multiplicity >= n-2 forces pure power, so a counterexample has M <= n-3).

from math import comb

def partitions(n, minp=1):
    # integer partitions of n
    if n == 0:
        yield []
        return
    for first in range(minp, n+1):
        for rest in partitions(n-first, first):
            yield [first]+rest

for n in range(6, 21):
    bad = []   # partitions where count does NOT overdetermine (n-M <= r-1)
    examples = []
    for p in partitions(n):
        r = len(p)
        if r < 5:
            continue
        M = max(p)
        if M >= n-2:
            continue  # ruled out by Laterveer-Ounaiës multiplicity constraint anyway
        hard = n-M
        free = r-1
        if hard <= free:
            bad.append((p, M, hard, free))
    print(f"n={n}: partitions with r>=5, M<=n-3: "
          f"{sum(1 for p in partitions(n) if len(p)>=5 and max(p)<=n-3)} total; "
          f"{len(bad)} with n-M <= r-1 (count NOT overdetermined)")
    if bad and len(bad) <= 3:
        for b in bad[:3]:
            print(f"    e.g. {b[0]} M={b[1]} n-M={b[2]} r-1={b[3]}")
