"""Fine structure of the census: long-span end and multiplicity spectrum.

Answers, for n = 32, 64, 128:
  A. span-(n-1) sets: how many distinct A realize the maximal span, their run
     decompositions, multiplicities, weight  (= sum of m), and representative
     (d,d') pairs.
  B. multiplicity spectrum: histogram of m(A) over distinct A.
  C. where the weight mass sits: weighted mean span, weight on span >= n/2
     vs < n/2, number of spans with positive weight.
  D. few mid-long-span examples (span ~ n/2, m >= 1) with (d,d') and run
     decomposition — material for the fiber testers.

Uses lib.collapse (the canonical frozenset oracle, already cross-checked by
verify_census_bitset.py).
"""

from collections import Counter
from lib.collapse import downset, run_count


def run_decomp(A):
    if not A:
        return []
    s = sorted(A)
    out, cur = [], 1
    for a, b in zip(s, s[1:]):
        if b == a + 1:
            cur += 1
        else:
            out.append(cur)
            cur = 1
    out.append(cur)
    return out


def census(n):
    ds = {d: downset(d, n) for d in range(2, n)}
    mp = {}
    for d in range(2, n):
        for dp in range(2, n):
            A = frozenset(ds[d] ^ ds[dp])
            e = mp.get(A)
            if e is None:
                mp[A] = [1, (max(A) - min(A) + 1) if A else 0, run_decomp(A), (d, dp)]
            else:
                e[0] += 1
    return mp


def main():
    for n in (32, 64, 128):
        mp = census(n)
        print("=" * 78)
        print(f"n = {n}: entries (n-2)^2 = {(n-2)**2}, distinct sets = {len(mp)}")
        print("=" * 78)

        # A. span-(n-1) sets
        mspan = n - 1
        tops = [(A, e) for A, e in mp.items() if e[1] == mspan]
        top_weight = sum(e[0] for _, e in tops)
        print(f"\nA. span = n-1 = {mspan}: {len(tops)} distinct sets, "
              f"total weight = {top_weight} (diagonal weight is {n-2})")
        for A, e in sorted(tops, key=lambda t: (-t[1][0], t[1][2])):
            print(f"    runs(len)={e[2]}  |A|={len(A):4d}  m={e[0]:3d}  "
                  f"ex.(d,d')={e[3]}")
        print(f"    span-(n-1) weight {top_weight} vs diagonal weight {n-2}")

        # B. multiplicity spectrum
        spec = Counter(e[0] for _, e in mp.items())
        print(f"\nB. multiplicity spectrum: (m, #distinct sets)")
        for m in sorted(spec):
            print(f"    m={m:3d}: {spec[m]:5d} sets")

        # C. weight mass
        total_w = sum(e[0] for _, e in mp.items())
        wspan = sum(e[0] * e[1] for _, e in mp.items())
        w_large = sum(e[0] for _, e in mp.items() if e[1] >= n / 2)
        pos_spans = len({e[1] for _, e in mp.items()})
        print(f"\nC. total weight = {total_w} (== (n-2)^2 = {(n-2)**2})")
        print(f"    weighted mean span = {wspan / total_w:.2f}")
        print(f"    weight on span >= n/2 = {w_large} ({100.0 * w_large / total_w:.1f}%)")
        print(f"    spans with positive weight = {pos_spans} (values "
              f"{sorted({e[1] for _, e in mp.items()})[:12]} ... "
              f"{sorted({e[1] for _, e in mp.items()})[-4:]})")

        # D. examples at span ~ n/2 and ~ n/4 with m >= 1
        print(f"\nD. long-span examples (span comparable to n, m >= 1):")
        targets = [n // 2, n // 2 + 1, n // 4, 3 * n // 4, n - n // 8]
        for t in sorted(set(targets)):
            best = min(mp.items(), key=lambda kv: abs(kv[1][1] - t))
            A, e = best
            print(f"    span target {t:3d}: actual span={e[1]:3d} runs(len)={e[2]} "
                  f"|A|={len(A):3d} m={e[0]} ex.(d,d')={e[3]}")

    print("\nDONE")


if __name__ == "__main__":
    main()