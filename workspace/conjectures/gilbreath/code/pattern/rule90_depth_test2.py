"""More checks on the Rule 90 prediction and minima structure.

(C) Do large regeneration jumps occur at depths d=2^j measured from k=1,
    i.e. is big-regeneration a power-of-2 phenomenon at all? 
(D) Structure of local-minima rows: are their row indices or b-values related
    to powers of 2?
(E) Distribution of the regen offset in (B2) vs a uniform null: is
    power-of-2-ish-ness of next-regen offset above chance given regen density?
"""
import json
from collections import Counter
d = json.load(open('code/out/blocks_depth1000.json'))
b = d['b']; D = d['D']
regen = [k for k in range(1, D) if b[k] > b[k-1]]

# (C) big-jump regen rows: are their absolute k near powers of 2?
big = [k for k in regen if (b[k]-b[k-1]) >= 1000]
pow2s = [2**j for j in range(1,11)]
print("(C) big regen rows at absolute k:", big)
print("    closest power-of-2 to each big k:", [(k, min(pow2s,key=lambda p:abs(p-k))) for k in big])

# (D) local minima of b: k where b[k] < both neighbors (and value)
minima = []
for k in range(1, D-1):
    if b[k] < b[k-1] and b[k] < b[k+1]:
        minima.append(k)
# also k where b[k] <= b[k-1] and b[k] < b[k+1] etc. Use strict local min + plateaus
print("\n(D) strict local minima count:", len(minima))
print("    row indices:", minima[:50])
print("    are any powers of 2?", [k for k in minima if k in pow2s])

# (E) null: probability a random regen row k (in the observed k-set) has its
# next regen at power-of-2-ish offset. Compare to observed 9/13.
obs_matched = 0
for K in big:
    try: idx = regen.index(K)
    except ValueError: continue
    if idx+1 < len(regen):
        off = regen[idx+1]-K
        if (off in pow2s) or (off+1 in pow2s): obs_matched += 1
print("\n(E) observed big-rows matched:", obs_matched, "/", len(big))

# null: for ALL regen rows, fraction whose next-regen offset is power-of-2-ish
all_matched=0; tot=0
for i,K in enumerate(regen):
    if i+1 < len(regen):
        off=regen[i+1]-K
        tot+=1
        if (off in pow2s) or (off+1 in pow2s): all_matched+=1
print("    null: all-regen-rows fraction matched = %d/%d = %.3f" % (all_matched,tot,all_matched/tot))

# (F) offset histogram among next-regen offsets
offs=[regen[i+1]-regen[i] for i in range(len(regen)-1)]
print("\n(F) next-regen offset histogram:", dict(sorted(Counter(offs).items())))
