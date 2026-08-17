"""Probe: does a REGULAR union-closed family (all present elements equi-frequent,
count c each) always have an abundant element (c >= |F|/2)?

A counterexample-regular family would be a UC family with all r present elements
at count c and c < |F|/2 (no abundant element). Over n<=5 no UC family at all
lacks an abundant element (no-abundant=0), so a fortiori none is regular -- but
we want the DISTRIBUTION: the min of density c/|F| over regular UC families, and
whether the minimizing value is exactly 1/2 (attained by Boolean subalgebras) or
below.

Report, per n:
  - # regular UC families
  - min density c/|F| over regular UC families, and a realizing profile
  - # regular UC families with c == |F|/2 (equality, abundant), c > |F|/2, c < |F|/2
  - full distribution of (r, c) -> density, with min

Oracle: profile_count_cascade (validated vs A121921 all levels).
Range:  n=1..5, ALL nonempty regular-profile UC families, exact fractions.
"""
import importlib.util
from collections import defaultdict
from fractions import Fraction

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
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    levels = {1: {f for f in level if f != frozenset({0})}}
    for k in range(1, 5):
        level = pc.extend_level(level, k)
        levels[k + 1] = {f for f in level if f != frozenset({0})}

    expected = {1: 2, 2: 12, 3: 120, 4: 4958, 5: 2771102}
    print("REGULAR UC families: abundance behaviour, n=1..5")
    print("oracle: profile_count_cascade (validated vs A121921 all levels)")
    print("range : n=1..5 ALL nonempty regular-profile UC families; exact")
    for n in range(1, 6):
        assert len(levels[n]) == expected[n], (n, len(levels[n]), expected[n])
        nreg = 0
        eq = 0      # c == m/2  (equality, abundant)
        above = 0   # c > m/2
        below = 0   # c < m/2  (would be a regular counterexample)
        min_dens = Fraction(1, 1)
        min_p = None
        for F in levels[n]:
            p = profile_of(F, n)
            if len(set(p)) != 1:
                continue
            nreg += 1
            m = len(F)
            c = p[0]
            d = Fraction(c, m)
            if d < min_dens:
                min_dens = d
                min_p = (sorted(F), p)
            if 2 * c > m:
                above += 1
            elif 2 * c == m:
                eq += 1
            else:
                below += 1
        print(f"n={n}: regular families={nreg}  min density={min_dens} "
              f"(~{float(min_dens):.6f})  above={above} eq={eq} below={below}")
        if min_p:
            print(f"     min-density regular family profile={min_p[1]} "
                  f"|F|={len(min_p[0])}")
        print(f"     regular c < m/2 (counterexample-regular): {below} "
              f"(should be 0 on n<=5 if UC holds there)")


if __name__ == "__main__":
    main()