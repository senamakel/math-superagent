#!/usr/bin/env python3
"""Empirical event-rate bound probe for candidate 1 (window-range-bound).

The stated conditional theorem: with the range bound A_k(i) <= R(k) on the
intruder's feeding window, the drain law gives a (2,4)-event at least once
every ~(R(k)-4)/(2p) rows, where p is the edge-2 frequency.  Check on the
real live rows (k=1..160): measure the intruder window range R at each live
row and the intruder value y; see how often a (2,4)-event actually occurs,
and whether the simple bound is tight or enormously loose.
"""
from lib.gilbreath import primes_up_to, rows_generator

primes = primes_up_to(200000)
rows = list(rows_generator(primes, 160))
A1 = rows[1]

# live rows: block b_k with an intruder
def block_profile(row):
    L = 0
    for x in row[1:]:
        if x in (0, 2):
            L += 1
        else:
            break
    return L

events = 0
n_live = 0
total_R = 0
maxR_at_event = 0
for k in range(1, 160):
    row = rows[k]
    b = block_profile(row)
    if b + 1 >= len(row):
        continue                    # no intruder
    n_live += 1
    y = row[b + 1]                  # intruder
    # window feeding cell (k, b+1): gaps A1[b .. b+k-1]
    hi = b + (k - 1)
    if hi >= len(A1):
        continue
    w = A1[b:hi + 1]
    R = max(w) - min(w)
    total_R += R
    edge = row[b]
    if (edge, y) == (2, 4):
        events += 1
        maxR_at_event = max(maxR_at_event, R)

print(f"live rows checked: {n_live}, (2,4)-events: {events}")
print(f"mean intruder-window range R over live rows: {total_R/max(1,n_live):.1f}")
print(f"max R at an event row: {maxR_at_event}")
# Compare with (R-4)/2 bound: typical R ~ ?, events dense (60 in ~160 rows)?
