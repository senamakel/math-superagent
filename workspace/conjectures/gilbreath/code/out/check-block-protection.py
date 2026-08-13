#!/usr/bin/env python3
"""Check the exact protection constant of a {0,2} block.

Claim under test (Odlyzko 1993, intro, and Killgrove-Ralston 1959):
if row K is 1 followed by L entries in {0,2}, then rows K+1..? also start with 1.
The run's problem.md asserts "~n/2 rows"; the papers imply L further rows (L+1
rows total). Brute-force oracle check on small rows with random tails.
"""
import random

def protect(L, tail_max, trials, tail_len=6):
    """Return (rows_protected_after, ...) stats over random trials."""
    counts = {}
    for _ in range(trials):
        row = [1] + [random.choice((0, 2)) for _ in range(L)]
        # tail: large even numbers, anything beyond the block
        row += [random.randrange(4, tail_max + 1, 2) for _ in range(tail_len)]
        k = 0
        # how many further rows keep leading entry 1
        while True:
            nxt = [abs(row[i] - row[i + 1]) for i in range(len(row) - 1)]
            k += 1
            if nxt[0] != 1:
                counts[k] = counts.get(k, 0) + 1
                break
            row = nxt
    return counts

for L in (1, 2, 3, 4, 5, 8):
    counts = protect(L, 1000, 2000)
    # k = first row index (counting rows after row K) whose leading entry != 1
    # so rows K+1..K+k-1 are protected
    print(f"L={L}: protection ends after k={sorted(counts)[0] if len(counts)==1 else sorted(counts)}, "
          f"i.e. leading-1 rows after K: {sorted(counts)[0]-1 if len(counts)==1 else 'varies'} "
          f"(expected {L})")