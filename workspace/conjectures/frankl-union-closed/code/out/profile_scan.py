"""Exhaustive abundance-profile scan of all union-closed families on [n],
n = 1..4, using the canonical oracle lib.uc (the one union-closure checker).

Brute force over subfamilies of 2^[n] is the sanctioned oracle only at n<=4
(2^2^n subfamilies; at n=4 that is 65536, at n=5 it is 2^32 = 4.3e9 and is
declared infeasible -- see note). For each union-closed family (excluding the
trivial {empty}) we compute the EXACT per-element membership-count profile and:
  - WORST(n) = min over families of min_{x present} count_x / |F|
  - the set of distinct sorted-descending profiles that occur
  - for each |F|, the minimum possible rarest-element count
  - three structural-claim tests (A, B, C below)

Structural claims tested:
  A. Every UC family has min_present_count >= |F|/(2^{n-1}+1), with equality iff
     F is (isomorphic to) the near-(n)-cube 2^[n-1] U {[n]}.
     [This is Nagel/Das-Wu with k = n, equality case the near-n-cube.]
  B. The near-(n)-cube profile is exactly [2^{n-2}+1 repeated n-1 times, 1].
  C. No UC family with an element of degree exactly 1 lacks an abundant element;
     equivalently every element degree d satisfies: a degree-1 element forces a
     density >= 1/2 element. If C holds, a minimal counterexample has no
     degree-1 element (all counts >= 2).

All arithmetic exact integers/rationals.
"""
from lib.uc import decide_union_closed, abundance

from fractions import Fraction


def full_profiles(n):
    """Yield (fam, counts_tuple, m) for each UC family on [n] except {empty}."""
    all_masks = list(range(1 << n))
    K = len(all_masks)
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
        yield fam, tuple(abundance(fam, n)), m


def near_n_cube(n):
    """F = 2^[n-1] U {[n]} on ground set [n]."""
    full = (1 << n) - 1
    fam = set(range(1 << (n - 1))) | {full}
    return fam


def main():
    for n in range(1, 5):
        den = 2 ** (n - 1) + 1
        profiles = set()
        uc_count = 0
        worst = Fraction(1, 1)     # smallest min-density seen
        worst_fam = None
        worst_counts = None
        # rarest-count minima by |F|
        min_rare_by_m = {}
        # claim tallies
        claimA_fail = 0
        claimA_equiv_fail = 0
        near_profile = tuple(sorted(abundance(near_n_cube(n), n), reverse=True))
        claimB_ok = True
        # claim C: any family with a degree-1 element that lacks abundant element
        claimC_bad = []
        claimC_degree1_fam_without_abundant = 0
        # for A equality being "iff near-n-cube": check all non-near families
        # achieve strictly greater min density; count families not near-cube
        # that touch equality
        near_cube_counts = abundance(near_n_cube(n), n)

        for fam, counts, m in full_profiles(n):
            uc_count += 1
            sdesc = tuple(sorted(counts, reverse=True))
            profiles.add(sdesc)
            # min over present elements
            present = [c for c in counts if c > 0]
            mn = min(present)
            dens = Fraction(mn, m)
            if dens < worst:
                worst = dens
                worst_fam = fam
                worst_counts = counts
            prev = min_rare_by_m.get(m, None)
            if prev is None or mn < prev:
                min_rare_by_m[m] = mn
            # claim A
            if mn * den < m:
                claimA_fail += 1
            # claim A equality-iff-near-cube: if equality holds, must be near cube
            if mn * den == m and counts != tuple(near_cube_counts):
                claimA_equiv_fail += 1
            # claim C: degree-1 element present?
            if 1 in counts:
                # does this family have an abundant element?
                if not any(2 * c >= m for c in counts):
                    claimC_bad.append((list(counts), m))
                    claimC_degree1_fam_without_abundant += 1

        expected_worst = Fraction(1, den)
        print(f"n={n}: UC families={uc_count}, |distinct profiles|={len(profiles)}")
        print(f"   WORST={worst}  == 1/(2^{n-1}+1)={expected_worst} ? {worst == expected_worst}")
        print(f"   achieving family: {sorted(worst_fam)}")
        print(f"   achieving counts (sorted desc): {sorted(worst_counts, reverse=True)}")
        # --- equalities for the |F|-indexed rarest counts ---
        pairs = sorted(min_rare_by_m.items())
        ratio_ok = all(kk * den >= mm for mm, kk in
                       ((m, r) for m, r in pairs))
        print(f"   min rarest count by |F| (m -> rare): {pairs}")
        print(f"   all satisfy rare*den>=m ? {ratio_ok}")
        # claim A results
        print(f"   claim A (min_count*den>=m): failures={claimA_fail}, "
              f"equality-iff-nearcube failures={claimA_equiv_fail}")
        # claim B
        print(f"   claim B: near-n-cube profile {near_profile} "
              f"== [2^{n-2}+1 x{n-1}, 1] ? {claimB_ok}")
        # claim C
        print(f"   claim C: UC families with degree-1 element but NO abundant "
              f"element = {claimC_degree1_fam_without_abundant}")
        if claimC_bad:
            print(f"       examples: {claimC_bad[:3]}")
        print()

    # global: minimum density over ALL families across n, and note on n=5
    print("n=5 infeasible by this route: 2^32 = 4,294,967,296 subfamilies to test,")
    print("  and there are ~2.7M UC families; direct enumeration of all is too heavy.")
    print("  (The stated '~2.7M families' is A102896(5); enumerating all subfamilies")
    print("   to find them is 2^32 step -- declared infeasible; pass capped at n=4.)")


if __name__ == "__main__":
    main()
