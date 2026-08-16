"""Identify the families where min_present_count * (2^{n-1}+1) == |F| (equality
in the weak k=n Nagel/Das-Wu bound) but the family is NOT the near-n-cube.
Exact, via lib.uc (n<=4 brute-force oracle).
"""
from lib.uc import decide_union_closed, abundance


def near_n_cube(n):
    full = (1 << n) - 1
    return set(range(1 << (n - 1))) | {full}


def union_size(F, n):
    u = 0
    for s in F:
        u |= s
    present = [i for i in range(n) if (u >> i) & 1]
    return len(present)


def main():
    for n in range(1, 5):
        den = 2 ** (n - 1) + 1
        nc = near_n_cube(n)
        nc_counts = abundance(nc, n)
        all_masks = list(range(1 << n))
        hits = []
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
            if min(present) * den == m:
                r = union_size(fam, n)
                is_nc = (counts == tuple(nc_counts))
                hits.append((fam, counts, m, r, is_nc))
        print(f"=== n={n} (near-cube profile {tuple(sorted(nc_counts, reverse=True))}) ===")
        print(f"  families with min_present*{den}==m : {len(hits)}")
        for fam, counts, m, r, is_nc in hits:
            print(f"    |F|={m} |UF|={r} counts={counts} "
                  f"nearcube_sorted_profile={tuple(sorted(nc_counts, reverse=True))} "
                  f"is_nearcube={is_nc} fam={sorted(fam)}")


if __name__ == "__main__":
    main()
