"""Independent direct-brute verification of the top-density==1/2 counts at
n<=4, WITHOUT the cascade (uses lib.uc oracle directly over 2^(2^n) subfamilies,
the sanctioned oracle at n<=4). Cross-checks the cascade-produced sequence
1,4,14,51 (n=1..4) and gives an honest n=4 number.
"""
from lib.uc import decide_union_closed, abundance
from fractions import Fraction


def count(n):
    all_masks = list(range(1 << n))
    K = len(all_masks)
    half = 0
    total = 0
    for sub in range(1 << K):
        fam = set()
        for i, mask in enumerate(all_masks):
            if (sub >> i) & 1:
                fam.add(mask)
        if not fam or fam == {0}:
            continue
        if not decide_union_closed(fam):
            continue
        total += 1
        counts = abundance(fam, n)
        m = len(fam)
        present = [c for c in counts if c > 0]
        top = max(present)
        if Fraction(top, m) == Fraction(1, 2):
            half += 1
    return total, half


for n in range(1, 5):
    total, half = count(n)
    print(f"n={n}: direct-brute total UC={total}, top-density==1/2 count={half}")
