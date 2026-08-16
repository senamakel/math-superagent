"""Classify the distinct sets in S2_char(n), n=2..24.

Question: which sets occur? Is 1 + C(n-2,2) the count of distinct frozensets?
For a canonical labelling we print, for small n, every distinct set as its
binary mask over positions [0,n-1], grouped by run_count, and list the pairs
(d,d') that realize a couple of them.

Also checks the identity: distinct sets == { M_{d} △ M_{d'} } as frozensets.
"""
from collections import Counter, defaultdict
from lib.collapse import S2_char, downset, run_count


def main():
    for n in [5, 6, 8, 12]:
        c = S2_char(n)
        print(f"\n===== n={n} :: {len(c)} distinct sets =====")
        sets_by_runs = defaultdict(list)
        for A in sorted(c, key=lambda a: (len(a), sorted(a))):
            sets_by_runs[run_count(A)].append(A)
        for r in sorted(sets_by_runs):
            As = sorted(sets_by_runs[r], key=lambda a: (len(a), sorted(a)))
            print(f" run_count={r}  ({len(As)} sets)")
            for A in As[:8]:
                mask = ''.join('1' if j in A else '0' for j in range(n))
                print(f"    size={len(A):2d} mask={mask} mult={c[A]}")
            if len(As) > 8:
                print(f"    ... {len(As)-8} more")

    # Which pairs realize the empty set (should be d=d', n-2 of them)
    print("\n=== empty set pairing (n=12) ===")
    c = S2_char(12)
    empty = frozenset()
    ms = {d: downset(d, 12) for d in range(2, 12)}
    reps = []
    for d in range(2, 12):
        for dp in range(2, 12):
            if frozenset(ms[d] ^ ms[dp]) == empty:
                reps.append((d, dp))
    print("pairs with M_d △ M_{d'} = empty:", reps)


if __name__ == "__main__":
    main()
