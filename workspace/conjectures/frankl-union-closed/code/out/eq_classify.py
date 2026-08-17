"""Classify the KPT Thm 5(3) equality families (f == min{nn, 2k-nn+1}) on
[n], n=1..5, exhaustively via the validated canonical cascade.

For every empty-free nonempty UC family F on [n]:
  k   = min |S| over S in F
  nn  = max |S| over S in F
  m   = |F|
  f   = #{elements with 2*count > m}   (strict abundance)
  eq  = (f == min(nn, 2*k - nn + 1))
  j   = |union of all sets in F|

Output for each n:
  - EQ(n) total, split into single-set families (2^n - 1, provable) and the
    rest, checking rest == n*(2^{n-1} - 1);
  - the (k, nn) pairs realized by equality families, with counts;
  - the split of the rest by union size j;
  - at n=5: every non-single-set equality family printed as (sorted masks,
    k, nn, f, j, counts): the raw material for the structural bijection.
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
        assert len(nonempty) == expected[n], (n, len(nonempty), expected[n])

    rows = []
    for n in range(1, 6):
        nonempty = {f for f in levels[n] if f != frozenset({0})}
        eq_fams = []          # (sorted masks, k, nn, f, j, counts)
        knn = defaultdict(int)
        by_j = defaultdict(int)
        rest = []             # non-single-set equality families
        for F in nonempty:
            if 0 in F:
                continue      # KPT uses the empty-free convention
            counts = pc.abundance_counts if hasattr(pc, "abundance_counts") else None
            if counts is None:
                counts = [0] * n
                for s in F:
                    for i in range(n):
                        if (s >> i) & 1:
                            counts[i] += 1
            m = len(F)
            f = sum(1 for c in counts if 2 * c > m)
            ks = [popcount(s) for s in F]
            k = min(ks)
            nn = max(ks)
            if f != min(nn, 2 * k - nn + 1):
                continue
            union_mask = 0
            for s in F:
                union_mask |= s
            j = popcount(union_mask)
            eq_fams.append((sorted(F), k, nn, f, j, counts))
            knn[(k, nn)] += 1
            by_j[j] += 1
            if len(F) > 1:
                rest.append((sorted(F), k, nn, f, j, counts))
        rows.append((n, eq_fams, knn, by_j, rest))

    print("classify KPT Thm 5(3) equality families n=1..5 (cascade, exact)")
    print("oracle: profile_count_cascade (validated vs A121921 all levels)")
    print("range : n=1..5, ALL empty-free nonempty UC families")
    for n, eq_fams, knn, by_j, rest in rows:
        singles = sum(1 for (F, k, nn, f, j, c) in eq_fams if len(F) == 1)
        non_single = len(eq_fams) - singles
        print(f"n={n}: EQ={len(eq_fams)}  singles={singles} "
              f"rest={non_single}  (n*(2^(n-1)-1)={'nope' if non_single != n*(2**(n-1)-1) else 'OK'})")
        print(f"   by (k,nn): {dict(sorted(knn.items()))}")
        print(f"   rest by union size j: {dict(sorted(by_j.items()))}")

    n = 5
    _, eq_fams, knn, by_j, rest = rows[n - 1]
    print(f"\nn=5: all {len(rest)} non-single-set equality families:")
    for F, k, nn, f, j, counts in sorted(rest, key=lambda r: (r[1], r[2], r[0])):
        print(f"   k={k} nn={nn} f={f} j={j} counts={counts} masks={F}")


if __name__ == "__main__":
    main()