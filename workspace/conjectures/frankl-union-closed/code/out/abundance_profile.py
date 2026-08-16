"""Exact abundance-profile scan over all union-closed families on ground set [n],
n=1..4, using the canonical oracle lib.uc.

For each n we enumerate every subfamily of 2^[n] (this is the sanctioned
brute-force oracle at n<=4: 2^2^n families), keep those that are union-closed
and are NOT the trivial {empty} family, and for each compute:
  - m   = |F|
  - maxfreq  = max over elements of (count/|F|)   -- best frequent density
  - minfreq  = min over elements of (count/|F|)   -- worst element density

We then report, over all UC families on ground set [n]:
  - BEST(n)  = min over families of maxfreq   (worst possible 'best' density;
                the conjecture says BEST(n) >= 1/2; tightness says =1/2 achieved)
  - a(n)     = number of UC families (== A121921, oracle consistency check)
  - WORST(n) = min over families of minfreq  (the smallest density any element
                can have at all across all UC families on [n])
All exact integer/rational arithmetic.
"""
from lib.uc import decide_union_closed, abundance

for n in range(1, 5):
    all_masks = list(range(1 << n))
    K = len(all_masks)
    families = 0          # all subfamilies (each bitmask = a subfamily)
    uc_count = 0
    best_of_worst = 1.0   # min over UC families of maxfreq  (want this small)
    worst_minfreq = 1.0   # min over UC families of minfreq (want this small)
    best_fam = None
    for sub in range(1 << K):
        fam = set()
        for i, mask in enumerate(all_masks):
            if (sub >> i) & 1:
                fam.add(mask)
        if not fam or fam == {0}:
            continue
        if not decide_union_closed(fam):
            continue
        uc_count += 1
        m = len(fam)
        counts = abundance(fam, n)
        # only elements that actually appear matter; skip zero-count ones
        present = [c for c in counts if c > 0]
        if not present:
            continue
        maxfreq = max(present) / m
        minfreq = min(present) / m
        if maxfreq < best_of_worst:
            best_of_worst = maxfreq
            best_fam = fam
        if minfreq < worst_minfreq:
            worst_minfreq = minfreq
    print(f"n={n}: UC families={uc_count} | min-over-families of max-frequency "
          f"BEST={best_of_worst:.6f} | min-of-min-frequency WORST={worst_minfreq:.6f}")
    # print the achieving family for the smallest best-frequency
    if best_fam is not None:
        print(f"    achieving family (min max-freq): {sorted(best_fam)}")
