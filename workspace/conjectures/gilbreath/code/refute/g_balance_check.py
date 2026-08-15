#!/usr/bin/env python3
"""Attack G-balance: at every (2,4)-regeneration event, the jump j satisfies
j >= d, where d = number of erosion rows (b decreases by 1) since the previous
(2,4)-event.

Uses the depth-1000 on-disk record code/out/blocks_depth1000.json:
  b[0..999] = block length of rows k=1..1000
  s[0..999] = second entry of row k (0 or 2)  -- 1-based row k = index k-1
Transitions are between consecutive rows. A (2,4)-event is a transition where
b increases (b[k] > b[k-1]); the jump j = b[k] - b[k-1].
d for that event = number of strictly-epprox erosions since the previous event
= (number of transitions strictly between the two events that are erosions).
Equivalently: index gap minus (1 event) ... d = (# rows between) where b dropped.
"""
import json

data = json.load(open("/workspace/code/out/blocks_depth1000.json"))
b = data["b"]  # length 1000, b[k-1] = block length of row k (k=1..1000)

# transitions: for rows k=1..999, from row k to row k+1 is index t=k (1-based row);
# event at transition t means b[k] > b[k-1]  (0-based: b[t] > b[t-1]).
events = []  # (row k where block landed, j)
for t in range(1, 1000):  # transition from row t to row t+1 (1-based)
    if b[t] > b[t - 1]:
        j = b[t] - b[t - 1]
        events.append((t, j))  # event lands at row t+1

print("num events (transitions where b increased):", len(events))

# For each event, d = number of erosion transitions strictly since previous event.
# previous event lands at row prev_t+1; the current event is at transitions t.
violations = []
for m, (t, j) in enumerate(events):
    if m == 0:
        d = t - 1  # erosion rows from row 1 up to event? includes rows 2..t-1? use 0 for first
        # count transitions 1..t-1 that are erosions (b decreases by 1)
        d = sum(1 for tt in range(1, t) if b[tt] <= b[tt - 1] and b[tt] == b[tt-1]-1)
    else:
        prev_t = events[m - 1][0]
        # transitions strictly between prev_t and t
        d = sum(1 for tt in range(prev_t + 1, t) if b[tt] == b[tt - 1] - 1)
    ok = j >= d
    if not ok:
        violations.append((m, t, j, d))

print("total violations (j < d):", len(violations))
for v in violations[:20]:
    print("  event#%d  transition %d  j=%d  d=%d  FAIL" % v)
print()
print("-> per-event check complete. G-balance holds only if violations list is empty.")
