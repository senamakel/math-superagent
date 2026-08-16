"""Identify the family that achieves WORST(n): smallest min-frequency over all
union-closed families on [n]. n<=4 brute force (sanctioned oracle)."""
from lib.uc import decide_union_closed, abundance

for n in range(1, 5):
    all_masks = list(range(1 << n))
    K = len(all_masks)
    worst_minfreq = 1.0
    argfam = None
    for sub in range(1 << K):
        fam = set()
        for i, mask in enumerate(all_masks):
            if (sub >> i) & 1:
                fam.add(mask)
        if not fam or fam == {0}:
            continue
        if not decide_union_closed(fam):
            continue
        m = len(fam)
        counts = abundance(fam, n)
        present = [c for c in counts if c > 0]
        if not present:
            continue
        mn = min(present) / m
        if mn < worst_minfreq:
            worst_minfreq = mn
            argfam = fam
    # report the achieving family's structure
    print(f"n={n}: WORST={worst_minfreq} = 1/(2^{n-1}+1)? "
          f"{abs(worst_minfreq - 1/(2**(n-1)+1)) < 1e-12}")
    print(f"   |F|={len(argfam)}, family={sorted(argfam)}")
    # near-(n)-cube should be Boolean lattice 2^[n-1] plus one extra set
