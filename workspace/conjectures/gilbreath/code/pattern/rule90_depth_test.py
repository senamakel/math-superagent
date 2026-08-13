"""Test the Rule 90 power-of-2 depth prediction against the depth-1000 record.

Prediction (from research/threads/rule90-regeneration.md): regeneration
events should occur at depths d = 2^j (or 2^j - 1) measured from the start of
a block regime (a big regeneration that resets the block). We test two forms:

  (A) Simple: gaps between consecutive regeneration rows are powers of 2.
  (B) Regime-based: from each big regeneration row K (jump >= 1000), the next
      regeneration rows should appear at offsets 2^j or 2^j - 1.

Uses only data already on disk (blocks_depth1000.json). Exact arithmetic.
"""
import json

d = json.load(open('code/out/blocks_depth1000.json'))
b = d['b']  # block lengths, index 0 = row 1
D = d['D']

# regeneration rows: b_{k+1} > b_k, using 1-based k (index 0 in list is k=1)
regen = [k for k in range(1, D) if b[k] > b[k-1]]
# big regen rows: jump >= 1000
big = [k for k in regen if b[k-1] and (b[k] - b[k-1]) >= 1000]

# (A) gaps between consecutive regen rows
gaps = [regen[i+1]-regen[i] for i in range(len(regen)-1)]
pow2 = {1,2,4,8,16,32,64,128}
nonpow = [g for g in gaps if g not in pow2]
print("(A) regen-gap gaps (n=%d): non-powers of 2: %d / %d" % (len(gaps), len(nonpow), len(gaps)))
print("    non-power gaps:", nonpow)

# (B) regime offsets: for each big regen row K, check subsequent regen rows at K+2^j and K+2^j-1
regenset = set(regen)
print("\n(B) big regen rows K (jump>=1000):", big)
print("    for each K, list (offset 2^j, is a regen row? K+off in regen) for j=1..8:")
for K in big:
    hits = []
    for j in range(1, 9):
        off = 2**j
        if K+off in regenset:
            hits.append(off)
        if K+off-1 in regenset:
            hits.append(off-1)
    print("   K=%-4d big-regen -> regen rows within offsets 2^j,2^j-1: %s" % (K, sorted(hits)))

# % of big regen rows whose NEXT regen row is at a power-of-2 or power-of-2-minus-1 offset
print("\n(B2) next-regen offset after each big regen row:")
n_matched = 0
for K in big:
    nxt = regen[regen.index(K)+1] if K in regen and regen.index(K)+1 < len(regen) else None
    if nxt is not None:
        off = nxt - K
        matched = (off in pow2) or (off+1 in pow2)
        n_matched += matched
        print("   K=%-4d next regen at %-5d offset %-4d  power-of-2-ish: %s" % (K, nxt, off, matched))
print("   matched %d / %d big rows" % (n_matched, len(big)))
