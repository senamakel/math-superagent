#!/usr/bin/env python3
"""Verify G-balance (j >= d at every (2,4)-event) against the run's own
verified depth-1000 record code/out/blocks_depth1000.json.

An event is a transition k where b(k+1) >= b(k) (jump j = b(k+1)-b(k), j=0 a
stall). d for an event = number of erosion transitions (b decreases by exactly
1) strictly between the previous event and this one. G-balance claims j >= d
at EVERY event. We count every violation.
"""
import json

data = json.load(open("/workspace/code/out/blocks_depth1000.json"))
b = data["b"]  # b[k-1] = block length of row k

# transitions k=1..999: from row k to row k+1 (1-based); event iff b[k]>=b[k-1]
events = []
for k in range(1, 1000):
    if b[k] >= b[k - 1]:
        events.append((k, b[k] - b[k - 1]))

print("num events (transitions with b[k]>=b[k-1]):", len(events))

violations = []
for m, (k, j) in enumerate(events):
    if m == 0:
        d = sum(1 for kk in range(1, k) if b[kk] == b[kk - 1] - 1)
    else:
        prev_k = events[m - 1][0]
        d = sum(1 for kk in range(prev_k + 1, k) if b[kk] == b[kk - 1] - 1)
    if j < d:
        violations.append((k, j, d))

print("VIOLATIONS (j < d):", len(violations))
for (k, j, d) in violations:
    print("  event k=%d  j=%d  d=%d  (j<d)" % (k, j, d))
print()
print("G-balance (j>=d at every event) REFUTED iff violations list non-empty.")
