"""Verify that the near-(n)-cube family 2^[n-1] ∪ {[n]} achieves the worst
min-frequency, and that it matches Das-Wu daswu-nagel claim arithmetic:
  near-k-cube = Boolean lattice 2^[k-1] plus one extra set.
Here k = n (ground set size), so family = 2^[n-1] union {full set [n]},
|F| = 2^(n-1) + 1, and the (n)th = last/least element is in exactly 1 set,
density = 1/(2^(n-1)+1).
Exact integer arithmetic via lib.uc oracle.
"""
from lib.uc import decide_union_closed, abundance

for n in range(1, 6):
    full = (1 << n) - 1                  # bitmask of [n]
    submasks = range(1 << (n - 1))       # all subsets of [n-1]
    fam = set(submasks) | {full}         # 2^[n-1] plus the extra full set
    uc = decide_union_closed(fam)
    counts = abundance(fam, n)
    m = len(fam)
    # element n-1 (0-indexed, the 'nth' element) is only in the full set
    last = counts[n - 1]
    print(f"n={n}: |F|={m} (2^{n-1}+1={2**(n-1)+1}), UC={uc}, "
          f"last-element count={last}, density={last}/{m} "
          f"= 1/(2^{n-1}+1) ? {last==1}")
    # every present element's density, sorted ascending
    pres = sorted((c, i) for i, c in enumerate(counts) if c > 0)
    print(f"    density profile (count, elem): {pres}")
