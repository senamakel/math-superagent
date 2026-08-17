"""Independent cross-check of the g(n,m) = max(1, m-2^{n-1}) conjecture.

Route: DIRECT exhaustive brute force over 2^(2^n) subfamilies (sanctioned
oracle) on [4], NOT the cascade. For each size m compute g(4,m) = min over UC
families of the min present-element count, and exhibit one attaining family.

Also verify, by direct count, the lower bound is saturated - i.e. exhibit an
attaining family for a non-trivial size m where g > 1.
"""
from lib.uc import decide_union_closed, abundance


def brute_g(n):
    all_masks = list(range(1 << n))
    K = len(all_masks)
    best = {}   # m -> (min_count, family)
    fam_count = 0
    for sub in range(1 << K):
        fam = set()
        for i, mask in enumerate(all_masks):
            if (sub >> i) & 1:
                fam.add(mask)
        if not fam or fam == {0}:
            continue
        if not decide_union_closed(fam):
            continue
        fam_count += 1
        m = len(fam)
        counts = abundance(fam, n)
        present = [c for c in counts if c > 0]
        mn = min(present)
        if m not in best or mn < best[m][0]:
            best[m] = (mn, fam)
    return best, fam_count


n = 4
best, fam_count = brute_g(n)
print(f"n={n}: direct oracle enumerated {fam_count} UC families")
pred = lambda m: max(1, m - 2 ** (n - 1))
allmatch = True
for m in sorted(best):
    g, fam = best[m]
    matches = (g == pred(m))
    if not matches:
        allmatch = False
    flag = "" if matches else "  <-- MISMATCH"
    print(f"  m={m:2d} g={g:2d} pred={pred(m):2d} match={matches}{flag}")
print("ALL sizes match max(1, m-2^(n-1)):", allmatch)

# Exhibit one non-trivial attaining family (g>1): m=12 -> g=4
for m in (10, 12, 14, 16):
    if m in best:
        g, fam = best[m]
        print(f"\nExhibit attaining family for m={m}, g={g}:")
        print("  family (bitmasks):", sorted(fam))
        print("  abundances:", abundance(fam, n), "min present:", g)
