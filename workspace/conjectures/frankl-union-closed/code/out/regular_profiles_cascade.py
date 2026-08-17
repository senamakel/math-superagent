"""Count DISTINCT REGULAR abundance profiles over all nonempty UC families on
[n], n = 1..5, using the validated canonical cascade.

A profile (sorted-descending positive element counts) is REGULAR if all its
entries are equal: every present element of the family has the same count.

Two counts are reported:
  REG(n)     = # distinct regular profiles (equal counts, any number of
               present elements r = 1..n)
  FULLREG(n) = # distinct profiles [c x n] with ALL n ground elements present
               and equal counts

Pattern to test (observed from profile_listing.captured.txt at n = 1..4):
  REG(n)     = 1, 3, 7, 15  ->  2^n - 1
  FULLREG(n) = 1, 1, 4, 8   ->  ?
The n=5 terms are new (exhaustive over all 2,771,102 nonempty UC families).

Oracle: profile_count_cascade (validated vs A121921 at every level).
Range:  n=1..5, ALL nonempty UC families, exact integer counts.
"""
import importlib.util
from collections import defaultdict

spec = importlib.util.spec_from_file_location(
    "profile_count_cascade", "code/out/profile_count_cascade.py")
pc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pc)


def profile_of(F, k1):
    counts = [0] * k1
    for s in F:
        for i in range(k1):
            if (s >> i) & 1:
                counts[i] += 1
    return tuple(sorted((c for c in counts if c > 0), reverse=True))


def main():
    # build levels 1..5 (same seeding as the cascade's own validation)
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    levels = {1: {f for f in level if f != frozenset({0})}}
    for k in range(1, 5):
        level = pc.extend_level(level, k)
        levels[k + 1] = {f for f in level if f != frozenset({0})}

    expected = {1: 2, 2: 12, 3: 120, 4: 4958, 5: 2771102}
    print("REGULAR abundance profiles over nonempty UC families, n=1..5")
    print("oracle: profile_count_cascade (validated vs A121921 all levels)")
    print("range : n=1..5 ALL nonempty UC families; exact integer counts")
    for n in range(1, 6):
        assert len(levels[n]) == expected[n], (n, len(levels[n]), expected[n])
        reg = set()      # distinct regular profiles
        fullreg = set()  # distinct [c x n] profiles
        for F in levels[n]:
            p = profile_of(F, n)
            if len(set(p)) == 1:
                reg.add(p)
                if len(p) == n:
                    fullreg.add(p)
        print(f"n={n}: UC families={len(levels[n])}  REG={len(reg)} "
              f"(2^{n}-1={2**n - 1}, match={len(reg)==2**n-1})  "
              f"FULLREG={len(fullreg)}")
        if n == 5:
            print("  regular profiles at n=5 (sorted):",
                  sorted(reg, key=lambda t: (len(t), t[0])))

    # also: families counts for each regular profile at n=5 (multiplicity)
    n = 5
    reg_fams = defaultdict(int)
    for F in levels[n]:
        p = profile_of(F, n)
        if len(set(p)) == 1:
            reg_fams[p] += 1
    print("\nn=5: regular profile -> # families realizing it:")
    for p in sorted(reg_fams, key=lambda t: (len(t), t[0])):
        print(f"   {p} x{reg_fams[p]}")


if __name__ == "__main__":
    main()