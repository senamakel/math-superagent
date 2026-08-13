"""Structural probes the run has not yet reported:
(1) recharge surplus S_k = b_k - b_1 + (k-1) = sum of (j_i+1) over events i<k
    — does it stay positive / grow, and how?
(2) is the jump j_i related to b_i by a log-linear law across ALL events
    (not just big ones)?
(3) gap/jump joint structure at the event level: does a big jump follow a
    long gap (energy building up during erosion)?
(4) ratio b_{next_regen}/b_{this_regen} across ALL regeneration pairs.
"""
import json
from collections import Counter
d = json.load(open('code/out/blocks_depth1000.json'))
b = d['b']; D = d['D']
regen = [k for k in range(1, D) if b[k] >= b[k-1]]  # events incl. jump-0 stalls
live = [k for k in regen if k <= 161]  # genuine live regime
b1 = b[0]

# (1) surplus just before each event, and running
print("(1) Recharge surplus S_k = sum_{events i<k}(j_i+1) - (k-1):")
# Recharge identity: for 1-based row k, b_k = b_1 + sum_{events i<k} (j_i+1) - (k-1),
# where events are 1-based row indices i of transitions with b_{i+1} > b_i.
# CORRECTION (this run): the earlier version compared 1-based expected values
# against the 0-based list b[k], an off-by-one in the check that produced a
# spurious failure at k=1.  Here exp is checked against b[k-1].
events = regen  # 0-based transition indices with b[e] >= b[e-1] (incl. jump-0)
esum = 0
ev_it = 0
bad = []
for k in range(1, D + 1):
    while ev_it < len(events) and events[ev_it] < k:
        e = events[ev_it]
        esum += (b[e] - b[e - 1]) + 1
        ev_it += 1
    expect = b1 + esum - (k - 1)
    if expect != b[k - 1]:
        bad.append((k, expect, b[k - 1]))
print("   recharge identity exact over all rows k=1..%d: %s" % (D, len(bad) == 0))
if bad:
    print("   failures:", bad[:3])
# Surplus at 1-based row k is S_k = b_k - b_1 + (k-1); 0-based: b[i] - b1 + i.
surplus = [b[i] - b1 + i for i in range(D)]
print("   min surplus over k=1..1000:", min(surplus), "at k", surplus.index(min(surplus)) + 1)
print("   surplus monotone nondecreasing? ", all(surplus[i] <= surplus[i + 1] for i in range(D - 1)))
print("   surplus at the first 10 regen rows (row, S just before the event):",
      [(e + 1, b[e] - b1 + e) for e in events[:10]])

# (2) log(jump) vs log(b) across ALL events (jump>0)
import math
pairs = [(math.log(b[e]), math.log(b[e]-b[e-1])) for e in live if b[e]-b[e-1] > 0]
# naive OLS slope
xs=[p[0] for p in pairs]; ys=[p[1] for p in pairs]; n=len(xs)
mx=sum(xs)/n; my=sum(ys)/n
slope=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
print("\n(2) OLS slope log(jump) vs log(b) over %d positive-jump events: %.3f (near 1 => jump ~ c*b)" % (n, slope))

# (3) gap before big jump vs gap before small jump
gaps=[live[i+1]-live[i] for i in range(len(live)-1)]
big_edges=[(live[i+1]-live[i], b[live[i+1]]-b[live[i+1]-1]) for i in range(len(live)-1)]
small_big = [g for g,j in big_edges if j<1000]
big_big   = [g for g,j in big_edges if j>=1000]
print("\n(3) gap before small jumps (n=%d): mean %.2f" % (len(small_big), sum(small_big)/len(small_big) if small_big else 0))
print("    gap before big jumps (n=%d):   mean %.2f" % (len(big_big), sum(big_big)/len(big_big) if big_big else 0))

# (4) b at consecutive regen rows: ratio
ratios=[b[live[i+1]]/b[live[i]] for i in range(len(live)-1)]
print("\n(4) ratio b_next/b_this across consecutive regen rows: n=%d, min %.3f, median %.3f, max %.3f" % (
    len(ratios), min(ratios), sorted(ratios)[len(ratios)//2], max(ratios)))
