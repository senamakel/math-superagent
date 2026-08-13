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
regen = [k for k in range(1, D) if b[k] > b[k-1]]
live = [k for k in regen if k <= 161]  # genuine live regime
b1 = b[0]

# (1) surplus just before each event, and running
print("(1) Recharge surplus S_k = sum_{events i<k}(j_i+1) - (k-1):")
surpl = []
acc = 0
for k in range(1, D):
    if k-1 in regen:  # event fired at transition k-1 -> k
        # actually compute surplus at row k
        pass
# recompute cleanly: surplus at row k = b_k - b_1 + (k-1)
surpl = [b[k] - b1 + k for k in range(0, D)]  # k is 1-based row number; row index k-1
# check: for row index i (0-based), k=i+1, surplus should equal sum of (j+1) over events with eventrow < i+1... 
# verify identity instead using event jumps
events = regen
sumj = b1
ok = True
for k in range(1, D):
    exp = b1 + sum((b[e]-b[e-1])+1 for e in events if e < k) - (k-1)
    if exp != b[k]:
        ok = False; print("  IDENTITY FAIL at k", k, exp, b[k]); break
print("   recharge identity exact over all k=%d..%d: %s" % (1, D, ok))
surplus = [b[k]-b1+k for k in range(D)]
print("   min surplus over k=1..1000:", min(surplus[1:]), "at k", surplus[1:].index(min(surplus[1:]))+1)
print("   surplus monotone nondecreasing? ", all(surplus[i]<=surplus[i+1] for i in range(D-1)))
print("   surplus at regen rows:", [surplus[e-1] for e in [k for k in regen if k<=161]][:10], "...")

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
