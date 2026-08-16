"""List every distinct sorted-descending abundance profile that occurs among
union-closed families on [n], n=1..4, plus per-profile family counts, and
record claim C precisely (a degree-1 element forces an abundant element).

Uses the canonical oracle lib.uc. n<=4 brute-force (sanctioned oracle).
"""
from lib.uc import decide_union_closed, abundance


def main():
    for n in range(1, 5):
        all_masks = list(range(1 << n))
        from collections import defaultdict
        prof_count = defaultdict(int)
        uc_count = 0
        degree1_no_abundant = 0
        for sub in range(1 << len(all_masks)):
            fam = set()
            for i, mask in enumerate(all_masks):
                if (sub >> i) & 1:
                    fam.add(mask)
            if not fam or fam == {0}:
                continue
            if not decide_union_closed(fam):
                continue
            uc_count += 1
            counts = abundance(fam, n)
            m = len(fam)
            sdesc = tuple(sorted((c for c in counts if c > 0), reverse=True))
            prof_count[sdesc] += 1
            if 1 in counts and not any(2 * c >= m for c in counts):
                degree1_no_abundant += 1
        profs = sorted(prof_count.items(), key=lambda kv: (sum(kv[0]), kv[0]))
        print(f"n={n}: {uc_count} UC families, {len(profs)} distinct profiles:")
        for prof, cnt in profs:
            print(f"   {list(prof)}  (x{cnt})")
        print(f"   claim C: families with a degree-1 element but NO abundant "
              f"element = {degree1_no_abundant}")
        print()


if __name__ == "__main__":
    main()
