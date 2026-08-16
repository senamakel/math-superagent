"""Independent brute force for WORST(2) and WORST(3): a second, hand-written
route that does NOT import from lib.uc -- it re-implements union-closure and
abundance from scratch, so a disagreement would expose an oracle bug.

We enumerate every subfamily of 2^[n] (n=2,3), keep those that are union-closed
under all pairwise unions (nonempty, excluding {empty}), and compute the exact
minimum element-density. Compare to 1/(2^{n-1}+1). Independent of lib.uc.
"""
from fractions import Fraction


def decide_uc(F):
    """Closed under pairwise OR, hand-written (no lib.uc)."""
    for a in F:
        for b in F:
            if (a | b) not in F:
                return False
    return True


def abundance(F, n):
    counts = [0] * n
    for s in F:
        for i in range(n):
            if (s >> i) & 1:
                counts[i] += 1
    return counts


def main():
    for n in (2, 3):
        all_masks = list(range(1 << n))
        K = len(all_masks)
        worst = Fraction(1, 1)
        worst_fam = None
        uc_count = 0
        for sub in range(1 << K):
            fam = set()
            for i, mask in enumerate(all_masks):
                if (sub >> i) & 1:
                    fam.add(mask)
            if not fam or fam == {0}:
                continue
            if not decide_uc(fam):
                continue
            uc_count += 1
            counts = abundance(fam, n)
            present = [c for c in counts if c > 0]
            if not present:
                continue
            dens = Fraction(min(present), len(fam))
            if dens < worst:
                worst = dens
                worst_fam = fam
        expected = Fraction(1, 2 ** (n - 1) + 1)
        print(f"INDEPENDENT n={n}: UC count={uc_count}, "
              f"WORST={worst} == 1/(2^{n-1}+1)={expected} ? {worst == expected}")
        print(f"   achieving family: {sorted(worst_fam)}")


if __name__ == "__main__":
    main()
