"""Examine the size-2 EQ families that are NOT strict two-chains {A,A u {x}}
at n=4,5. Print them fully. Also print, for comparison, a few strict two-chains.
A 2-element family {A,B}, A subset B, is union-closed automatically. Its
equality condition: f = |A| = min{nn, 2k-nn+1} with k=|A|,nn=|B|, which forces
|B| <= |A|+1 and hence |B| == |A|+1. So ALL len-2 EQ must be strict two-chains.
If we find otherwise, the claim/data conflict -- investigate.
"""
import importlib.util
from collections import defaultdict

spec = importlib.util.spec_from_file_location(
    "profile_count_cascade", "code/out/profile_count_cascade.py")
pc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pc)


def popcount(x):
    return bin(x).count("1")


def main():
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    levels = {1: level}
    for k in range(1, 5):
        level = pc.extend_level(level, k)
        levels[k + 1] = level
    expected = {1: 2, 2: 12, 3: 120, 4: 4958, 5: 2771102}
    for n in range(1, 6):
        nonempty = {f for f in levels[n] if f != frozenset({0})}
        assert len(nonempty) == expected[n]

    for n in [4, 5]:
        nonempty = {f for f in levels[n] if f != frozenset({0})}
        print(f"=== n={n}: size-2 EQ families that are NOT strict two-chains ===")
        count = 0
        for F in sorted(nonempty, key=lambda f: (len(f), sorted(f))):
            if 0 in F:
                continue
            m = len(F)
            if m != 2:
                continue
            counts = [0] * n
            for s in F:
                for i in range(n):
                    if (s >> i) & 1:
                        counts[i] += 1
            f = sum(1 for c in counts if 2 * c > m)
            ks = [popcount(s) for s in F]
            k = min(ks); nn = max(ks)
            if f != min(nn, 2 * k - nn + 1):
                continue
            a, b = tuple(F)
            sa, sb = popcount(a), popcount(b)
            strict_tc = ((a | b) == b and sb == sa + 1) or \
                        ((a | b) == a and sa == sb + 1)
            if not strict_tc:
                count += 1
                print(f"   masks={sorted(F)} |A|={sa} |B|={sb} "
                      f"f={f} k={k} nn={nn}")
        print(f"   non-strict size-2 EQ families: {count}")
        # confirm total size-2 EQ
        tot2 = 0
        for F in nonempty:
            if 0 in F or len(F) != 2:
                continue
            counts = [0] * n
            for s in F:
                for i in range(n):
                    if (s >> i) & 1:
                        counts[i] += 1
            m = 2
            f = sum(1 for c in counts if 2 * c > m)
            ks = [popcount(s) for s in F]
            k = min(ks); nn = max(ks)
            if f == min(nn, 2 * k - nn + 1):
                tot2 += 1
        print(f"   total size-2 EQ families at n={n}: {tot2}")


if __name__ == "__main__":
    main()
