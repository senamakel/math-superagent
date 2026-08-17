"""Examine the actual UC families with top element density == 1/2 at n=3,4.
Look for structural support for the Bell-number connection: does a half-density
element force a clean structure (e.g. related to set partitions)?
"""
from lib.uc import decide_union_closed, abundance
from fractions import Fraction


def find_half(n):
    all_masks = list(range(1 << n))
    halffams = []
    for sub in range(1 << len(all_masks)):
        fam = set()
        for i, mask in enumerate(all_masks):
            if (sub >> i) & 1:
                fam.add(mask)
        if not fam or fam == {0}:
            continue
        if not decide_union_closed(fam):
            continue
        counts = abundance(fam, n)
        m = len(fam)
        present = [c for c in counts if c > 0]
        top = max(present)
        if Fraction(top, m) == Fraction(1, 2):
            # record which element(s) are at density exactly 1/2
            half_elems = [i for i, c in enumerate(counts) if c > 0 and 2*c == m]
            halffams.append((sorted(fam), m, counts, half_elems))
    return halffams


for n in [3, 4]:
    hf = find_half(n)
    print(f"=== n={n}: {len(hf)} half-density families ===")
    # show families and their element densities
    for fam, m, counts, half_elems in hf[:40]:
        dens = [Fraction(c, m) for c in counts]
        print(f"  F={fam}  |F|={m}  counts={counts}  half-elems={half_elems}")
    print()
