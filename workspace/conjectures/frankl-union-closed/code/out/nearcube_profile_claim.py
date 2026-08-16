"""Dedicated structural-claim tests on near-n-cube extremal profiles, exact.

Claim B: the near-(n)-cube F = 2^[n-1] U {[n]} on [n] has abundance profile
exactly [2^{n-2}+1 repeated n-1 times, 1].

Claim D (shape): among all UC families on [n] whose rarest element is the
global-minimum 1 (i.e. min element-frequency = 1/|F|), the profile is exactly
the near-cube profile [2^{n-2}+1 x (n-1), 1]. I test whether this "if the
minimum is 1, the family has the near-cube shape" holds exhaustively.

Also verify the max density of the near-n-cube is always >= 1/2 (so it is never
a counterexample).
"""
from lib.uc import decide_union_closed, abundance


def near_n_cube(n):
    full = (1 << n) - 1
    return set(range(1 << (n - 1))) | {full}


def main():
    print("Claim B: near-n-cube profiles (n=1..8), exact:\n")
    print(" n | |F|=2^{n-1}+1 | profile (sorted desc)          | shape | max/|F|")
    print("---+--------------+---------------------------------+-------+-------")
    all_ok = True
    for n in range(1, 9):
        F = near_n_cube(n)
        counts = sorted(abundance(F, n), reverse=True)
        m = len(F)
        expect = sorted([2 ** (n - 2) + 1] * (n - 1) + [1], reverse=True)
        ok = (counts == expect)
        all_ok &= ok
        mx = max(counts)
        print(f" {n} | {m:12} | {str(counts):30} | {['OK','FAIL'][not ok]:5} | {mx}/{m} >= 1/2 ? {2*mx >= m}")
    print(f"\nClaim B: {'ALL PASS' if all_ok else 'SOME FAIL'}")

    # Claim D: exhaustive over n<=4: every UC family whose rarest element count
    # is exactly 1 (min present count == 1) has the near-cube profile shape.
    for n in range(1, 5):
        all_masks = list(range(1 << n))
        bad = 0
        total_min1 = 0
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
            present = [c for c in counts if c > 0]
            if min(present) != 1:
                continue
            total_min1 += 1
            sdesc = tuple(sorted(counts, reverse=True))
            expect = tuple(sorted([2 ** (n - 2) + 1] * (n - 1) + [1], reverse=True))
            if sdesc != expect:
                bad += 1
                if bad <= 2:
                    print(f"   n={n} NON-near-cube min-1 profile: {sdesc}, fam={sorted(fam)}")
        print(f"Claim D n={n}: UC families with min present count == 1: {total_min1}, "
              f"of which non-near-cube-shaped: {bad} -> {'HOLDS' if bad == 0 else 'FAILS'}")


if __name__ == "__main__":
    main()
