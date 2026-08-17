"""INDEPENDENT verification: min-density union-closed families on n=2,3,4 are
exactly (up to relabeling) the near-n-cube families.

Route: direct exhaustive enumeration of the family space 2^(2^n) through the
canonical oracle lib.uc (decide_union_closed, abundance) and a hand-written,
separately-derived analyser that computes the min-density quantity and
canonicalizes profiles. This does NOT reuse any prior claim program or cascade:
the density/ratio computation, the profile canonicalisation, and the
isomorphism verdict are written from scratch against lib.uc's raw oracle
output alone.

Definitions (stated before executing).
  ground set [n] = {0..n-1}, family F = set of bitmasks.
  abundance(F,n) = per-element exact integer counts.
  min_count(F)   = min over PRESENT elements (count>0) of the count.
  density(F)     = min_count(F) / |F|   (the min element-frequency).
  WORST(n)       = min over all UC families F (nonempty, F != {empty})
                   of density(F).
  canonical(F)   = tuple(sorted(abundance(F,n), reverse=True)) — the abundance
                   profile up to relabeling (includes the zero entries for
                   absent elements).

Claim under test: the UC families on [n] achieving WORST(n) are, up to
relabeling, exactly the near-n-cube families F = 2^[n-1] ∪ {[n]}, with
canonical profile [(2^{n-2}+1)*n-1, 1, 0]. Equivalently:
  (a) exactly ONE distinct canonical profile achieves WORST(n);
  (b) that profile equals the near-n-cube profile;
  (c) every labeled family realizing it is isomorphic to the near-n-cube.

Cross-check: WORST(n) == 1/(2^{n-1}+1), i.e. 1/3 at n=2, 1/5 at n=3, 1/9 at n=4.

An ambiguity is resolved explicitly: "minimize the min present-count" strictly
as a count gives the degenerate value 1 for every n (any degree-1 family attains
it, e.g. F={0,{x}}). The density notion — what the cross-check 1/(2^{n-1}+1)
and the word "min-density" mean — normalises the count by |F| and is the
quantity that selects the near-n-cube. Both are computed and reported; the
density is the headline, the pure count is reported to show why it is the
degenerate reading.

Structural bound used as a sanity cross-check (not the method): for any element
x, the sets of F avoiding x all live in 2^[n-1], so m - c_x <= 2^{n-1}, i.e.
c_x >= m - 2^{n-1}. This implies density = min_c/m >= 1/(2^{n-1}+1), with
equality iff m = 2^{n-1}+1 and some element has degree 1; closure then forces
that element's containing set to be [n] and F = 2^[n-1] ∪ {[n]}. The
enumeration confirms this independently.
"""
from fractions import Fraction
from collections import defaultdict

from lib.uc import decide_union_closed, abundance


def density_of(F, n):
    """density = min over present elements of count / |F|, exact Fraction."""
    counts = abundance(F, n)
    present = [c for c in counts if c > 0]
    if not present:
        return None
    return Fraction(min(present), len(F))


def canonical_profile(F, n):
    """Abundance-profile up to relabeling: all n counts, sorted descending."""
    return tuple(sorted(abundance(F, n), reverse=True))


def enumerate_uc_families(n):
    """Yield every union-closed (nonempty, != {empty}) family on [n].

    Purely via the canonical oracle decide_union_closed. Brute force over all
    subfamilies of 2^[n], feasible for n<=4 (2^(2^n) subfamilies: 16, 256,
    65536). Sanctioned oracle-only exhaustive route.
    """
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
        yield fam


def near_n_cube(n):
    """F = power set of [n-1] union {[n]}; the candidate unique extremal."""
    full = (1 << n) - 1
    return set(range(1 << (n - 1))) | {full}


def is_near_cube(fam, n):
    """Direct mechanical test: is `fam` equal to the near-n-cube with the rare
    (degree-1) element relabelled to be the distinguished one?

    A UC family achieving density ref = 1/(2^{n-1}+1) has |F| = 2^{n-1}+1 and
    exactly one degree-1 element x (count 1). The near-n-cube with x as the
    distinguished element is the power set of [n]\{x} (all 2^{n-1} subsets
    avoiding x) union {[n]} (the unique set containing x that closure forces).
    We check that literal equality; this is a direct isomorphism test to the
    concrete near-n-cube, not an inference from profile counts.
    """
    if len(fam) != 2 ** (n - 1) + 1:
        return False
    counts = abundance(fam, n)
    rare = [i for i, c in enumerate(counts) if c == 1]
    if len(rare) != 1:
        return False
    x = rare[0]
    full = (1 << n) - 1
    # power set of [n] \ {x}
    other = [i for i in range(n) if i != x]
    powset = {0}
    for i in other:
        powset |= {s | (1 << i) for s in list(powset)}
    target = powset | {full}
    return fam == target


def reference_worst(n):
    return Fraction(1, 2 ** (n - 1) + 1)


def main():
    print("What: independent verification that min-density UC families on "
          "n=2,3,4 are exactly the near-n-cube families (up to relabeling).")
    print("Oracle: used lib.uc.decide_union_closed and lib.uc.abundance "
          "directly; density/profile/isomorphism analysis written from scratch "
          "against that output (no prior claim program or cascade reused).")
    print("Range: n in {2,3,4}, exhaustive over all subfamilies of 2^[n].")

    all_ok = True
    for n in (2, 3, 4):
        two_p = 2 ** (n - 1)
        ref = reference_worst(n)
        uc_count = 0
        density_eq = True
        min_pure_count = None
        min_pure_example = None
        achieved = False

        for fam in enumerate_uc_families(n):
            uc_count += 1
            counts = abundance(fam, n)
            m = len(fam)
            present = [c for c in counts if c > 0]
            mn = min(present)
            if min_pure_count is None or mn < min_pure_count:
                min_pure_count = mn
                min_pure_example = sorted(fam)
            for c in present:
                if c < m - two_p:
                    density_eq = False
            if Fraction(mn, m) == ref:
                achieved = True

        # Second pass: every UC family with density == ref, keyed by
        # canonical profile (distinct min-density profiles, and # labeled
        # families realizing each).
        worst_profiles = defaultdict(int)
        n_min_density_labeled = 0
        n_direct_isomorphic = 0
        non_iso_examples = []
        for fam in enumerate_uc_families(n):
            if density_of(fam, n) == ref:
                worst_profiles[canonical_profile(fam, n)] += 1
                n_min_density_labeled += 1
                if is_near_cube(fam, n):
                    n_direct_isomorphic += 1
                else:
                    non_iso_examples.append(sorted(fam))

        NC = near_n_cube(n)
        nc_prof = canonical_profile(NC, n)
        nc_density = density_of(NC, n)

        unique_profile = len(worst_profiles) == 1
        profile_is_nc = (unique_profile and nc_prof in worst_profiles)
        # every labeled min-density family isomorphic to near-n-cube: the
        # number of labeled realizations equals the number of relabelings n,
        # and each one is DIRECTLY verified by is_near_cube to equal the
        # near-cube with its rare element relabelled.
        direct_iso = (n_direct_isomorphic == n_min_density_labeled and
                      n_min_density_labeled == n)
        all_iso = (unique_profile and profile_is_nc and direct_iso)
        ok = (achieved and unique_profile and profile_is_nc and all_iso
              and nc_density == ref and density_eq)
        all_ok &= ok

        worst = ref if achieved else None
        print(f"\nn={n}: WORST(n) = {worst}  (reference 1/(2^{n-1}+1) = {ref}; "
              f"match {achieved})")
        print(f"   {uc_count} union-closed families; min present-count (pure)="
              f" {min_pure_count}, example {min_pure_example} (degenerate)")
        print(f"   elementwise bound c_x >= m-2^{n-1} holds: {density_eq}")
        print(f"   near-n-cube profile {list(nc_prof)}, density {nc_density}")
        print(f"   distinct canonical min-density profiles: "
              f"{len(worst_profiles)}")
        for prof, cnt in sorted(worst_profiles.items()):
            print(f"      {list(prof)}  (x{cnt} labeled families)")
        print(f"   unique profile == near-n-cube profile: {profile_is_nc}")
        print(f"   all min-density families isomorphic to near-n-cube "
              f"({n_direct_isomorphic} direct / {n_min_density_labeled} "
              f"labeled, {n} relabelings): {direct_iso}")
        print(f"   VERDICT n={n}: {'PASS' if ok else 'FAIL'}")

    print(f"\nOVERALL: {'ALL PASS' if all_ok else 'SOME FAIL'}")


if __name__ == "__main__":
    main()
